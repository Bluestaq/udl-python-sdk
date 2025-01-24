# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PersonnelrecoveryResource", "AsyncPersonnelrecoveryResource"]


class PersonnelrecoveryResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> PersonnelrecoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return PersonnelrecoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonnelrecoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return PersonnelrecoveryResourceWithStreamingResponse(self)


class AsyncPersonnelrecoveryResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPersonnelrecoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonnelrecoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonnelrecoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncPersonnelrecoveryResourceWithStreamingResponse(self)


class PersonnelrecoveryResourceWithRawResponse:
    def __init__(self, personnelrecovery: PersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._personnelrecovery.history)


class AsyncPersonnelrecoveryResourceWithRawResponse:
    def __init__(self, personnelrecovery: AsyncPersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._personnelrecovery.history)


class PersonnelrecoveryResourceWithStreamingResponse:
    def __init__(self, personnelrecovery: PersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._personnelrecovery.history)


class AsyncPersonnelrecoveryResourceWithStreamingResponse:
    def __init__(self, personnelrecovery: AsyncPersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._personnelrecovery.history)
