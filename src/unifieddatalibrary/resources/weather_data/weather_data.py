# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    weather_data_get_params,
    weather_data_list_params,
    weather_data_count_params,
    weather_data_tuple_params,
    weather_data_create_params,
    weather_data_create_bulk_params,
    weather_data_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.weather_data_list_response import WeatherDataListResponse
from ...types.weather_data_tuple_response import WeatherDataTupleResponse
from ...types.weather_data.weather_data_full import WeatherDataFull

__all__ = ["WeatherDataResource", "AsyncWeatherDataResource"]


class WeatherDataResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> WeatherDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WeatherDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WeatherDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return WeatherDataResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        angle_orientation: float | NotGiven = NOT_GIVEN,
        avg_ref_pwr: float | NotGiven = NOT_GIVEN,
        avg_tx_pwr: float | NotGiven = NOT_GIVEN,
        checksum: int | NotGiven = NOT_GIVEN,
        co_integs: Iterable[int] | NotGiven = NOT_GIVEN,
        cons_recs: Iterable[int] | NotGiven = NOT_GIVEN,
        dopp_vels: Iterable[float] | NotGiven = NOT_GIVEN,
        file_creation: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_guess_avgs: Iterable[int] | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        interpulse_periods: Iterable[float] | NotGiven = NOT_GIVEN,
        light_det_sensors: Iterable[int] | NotGiven = NOT_GIVEN,
        light_event_num: int | NotGiven = NOT_GIVEN,
        noise_lvls: Iterable[float] | NotGiven = NOT_GIVEN,
        num_elements: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pos_confidence: float | NotGiven = NOT_GIVEN,
        qc_value: int | NotGiven = NOT_GIVEN,
        sector_num: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        semi_minor_axis: float | NotGiven = NOT_GIVEN,
        sig_pwrs: Iterable[float] | NotGiven = NOT_GIVEN,
        sig_strength: float | NotGiven = NOT_GIVEN,
        snrs: Iterable[float] | NotGiven = NOT_GIVEN,
        spec_avgs: Iterable[int] | NotGiven = NOT_GIVEN,
        spec_widths: Iterable[float] | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        td_avg_sample_nums: Iterable[int] | NotGiven = NOT_GIVEN,
        term_alt: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single WeatherData as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          angle_orientation: Angle of orientation of the 50% positional confidence ellipse, in degrees
              clockwise from true north.

          avg_ref_pwr: Average power of the reflected signal received by the radar, in Watts.

          avg_tx_pwr: Average transmitted power of the radar, in kilowatts.

          checksum: Checksum value for the data.

          co_integs: Array of the number(s) of measurements used in coherent integrations used for
              radar data processing. Users should consult the data provider for information on
              the coherent integrations array structure.

          cons_recs: Array of the number(s) of records in consensus for a radar beam. Users should
              consult the data provider for information on the consensus records array
              structure.

          dopp_vels: Array of full scale Nyquist Doppler velocities measured by radar, in meters per
              second. Nyquist velocity refers to the maximum velocity magnitude that the radar
              system can unambiguously detect. Doppler velocities with absolute values
              exceeding the Nyquist threshold suffer from aliasing at the time of collection.
              Users should consult the data provider for information on the doppler velocities
              array structure.

          file_creation: Datetime the system files were created.

          first_guess_avgs: Array of average maximum number(s) of consecutive instances in which the same
              first guess velocity is used in radar data processing to estimate wind speed.
              Users should consult the data provider for information on the first guess
              averages array structure.

          id_sensor: Unique identifier of the sensor making the weather measurement.

          interpulse_periods: Array of the elapsed time(s) from the beginning of one pulse to the beginning of
              the next pulse for a radar beam, in microseconds. Users should consult the data
              provider for information on the interpulse periods array structure.

          light_det_sensors: Array of sensor(s) that participated in the lightning event location
              determination.

          light_event_num: Number of sensors used in the lightning event location solution.

          noise_lvls: Array of noise level(s) measured by radar, in decibels. Users should consult the
              data provider for information on the noise levels array structure.

          num_elements: Number of antennas across all sectors within the radar coverage area.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the record source. This may be an internal
              identifier and not necessarily a valid sensor ID.

          pos_confidence: The positional confidence of the calculated lightning event location using the
              chi-square statistical method.

          qc_value: Quality control flag value, as defined by the data provider.

          sector_num: Number of sectors within the radar coverage area, each containing a number of
              antennas.

          semi_major_axis: Semi-major axis of the 50% positional confidence ellipse, in kilometers.

          semi_minor_axis: Semi-minor axis of the 50% positional confidence ellipse, in kilometers.

          sig_pwrs: Array of signal power(s) measured by the sensor, in decibels. Users should
              consult the data provider for information on the signal powers array structure.

          sig_strength: Signal strength of the electromagnetic energy received due to a lightning event,
              in kiloamps.

          snrs: Array of signal to noise ratio(s) for a radar beam, in decibels. Users should
              consult the data provider for information on the signal to noise ratios array
              structure.

          spec_avgs: Array of the number(s) of spectral averages used in radar data processing. Users
              should consult the data provider for information on the spectral averages array
              structure.

          spec_widths: Array of width(s) of the distribution in Doppler velocity measured by radar, in
              meters/second. Spectral width depends on the particle size distribution, the
              wind shear across the radar beam, and turbulence. Users should consult the data
              provider for information on the spectral widths array structure.

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this WeatherData
              record. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. See the corresponding srcTyps array element
              for the data type of the UUID and use the appropriate API operation to retrieve
              that object.

          src_typs: Array of UDL record types (SENSOR, WEATHERREPORT) that are related to this
              WeatherData record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          td_avg_sample_nums: Array of the number(s) of radar samples used in time domain averaging for radar
              data processing. Time domain averaging improves the quality of the measured
              signal by reducing random noise and enhancing the signal-to-noise ratio. Users
              should consult the data provider for information on the time domain sample
              numbers array structure.

          term_alt: Last altitude with recorded measurements in this record, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/weatherdata",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "angle_orientation": angle_orientation,
                    "avg_ref_pwr": avg_ref_pwr,
                    "avg_tx_pwr": avg_tx_pwr,
                    "checksum": checksum,
                    "co_integs": co_integs,
                    "cons_recs": cons_recs,
                    "dopp_vels": dopp_vels,
                    "file_creation": file_creation,
                    "first_guess_avgs": first_guess_avgs,
                    "id_sensor": id_sensor,
                    "interpulse_periods": interpulse_periods,
                    "light_det_sensors": light_det_sensors,
                    "light_event_num": light_event_num,
                    "noise_lvls": noise_lvls,
                    "num_elements": num_elements,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "pos_confidence": pos_confidence,
                    "qc_value": qc_value,
                    "sector_num": sector_num,
                    "semi_major_axis": semi_major_axis,
                    "semi_minor_axis": semi_minor_axis,
                    "sig_pwrs": sig_pwrs,
                    "sig_strength": sig_strength,
                    "snrs": snrs,
                    "spec_avgs": spec_avgs,
                    "spec_widths": spec_widths,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "td_avg_sample_nums": td_avg_sample_nums,
                    "term_alt": term_alt,
                },
                weather_data_create_params.WeatherDataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WeatherDataListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/weatherdata",
            page=SyncOffsetPage[WeatherDataListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_list_params.WeatherDataListParams,
                ),
            ),
            model=WeatherDataListResponse,
        )

    def count(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/weatherdata/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_count_params.WeatherDataCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[weather_data_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple WeatherData as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/weatherdata/createBulk",
            body=maybe_transform(body, Iterable[weather_data_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WeatherDataFull:
        """
        Service operation to get a single WeatherData by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/weatherdata/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_get_params.WeatherDataGetParams,
                ),
            ),
            cast_to=WeatherDataFull,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/weatherdata/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WeatherDataTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/weatherdata/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_tuple_params.WeatherDataTupleParams,
                ),
            ),
            cast_to=WeatherDataTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[weather_data_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of WeatherData as a POST body and ingest into
        the database. This operation is intended to be used for automated feeds into
        UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-weatherdata",
            body=maybe_transform(body, Iterable[weather_data_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWeatherDataResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWeatherDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWeatherDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeatherDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncWeatherDataResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        angle_orientation: float | NotGiven = NOT_GIVEN,
        avg_ref_pwr: float | NotGiven = NOT_GIVEN,
        avg_tx_pwr: float | NotGiven = NOT_GIVEN,
        checksum: int | NotGiven = NOT_GIVEN,
        co_integs: Iterable[int] | NotGiven = NOT_GIVEN,
        cons_recs: Iterable[int] | NotGiven = NOT_GIVEN,
        dopp_vels: Iterable[float] | NotGiven = NOT_GIVEN,
        file_creation: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_guess_avgs: Iterable[int] | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        interpulse_periods: Iterable[float] | NotGiven = NOT_GIVEN,
        light_det_sensors: Iterable[int] | NotGiven = NOT_GIVEN,
        light_event_num: int | NotGiven = NOT_GIVEN,
        noise_lvls: Iterable[float] | NotGiven = NOT_GIVEN,
        num_elements: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pos_confidence: float | NotGiven = NOT_GIVEN,
        qc_value: int | NotGiven = NOT_GIVEN,
        sector_num: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        semi_minor_axis: float | NotGiven = NOT_GIVEN,
        sig_pwrs: Iterable[float] | NotGiven = NOT_GIVEN,
        sig_strength: float | NotGiven = NOT_GIVEN,
        snrs: Iterable[float] | NotGiven = NOT_GIVEN,
        spec_avgs: Iterable[int] | NotGiven = NOT_GIVEN,
        spec_widths: Iterable[float] | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        td_avg_sample_nums: Iterable[int] | NotGiven = NOT_GIVEN,
        term_alt: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single WeatherData as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          angle_orientation: Angle of orientation of the 50% positional confidence ellipse, in degrees
              clockwise from true north.

          avg_ref_pwr: Average power of the reflected signal received by the radar, in Watts.

          avg_tx_pwr: Average transmitted power of the radar, in kilowatts.

          checksum: Checksum value for the data.

          co_integs: Array of the number(s) of measurements used in coherent integrations used for
              radar data processing. Users should consult the data provider for information on
              the coherent integrations array structure.

          cons_recs: Array of the number(s) of records in consensus for a radar beam. Users should
              consult the data provider for information on the consensus records array
              structure.

          dopp_vels: Array of full scale Nyquist Doppler velocities measured by radar, in meters per
              second. Nyquist velocity refers to the maximum velocity magnitude that the radar
              system can unambiguously detect. Doppler velocities with absolute values
              exceeding the Nyquist threshold suffer from aliasing at the time of collection.
              Users should consult the data provider for information on the doppler velocities
              array structure.

          file_creation: Datetime the system files were created.

          first_guess_avgs: Array of average maximum number(s) of consecutive instances in which the same
              first guess velocity is used in radar data processing to estimate wind speed.
              Users should consult the data provider for information on the first guess
              averages array structure.

          id_sensor: Unique identifier of the sensor making the weather measurement.

          interpulse_periods: Array of the elapsed time(s) from the beginning of one pulse to the beginning of
              the next pulse for a radar beam, in microseconds. Users should consult the data
              provider for information on the interpulse periods array structure.

          light_det_sensors: Array of sensor(s) that participated in the lightning event location
              determination.

          light_event_num: Number of sensors used in the lightning event location solution.

          noise_lvls: Array of noise level(s) measured by radar, in decibels. Users should consult the
              data provider for information on the noise levels array structure.

          num_elements: Number of antennas across all sectors within the radar coverage area.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the record source. This may be an internal
              identifier and not necessarily a valid sensor ID.

          pos_confidence: The positional confidence of the calculated lightning event location using the
              chi-square statistical method.

          qc_value: Quality control flag value, as defined by the data provider.

          sector_num: Number of sectors within the radar coverage area, each containing a number of
              antennas.

          semi_major_axis: Semi-major axis of the 50% positional confidence ellipse, in kilometers.

          semi_minor_axis: Semi-minor axis of the 50% positional confidence ellipse, in kilometers.

          sig_pwrs: Array of signal power(s) measured by the sensor, in decibels. Users should
              consult the data provider for information on the signal powers array structure.

          sig_strength: Signal strength of the electromagnetic energy received due to a lightning event,
              in kiloamps.

          snrs: Array of signal to noise ratio(s) for a radar beam, in decibels. Users should
              consult the data provider for information on the signal to noise ratios array
              structure.

          spec_avgs: Array of the number(s) of spectral averages used in radar data processing. Users
              should consult the data provider for information on the spectral averages array
              structure.

          spec_widths: Array of width(s) of the distribution in Doppler velocity measured by radar, in
              meters/second. Spectral width depends on the particle size distribution, the
              wind shear across the radar beam, and turbulence. Users should consult the data
              provider for information on the spectral widths array structure.

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this WeatherData
              record. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. See the corresponding srcTyps array element
              for the data type of the UUID and use the appropriate API operation to retrieve
              that object.

          src_typs: Array of UDL record types (SENSOR, WEATHERREPORT) that are related to this
              WeatherData record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          td_avg_sample_nums: Array of the number(s) of radar samples used in time domain averaging for radar
              data processing. Time domain averaging improves the quality of the measured
              signal by reducing random noise and enhancing the signal-to-noise ratio. Users
              should consult the data provider for information on the time domain sample
              numbers array structure.

          term_alt: Last altitude with recorded measurements in this record, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/weatherdata",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "angle_orientation": angle_orientation,
                    "avg_ref_pwr": avg_ref_pwr,
                    "avg_tx_pwr": avg_tx_pwr,
                    "checksum": checksum,
                    "co_integs": co_integs,
                    "cons_recs": cons_recs,
                    "dopp_vels": dopp_vels,
                    "file_creation": file_creation,
                    "first_guess_avgs": first_guess_avgs,
                    "id_sensor": id_sensor,
                    "interpulse_periods": interpulse_periods,
                    "light_det_sensors": light_det_sensors,
                    "light_event_num": light_event_num,
                    "noise_lvls": noise_lvls,
                    "num_elements": num_elements,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "pos_confidence": pos_confidence,
                    "qc_value": qc_value,
                    "sector_num": sector_num,
                    "semi_major_axis": semi_major_axis,
                    "semi_minor_axis": semi_minor_axis,
                    "sig_pwrs": sig_pwrs,
                    "sig_strength": sig_strength,
                    "snrs": snrs,
                    "spec_avgs": spec_avgs,
                    "spec_widths": spec_widths,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "td_avg_sample_nums": td_avg_sample_nums,
                    "term_alt": term_alt,
                },
                weather_data_create_params.WeatherDataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WeatherDataListResponse, AsyncOffsetPage[WeatherDataListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/weatherdata",
            page=AsyncOffsetPage[WeatherDataListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_list_params.WeatherDataListParams,
                ),
            ),
            model=WeatherDataListResponse,
        )

    async def count(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/weatherdata/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_count_params.WeatherDataCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[weather_data_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple WeatherData as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/weatherdata/createBulk",
            body=await async_maybe_transform(body, Iterable[weather_data_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WeatherDataFull:
        """
        Service operation to get a single WeatherData by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/weatherdata/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_get_params.WeatherDataGetParams,
                ),
            ),
            cast_to=WeatherDataFull,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/weatherdata/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WeatherDataTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          ob_time: Datetime of the weather observation in ISO 8601 UTC datetime format with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/weatherdata/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_data_tuple_params.WeatherDataTupleParams,
                ),
            ),
            cast_to=WeatherDataTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[weather_data_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of WeatherData as a POST body and ingest into
        the database. This operation is intended to be used for automated feeds into
        UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-weatherdata",
            body=await async_maybe_transform(body, Iterable[weather_data_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WeatherDataResourceWithRawResponse:
    def __init__(self, weather_data: WeatherDataResource) -> None:
        self._weather_data = weather_data

        self.create = to_raw_response_wrapper(
            weather_data.create,
        )
        self.list = to_raw_response_wrapper(
            weather_data.list,
        )
        self.count = to_raw_response_wrapper(
            weather_data.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            weather_data.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            weather_data.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            weather_data.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            weather_data.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            weather_data.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._weather_data.history)


class AsyncWeatherDataResourceWithRawResponse:
    def __init__(self, weather_data: AsyncWeatherDataResource) -> None:
        self._weather_data = weather_data

        self.create = async_to_raw_response_wrapper(
            weather_data.create,
        )
        self.list = async_to_raw_response_wrapper(
            weather_data.list,
        )
        self.count = async_to_raw_response_wrapper(
            weather_data.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            weather_data.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            weather_data.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            weather_data.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            weather_data.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            weather_data.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._weather_data.history)


class WeatherDataResourceWithStreamingResponse:
    def __init__(self, weather_data: WeatherDataResource) -> None:
        self._weather_data = weather_data

        self.create = to_streamed_response_wrapper(
            weather_data.create,
        )
        self.list = to_streamed_response_wrapper(
            weather_data.list,
        )
        self.count = to_streamed_response_wrapper(
            weather_data.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            weather_data.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            weather_data.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            weather_data.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            weather_data.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            weather_data.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._weather_data.history)


class AsyncWeatherDataResourceWithStreamingResponse:
    def __init__(self, weather_data: AsyncWeatherDataResource) -> None:
        self._weather_data = weather_data

        self.create = async_to_streamed_response_wrapper(
            weather_data.create,
        )
        self.list = async_to_streamed_response_wrapper(
            weather_data.list,
        )
        self.count = async_to_streamed_response_wrapper(
            weather_data.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            weather_data.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            weather_data.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            weather_data.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            weather_data.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            weather_data.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._weather_data.history)
