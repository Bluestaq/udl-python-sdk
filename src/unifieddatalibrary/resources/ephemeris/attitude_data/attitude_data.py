# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.ephemeris import attitude_data_list_params, attitude_data_count_params
from ....types.ephemeris.attitude_data_abridged import AttitudeDataAbridged

__all__ = ["AttitudeDataResource", "AsyncAttitudeDataResource"]


class AttitudeDataResource(SyncAPIResource):
    """
    These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
    """

    @cached_property
    def history(self) -> HistoryResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AttitudeDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AttitudeDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttitudeDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AttitudeDataResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        as_id: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[AttitudeDataAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          as_id: Unique identifier of the parent AttitudeSet associated with this record. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/attitudedata",
            page=SyncOffsetPage[AttitudeDataAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "as_id": as_id,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_data_list_params.AttitudeDataListParams,
                ),
            ),
            model=AttitudeDataAbridged,
        )

    def count(
        self,
        *,
        as_id: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          as_id: Unique identifier of the parent AttitudeSet associated with this record. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/attitudedata/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "as_id": as_id,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_data_count_params.AttitudeDataCountParams,
                ),
            ),
            cast_to=str,
        )


class AsyncAttitudeDataResource(AsyncAPIResource):
    """
    These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
    """

    @cached_property
    def history(self) -> AsyncHistoryResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttitudeDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAttitudeDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttitudeDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAttitudeDataResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        as_id: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AttitudeDataAbridged, AsyncOffsetPage[AttitudeDataAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          as_id: Unique identifier of the parent AttitudeSet associated with this record. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/attitudedata",
            page=AsyncOffsetPage[AttitudeDataAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "as_id": as_id,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_data_list_params.AttitudeDataListParams,
                ),
            ),
            model=AttitudeDataAbridged,
        )

    async def count(
        self,
        *,
        as_id: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          as_id: Unique identifier of the parent AttitudeSet associated with this record. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/attitudedata/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "as_id": as_id,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_data_count_params.AttitudeDataCountParams,
                ),
            ),
            cast_to=str,
        )


class AttitudeDataResourceWithRawResponse:
    def __init__(self, attitude_data: AttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.list = to_raw_response_wrapper(
            attitude_data.list,
        )
        self.count = to_raw_response_wrapper(
            attitude_data.count,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        return HistoryResourceWithRawResponse(self._attitude_data.history)


class AsyncAttitudeDataResourceWithRawResponse:
    def __init__(self, attitude_data: AsyncAttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.list = async_to_raw_response_wrapper(
            attitude_data.list,
        )
        self.count = async_to_raw_response_wrapper(
            attitude_data.count,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        return AsyncHistoryResourceWithRawResponse(self._attitude_data.history)


class AttitudeDataResourceWithStreamingResponse:
    def __init__(self, attitude_data: AttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.list = to_streamed_response_wrapper(
            attitude_data.list,
        )
        self.count = to_streamed_response_wrapper(
            attitude_data.count,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        return HistoryResourceWithStreamingResponse(self._attitude_data.history)


class AsyncAttitudeDataResourceWithStreamingResponse:
    def __init__(self, attitude_data: AsyncAttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.list = async_to_streamed_response_wrapper(
            attitude_data.list,
        )
        self.count = async_to_streamed_response_wrapper(
            attitude_data.count,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        return AsyncHistoryResourceWithStreamingResponse(self._attitude_data.history)
