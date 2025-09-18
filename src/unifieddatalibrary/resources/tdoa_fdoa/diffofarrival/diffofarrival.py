# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
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
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.tdoa_fdoa import (
    diffofarrival_list_params,
    diffofarrival_count_params,
    diffofarrival_create_params,
    diffofarrival_create_bulk_params,
)
from ....types.tdoa_fdoa.diffofarrival_abridged import DiffofarrivalAbridged

__all__ = ["DiffofarrivalResource", "AsyncDiffofarrivalResource"]


class DiffofarrivalResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiffofarrivalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DiffofarrivalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiffofarrivalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DiffofarrivalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | Omit = omit,
        bandwidth: float | Omit = omit,
        collection_mode: str | Omit = omit,
        delta_range: float | Omit = omit,
        delta_range_rate: float | Omit = omit,
        delta_range_rate_unc: float | Omit = omit,
        delta_range_unc: float | Omit = omit,
        descriptor: str | Omit = omit,
        fdoa: float | Omit = omit,
        fdoa_unc: float | Omit = omit,
        frequency: float | Omit = omit,
        id_sensor1: str | Omit = omit,
        id_sensor2: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        orig_sensor_id1: str | Omit = omit,
        orig_sensor_id2: str | Omit = omit,
        raw_file_uri: str | Omit = omit,
        sat_no: int | Omit = omit,
        sen2alt: float | Omit = omit,
        sen2lat: float | Omit = omit,
        sen2lon: float | Omit = omit,
        senalt: float | Omit = omit,
        senlat: float | Omit = omit,
        senlon: float | Omit = omit,
        sensor1_delay: float | Omit = omit,
        sensor2_delay: float | Omit = omit,
        snr: float | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        task_id: str | Omit = omit,
        tdoa: float | Omit = omit,
        tdoa_unc: float | Omit = omit,
        transaction_id: str | Omit = omit,
        uct: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single TDOA/FDOA record as a POST body and ingest
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

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          bandwidth: Bandwidth of the signal in Hz.

          collection_mode: Collection mode (e.g. SURVEY, SPOT_SEARCH, NEIGHBORHOOD_WATCH, DIRECTED_SEARCH,
              MANUAL, etc).

          delta_range: Delta range, in km. Delta range calculation convention is (sensor2 - sensor1).

          delta_range_rate: Delta range rate, in km/sec. Delta range rate calculation convention is
              (sensor2 - sensor1).

          delta_range_rate_unc: One sigma uncertainty in the delta range rate, in km/sec.

          delta_range_unc: One sigma uncertainty in delta range, in km.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          fdoa: Frequency difference of arrival of the center frequency signal, in Hz. FDOA
              calculation convention is (sensor2 - sensor1).

          fdoa_unc: One sigma uncertainty in frequency difference of arrival of the center frequency
              signal, in Hz.

          frequency: Center frequency of the collect in Hz.

          id_sensor1: Sensor ID of the primary/1st sensor used for this measurement.

          id_sensor2: Sensor ID of the secondary/2nd sensor used for this measurement.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id1: Optional identifier provided by DOA source to indicate the primary/1st sensor
              identifier used for this measurement. This may be an internal identifier and not
              necessarily a valid sensor ID.

          orig_sensor_id2: Optional identifier provided by DOA source to indicate the secondary/2nd sensor
              identifier used for this this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          sat_no: Catalog number of the target on-orbit object.

          sen2alt: Sensor 2 altitude at obTime (if mobile/onorbit) in km. If null, can be obtained
              from sensor info.

          sen2lat: Sensor 2 WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info.

          sen2lon: Sensor 2 WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info.

          senalt: Sensor altitude at obTime (if mobile/onorbit) in km. If null, can be obtained
              from sensor info.

          senlat: Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -180 to 180 degrees (negative values west of Prime
              Meridian).

          sensor1_delay: The signal arrival delay relative to sensor 1 in seconds.

          sensor2_delay: The signal arrival delay relative to sensor 2 in seconds.

          snr: Signal to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          tdoa: Time difference of arrival of the center frequency signal, in seconds. TDOA
              calculation convention is (sensor2 - sensor1).

          tdoa_unc: One sigma uncertainty in time difference of arrival of the center frequency
              signal, in seconds.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/diffofarrival",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "bandwidth": bandwidth,
                    "collection_mode": collection_mode,
                    "delta_range": delta_range,
                    "delta_range_rate": delta_range_rate,
                    "delta_range_rate_unc": delta_range_rate_unc,
                    "delta_range_unc": delta_range_unc,
                    "descriptor": descriptor,
                    "fdoa": fdoa,
                    "fdoa_unc": fdoa_unc,
                    "frequency": frequency,
                    "id_sensor1": id_sensor1,
                    "id_sensor2": id_sensor2,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id1": orig_sensor_id1,
                    "orig_sensor_id2": orig_sensor_id2,
                    "raw_file_uri": raw_file_uri,
                    "sat_no": sat_no,
                    "sen2alt": sen2alt,
                    "sen2lat": sen2lat,
                    "sen2lon": sen2lon,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sensor1_delay": sensor1_delay,
                    "sensor2_delay": sensor2_delay,
                    "snr": snr,
                    "tags": tags,
                    "task_id": task_id,
                    "tdoa": tdoa,
                    "tdoa_unc": tdoa_unc,
                    "transaction_id": transaction_id,
                    "uct": uct,
                },
                diffofarrival_create_params.DiffofarrivalCreateParams,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[DiffofarrivalAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/diffofarrival",
            page=SyncOffsetPage[DiffofarrivalAbridged],
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
                    diffofarrival_list_params.DiffofarrivalListParams,
                ),
            ),
            model=DiffofarrivalAbridged,
        )

    def count(
        self,
        *,
        ob_time: Union[str, datetime],
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
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/diffofarrival/count",
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
                    diffofarrival_count_params.DiffofarrivalCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[diffofarrival_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        TDOA/FDOA records as a POST body and ingest into the database. This operation is
        not intended to be used for automated feeds into UDL. Data providers should
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
            "/udl/diffofarrival/createBulk",
            body=maybe_transform(body, Iterable[diffofarrival_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDiffofarrivalResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiffofarrivalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDiffofarrivalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiffofarrivalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDiffofarrivalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | Omit = omit,
        bandwidth: float | Omit = omit,
        collection_mode: str | Omit = omit,
        delta_range: float | Omit = omit,
        delta_range_rate: float | Omit = omit,
        delta_range_rate_unc: float | Omit = omit,
        delta_range_unc: float | Omit = omit,
        descriptor: str | Omit = omit,
        fdoa: float | Omit = omit,
        fdoa_unc: float | Omit = omit,
        frequency: float | Omit = omit,
        id_sensor1: str | Omit = omit,
        id_sensor2: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        orig_sensor_id1: str | Omit = omit,
        orig_sensor_id2: str | Omit = omit,
        raw_file_uri: str | Omit = omit,
        sat_no: int | Omit = omit,
        sen2alt: float | Omit = omit,
        sen2lat: float | Omit = omit,
        sen2lon: float | Omit = omit,
        senalt: float | Omit = omit,
        senlat: float | Omit = omit,
        senlon: float | Omit = omit,
        sensor1_delay: float | Omit = omit,
        sensor2_delay: float | Omit = omit,
        snr: float | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        task_id: str | Omit = omit,
        tdoa: float | Omit = omit,
        tdoa_unc: float | Omit = omit,
        transaction_id: str | Omit = omit,
        uct: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single TDOA/FDOA record as a POST body and ingest
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

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          bandwidth: Bandwidth of the signal in Hz.

          collection_mode: Collection mode (e.g. SURVEY, SPOT_SEARCH, NEIGHBORHOOD_WATCH, DIRECTED_SEARCH,
              MANUAL, etc).

          delta_range: Delta range, in km. Delta range calculation convention is (sensor2 - sensor1).

          delta_range_rate: Delta range rate, in km/sec. Delta range rate calculation convention is
              (sensor2 - sensor1).

          delta_range_rate_unc: One sigma uncertainty in the delta range rate, in km/sec.

          delta_range_unc: One sigma uncertainty in delta range, in km.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          fdoa: Frequency difference of arrival of the center frequency signal, in Hz. FDOA
              calculation convention is (sensor2 - sensor1).

          fdoa_unc: One sigma uncertainty in frequency difference of arrival of the center frequency
              signal, in Hz.

          frequency: Center frequency of the collect in Hz.

          id_sensor1: Sensor ID of the primary/1st sensor used for this measurement.

          id_sensor2: Sensor ID of the secondary/2nd sensor used for this measurement.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id1: Optional identifier provided by DOA source to indicate the primary/1st sensor
              identifier used for this measurement. This may be an internal identifier and not
              necessarily a valid sensor ID.

          orig_sensor_id2: Optional identifier provided by DOA source to indicate the secondary/2nd sensor
              identifier used for this this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          sat_no: Catalog number of the target on-orbit object.

          sen2alt: Sensor 2 altitude at obTime (if mobile/onorbit) in km. If null, can be obtained
              from sensor info.

          sen2lat: Sensor 2 WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info.

          sen2lon: Sensor 2 WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info.

          senalt: Sensor altitude at obTime (if mobile/onorbit) in km. If null, can be obtained
              from sensor info.

          senlat: Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -180 to 180 degrees (negative values west of Prime
              Meridian).

          sensor1_delay: The signal arrival delay relative to sensor 1 in seconds.

          sensor2_delay: The signal arrival delay relative to sensor 2 in seconds.

          snr: Signal to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          tdoa: Time difference of arrival of the center frequency signal, in seconds. TDOA
              calculation convention is (sensor2 - sensor1).

          tdoa_unc: One sigma uncertainty in time difference of arrival of the center frequency
              signal, in seconds.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/diffofarrival",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "bandwidth": bandwidth,
                    "collection_mode": collection_mode,
                    "delta_range": delta_range,
                    "delta_range_rate": delta_range_rate,
                    "delta_range_rate_unc": delta_range_rate_unc,
                    "delta_range_unc": delta_range_unc,
                    "descriptor": descriptor,
                    "fdoa": fdoa,
                    "fdoa_unc": fdoa_unc,
                    "frequency": frequency,
                    "id_sensor1": id_sensor1,
                    "id_sensor2": id_sensor2,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id1": orig_sensor_id1,
                    "orig_sensor_id2": orig_sensor_id2,
                    "raw_file_uri": raw_file_uri,
                    "sat_no": sat_no,
                    "sen2alt": sen2alt,
                    "sen2lat": sen2lat,
                    "sen2lon": sen2lon,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sensor1_delay": sensor1_delay,
                    "sensor2_delay": sensor2_delay,
                    "snr": snr,
                    "tags": tags,
                    "task_id": task_id,
                    "tdoa": tdoa,
                    "tdoa_unc": tdoa_unc,
                    "transaction_id": transaction_id,
                    "uct": uct,
                },
                diffofarrival_create_params.DiffofarrivalCreateParams,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DiffofarrivalAbridged, AsyncOffsetPage[DiffofarrivalAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/diffofarrival",
            page=AsyncOffsetPage[DiffofarrivalAbridged],
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
                    diffofarrival_list_params.DiffofarrivalListParams,
                ),
            ),
            model=DiffofarrivalAbridged,
        )

    async def count(
        self,
        *,
        ob_time: Union[str, datetime],
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
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/diffofarrival/count",
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
                    diffofarrival_count_params.DiffofarrivalCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[diffofarrival_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        TDOA/FDOA records as a POST body and ingest into the database. This operation is
        not intended to be used for automated feeds into UDL. Data providers should
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
            "/udl/diffofarrival/createBulk",
            body=await async_maybe_transform(body, Iterable[diffofarrival_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DiffofarrivalResourceWithRawResponse:
    def __init__(self, diffofarrival: DiffofarrivalResource) -> None:
        self._diffofarrival = diffofarrival

        self.create = to_raw_response_wrapper(
            diffofarrival.create,
        )
        self.list = to_raw_response_wrapper(
            diffofarrival.list,
        )
        self.count = to_raw_response_wrapper(
            diffofarrival.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            diffofarrival.create_bulk,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._diffofarrival.history)


class AsyncDiffofarrivalResourceWithRawResponse:
    def __init__(self, diffofarrival: AsyncDiffofarrivalResource) -> None:
        self._diffofarrival = diffofarrival

        self.create = async_to_raw_response_wrapper(
            diffofarrival.create,
        )
        self.list = async_to_raw_response_wrapper(
            diffofarrival.list,
        )
        self.count = async_to_raw_response_wrapper(
            diffofarrival.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            diffofarrival.create_bulk,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._diffofarrival.history)


class DiffofarrivalResourceWithStreamingResponse:
    def __init__(self, diffofarrival: DiffofarrivalResource) -> None:
        self._diffofarrival = diffofarrival

        self.create = to_streamed_response_wrapper(
            diffofarrival.create,
        )
        self.list = to_streamed_response_wrapper(
            diffofarrival.list,
        )
        self.count = to_streamed_response_wrapper(
            diffofarrival.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            diffofarrival.create_bulk,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._diffofarrival.history)


class AsyncDiffofarrivalResourceWithStreamingResponse:
    def __init__(self, diffofarrival: AsyncDiffofarrivalResource) -> None:
        self._diffofarrival = diffofarrival

        self.create = async_to_streamed_response_wrapper(
            diffofarrival.create,
        )
        self.list = async_to_streamed_response_wrapper(
            diffofarrival.list,
        )
        self.count = async_to_streamed_response_wrapper(
            diffofarrival.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            diffofarrival.create_bulk,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._diffofarrival.history)
