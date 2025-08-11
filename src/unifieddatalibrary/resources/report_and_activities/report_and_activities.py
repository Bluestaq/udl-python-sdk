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

__all__ = ["ReportAndActivitiesResource", "AsyncReportAndActivitiesResource"]


class ReportAndActivitiesResource(SyncAPIResource):
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
    def with_raw_response(self) -> ReportAndActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportAndActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportAndActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ReportAndActivitiesResourceWithStreamingResponse(self)


class AsyncReportAndActivitiesResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncReportAndActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportAndActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportAndActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncReportAndActivitiesResourceWithStreamingResponse(self)


class ReportAndActivitiesResourceWithRawResponse:
    def __init__(self, report_and_activities: ReportAndActivitiesResource) -> None:
        self._report_and_activities = report_and_activities

    @cached_property
    def poi(self) -> PoiResourceWithRawResponse:
        return PoiResourceWithRawResponse(self._report_and_activities.poi)

    @cached_property
    def udl_h3geo(self) -> UdlH3geoResourceWithRawResponse:
        return UdlH3geoResourceWithRawResponse(self._report_and_activities.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> UdlSigactResourceWithRawResponse:
        return UdlSigactResourceWithRawResponse(self._report_and_activities.udl_sigact)


class AsyncReportAndActivitiesResourceWithRawResponse:
    def __init__(self, report_and_activities: AsyncReportAndActivitiesResource) -> None:
        self._report_and_activities = report_and_activities

    @cached_property
    def poi(self) -> AsyncPoiResourceWithRawResponse:
        return AsyncPoiResourceWithRawResponse(self._report_and_activities.poi)

    @cached_property
    def udl_h3geo(self) -> AsyncUdlH3geoResourceWithRawResponse:
        return AsyncUdlH3geoResourceWithRawResponse(self._report_and_activities.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> AsyncUdlSigactResourceWithRawResponse:
        return AsyncUdlSigactResourceWithRawResponse(self._report_and_activities.udl_sigact)


class ReportAndActivitiesResourceWithStreamingResponse:
    def __init__(self, report_and_activities: ReportAndActivitiesResource) -> None:
        self._report_and_activities = report_and_activities

    @cached_property
    def poi(self) -> PoiResourceWithStreamingResponse:
        return PoiResourceWithStreamingResponse(self._report_and_activities.poi)

    @cached_property
    def udl_h3geo(self) -> UdlH3geoResourceWithStreamingResponse:
        return UdlH3geoResourceWithStreamingResponse(self._report_and_activities.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> UdlSigactResourceWithStreamingResponse:
        return UdlSigactResourceWithStreamingResponse(self._report_and_activities.udl_sigact)


class AsyncReportAndActivitiesResourceWithStreamingResponse:
    def __init__(self, report_and_activities: AsyncReportAndActivitiesResource) -> None:
        self._report_and_activities = report_and_activities

    @cached_property
    def poi(self) -> AsyncPoiResourceWithStreamingResponse:
        return AsyncPoiResourceWithStreamingResponse(self._report_and_activities.poi)

    @cached_property
    def udl_h3geo(self) -> AsyncUdlH3geoResourceWithStreamingResponse:
        return AsyncUdlH3geoResourceWithStreamingResponse(self._report_and_activities.udl_h3geo)

    @cached_property
    def udl_sigact(self) -> AsyncUdlSigactResourceWithStreamingResponse:
        return AsyncUdlSigactResourceWithStreamingResponse(self._report_and_activities.udl_sigact)
