# Proposed approach 1 for supporting query parameters in a typed and composable way

from typing import Any, Dict, Type, Tuple, Union, Generic, TypeVar, Protocol, cast
from datetime import datetime

from pydantic import BaseModel

from .util import sanitize_datetime

T = TypeVar("T", bound=BaseModel)


class QueryField(Protocol):
    """
    Protocol defining supported query operations on a single model field.

    Each method represents a filter operation that returns a modified Query object
    with the new filter applied.
    """

    def eq(self, value: Any) -> "Query[Any]": ...
    def gte(self, value: Any) -> "Query[Any]": ...
    def lte(self, value: Any) -> "Query[Any]": ...
    def like(self, value: str) -> "Query[Any]": ...
    def between(self, start: Any, end: Any) -> "Query[Any]": ...
    def not_(self, value: Any) -> "Query[Any]": ...


class Query(Generic[T]):
    """
    A fluent query builder for filtering instances of a given Pydantic model.

    Supports field-based operations like equality, range comparisons, pattern matching,
    and negation. Query filters are internally stored and can be serialized as
    query parameter strings (e.g., for REST APIs).
    """

    def __init__(self, model: Type[T]) -> None:
        """
        Initialize a new query builder for a given Pydantic model class.

        Args:
            model: A class inheriting from pydantic.BaseModel
        """
        self.model: Type[T] = model
        self._filters: Dict[str, str] = {}

    def field(self, field_name: str) -> QueryField:
        """
        Get a queryable interface for a given field name in the model.

        Args:
            field_name: The name of the model field to query.

        Returns:
            A QueryField-compatible object supporting fluent comparison operators.
        """

        class FieldQuery(QueryField):
            """
            Internal implementation of QueryField for one specific field.
            """

            def __init__(self, query: "Query[T]", field_name: str) -> None:
                self.query = query
                self.field_name = field_name

            def _handle_dates(self, value: Union[Any, Tuple[Any, Any]]) -> Union[Any, Tuple[Any, Any]]:
                """
                Normalize datetime values into string representations using sanitize_datetime.
                Supports both individual and tuple values (for 'between').
                """
                if isinstance(value, datetime):
                    return sanitize_datetime(value)
                if isinstance(value, tuple):
                    return tuple(sanitize_datetime(v) if isinstance(v, datetime) else v for v in value)
                return value

            def _add_filter(self, operator: str, value: Any) -> "Query[T]":
                """
                Add a new filter to the parent Query object using the provided operator.

                Args:
                    operator: The comparison operator (e.g., '=', '>=', '<', 'like', etc.)
                    value: The value to compare against.

                Returns:
                    The parent Query object with the filter applied.
                """
                value = self._handle_dates(value)

                model_info = self.query.model.model_fields.get(self.field_name)
                if model_info is None:
                    raise KeyError(f"{self.field_name} does not exist in {self.query.model}")

                key = getattr(model_info, "alias", None) or self.field_name

                if operator == "between":
                    if not isinstance(value, tuple) or len(value) != 2:
                        raise ValueError("'between' requires a tuple with exactly two values.")
                    self.query._filters[key] = f"{value[0]}..{value[1]}"
                elif operator == "not":
                    self.query._filters[key] = f"~{value}"
                elif operator == "like":
                    self.query._filters[key] = f"*{value}*"
                else:
                    self.query._filters[key] = f"{operator}{value}"

                return self.query

            def eq(self, value: Any) -> "Query[T]":
                """Adds an equality filter to the query."""
                return self._add_filter("", value)

            def gte(self, value: Any) -> "Query[T]":
                """Adds a 'greater than or equal to' filter."""
                return self._add_filter(">", value)

            def lte(self, value: Any) -> "Query[T]":
                """Adds a 'less than or equal to' filter."""
                return self._add_filter("<", value)

            def like(self, value: str) -> "Query[T]":
                """Adds a case-insensitive partial match filter."""
                return self._add_filter("like", value)

            def between(self, start: Any, end: Any) -> "Query[T]":
                """Adds a range filter with inclusive bounds."""
                return self._add_filter("between", (start, end))

            def not_(self, value: Any) -> "Query[T]":
                """Adds a negation filter."""
                return self._add_filter("not", value)

        return cast(QueryField, FieldQuery(self, field_name))

    def to_params(self) -> Dict[str, str]:
        """
        Convert all collected filters into query parameter strings.

        Returns:
            A dictionary of query parameters suitable for appending to a REST request.
        """
        return {key: str(value) for key, value in self._filters.items()}
