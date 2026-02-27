# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.eop import history_aodr_params, history_list_params, history_count_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.eop_full import EopFull

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    """
    This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
    """

    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        eop_date: Union[str, datetime],
        columns: str | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[EopFull]:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eop/history",
            page=SyncOffsetPage[EopFull],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=EopFull,
        )

    def aodr(
        self,
        *,
        eop_date: Union[str, datetime],
        columns: str | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        notification: str | Omit = omit,
        output_delimiter: str | Omit = omit,
        output_format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation, then write that data to the
        Secure Content Store. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/eop/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    history_aodr_params.HistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        eop_date: Union[str, datetime],
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
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/eop/history/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    history_count_params.HistoryCountParams,
                ),
            ),
            cast_to=str,
        )


class AsyncHistoryResource(AsyncAPIResource):
    """
    This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
    """

    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        eop_date: Union[str, datetime],
        columns: str | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EopFull, AsyncOffsetPage[EopFull]]:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eop/history",
            page=AsyncOffsetPage[EopFull],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=EopFull,
        )

    async def aodr(
        self,
        *,
        eop_date: Union[str, datetime],
        columns: str | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        notification: str | Omit = omit,
        output_delimiter: str | Omit = omit,
        output_format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation, then write that data to the
        Secure Content Store. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/eop/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "eop_date": eop_date,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    history_aodr_params.HistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        eop_date: Union[str, datetime],
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
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/eop/history/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    history_count_params.HistoryCountParams,
                ),
            ),
            cast_to=str,
        )


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.list = to_raw_response_wrapper(
            history.list,
        )
        self.aodr = to_raw_response_wrapper(
            history.aodr,
        )
        self.count = to_raw_response_wrapper(
            history.count,
        )


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_raw_response_wrapper(
            history.list,
        )
        self.aodr = async_to_raw_response_wrapper(
            history.aodr,
        )
        self.count = async_to_raw_response_wrapper(
            history.count,
        )


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.list = to_streamed_response_wrapper(
            history.list,
        )
        self.aodr = to_streamed_response_wrapper(
            history.aodr,
        )
        self.count = to_streamed_response_wrapper(
            history.count,
        )


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_streamed_response_wrapper(
            history.list,
        )
        self.aodr = async_to_streamed_response_wrapper(
            history.aodr,
        )
        self.count = async_to_streamed_response_wrapper(
            history.count,
        )
