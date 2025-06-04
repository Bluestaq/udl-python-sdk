# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Headers, Response

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncOffsetPage", "AsyncOffsetPage", "SyncKafkaOffsetPage", "AsyncKafkaOffsetPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class SyncOffsetPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("firstResult") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "firstResult" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"firstResult": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncOffsetPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("firstResult") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "firstResult" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"firstResult": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class SyncKafkaOffsetPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    """Pagination for Kafka-style endpoints that return the next offset in a response header."""

    items: List[_T]
    _headers: Headers

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset_str = self._headers.get("KAFKA_NEXT_OFFSET")
        if not next_offset_str:
            return None

        try:
            next_offset = int(next_offset_str)
        except ValueError:
            return None

        return PageInfo(params={"offset": next_offset})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        instance = cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )
        if issubclass(cls, SyncKafkaOffsetPage):
            instance._headers = response.headers.copy()  # type: ignore[attr-defined]

        return instance


class AsyncKafkaOffsetPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    """Async pagination for Kafka-style endpoints that return the next offset in a response header."""

    items: List[_T]
    _headers: Headers

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset_str = self._headers.get("KAFKA_NEXT_OFFSET")
        if not next_offset_str:
            return None

        try:
            next_offset = int(next_offset_str)
        except ValueError:
            return None

        return PageInfo(params={"offset": next_offset})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        instance = cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )
        if isinstance(cls, AsyncKafkaOffsetPage):
            instance._headers = response.headers.copy()  # type: ignore[attr-defined]

        return instance
