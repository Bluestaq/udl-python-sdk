# Proposed approach 2 for supporting query parameters with dynamic method generation

from typing import Any, Dict, Type, Generic, TypeVar, Callable

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class Query(Generic[T]):
    """
    A dynamic query builder that generates field-based filter methods at runtime.

    This class enables fluent query construction for a Pydantic model by dynamically
    attaching methods to the instance based on each model field and a set of supported
    query operators (e.g., _eq, _gte, _lte, _like, _not, _between).

    Example:
        class User(BaseModel):
            id: int
            name: str

        query = Query(User)
        query.name_like("Rob").id_gte(100)
        params = query.to_params()
        # Result: {"name": "*Rob*", "id": ">=100"}
    """

    def __init__(self, model: Type[T]) -> None:
        """
        Initialize the query builder for a given Pydantic model class.

        Dynamically attaches methods like `field_eq`, `field_gte`, `field_like`, etc.
        for each model field, allowing structured filter construction.

        Args:
            model: A Pydantic model class to query.
        """
        self.model: Type[T] = model
        self._filters: Dict[str, str] = {}

        # Define supported query suffixes and their corresponding operator symbols
        operators: Dict[str, str] = {
            "_eq": "",
            "_gte": ">=",
            "_lte": "<=",
            "_like": "like",
            "_not": "not",
            "_between": "between",
        }

        # Dynamically create query methods for each field/operator combination
        for field_name, _field_info in model.model_fields.items():
            for suffix, operator in operators.items():
                method_name = f"{field_name}{suffix}"
                method = self._make_method(field_name, operator)
                setattr(self, method_name, method.__get__(self, self.__class__))

    def _make_method(self, field_name: str, operator: str) -> Callable[["Query[T]", Any], "Query[T]"]:
        """
        Create a method for applying a filter on a specific field with the given operator.

        Args:
            field_name: The name of the model field to filter.
            operator: A string representing the filter operator.

        Returns:
            A callable method that accepts a value and returns the updated Query object.
        """

        def method(self: "Query[T]", value: Any) -> "Query[T]":
            return self._add_filter(field_name, operator, value)

        return method

    def _add_filter(self, field_name: str, operator: str, value: Any) -> "Query[T]":
        """
        Add a new filter to the internal filter store using the specified operator and value.

        Supports special formatting for 'between', 'not', and 'like' operations.

        Args:
            field_name: The name of the model field to filter.
            operator: The operation symbol (e.g., '>=', 'like', 'not').
            value: The value to compare against. For 'between', this must be a 2-tuple.

        Returns:
            The Query object with the new filter applied.
        """
        model_field = self.model.model_fields.get(field_name)
        if model_field is None:
            raise KeyError(f"{field_name} does not exist in {self.model}")

        key = getattr(model_field, "alias", None) or field_name

        if operator == "between":
            if not isinstance(value, tuple) or len(value) != 2:
                raise ValueError("'between' requires a tuple with exactly two values.")
            self._filters[key] = f"{value[0]}..{value[1]}"
        elif operator == "not":
            self._filters[key] = f"~{value}"
        elif operator == "like":
            self._filters[key] = f"*{value}*"
        else:
            self._filters[key] = f"{operator}{value}"
        return self

    def to_params(self) -> Dict[str, str]:
        """
        Serialize the query into a dictionary of query parameters.

        Returns:
            A dictionary where each key is the field alias (or name),
            and the value is a string representation of the filter condition.
        """
        return dict(self._filters)
