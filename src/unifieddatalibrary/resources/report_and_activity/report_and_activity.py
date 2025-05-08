# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .poi.poi import (
    PoiResource,
    AsyncPoiResource,
    PoiResourceWithRawResponse,
    AsyncPoiResourceWithRawResponse,
    PoiResourceWithStreamingResponse,
    AsyncPoiResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .udl_h3geo import (
    UdlH3geoResource,
    AsyncUdlH3geoResource,
    UdlH3geoResourceWithRawResponse,
    AsyncUdlH3geoResourceWithRawResponse,
    UdlH3geoResourceWithStreamingResponse,
    AsyncUdlH3geoResourceWithStreamingResponse,
)
from .udl_sigact import (
    UdlSigactResource,
    AsyncUdlSigactResource,
    UdlSigactResourceWithRawResponse,
    AsyncUdlSigactResourceWithRawResponse,
    UdlSigactResourceWithStreamingResponse,
    AsyncUdlSigactResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ReportAndActivityResource", "AsyncReportAndActivityResource"]


class ReportAndActivityResource(SyncAPIResource):
    @cached_property
    def poi(self) -> PoiResource:
        return PoiResource(self._client)

    @cached_property
    def udl_h3geo(self) -> UdlH3geoResource:
        return UdlH3geoResource(self._client)

    @cached_property
    def udl_sigact(self) -> UdlSigactResource:
        return UdlSigactResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportAndActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportAndActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportAndActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ReportAndActivityResourceWithStreamingResponse(self)


class AsyncReportAndActivityResource(AsyncAPIResource):
    @cached_property
    def poi(self) -> AsyncPoiResource:
        return AsyncPoiResource(self._client)

    @cached_property
    def udl_h3geo(self) -> AsyncUdlH3geoResource:
        return AsyncUdlH3geoResource(self._client)

    @cached_property
    def udl_sigact(self) -> AsyncUdlSigactResource:
        return AsyncUdlSigactResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportAndActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportAndActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportAndActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncReportAndActivityResourceWithStreamingResponse(self)


class ReportAndActivityResourceWithRawResponse:
    def __init__(self, report_and_activity: ReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> PoiResourceWithRawResponse:
        return PoiResourceWithRawResponse(self._report_and_activity.poi)

    @cached_property
    def udl_h3geo(self) -> UdlH3geoResourceWithRawResponse:
        return UdlH3geoResourceWithRawResponse(self._report_and_activity.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> UdlSigactResourceWithRawResponse:
        return UdlSigactResourceWithRawResponse(self._report_and_activity.udl_sigact)


class AsyncReportAndActivityResourceWithRawResponse:
    def __init__(self, report_and_activity: AsyncReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> AsyncPoiResourceWithRawResponse:
        return AsyncPoiResourceWithRawResponse(self._report_and_activity.poi)

    @cached_property
    def udl_h3geo(self) -> AsyncUdlH3geoResourceWithRawResponse:
        return AsyncUdlH3geoResourceWithRawResponse(self._report_and_activity.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> AsyncUdlSigactResourceWithRawResponse:
        return AsyncUdlSigactResourceWithRawResponse(self._report_and_activity.udl_sigact)


class ReportAndActivityResourceWithStreamingResponse:
    def __init__(self, report_and_activity: ReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> PoiResourceWithStreamingResponse:
        return PoiResourceWithStreamingResponse(self._report_and_activity.poi)

    @cached_property
    def udl_h3geo(self) -> UdlH3geoResourceWithStreamingResponse:
        return UdlH3geoResourceWithStreamingResponse(self._report_and_activity.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> UdlSigactResourceWithStreamingResponse:
        return UdlSigactResourceWithStreamingResponse(self._report_and_activity.udl_sigact)


class AsyncReportAndActivityResourceWithStreamingResponse:
    def __init__(self, report_and_activity: AsyncReportAndActivityResource) -> None:
        self._report_and_activity = report_and_activity

    @cached_property
    def poi(self) -> AsyncPoiResourceWithStreamingResponse:
        return AsyncPoiResourceWithStreamingResponse(self._report_and_activity.poi)

    @cached_property
    def udl_h3geo(self) -> AsyncUdlH3geoResourceWithStreamingResponse:
        return AsyncUdlH3geoResourceWithStreamingResponse(self._report_and_activity.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> AsyncUdlSigactResourceWithStreamingResponse:
        return AsyncUdlSigactResourceWithStreamingResponse(self._report_and_activity.udl_sigact)
