# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.sensor import (
    calibration_count_params,
    calibration_query_params,
    calibration_tuple_params,
    calibration_create_params,
    calibration_retrieve_params,
    calibration_create_bulk_params,
    calibration_unvalidated_publish_params,
)
from ....types.sensor.calibration_query_response import CalibrationQueryResponse
from ....types.sensor.calibration_tuple_response import CalibrationTupleResponse
from ....types.sensor.calibration_retrieve_response import CalibrationRetrieveResponse
from ....types.sensor.calibration_query_help_response import CalibrationQueryHelpResponse

__all__ = ["CalibrationResource", "AsyncCalibrationResource"]


class CalibrationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CalibrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CalibrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalibrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CalibrationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_sensor: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        az_ra_accel_bias: float | NotGiven = NOT_GIVEN,
        az_ra_accel_sigma: float | NotGiven = NOT_GIVEN,
        az_ra_bias: float | NotGiven = NOT_GIVEN,
        az_ra_rate_bias: float | NotGiven = NOT_GIVEN,
        az_ra_rate_sigma: float | NotGiven = NOT_GIVEN,
        az_ra_rms: float | NotGiven = NOT_GIVEN,
        az_ra_sigma: float | NotGiven = NOT_GIVEN,
        cal_angle_ref: str | NotGiven = NOT_GIVEN,
        cal_track_mode: str | NotGiven = NOT_GIVEN,
        cal_type: str | NotGiven = NOT_GIVEN,
        confidence_noise_bias: float | NotGiven = NOT_GIVEN,
        duration: float | NotGiven = NOT_GIVEN,
        ecr: Iterable[float] | NotGiven = NOT_GIVEN,
        el_dec_accel_bias: float | NotGiven = NOT_GIVEN,
        el_dec_accel_sigma: float | NotGiven = NOT_GIVEN,
        el_dec_bias: float | NotGiven = NOT_GIVEN,
        el_dec_rate_bias: float | NotGiven = NOT_GIVEN,
        el_dec_rate_sigma: float | NotGiven = NOT_GIVEN,
        el_dec_rms: float | NotGiven = NOT_GIVEN,
        el_dec_sigma: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        num_az_ra_obs: int | NotGiven = NOT_GIVEN,
        num_el_dec_obs: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_photo_obs: int | NotGiven = NOT_GIVEN,
        num_range_obs: int | NotGiven = NOT_GIVEN,
        num_range_rate_obs: int | NotGiven = NOT_GIVEN,
        num_rcs_obs: int | NotGiven = NOT_GIVEN,
        num_time_obs: int | NotGiven = NOT_GIVEN,
        num_tracks: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        photo_bias: float | NotGiven = NOT_GIVEN,
        photo_sigma: float | NotGiven = NOT_GIVEN,
        range_accel_bias: float | NotGiven = NOT_GIVEN,
        range_accel_sigma: float | NotGiven = NOT_GIVEN,
        range_bias: float | NotGiven = NOT_GIVEN,
        range_rate_bias: float | NotGiven = NOT_GIVEN,
        range_rate_rms: float | NotGiven = NOT_GIVEN,
        range_rate_sigma: float | NotGiven = NOT_GIVEN,
        range_rms: float | NotGiven = NOT_GIVEN,
        range_sigma: float | NotGiven = NOT_GIVEN,
        rcs_bias: float | NotGiven = NOT_GIVEN,
        rcs_sigma: float | NotGiven = NOT_GIVEN,
        ref_targets: List[str] | NotGiven = NOT_GIVEN,
        ref_type: str | NotGiven = NOT_GIVEN,
        sen_type: str | NotGiven = NOT_GIVEN,
        time_bias: float | NotGiven = NOT_GIVEN,
        time_bias_sigma: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SensorCalibration as a POST body and ingest
        into the database. This operation is not intended to be used for automated feeds
        into UDL. Data providers should contact the UDL team for specific role
        assignments and for instructions on setting up a permanent feed through an
        alternate mechanism.

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

          id_sensor: Unique identifier of the sensor to which this calibration data applies. This ID
              can be used to obtain additional information on a sensor using the 'get by ID'
              operation (e.g. /udl/sensor/{id}). For example, the sensor with idSensor = abc
              would be queried as /udl/sensor/abc.

          source: Source of the data.

          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          az_ra_accel_bias: Sensor azimuth/right-ascension acceleration bias, in degrees per second squared.

          az_ra_accel_sigma: The standard deviation of the azimuth/right ascension acceleration residuals, in
              degrees, used to determine the sensor azimuth/right-ascension acceleration bias.

          az_ra_bias: Sensor azimuth/right-ascension bias, in degrees.

          az_ra_rate_bias: Sensor azimuth/right-ascension rate bias, in degrees per second.

          az_ra_rate_sigma: The standard deviation of the azimuth/right ascension rate residuals, in
              degrees, used to determine the sensor azimuth/right-ascension rate bias.

          az_ra_rms: The root mean square of the azimuth/right-ascension residuals, in degrees, used
              to determine the sensor azimuth/right-ascension bias.

          az_ra_sigma: The standard deviation of the azimuth/right ascension residuals, in degrees,
              used to determine the sensor azimuth/right-ascension bias.

          cal_angle_ref: Specifies the calibration reference angle set for this calibration data set.
              Azimuth and Elevation (AZEL) or Right Ascension and Declination (RADEC).

          cal_track_mode: Specifies that the calibration data are from INTRA_TRACK or INTER_TRACK
              residuals.

          cal_type: The basis of calibration values contained in this record (COMPUTED,
              OPERATIONAL).

          confidence_noise_bias: The confidence noise bias of the duration span.

          duration: Duration of the sensor calibration data which produced these values, measured in
              days.

          ecr: Three element array, expressing the sensor location in Earth Centered Rotating
              (ECR) coordinates, in kilometers. The array element order is [x, y, z].

          el_dec_accel_bias: Sensor elevation/declination acceleration bias, in degrees per second squared.

          el_dec_accel_sigma: The standard deviation of the elevation/declination acceleration residuals, in
              degrees, used to determine the sensor elevation/declination acceleration bias.

          el_dec_bias: Sensor elevation/declination bias, in degrees.

          el_dec_rate_bias: Sensor elevation/declination rate bias, in degrees per second.

          el_dec_rate_sigma: The standard deviation of the elevation/declination rate residuals, in degrees,
              used to determine the sensor elevation/declination rate bias.

          el_dec_rms: The root mean square of the elevation/declination residuals, in degrees, used to
              determine the sensor elevation/declination bias.

          el_dec_sigma: The standard deviation of the elevation/declination residuals, in degrees, used
              to determine the sensor elevation/declination bias.

          end_time: Calibration data span end time in ISO 8601 UTC format with millisecond
              precision. If provided, the endTime must be greater than or equal to the
              startTime in the SensorCalibration record.

          num_az_ra_obs: The number of observables used in determining the azimuth or right-ascension
              calibration values.

          num_el_dec_obs: The number of observables used in determining the elevation or declination
              calibration values.

          num_obs: The total number of observables available over the calibration span.

          num_photo_obs: The number of observables used in determining the photometric calibration
              values.

          num_range_obs: The number of observables used in determining the range calibration values.

          num_range_rate_obs: The number of observables used in determining the range rate calibration values.

          num_rcs_obs: The number of observables used in determining the radar cross section (RCS)
              calibration values.

          num_time_obs: The number of observables used in determining the time calibration values.

          num_tracks: The total number of tracks available over the calibration span.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          photo_bias: The sensor photometric observation magnitude bias, in visual magnitude.

          photo_sigma: The standard deviation of the magnitude residuals, in visual magnitude, used to
              determine the photometric bias.

          range_accel_bias: Sensor range rate acceleration bias, in kilometers per second squared.

          range_accel_sigma: The standard deviation of the range acceleration residuals, in kilometers per
              second squared, used to determine the sensor range acceleration bias.

          range_bias: Sensor range bias, in kilometers.

          range_rate_bias: Sensor range rate bias, in kilometers per second.

          range_rate_rms: The root mean square of the range rate residuals, in kilometers per second, used
              to determine the sensor range rate bias.

          range_rate_sigma: The standard deviation of the range rate residuals, in kilometers per second,
              used to determine the sensor range rate bias.

          range_rms: The root mean square of the range residuals, in kilometers, used to determine
              the sensor range bias.

          range_sigma: The standard deviation of the range residuals, in kilometers, used to determine
              the sensor range bias.

          rcs_bias: The sensor radar cross section (RCS) observation bias, in square meters.

          rcs_sigma: The standard deviation of the radar cross section residuals, in square meters,
              used to determine the radar cross section bias.

          ref_targets: Array of the catalog IDs of the reference targets used in the calibration.

          ref_type: The reference type used in the calibration.

          sen_type: The sensor type (MECHANICAL, OPTICAL, PHASED ARRAY, RF).

          time_bias: Sensor time bias, in seconds.

          time_bias_sigma: The standard deviation of the time residuals, in seconds, used to determine the
              sensor time bias.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/sensorcalibration",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_sensor": id_sensor,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "az_ra_accel_bias": az_ra_accel_bias,
                    "az_ra_accel_sigma": az_ra_accel_sigma,
                    "az_ra_bias": az_ra_bias,
                    "az_ra_rate_bias": az_ra_rate_bias,
                    "az_ra_rate_sigma": az_ra_rate_sigma,
                    "az_ra_rms": az_ra_rms,
                    "az_ra_sigma": az_ra_sigma,
                    "cal_angle_ref": cal_angle_ref,
                    "cal_track_mode": cal_track_mode,
                    "cal_type": cal_type,
                    "confidence_noise_bias": confidence_noise_bias,
                    "duration": duration,
                    "ecr": ecr,
                    "el_dec_accel_bias": el_dec_accel_bias,
                    "el_dec_accel_sigma": el_dec_accel_sigma,
                    "el_dec_bias": el_dec_bias,
                    "el_dec_rate_bias": el_dec_rate_bias,
                    "el_dec_rate_sigma": el_dec_rate_sigma,
                    "el_dec_rms": el_dec_rms,
                    "el_dec_sigma": el_dec_sigma,
                    "end_time": end_time,
                    "num_az_ra_obs": num_az_ra_obs,
                    "num_el_dec_obs": num_el_dec_obs,
                    "num_obs": num_obs,
                    "num_photo_obs": num_photo_obs,
                    "num_range_obs": num_range_obs,
                    "num_range_rate_obs": num_range_rate_obs,
                    "num_rcs_obs": num_rcs_obs,
                    "num_time_obs": num_time_obs,
                    "num_tracks": num_tracks,
                    "origin": origin,
                    "photo_bias": photo_bias,
                    "photo_sigma": photo_sigma,
                    "range_accel_bias": range_accel_bias,
                    "range_accel_sigma": range_accel_sigma,
                    "range_bias": range_bias,
                    "range_rate_bias": range_rate_bias,
                    "range_rate_rms": range_rate_rms,
                    "range_rate_sigma": range_rate_sigma,
                    "range_rms": range_rms,
                    "range_sigma": range_sigma,
                    "rcs_bias": rcs_bias,
                    "rcs_sigma": rcs_sigma,
                    "ref_targets": ref_targets,
                    "ref_type": ref_type,
                    "sen_type": sen_type,
                    "time_bias": time_bias,
                    "time_bias_sigma": time_bias_sigma,
                },
                calibration_create_params.CalibrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
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
    ) -> CalibrationRetrieveResponse:
        """
        Service operation to get a single SensorCalibration by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/sensorcalibration/{id}",
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
                    calibration_retrieve_params.CalibrationRetrieveParams,
                ),
            ),
            cast_to=CalibrationRetrieveResponse,
        )

    def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/sensorcalibration/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    calibration_count_params.CalibrationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[calibration_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        SensorCalibrations as a POST body and ingest into the database. This operation
        is not intended to be used for automated feeds into UDL. Data providers should
        contact the UDL team for specific role assignments and for instructions on
        setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/sensorcalibration/createBulk",
            body=maybe_transform(body, Iterable[calibration_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/sensorcalibration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    calibration_query_params.CalibrationQueryParams,
                ),
            ),
            cast_to=CalibrationQueryResponse,
        )

    def query_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/sensorcalibration/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationTupleResponse:
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

          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/sensorcalibration/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    calibration_tuple_params.CalibrationTupleParams,
                ),
            ),
            cast_to=CalibrationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[calibration_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple sensorcalibration records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-sensorcalibration",
            body=maybe_transform(body, Iterable[calibration_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCalibrationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCalibrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCalibrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalibrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCalibrationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_sensor: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        az_ra_accel_bias: float | NotGiven = NOT_GIVEN,
        az_ra_accel_sigma: float | NotGiven = NOT_GIVEN,
        az_ra_bias: float | NotGiven = NOT_GIVEN,
        az_ra_rate_bias: float | NotGiven = NOT_GIVEN,
        az_ra_rate_sigma: float | NotGiven = NOT_GIVEN,
        az_ra_rms: float | NotGiven = NOT_GIVEN,
        az_ra_sigma: float | NotGiven = NOT_GIVEN,
        cal_angle_ref: str | NotGiven = NOT_GIVEN,
        cal_track_mode: str | NotGiven = NOT_GIVEN,
        cal_type: str | NotGiven = NOT_GIVEN,
        confidence_noise_bias: float | NotGiven = NOT_GIVEN,
        duration: float | NotGiven = NOT_GIVEN,
        ecr: Iterable[float] | NotGiven = NOT_GIVEN,
        el_dec_accel_bias: float | NotGiven = NOT_GIVEN,
        el_dec_accel_sigma: float | NotGiven = NOT_GIVEN,
        el_dec_bias: float | NotGiven = NOT_GIVEN,
        el_dec_rate_bias: float | NotGiven = NOT_GIVEN,
        el_dec_rate_sigma: float | NotGiven = NOT_GIVEN,
        el_dec_rms: float | NotGiven = NOT_GIVEN,
        el_dec_sigma: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        num_az_ra_obs: int | NotGiven = NOT_GIVEN,
        num_el_dec_obs: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_photo_obs: int | NotGiven = NOT_GIVEN,
        num_range_obs: int | NotGiven = NOT_GIVEN,
        num_range_rate_obs: int | NotGiven = NOT_GIVEN,
        num_rcs_obs: int | NotGiven = NOT_GIVEN,
        num_time_obs: int | NotGiven = NOT_GIVEN,
        num_tracks: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        photo_bias: float | NotGiven = NOT_GIVEN,
        photo_sigma: float | NotGiven = NOT_GIVEN,
        range_accel_bias: float | NotGiven = NOT_GIVEN,
        range_accel_sigma: float | NotGiven = NOT_GIVEN,
        range_bias: float | NotGiven = NOT_GIVEN,
        range_rate_bias: float | NotGiven = NOT_GIVEN,
        range_rate_rms: float | NotGiven = NOT_GIVEN,
        range_rate_sigma: float | NotGiven = NOT_GIVEN,
        range_rms: float | NotGiven = NOT_GIVEN,
        range_sigma: float | NotGiven = NOT_GIVEN,
        rcs_bias: float | NotGiven = NOT_GIVEN,
        rcs_sigma: float | NotGiven = NOT_GIVEN,
        ref_targets: List[str] | NotGiven = NOT_GIVEN,
        ref_type: str | NotGiven = NOT_GIVEN,
        sen_type: str | NotGiven = NOT_GIVEN,
        time_bias: float | NotGiven = NOT_GIVEN,
        time_bias_sigma: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SensorCalibration as a POST body and ingest
        into the database. This operation is not intended to be used for automated feeds
        into UDL. Data providers should contact the UDL team for specific role
        assignments and for instructions on setting up a permanent feed through an
        alternate mechanism.

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

          id_sensor: Unique identifier of the sensor to which this calibration data applies. This ID
              can be used to obtain additional information on a sensor using the 'get by ID'
              operation (e.g. /udl/sensor/{id}). For example, the sensor with idSensor = abc
              would be queried as /udl/sensor/abc.

          source: Source of the data.

          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          az_ra_accel_bias: Sensor azimuth/right-ascension acceleration bias, in degrees per second squared.

          az_ra_accel_sigma: The standard deviation of the azimuth/right ascension acceleration residuals, in
              degrees, used to determine the sensor azimuth/right-ascension acceleration bias.

          az_ra_bias: Sensor azimuth/right-ascension bias, in degrees.

          az_ra_rate_bias: Sensor azimuth/right-ascension rate bias, in degrees per second.

          az_ra_rate_sigma: The standard deviation of the azimuth/right ascension rate residuals, in
              degrees, used to determine the sensor azimuth/right-ascension rate bias.

          az_ra_rms: The root mean square of the azimuth/right-ascension residuals, in degrees, used
              to determine the sensor azimuth/right-ascension bias.

          az_ra_sigma: The standard deviation of the azimuth/right ascension residuals, in degrees,
              used to determine the sensor azimuth/right-ascension bias.

          cal_angle_ref: Specifies the calibration reference angle set for this calibration data set.
              Azimuth and Elevation (AZEL) or Right Ascension and Declination (RADEC).

          cal_track_mode: Specifies that the calibration data are from INTRA_TRACK or INTER_TRACK
              residuals.

          cal_type: The basis of calibration values contained in this record (COMPUTED,
              OPERATIONAL).

          confidence_noise_bias: The confidence noise bias of the duration span.

          duration: Duration of the sensor calibration data which produced these values, measured in
              days.

          ecr: Three element array, expressing the sensor location in Earth Centered Rotating
              (ECR) coordinates, in kilometers. The array element order is [x, y, z].

          el_dec_accel_bias: Sensor elevation/declination acceleration bias, in degrees per second squared.

          el_dec_accel_sigma: The standard deviation of the elevation/declination acceleration residuals, in
              degrees, used to determine the sensor elevation/declination acceleration bias.

          el_dec_bias: Sensor elevation/declination bias, in degrees.

          el_dec_rate_bias: Sensor elevation/declination rate bias, in degrees per second.

          el_dec_rate_sigma: The standard deviation of the elevation/declination rate residuals, in degrees,
              used to determine the sensor elevation/declination rate bias.

          el_dec_rms: The root mean square of the elevation/declination residuals, in degrees, used to
              determine the sensor elevation/declination bias.

          el_dec_sigma: The standard deviation of the elevation/declination residuals, in degrees, used
              to determine the sensor elevation/declination bias.

          end_time: Calibration data span end time in ISO 8601 UTC format with millisecond
              precision. If provided, the endTime must be greater than or equal to the
              startTime in the SensorCalibration record.

          num_az_ra_obs: The number of observables used in determining the azimuth or right-ascension
              calibration values.

          num_el_dec_obs: The number of observables used in determining the elevation or declination
              calibration values.

          num_obs: The total number of observables available over the calibration span.

          num_photo_obs: The number of observables used in determining the photometric calibration
              values.

          num_range_obs: The number of observables used in determining the range calibration values.

          num_range_rate_obs: The number of observables used in determining the range rate calibration values.

          num_rcs_obs: The number of observables used in determining the radar cross section (RCS)
              calibration values.

          num_time_obs: The number of observables used in determining the time calibration values.

          num_tracks: The total number of tracks available over the calibration span.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          photo_bias: The sensor photometric observation magnitude bias, in visual magnitude.

          photo_sigma: The standard deviation of the magnitude residuals, in visual magnitude, used to
              determine the photometric bias.

          range_accel_bias: Sensor range rate acceleration bias, in kilometers per second squared.

          range_accel_sigma: The standard deviation of the range acceleration residuals, in kilometers per
              second squared, used to determine the sensor range acceleration bias.

          range_bias: Sensor range bias, in kilometers.

          range_rate_bias: Sensor range rate bias, in kilometers per second.

          range_rate_rms: The root mean square of the range rate residuals, in kilometers per second, used
              to determine the sensor range rate bias.

          range_rate_sigma: The standard deviation of the range rate residuals, in kilometers per second,
              used to determine the sensor range rate bias.

          range_rms: The root mean square of the range residuals, in kilometers, used to determine
              the sensor range bias.

          range_sigma: The standard deviation of the range residuals, in kilometers, used to determine
              the sensor range bias.

          rcs_bias: The sensor radar cross section (RCS) observation bias, in square meters.

          rcs_sigma: The standard deviation of the radar cross section residuals, in square meters,
              used to determine the radar cross section bias.

          ref_targets: Array of the catalog IDs of the reference targets used in the calibration.

          ref_type: The reference type used in the calibration.

          sen_type: The sensor type (MECHANICAL, OPTICAL, PHASED ARRAY, RF).

          time_bias: Sensor time bias, in seconds.

          time_bias_sigma: The standard deviation of the time residuals, in seconds, used to determine the
              sensor time bias.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/sensorcalibration",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_sensor": id_sensor,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "az_ra_accel_bias": az_ra_accel_bias,
                    "az_ra_accel_sigma": az_ra_accel_sigma,
                    "az_ra_bias": az_ra_bias,
                    "az_ra_rate_bias": az_ra_rate_bias,
                    "az_ra_rate_sigma": az_ra_rate_sigma,
                    "az_ra_rms": az_ra_rms,
                    "az_ra_sigma": az_ra_sigma,
                    "cal_angle_ref": cal_angle_ref,
                    "cal_track_mode": cal_track_mode,
                    "cal_type": cal_type,
                    "confidence_noise_bias": confidence_noise_bias,
                    "duration": duration,
                    "ecr": ecr,
                    "el_dec_accel_bias": el_dec_accel_bias,
                    "el_dec_accel_sigma": el_dec_accel_sigma,
                    "el_dec_bias": el_dec_bias,
                    "el_dec_rate_bias": el_dec_rate_bias,
                    "el_dec_rate_sigma": el_dec_rate_sigma,
                    "el_dec_rms": el_dec_rms,
                    "el_dec_sigma": el_dec_sigma,
                    "end_time": end_time,
                    "num_az_ra_obs": num_az_ra_obs,
                    "num_el_dec_obs": num_el_dec_obs,
                    "num_obs": num_obs,
                    "num_photo_obs": num_photo_obs,
                    "num_range_obs": num_range_obs,
                    "num_range_rate_obs": num_range_rate_obs,
                    "num_rcs_obs": num_rcs_obs,
                    "num_time_obs": num_time_obs,
                    "num_tracks": num_tracks,
                    "origin": origin,
                    "photo_bias": photo_bias,
                    "photo_sigma": photo_sigma,
                    "range_accel_bias": range_accel_bias,
                    "range_accel_sigma": range_accel_sigma,
                    "range_bias": range_bias,
                    "range_rate_bias": range_rate_bias,
                    "range_rate_rms": range_rate_rms,
                    "range_rate_sigma": range_rate_sigma,
                    "range_rms": range_rms,
                    "range_sigma": range_sigma,
                    "rcs_bias": rcs_bias,
                    "rcs_sigma": rcs_sigma,
                    "ref_targets": ref_targets,
                    "ref_type": ref_type,
                    "sen_type": sen_type,
                    "time_bias": time_bias,
                    "time_bias_sigma": time_bias_sigma,
                },
                calibration_create_params.CalibrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
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
    ) -> CalibrationRetrieveResponse:
        """
        Service operation to get a single SensorCalibration by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/sensorcalibration/{id}",
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
                    calibration_retrieve_params.CalibrationRetrieveParams,
                ),
            ),
            cast_to=CalibrationRetrieveResponse,
        )

    async def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/sensorcalibration/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    calibration_count_params.CalibrationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[calibration_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        SensorCalibrations as a POST body and ingest into the database. This operation
        is not intended to be used for automated feeds into UDL. Data providers should
        contact the UDL team for specific role assignments and for instructions on
        setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/sensorcalibration/createBulk",
            body=await async_maybe_transform(body, Iterable[calibration_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/sensorcalibration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    calibration_query_params.CalibrationQueryParams,
                ),
            ),
            cast_to=CalibrationQueryResponse,
        )

    async def query_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/sensorcalibration/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CalibrationTupleResponse:
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

          start_time: Calibration data span start time in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/sensorcalibration/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    calibration_tuple_params.CalibrationTupleParams,
                ),
            ),
            cast_to=CalibrationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[calibration_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple sensorcalibration records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-sensorcalibration",
            body=await async_maybe_transform(body, Iterable[calibration_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CalibrationResourceWithRawResponse:
    def __init__(self, calibration: CalibrationResource) -> None:
        self._calibration = calibration

        self.create = to_raw_response_wrapper(
            calibration.create,
        )
        self.retrieve = to_raw_response_wrapper(
            calibration.retrieve,
        )
        self.count = to_raw_response_wrapper(
            calibration.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            calibration.create_bulk,
        )
        self.query = to_raw_response_wrapper(
            calibration.query,
        )
        self.query_help = to_raw_response_wrapper(
            calibration.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            calibration.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            calibration.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._calibration.history)


class AsyncCalibrationResourceWithRawResponse:
    def __init__(self, calibration: AsyncCalibrationResource) -> None:
        self._calibration = calibration

        self.create = async_to_raw_response_wrapper(
            calibration.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            calibration.retrieve,
        )
        self.count = async_to_raw_response_wrapper(
            calibration.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            calibration.create_bulk,
        )
        self.query = async_to_raw_response_wrapper(
            calibration.query,
        )
        self.query_help = async_to_raw_response_wrapper(
            calibration.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            calibration.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            calibration.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._calibration.history)


class CalibrationResourceWithStreamingResponse:
    def __init__(self, calibration: CalibrationResource) -> None:
        self._calibration = calibration

        self.create = to_streamed_response_wrapper(
            calibration.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            calibration.retrieve,
        )
        self.count = to_streamed_response_wrapper(
            calibration.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            calibration.create_bulk,
        )
        self.query = to_streamed_response_wrapper(
            calibration.query,
        )
        self.query_help = to_streamed_response_wrapper(
            calibration.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            calibration.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            calibration.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._calibration.history)


class AsyncCalibrationResourceWithStreamingResponse:
    def __init__(self, calibration: AsyncCalibrationResource) -> None:
        self._calibration = calibration

        self.create = async_to_streamed_response_wrapper(
            calibration.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            calibration.retrieve,
        )
        self.count = async_to_streamed_response_wrapper(
            calibration.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            calibration.create_bulk,
        )
        self.query = async_to_streamed_response_wrapper(
            calibration.query,
        )
        self.query_help = async_to_streamed_response_wrapper(
            calibration.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            calibration.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            calibration.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._calibration.history)
