# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .poi import (
    PoiResource,
    AsyncPoiResource,
    PoiResourceWithRawResponse,
    AsyncPoiResourceWithRawResponse,
    PoiResourceWithStreamingResponse,
    AsyncPoiResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .rf_geolocation import (
    RfGeolocationResource,
    AsyncRfGeolocationResource,
    RfGeolocationResourceWithRawResponse,
    AsyncRfGeolocationResourceWithRawResponse,
    RfGeolocationResourceWithStreamingResponse,
    AsyncRfGeolocationResourceWithStreamingResponse,
)

__all__ = ["ReportAndActivityResource", "AsyncReportAndActivityResource"]


class ReportAndActivityResource(SyncAPIResource):
    @cached_property
    def poi(self) -> PoiResource:
        return PoiResource(self._client)

    @cached_property
    def rf_geolocation(self) -> RfGeolocationResource:
        return RfGeolocationResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportAndActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return ReportAndActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportAndActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return ReportAndActivityResourceWithStreamingResponse(self)


class AsyncReportAndActivityResource(AsyncAPIResource):
    @cached_property
    def poi(self) -> AsyncPoiResource:
        return AsyncPoiResource(self._client)

    @cached_property
    def rf_geolocation(self) -> AsyncRfGeolocationResource:
        return AsyncRfGeolocationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportAndActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportAndActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportAndActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncReportAndActivityResourceWithStreamingResponse(self)


class ReportAndActivityResourceWithRawResponse:
    def __init__(self, report_and_activity: ReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> PoiResourceWithRawResponse:
        return PoiResourceWithRawResponse(self._report_and_activity.poi)

    @cached_property
    def rf_geolocation(self) -> RfGeolocationResourceWithRawResponse:
        return RfGeolocationResourceWithRawResponse(self._report_and_activity.rf_geolocation)


class AsyncReportAndActivityResourceWithRawResponse:
    def __init__(self, report_and_activity: AsyncReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> AsyncPoiResourceWithRawResponse:
        return AsyncPoiResourceWithRawResponse(self._report_and_activity.poi)

    @cached_property
    def rf_geolocation(self) -> AsyncRfGeolocationResourceWithRawResponse:
        return AsyncRfGeolocationResourceWithRawResponse(self._report_and_activity.rf_geolocation)


class ReportAndActivityResourceWithStreamingResponse:
    def __init__(self, report_and_activity: ReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> PoiResourceWithStreamingResponse:
        return PoiResourceWithStreamingResponse(self._report_and_activity.poi)

    @cached_property
    def rf_geolocation(self) -> RfGeolocationResourceWithStreamingResponse:
        return RfGeolocationResourceWithStreamingResponse(self._report_and_activity.rf_geolocation)


class AsyncReportAndActivityResourceWithStreamingResponse:
    def __init__(self, report_and_activity: AsyncReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> AsyncPoiResourceWithStreamingResponse:
        return AsyncPoiResourceWithStreamingResponse(self._report_and_activity.poi)

    @cached_property
    def rf_geolocation(self) -> AsyncRfGeolocationResourceWithStreamingResponse:
        return AsyncRfGeolocationResourceWithStreamingResponse(self._report_and_activity.rf_geolocation)
