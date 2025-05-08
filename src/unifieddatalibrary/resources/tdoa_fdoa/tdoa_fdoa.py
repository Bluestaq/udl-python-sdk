# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .diffofarrival.diffofarrival import (
    DiffofarrivalResource,
    AsyncDiffofarrivalResource,
    DiffofarrivalResourceWithRawResponse,
    AsyncDiffofarrivalResourceWithRawResponse,
    DiffofarrivalResourceWithStreamingResponse,
    AsyncDiffofarrivalResourceWithStreamingResponse,
)

__all__ = ["TdoaFdoaResource", "AsyncTdoaFdoaResource"]


class TdoaFdoaResource(SyncAPIResource):
    @cached_property
    def diffofarrival(self) -> DiffofarrivalResource:
        return DiffofarrivalResource(self._client)

    @cached_property
    def with_raw_response(self) -> TdoaFdoaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TdoaFdoaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TdoaFdoaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return TdoaFdoaResourceWithStreamingResponse(self)


class AsyncTdoaFdoaResource(AsyncAPIResource):
    @cached_property
    def diffofarrival(self) -> AsyncDiffofarrivalResource:
        return AsyncDiffofarrivalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTdoaFdoaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTdoaFdoaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTdoaFdoaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncTdoaFdoaResourceWithStreamingResponse(self)


class TdoaFdoaResourceWithRawResponse:
    def __init__(self, tdoa_fdoa: TdoaFdoaResource) -> None:
        self._tdoa_fdoa = tdoa_fdoa

    @cached_property
    def diffofarrival(self) -> DiffofarrivalResourceWithRawResponse:
        return DiffofarrivalResourceWithRawResponse(self._tdoa_fdoa.diffofarrival)


class AsyncTdoaFdoaResourceWithRawResponse:
    def __init__(self, tdoa_fdoa: AsyncTdoaFdoaResource) -> None:
        self._tdoa_fdoa = tdoa_fdoa

    @cached_property
    def diffofarrival(self) -> AsyncDiffofarrivalResourceWithRawResponse:
        return AsyncDiffofarrivalResourceWithRawResponse(self._tdoa_fdoa.diffofarrival)


class TdoaFdoaResourceWithStreamingResponse:
    def __init__(self, tdoa_fdoa: TdoaFdoaResource) -> None:
        self._tdoa_fdoa = tdoa_fdoa

    @cached_property
    def diffofarrival(self) -> DiffofarrivalResourceWithStreamingResponse:
        return DiffofarrivalResourceWithStreamingResponse(self._tdoa_fdoa.diffofarrival)


class AsyncTdoaFdoaResourceWithStreamingResponse:
    def __init__(self, tdoa_fdoa: AsyncTdoaFdoaResource) -> None:
        self._tdoa_fdoa = tdoa_fdoa

    @cached_property
    def diffofarrival(self) -> AsyncDiffofarrivalResourceWithStreamingResponse:
        return AsyncDiffofarrivalResourceWithStreamingResponse(self._tdoa_fdoa.diffofarrival)
