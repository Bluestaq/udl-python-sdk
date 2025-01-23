# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.filedrop import gnssrawif_create_params

__all__ = ["GnssrawifResource", "AsyncGnssrawifResource"]


class GnssrawifResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GnssrawifResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return GnssrawifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GnssrawifResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return GnssrawifResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        center_freq: Iterable[float],
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        file_name: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        bit_depth: int | NotGiven = NOT_GIVEN,
        boresight: Iterable[float] | NotGiven = NOT_GIVEN,
        data_rate: float | NotGiven = NOT_GIVEN,
        diff_code_bias: Iterable[float] | NotGiven = NOT_GIVEN,
        end_alt: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        event_id: str | NotGiven = NOT_GIVEN,
        if_freq: Iterable[float] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        post_fourier: List[str] | NotGiven = NOT_GIVEN,
        quat: Iterable[float] | NotGiven = NOT_GIVEN,
        receiver: str | NotGiven = NOT_GIVEN,
        sample_rate: Iterable[int] | NotGiven = NOT_GIVEN,
        sample_type: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sequence_id: int | NotGiven = NOT_GIVEN,
        set_id: str | NotGiven = NOT_GIVEN,
        set_length: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        start_alt: float | NotGiven = NOT_GIVEN,
        start_index: int | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """The GNSSRawIF service allows for contribution of raw GNSS IF data..

        This service
        operation requires a zip file in the body of the POST request. The zip file must
        contain exactly two files. <h3> 1) A json file with any file name that ends in
        .json e.g. payload.json The contents of the json file must be valid according to
        the schema for GNSSRawIF. 2) A .hdf5 file for GNSSRawIF. </h3> The metadata and
        hdf5 files will be stored and associated with each other allowing queries of the
        data retrieval of the binary images. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          center_freq: The center frequency, in MHz, of the observation bands. More than one band may
              be reported in each binary file, so this is an array of the center frequency of
              each band (including an array of length 1 if only one band is present).

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

          end_time: End time of the data contained in the associated binary file, in ISO 8601 UTC
              format with microsecond precision.

          file_name: The file name of the Raw IF Binary file. The files should be in the Hierarchical
              Data Format (HDF5).

          source: Source of the data.

          start_time: Start time of the data contained in the associated binary file, in ISO 8601 UTC
              format with microsecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          bit_depth: The number of bits in each datum, for example 2 for 2-bit integers or 8 for
              8-bit integers.

          boresight: Unit vector of the outward facing direction of the receiver boresight in a
              body-fixed coordinate system.

          data_rate: The amount of data generated per unit time, expressed in Megabytes/minute.

          diff_code_bias: Differential Code Biases (DCBs) are the systematic errors, or biases, between
              two GNSS code observations at the same or different frequencies. If applicable,
              this field should contain an array of DBC with length equal to the number of
              frequencies in the binary file. The reference frequency should show DCB equal
              to 0. If null, it is assumed that there is no DCB (all values are 0).

          end_alt: Spacecraft altitude at end time (endTime), expressed in kilometers above WGS-84
              ellipsoid.

          end_lat: WGS-84 spacecraft latitude sub-point at end time (endTime), represented as -90
              to 90 degrees (negative values south of equator).

          end_lon: WGS-84 spacecraft longitude sub-point at end time (endTime), represented as -180
              to 180 degrees (negative values west of Prime Meridian).

          es_id: Unique identifier of the parent Ephemeris Set, if this data is correlated with
              an Ephemeris. If reporting for a spacecraft with multiple onboard GNSS
              receivers, this ID may be associated with multiple GNSS Raw IF records if each
              receiver is synced to the ephemeris points.

          event_id: Optional source-provided identifier for this collection event. This field can be
              used to associate records related to the same event.

          if_freq: The center frequency, in MHz, after downconversion to intermediate frequency. If
              provided, this array should have the same length as centerFreqs.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the data source to indicate the target object of
              this record. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          post_fourier: After converting the raw data in the file, to generate (frequency-space) spectra
              some sets require an additional transformation or correction based on details of
              the hardware that recorded it. This field marks any such transformations.
              Currently supported options are NONE (no correction) and MIRRORED (frequency
              axis is flipped around the corresponding value of ifFreq). If null, it is
              assumed that NONE applies to all frequency bands.

          quat: The quaternion describing the rotation of the body-fixed frame used for this
              system into the local geodetic frame, at the sample start time (startTime). The
              array element order convention is scalar component first, followed by the three
              vector components. For a vector u in the body-fixed frame, the corresponding
              vector u' in the geodetic frame should satisfy u' = quq\\**, where q is this
              quaternion. The quaternion should be normalized to 1.

          receiver: The number or ID of the GNSS receiver associated with this data. If reporting
              for multiple receivers a separate record should be generated for each. If null,
              it is assumed to indicate that only one receiver is present, or reported.

          sample_rate: The number of samples taken per second.

          sample_type: The sample type associated with the IF data. REAL for data with only an
              I-component or COMPLEX for data with both I & Q components.

          sat_no: Satellite/catalog number of the target on-orbit object.

          sequence_id: The sequence number of a raw IF record/file within a set. Sequence number should
              start at 1. If null, then it is assumed that the order of records within a raw
              IF set is not relevant.

          set_id: User-defined ID of a set or sequence of records/files. Used to associate a set
              of related raw IF records.

          set_length: The number of raw IF records/files in a set.

          src_ids: Array of UUIDs of the UDL data records associated with this GNSSRawIF record.
              See the associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object (e.g.
              /udl/gnssobservationset/{uuid}).

          src_typs: Array of UDL record types (GNSSSET) associated with this GNSSRawIF record. See
              the associated 'srcIds' array for the record UUIDs, positionally corresponding
              to the record types in this array. The 'srcTyps' and 'srcIds' arrays must match
              in size.

          start_alt: Spacecraft altitude at start time (startTime), expressed in kilometers above
              WGS-84 ellipsoid.

          start_index: The index of the sample within the associated binary file that corresponds to
              the startTime indicated in this record. This is especially useful on high
              sample-rate sensors when some samples are less than one microsecond before the
              value of startTime. This index is 0-based. If null, the startIndex is assumed to
              be 0.

          start_lat: WGS-84 spacecraft latitude sub-point at start time (startTime), represented as
              -90 to 90 degrees (negative values south of equator).

          start_lon: WGS-84 spacecraft longitude sub-point at start time (startTime), represented as
              -180 to 180 degrees (negative values west of Prime Meridian).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-gnssrawif",
            body=maybe_transform(
                {
                    "center_freq": center_freq,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "file_name": file_name,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "bit_depth": bit_depth,
                    "boresight": boresight,
                    "data_rate": data_rate,
                    "diff_code_bias": diff_code_bias,
                    "end_alt": end_alt,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "es_id": es_id,
                    "event_id": event_id,
                    "if_freq": if_freq,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "post_fourier": post_fourier,
                    "quat": quat,
                    "receiver": receiver,
                    "sample_rate": sample_rate,
                    "sample_type": sample_type,
                    "sat_no": sat_no,
                    "sequence_id": sequence_id,
                    "set_id": set_id,
                    "set_length": set_length,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "start_alt": start_alt,
                    "start_index": start_index,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "tags": tags,
                },
                gnssrawif_create_params.GnssrawifCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGnssrawifResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGnssrawifResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGnssrawifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGnssrawifResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncGnssrawifResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        center_freq: Iterable[float],
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        file_name: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        bit_depth: int | NotGiven = NOT_GIVEN,
        boresight: Iterable[float] | NotGiven = NOT_GIVEN,
        data_rate: float | NotGiven = NOT_GIVEN,
        diff_code_bias: Iterable[float] | NotGiven = NOT_GIVEN,
        end_alt: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        event_id: str | NotGiven = NOT_GIVEN,
        if_freq: Iterable[float] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        post_fourier: List[str] | NotGiven = NOT_GIVEN,
        quat: Iterable[float] | NotGiven = NOT_GIVEN,
        receiver: str | NotGiven = NOT_GIVEN,
        sample_rate: Iterable[int] | NotGiven = NOT_GIVEN,
        sample_type: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sequence_id: int | NotGiven = NOT_GIVEN,
        set_id: str | NotGiven = NOT_GIVEN,
        set_length: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        start_alt: float | NotGiven = NOT_GIVEN,
        start_index: int | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """The GNSSRawIF service allows for contribution of raw GNSS IF data..

        This service
        operation requires a zip file in the body of the POST request. The zip file must
        contain exactly two files. <h3> 1) A json file with any file name that ends in
        .json e.g. payload.json The contents of the json file must be valid according to
        the schema for GNSSRawIF. 2) A .hdf5 file for GNSSRawIF. </h3> The metadata and
        hdf5 files will be stored and associated with each other allowing queries of the
        data retrieval of the binary images. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          center_freq: The center frequency, in MHz, of the observation bands. More than one band may
              be reported in each binary file, so this is an array of the center frequency of
              each band (including an array of length 1 if only one band is present).

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

          end_time: End time of the data contained in the associated binary file, in ISO 8601 UTC
              format with microsecond precision.

          file_name: The file name of the Raw IF Binary file. The files should be in the Hierarchical
              Data Format (HDF5).

          source: Source of the data.

          start_time: Start time of the data contained in the associated binary file, in ISO 8601 UTC
              format with microsecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          bit_depth: The number of bits in each datum, for example 2 for 2-bit integers or 8 for
              8-bit integers.

          boresight: Unit vector of the outward facing direction of the receiver boresight in a
              body-fixed coordinate system.

          data_rate: The amount of data generated per unit time, expressed in Megabytes/minute.

          diff_code_bias: Differential Code Biases (DCBs) are the systematic errors, or biases, between
              two GNSS code observations at the same or different frequencies. If applicable,
              this field should contain an array of DBC with length equal to the number of
              frequencies in the binary file. The reference frequency should show DCB equal
              to 0. If null, it is assumed that there is no DCB (all values are 0).

          end_alt: Spacecraft altitude at end time (endTime), expressed in kilometers above WGS-84
              ellipsoid.

          end_lat: WGS-84 spacecraft latitude sub-point at end time (endTime), represented as -90
              to 90 degrees (negative values south of equator).

          end_lon: WGS-84 spacecraft longitude sub-point at end time (endTime), represented as -180
              to 180 degrees (negative values west of Prime Meridian).

          es_id: Unique identifier of the parent Ephemeris Set, if this data is correlated with
              an Ephemeris. If reporting for a spacecraft with multiple onboard GNSS
              receivers, this ID may be associated with multiple GNSS Raw IF records if each
              receiver is synced to the ephemeris points.

          event_id: Optional source-provided identifier for this collection event. This field can be
              used to associate records related to the same event.

          if_freq: The center frequency, in MHz, after downconversion to intermediate frequency. If
              provided, this array should have the same length as centerFreqs.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the data source to indicate the target object of
              this record. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          post_fourier: After converting the raw data in the file, to generate (frequency-space) spectra
              some sets require an additional transformation or correction based on details of
              the hardware that recorded it. This field marks any such transformations.
              Currently supported options are NONE (no correction) and MIRRORED (frequency
              axis is flipped around the corresponding value of ifFreq). If null, it is
              assumed that NONE applies to all frequency bands.

          quat: The quaternion describing the rotation of the body-fixed frame used for this
              system into the local geodetic frame, at the sample start time (startTime). The
              array element order convention is scalar component first, followed by the three
              vector components. For a vector u in the body-fixed frame, the corresponding
              vector u' in the geodetic frame should satisfy u' = quq\\**, where q is this
              quaternion. The quaternion should be normalized to 1.

          receiver: The number or ID of the GNSS receiver associated with this data. If reporting
              for multiple receivers a separate record should be generated for each. If null,
              it is assumed to indicate that only one receiver is present, or reported.

          sample_rate: The number of samples taken per second.

          sample_type: The sample type associated with the IF data. REAL for data with only an
              I-component or COMPLEX for data with both I & Q components.

          sat_no: Satellite/catalog number of the target on-orbit object.

          sequence_id: The sequence number of a raw IF record/file within a set. Sequence number should
              start at 1. If null, then it is assumed that the order of records within a raw
              IF set is not relevant.

          set_id: User-defined ID of a set or sequence of records/files. Used to associate a set
              of related raw IF records.

          set_length: The number of raw IF records/files in a set.

          src_ids: Array of UUIDs of the UDL data records associated with this GNSSRawIF record.
              See the associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object (e.g.
              /udl/gnssobservationset/{uuid}).

          src_typs: Array of UDL record types (GNSSSET) associated with this GNSSRawIF record. See
              the associated 'srcIds' array for the record UUIDs, positionally corresponding
              to the record types in this array. The 'srcTyps' and 'srcIds' arrays must match
              in size.

          start_alt: Spacecraft altitude at start time (startTime), expressed in kilometers above
              WGS-84 ellipsoid.

          start_index: The index of the sample within the associated binary file that corresponds to
              the startTime indicated in this record. This is especially useful on high
              sample-rate sensors when some samples are less than one microsecond before the
              value of startTime. This index is 0-based. If null, the startIndex is assumed to
              be 0.

          start_lat: WGS-84 spacecraft latitude sub-point at start time (startTime), represented as
              -90 to 90 degrees (negative values south of equator).

          start_lon: WGS-84 spacecraft longitude sub-point at start time (startTime), represented as
              -180 to 180 degrees (negative values west of Prime Meridian).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-gnssrawif",
            body=await async_maybe_transform(
                {
                    "center_freq": center_freq,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "file_name": file_name,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "bit_depth": bit_depth,
                    "boresight": boresight,
                    "data_rate": data_rate,
                    "diff_code_bias": diff_code_bias,
                    "end_alt": end_alt,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "es_id": es_id,
                    "event_id": event_id,
                    "if_freq": if_freq,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "post_fourier": post_fourier,
                    "quat": quat,
                    "receiver": receiver,
                    "sample_rate": sample_rate,
                    "sample_type": sample_type,
                    "sat_no": sat_no,
                    "sequence_id": sequence_id,
                    "set_id": set_id,
                    "set_length": set_length,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "start_alt": start_alt,
                    "start_index": start_index,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "tags": tags,
                },
                gnssrawif_create_params.GnssrawifCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GnssrawifResourceWithRawResponse:
    def __init__(self, gnssrawif: GnssrawifResource) -> None:
        self._gnssrawif = gnssrawif

        self.create = to_raw_response_wrapper(
            gnssrawif.create,
        )


class AsyncGnssrawifResourceWithRawResponse:
    def __init__(self, gnssrawif: AsyncGnssrawifResource) -> None:
        self._gnssrawif = gnssrawif

        self.create = async_to_raw_response_wrapper(
            gnssrawif.create,
        )


class GnssrawifResourceWithStreamingResponse:
    def __init__(self, gnssrawif: GnssrawifResource) -> None:
        self._gnssrawif = gnssrawif

        self.create = to_streamed_response_wrapper(
            gnssrawif.create,
        )


class AsyncGnssrawifResourceWithStreamingResponse:
    def __init__(self, gnssrawif: AsyncGnssrawifResource) -> None:
        self._gnssrawif = gnssrawif

        self.create = async_to_streamed_response_wrapper(
            gnssrawif.create,
        )
