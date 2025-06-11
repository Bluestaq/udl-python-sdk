# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response, URL

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncOffsetPage", "AsyncOffsetPage", "SyncKafkaOffsetPage", "AsyncKafkaOffsetPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)
_BasePageT = TypeVar("_BasePageT", bound=BasePage[Any])

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
    @override
    def build(cls: Type[_BasePageT], *, response: Response, data: object) -> _BasePageT:  # noqa: ARG003
        return cls._with_response(
            cls.construct(
                None,
                **{
                    **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                },
            ),
            response,
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
    @override
    def build(cls: Type[_BasePageT], *, response: Response, data: object) -> _BasePageT:  # noqa: ARG003
        return cls._with_response(
            cls.construct(
                None,
                **{
                    **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                },
            ),
            response,
        )


class SyncKafkaOffsetPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    """Pagination for Kafka-style endpoints that return the next offset in a response header."""

    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset_str = self._response.headers.get("KAFKA_NEXT_OFFSET")
        if not next_offset_str:
            return None

        try:
            next_offset = int(next_offset_str)
        except ValueError:
            return None
        
        url = str(self._response.url).replace(
            f"/sm/getMessages/eop/{self._options.params.get('offset', 0)}",
            f"/sm/getMessages/eop/{next_offset}",
        )

        return PageInfo(url=URL(url))

    @classmethod
    @override
    def build(cls: Type[_BasePageT], *, response: Response, data: object) -> _BasePageT:  # noqa: ARG003
        return cls._with_response(
            cls.construct(
                None,
                **{
                    **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                },
            ),
            response,
        )


class AsyncKafkaOffsetPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    """Async pagination for Kafka-style endpoints that return the next offset in a response header."""

    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset_str = self._response.headers.get("KAFKA_NEXT_OFFSET")
        if not next_offset_str:
            return None

        try:
            next_offset = int(next_offset_str)
        except ValueError:
            return None

        url = str(self._response.url).replace(
            f"/sm/getMessages/eop/{self._options.params.get('offset', 0)}",
            f"/sm/getMessages/eop/{next_offset}",
        )

        return PageInfo(url=URL(url))

    @classmethod
    @override
    def build(cls: Type[_BasePageT], *, response: Response, data: object) -> _BasePageT:  # noqa: ARG003
        return cls._with_response(
            cls.construct(
                None,
                **{
                    **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                },
            ),
            response,
        )
