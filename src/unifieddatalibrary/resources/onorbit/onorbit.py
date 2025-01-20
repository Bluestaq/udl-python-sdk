# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .antenna_details import (
    AntennaDetailsResource,
    AsyncAntennaDetailsResource,
    AntennaDetailsResourceWithRawResponse,
    AsyncAntennaDetailsResourceWithRawResponse,
    AntennaDetailsResourceWithStreamingResponse,
    AsyncAntennaDetailsResourceWithStreamingResponse,
)

__all__ = ["OnorbitResource", "AsyncOnorbitResource"]


class OnorbitResource(SyncAPIResource):
    @cached_property
    def antenna_details(self) -> AntennaDetailsResource:
        return AntennaDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnorbitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return OnorbitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return OnorbitResourceWithStreamingResponse(self)


class AsyncOnorbitResource(AsyncAPIResource):
    @cached_property
    def antenna_details(self) -> AsyncAntennaDetailsResource:
        return AsyncAntennaDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnorbitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncOnorbitResourceWithStreamingResponse(self)


class OnorbitResourceWithRawResponse:
    def __init__(self, onorbit: OnorbitResource) -> None:
        self._onorbit = onorbit

    @cached_property
    def antenna_details(self) -> AntennaDetailsResourceWithRawResponse:
        return AntennaDetailsResourceWithRawResponse(self._onorbit.antenna_details)


class AsyncOnorbitResourceWithRawResponse:
    def __init__(self, onorbit: AsyncOnorbitResource) -> None:
        self._onorbit = onorbit

    @cached_property
    def antenna_details(self) -> AsyncAntennaDetailsResourceWithRawResponse:
        return AsyncAntennaDetailsResourceWithRawResponse(self._onorbit.antenna_details)


class OnorbitResourceWithStreamingResponse:
    def __init__(self, onorbit: OnorbitResource) -> None:
        self._onorbit = onorbit

    @cached_property
    def antenna_details(self) -> AntennaDetailsResourceWithStreamingResponse:
        return AntennaDetailsResourceWithStreamingResponse(self._onorbit.antenna_details)


class AsyncOnorbitResourceWithStreamingResponse:
    def __init__(self, onorbit: AsyncOnorbitResource) -> None:
        self._onorbit = onorbit

    @cached_property
    def antenna_details(self) -> AsyncAntennaDetailsResourceWithStreamingResponse:
        return AsyncAntennaDetailsResourceWithStreamingResponse(self._onorbit.antenna_details)
