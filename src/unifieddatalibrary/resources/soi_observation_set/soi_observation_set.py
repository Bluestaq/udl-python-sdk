# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    soi_observation_set_get_params,
    soi_observation_set_list_params,
    soi_observation_set_count_params,
    soi_observation_set_tuple_params,
    soi_observation_set_create_params,
    soi_observation_set_create_bulk_params,
    soi_observation_set_unvalidated_publish_params,
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
from ...types.soi_observation_set_list_response import SoiObservationSetListResponse
from ...types.soi_observation_set_tuple_response import SoiObservationSetTupleResponse
from ...types.soi_observation_set.soi_observation_set_full import SoiObservationSetFull

__all__ = ["SoiObservationSetResource", "AsyncSoiObservationSetResource"]


class SoiObservationSetResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SoiObservationSetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SoiObservationSetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SoiObservationSetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SoiObservationSetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        num_obs: int,
        source: str,
        start_time: Union[str, datetime],
        type: Literal["OPTICAL", "RADAR"],
        id: str | NotGiven = NOT_GIVEN,
        binning_horiz: int | NotGiven = NOT_GIVEN,
        binning_vert: int | NotGiven = NOT_GIVEN,
        brightness_variance_change_detected: bool | NotGiven = NOT_GIVEN,
        calibrations: Iterable[soi_observation_set_create_params.Calibration] | NotGiven = NOT_GIVEN,
        calibration_type: str | NotGiven = NOT_GIVEN,
        change_conf: str | NotGiven = NOT_GIVEN,
        change_detected: bool | NotGiven = NOT_GIVEN,
        collection_density_conf: str | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        collection_mode: str | NotGiven = NOT_GIVEN,
        corr_quality: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        gain: float | NotGiven = NOT_GIVEN,
        id_elset: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        los_declination_end: float | NotGiven = NOT_GIVEN,
        los_declination_start: float | NotGiven = NOT_GIVEN,
        msg_create_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        num_spectral_filters: int | NotGiven = NOT_GIVEN,
        optical_soi_observation_list: Iterable[soi_observation_set_create_params.OpticalSoiObservationList]
        | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        percent_sat_threshold: float | NotGiven = NOT_GIVEN,
        periodicity_change_detected: bool | NotGiven = NOT_GIVEN,
        periodicity_detection_conf: str | NotGiven = NOT_GIVEN,
        periodicity_sampling_conf: str | NotGiven = NOT_GIVEN,
        pixel_array_height: int | NotGiven = NOT_GIVEN,
        pixel_array_width: int | NotGiven = NOT_GIVEN,
        pixel_max: int | NotGiven = NOT_GIVEN,
        pixel_min: int | NotGiven = NOT_GIVEN,
        pointing_angle_az_end: float | NotGiven = NOT_GIVEN,
        pointing_angle_az_start: float | NotGiven = NOT_GIVEN,
        pointing_angle_el_end: float | NotGiven = NOT_GIVEN,
        pointing_angle_el_start: float | NotGiven = NOT_GIVEN,
        polar_angle_end: float | NotGiven = NOT_GIVEN,
        polar_angle_start: float | NotGiven = NOT_GIVEN,
        radar_soi_observation_list: Iterable[soi_observation_set_create_params.RadarSoiObservationList]
        | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        satellite_name: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        sen_reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        sensor_as_id: str | NotGiven = NOT_GIVEN,
        senvelx: float | NotGiven = NOT_GIVEN,
        senvely: float | NotGiven = NOT_GIVEN,
        senvelz: float | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        software_version: str | NotGiven = NOT_GIVEN,
        solar_mag: float | NotGiven = NOT_GIVEN,
        solar_phase_angle_brightness_change_detected: bool | NotGiven = NOT_GIVEN,
        spectral_filters: List[str] | NotGiven = NOT_GIVEN,
        star_cat_name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        valid_calibrations: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SOIObservationSet record as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          num_obs: The number of observation records in the set.

          source: Source of the data.

          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.

          type: Observation type (OPTICAL, RADAR).

          id: Unique identifier of the record, auto-generated by the system.

          binning_horiz: The number of pixels binned horizontally.

          binning_vert: The number of pixels binned vertically.

          brightness_variance_change_detected: Boolean indicating if a brightness variance change event was detected, based on
              historical collection data for the object.

          calibrations: Array of SOI Calibrations associated with this SOIObservationSet.

          calibration_type: Type of calibration used by the Sensor (e.g. ALL SKY, DIFFERENTIAL, DEFAULT,
              NONE).

          change_conf: Overall qualitative confidence assessment of change detection results (e.g.
              HIGH, MEDIUM, LOW).

          change_detected: Boolean indicating if any change event was detected, based on historical
              collection data for the object.

          collection_density_conf: Qualitative Collection Density assessment, with respect to confidence of
              detecting a change event (e.g. HIGH, MEDIUM, LOW).

          collection_id: Universally Unique collection ID. Mechanism to correlate Single Point Photometry
              (SPP) JSON files to images.

          collection_mode: Mode indicating telescope movement during collection (AUTOTRACK, MANUAL
              AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).

          corr_quality: Object Correlation Quality value. Measures how close the observed object's orbit
              is to matching an object in the catalog. The scale of this field may vary
              depending on provider. Users should consult the data provider to verify the
              meaning of the value (e.g. A value of 0.0 indicates a high/strong correlation,
              while a value closer to 1.0 indicates low/weak correlation).

          end_time: Observation set detection end time in ISO 8601 UTC with microsecond precision.

          gain: The gain used during the collection, in units of photoelectrons per
              analog-to-digital unit (e-/ADU). If no gain is used, the value = 1.

          id_elset: ID of the UDL Elset of the Space Object under observation.

          id_sensor: ID of the observing sensor.

          los_declination_end: Line of sight declination at observation set detection end time. Specified in
              degrees, in the specified referenceFrame. If referenceFrame is null then J2K
              should be assumed (e.g -30 to 130.0).

          los_declination_start: Line of sight declination at observation set detection start time. Specified in
              degrees, in the specified referenceFrame. If referenceFrame is null then J2K
              should be assumed (e.g -30 to 130.0).

          msg_create_date: SOI msgCreateDate time in ISO 8601 UTC time, with millisecond precision.

          num_spectral_filters: The value is the number of spectral filters used.

          optical_soi_observation_list: OpticalSOIObservations associated with this SOIObservationSet.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier to which this attitude set applies if this set is reporting a single
              sensor orientation. This may be an internal identifier and not necessarily a
              valid sensor ID.

          percent_sat_threshold: A threshold for percent of pixels that make up object signal that are beyond the
              saturation point for the sensor that are removed in the EOSSA file, in range of
              0 to 1.

          periodicity_change_detected: Boolean indicating if a periodicity change event was detected, based on
              historical collection data for the object.

          periodicity_detection_conf: Qualitative assessment of the periodicity detection results from the Attitude
              and Shape Retrieval (ASR) Periodicity Assessment (PA) Tool (e.g. HIGH, MEDIUM,
              LOW).

          periodicity_sampling_conf: Qualitative Periodicity Sampling assessment, with respect to confidence of
              detecting a change event (e.g. HIGH, MEDIUM, LOW).

          pixel_array_height: Pixel array size (height) in pixels.

          pixel_array_width: Pixel array size (width) in pixels.

          pixel_max: The maximum valid pixel value.

          pixel_min: The minimum valid pixel value.

          pointing_angle_az_end: Pointing angle of the Azimuth gimbal/mount at observation set detection end
              time. Specified in degrees.

          pointing_angle_az_start: Pointing angle of the Azimuth gimbal/mount at observation set detection start
              time. Specified in degrees.

          pointing_angle_el_end: Pointing angle of the Elevation gimbal/mount at observation set detection end
              time. Specified in degrees.

          pointing_angle_el_start: Pointing angle of the Elevation gimbal/mount at observation set detection start
              time. Specified in degrees.

          polar_angle_end: Polar angle of the gimbal/mount at observation set detection end time in
              degrees.

          polar_angle_start: Polar angle of the gimbal/mount at observation set detection start time in
              degrees.

          radar_soi_observation_list: RadarSOIObservations associated with this RadarSOIObservationSet.

          reference_frame: The reference frame of the observation measurements. If the referenceFrame is
              null it is assumed to be J2000.

          satellite_name: Name of the target satellite.

          sat_no: Satellite/catalog number of the target on-orbit object.

          senalt: Sensor altitude at startTime (if mobile/onorbit) in kilometers.

          senlat: Sensor WGS84 latitude at startTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info. -90 to 90 degrees (negative values south of
              equator).

          senlon: Sensor WGS84 longitude at startTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info. -180 to 180 degrees (negative values south of
              equator).

          sen_reference_frame: The reference frame of the observing sensor state. If the senReferenceFrame is
              null it is assumed to be J2000.

          sensor_as_id: ID of the AttitudeSet record for the observing sensor.

          senvelx: Cartesian X velocity of the observing mobile/onorbit sensor at startTime, in
              kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
              is null then J2K should be assumed.

          senvely: Cartesian Y velocity of the observing mobile/onorbit sensor at startTime, in
              kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
              is null then J2K should be assumed.

          senvelz: Cartesian Z velocity of the observing mobile/onorbit sensor at startTime, in
              kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
              is null then J2K should be assumed.

          senx: Cartesian X position of the observing mobile/onorbit sensor at startTime, in
              kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
              then J2K should be assumed.

          seny: Cartesian Y position of the observing mobile/onorbit sensor at startTime, in
              kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
              then J2K should be assumed.

          senz: Cartesian Z position of the observing mobile/onorbit sensor at startTime, in
              kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
              then J2K should be assumed.

          software_version: Software Version used to Capture, Process, and Deliver the data.

          solar_mag: The in-band solar magnitude at 1 A.U.

          solar_phase_angle_brightness_change_detected: Boolean indicating if a solar phase angle brightness change event was detected,
              based on historical collection data for the object.

          spectral_filters: Array of the SpectralFilters keywords, must be present for all values n=1 to
              numSpectralFilters, in incrementing order of n, and for no other values of n.

          star_cat_name: Name of the Star Catalog used for photometry and astrometry.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating whether the target object was unable to be correlated to a
              known object. This flag should only be set to true by data providers after an
              attempt to correlate to an OnOrbit object was made and failed. If unable to
              correlate, the 'origObjectId' field may be populated with an internal data
              provider specific identifier.

          valid_calibrations: Key to indicate which, if any of, the pre/post photometer calibrations are valid
              for use when generating data for the EOSSA file. If the field is not populated,
              then the provided calibration data will be used when generating the EOSSA file
              (e.g. PRE, POST, BOTH, NONE).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/soiobservationset",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "num_obs": num_obs,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "binning_horiz": binning_horiz,
                    "binning_vert": binning_vert,
                    "brightness_variance_change_detected": brightness_variance_change_detected,
                    "calibrations": calibrations,
                    "calibration_type": calibration_type,
                    "change_conf": change_conf,
                    "change_detected": change_detected,
                    "collection_density_conf": collection_density_conf,
                    "collection_id": collection_id,
                    "collection_mode": collection_mode,
                    "corr_quality": corr_quality,
                    "end_time": end_time,
                    "gain": gain,
                    "id_elset": id_elset,
                    "id_sensor": id_sensor,
                    "los_declination_end": los_declination_end,
                    "los_declination_start": los_declination_start,
                    "msg_create_date": msg_create_date,
                    "num_spectral_filters": num_spectral_filters,
                    "optical_soi_observation_list": optical_soi_observation_list,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "percent_sat_threshold": percent_sat_threshold,
                    "periodicity_change_detected": periodicity_change_detected,
                    "periodicity_detection_conf": periodicity_detection_conf,
                    "periodicity_sampling_conf": periodicity_sampling_conf,
                    "pixel_array_height": pixel_array_height,
                    "pixel_array_width": pixel_array_width,
                    "pixel_max": pixel_max,
                    "pixel_min": pixel_min,
                    "pointing_angle_az_end": pointing_angle_az_end,
                    "pointing_angle_az_start": pointing_angle_az_start,
                    "pointing_angle_el_end": pointing_angle_el_end,
                    "pointing_angle_el_start": pointing_angle_el_start,
                    "polar_angle_end": polar_angle_end,
                    "polar_angle_start": polar_angle_start,
                    "radar_soi_observation_list": radar_soi_observation_list,
                    "reference_frame": reference_frame,
                    "satellite_name": satellite_name,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sen_reference_frame": sen_reference_frame,
                    "sensor_as_id": sensor_as_id,
                    "senvelx": senvelx,
                    "senvely": senvely,
                    "senvelz": senvelz,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "software_version": software_version,
                    "solar_mag": solar_mag,
                    "solar_phase_angle_brightness_change_detected": solar_phase_angle_brightness_change_detected,
                    "spectral_filters": spectral_filters,
                    "star_cat_name": star_cat_name,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "valid_calibrations": valid_calibrations,
                },
                soi_observation_set_create_params.SoiObservationSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
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
    ) -> SyncOffsetPage[SoiObservationSetListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters.
        The query will return the SOI Observation Sets and not the associated SOI
        Observations. See the queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for
        more details on valid/required query parameter information.

        Args:
          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/soiobservationset",
            page=SyncOffsetPage[SoiObservationSetListResponse],
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
                    soi_observation_set_list_params.SoiObservationSetListParams,
                ),
            ),
            model=SoiObservationSetListResponse,
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
          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/soiobservationset/count",
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
                    soi_observation_set_count_params.SoiObservationSetCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[soi_observation_set_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        SOIObservationSet records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/soiobservationset/createBulk",
            body=maybe_transform(body, Iterable[soi_observation_set_create_bulk_params.Body]),
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
    ) -> SoiObservationSetFull:
        """
        Service operation to get a single SOIObservationSet by its unique ID passed as a
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
            f"/udl/soiobservationset/{id}",
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
                    soi_observation_set_get_params.SoiObservationSetGetParams,
                ),
            ),
            cast_to=SoiObservationSetFull,
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
            "/udl/soiobservationset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SoiObservationSetTupleResponse:
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

          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/soiobservationset/tuple",
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
                    soi_observation_set_tuple_params.SoiObservationSetTupleParams,
                ),
            ),
            cast_to=SoiObservationSetTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[soi_observation_set_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple SOIObservationSet records as a POST body and
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
            "/filedrop/udl-soiobservationset",
            body=maybe_transform(body, Iterable[soi_observation_set_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSoiObservationSetResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSoiObservationSetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSoiObservationSetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSoiObservationSetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSoiObservationSetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        num_obs: int,
        source: str,
        start_time: Union[str, datetime],
        type: Literal["OPTICAL", "RADAR"],
        id: str | NotGiven = NOT_GIVEN,
        binning_horiz: int | NotGiven = NOT_GIVEN,
        binning_vert: int | NotGiven = NOT_GIVEN,
        brightness_variance_change_detected: bool | NotGiven = NOT_GIVEN,
        calibrations: Iterable[soi_observation_set_create_params.Calibration] | NotGiven = NOT_GIVEN,
        calibration_type: str | NotGiven = NOT_GIVEN,
        change_conf: str | NotGiven = NOT_GIVEN,
        change_detected: bool | NotGiven = NOT_GIVEN,
        collection_density_conf: str | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        collection_mode: str | NotGiven = NOT_GIVEN,
        corr_quality: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        gain: float | NotGiven = NOT_GIVEN,
        id_elset: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        los_declination_end: float | NotGiven = NOT_GIVEN,
        los_declination_start: float | NotGiven = NOT_GIVEN,
        msg_create_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        num_spectral_filters: int | NotGiven = NOT_GIVEN,
        optical_soi_observation_list: Iterable[soi_observation_set_create_params.OpticalSoiObservationList]
        | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        percent_sat_threshold: float | NotGiven = NOT_GIVEN,
        periodicity_change_detected: bool | NotGiven = NOT_GIVEN,
        periodicity_detection_conf: str | NotGiven = NOT_GIVEN,
        periodicity_sampling_conf: str | NotGiven = NOT_GIVEN,
        pixel_array_height: int | NotGiven = NOT_GIVEN,
        pixel_array_width: int | NotGiven = NOT_GIVEN,
        pixel_max: int | NotGiven = NOT_GIVEN,
        pixel_min: int | NotGiven = NOT_GIVEN,
        pointing_angle_az_end: float | NotGiven = NOT_GIVEN,
        pointing_angle_az_start: float | NotGiven = NOT_GIVEN,
        pointing_angle_el_end: float | NotGiven = NOT_GIVEN,
        pointing_angle_el_start: float | NotGiven = NOT_GIVEN,
        polar_angle_end: float | NotGiven = NOT_GIVEN,
        polar_angle_start: float | NotGiven = NOT_GIVEN,
        radar_soi_observation_list: Iterable[soi_observation_set_create_params.RadarSoiObservationList]
        | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        satellite_name: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        sen_reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        sensor_as_id: str | NotGiven = NOT_GIVEN,
        senvelx: float | NotGiven = NOT_GIVEN,
        senvely: float | NotGiven = NOT_GIVEN,
        senvelz: float | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        software_version: str | NotGiven = NOT_GIVEN,
        solar_mag: float | NotGiven = NOT_GIVEN,
        solar_phase_angle_brightness_change_detected: bool | NotGiven = NOT_GIVEN,
        spectral_filters: List[str] | NotGiven = NOT_GIVEN,
        star_cat_name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        valid_calibrations: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SOIObservationSet record as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          num_obs: The number of observation records in the set.

          source: Source of the data.

          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.

          type: Observation type (OPTICAL, RADAR).

          id: Unique identifier of the record, auto-generated by the system.

          binning_horiz: The number of pixels binned horizontally.

          binning_vert: The number of pixels binned vertically.

          brightness_variance_change_detected: Boolean indicating if a brightness variance change event was detected, based on
              historical collection data for the object.

          calibrations: Array of SOI Calibrations associated with this SOIObservationSet.

          calibration_type: Type of calibration used by the Sensor (e.g. ALL SKY, DIFFERENTIAL, DEFAULT,
              NONE).

          change_conf: Overall qualitative confidence assessment of change detection results (e.g.
              HIGH, MEDIUM, LOW).

          change_detected: Boolean indicating if any change event was detected, based on historical
              collection data for the object.

          collection_density_conf: Qualitative Collection Density assessment, with respect to confidence of
              detecting a change event (e.g. HIGH, MEDIUM, LOW).

          collection_id: Universally Unique collection ID. Mechanism to correlate Single Point Photometry
              (SPP) JSON files to images.

          collection_mode: Mode indicating telescope movement during collection (AUTOTRACK, MANUAL
              AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).

          corr_quality: Object Correlation Quality value. Measures how close the observed object's orbit
              is to matching an object in the catalog. The scale of this field may vary
              depending on provider. Users should consult the data provider to verify the
              meaning of the value (e.g. A value of 0.0 indicates a high/strong correlation,
              while a value closer to 1.0 indicates low/weak correlation).

          end_time: Observation set detection end time in ISO 8601 UTC with microsecond precision.

          gain: The gain used during the collection, in units of photoelectrons per
              analog-to-digital unit (e-/ADU). If no gain is used, the value = 1.

          id_elset: ID of the UDL Elset of the Space Object under observation.

          id_sensor: ID of the observing sensor.

          los_declination_end: Line of sight declination at observation set detection end time. Specified in
              degrees, in the specified referenceFrame. If referenceFrame is null then J2K
              should be assumed (e.g -30 to 130.0).

          los_declination_start: Line of sight declination at observation set detection start time. Specified in
              degrees, in the specified referenceFrame. If referenceFrame is null then J2K
              should be assumed (e.g -30 to 130.0).

          msg_create_date: SOI msgCreateDate time in ISO 8601 UTC time, with millisecond precision.

          num_spectral_filters: The value is the number of spectral filters used.

          optical_soi_observation_list: OpticalSOIObservations associated with this SOIObservationSet.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier to which this attitude set applies if this set is reporting a single
              sensor orientation. This may be an internal identifier and not necessarily a
              valid sensor ID.

          percent_sat_threshold: A threshold for percent of pixels that make up object signal that are beyond the
              saturation point for the sensor that are removed in the EOSSA file, in range of
              0 to 1.

          periodicity_change_detected: Boolean indicating if a periodicity change event was detected, based on
              historical collection data for the object.

          periodicity_detection_conf: Qualitative assessment of the periodicity detection results from the Attitude
              and Shape Retrieval (ASR) Periodicity Assessment (PA) Tool (e.g. HIGH, MEDIUM,
              LOW).

          periodicity_sampling_conf: Qualitative Periodicity Sampling assessment, with respect to confidence of
              detecting a change event (e.g. HIGH, MEDIUM, LOW).

          pixel_array_height: Pixel array size (height) in pixels.

          pixel_array_width: Pixel array size (width) in pixels.

          pixel_max: The maximum valid pixel value.

          pixel_min: The minimum valid pixel value.

          pointing_angle_az_end: Pointing angle of the Azimuth gimbal/mount at observation set detection end
              time. Specified in degrees.

          pointing_angle_az_start: Pointing angle of the Azimuth gimbal/mount at observation set detection start
              time. Specified in degrees.

          pointing_angle_el_end: Pointing angle of the Elevation gimbal/mount at observation set detection end
              time. Specified in degrees.

          pointing_angle_el_start: Pointing angle of the Elevation gimbal/mount at observation set detection start
              time. Specified in degrees.

          polar_angle_end: Polar angle of the gimbal/mount at observation set detection end time in
              degrees.

          polar_angle_start: Polar angle of the gimbal/mount at observation set detection start time in
              degrees.

          radar_soi_observation_list: RadarSOIObservations associated with this RadarSOIObservationSet.

          reference_frame: The reference frame of the observation measurements. If the referenceFrame is
              null it is assumed to be J2000.

          satellite_name: Name of the target satellite.

          sat_no: Satellite/catalog number of the target on-orbit object.

          senalt: Sensor altitude at startTime (if mobile/onorbit) in kilometers.

          senlat: Sensor WGS84 latitude at startTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info. -90 to 90 degrees (negative values south of
              equator).

          senlon: Sensor WGS84 longitude at startTime (if mobile/onorbit) in degrees. If null, can
              be obtained from sensor info. -180 to 180 degrees (negative values south of
              equator).

          sen_reference_frame: The reference frame of the observing sensor state. If the senReferenceFrame is
              null it is assumed to be J2000.

          sensor_as_id: ID of the AttitudeSet record for the observing sensor.

          senvelx: Cartesian X velocity of the observing mobile/onorbit sensor at startTime, in
              kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
              is null then J2K should be assumed.

          senvely: Cartesian Y velocity of the observing mobile/onorbit sensor at startTime, in
              kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
              is null then J2K should be assumed.

          senvelz: Cartesian Z velocity of the observing mobile/onorbit sensor at startTime, in
              kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
              is null then J2K should be assumed.

          senx: Cartesian X position of the observing mobile/onorbit sensor at startTime, in
              kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
              then J2K should be assumed.

          seny: Cartesian Y position of the observing mobile/onorbit sensor at startTime, in
              kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
              then J2K should be assumed.

          senz: Cartesian Z position of the observing mobile/onorbit sensor at startTime, in
              kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
              then J2K should be assumed.

          software_version: Software Version used to Capture, Process, and Deliver the data.

          solar_mag: The in-band solar magnitude at 1 A.U.

          solar_phase_angle_brightness_change_detected: Boolean indicating if a solar phase angle brightness change event was detected,
              based on historical collection data for the object.

          spectral_filters: Array of the SpectralFilters keywords, must be present for all values n=1 to
              numSpectralFilters, in incrementing order of n, and for no other values of n.

          star_cat_name: Name of the Star Catalog used for photometry and astrometry.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating whether the target object was unable to be correlated to a
              known object. This flag should only be set to true by data providers after an
              attempt to correlate to an OnOrbit object was made and failed. If unable to
              correlate, the 'origObjectId' field may be populated with an internal data
              provider specific identifier.

          valid_calibrations: Key to indicate which, if any of, the pre/post photometer calibrations are valid
              for use when generating data for the EOSSA file. If the field is not populated,
              then the provided calibration data will be used when generating the EOSSA file
              (e.g. PRE, POST, BOTH, NONE).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/soiobservationset",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "num_obs": num_obs,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "binning_horiz": binning_horiz,
                    "binning_vert": binning_vert,
                    "brightness_variance_change_detected": brightness_variance_change_detected,
                    "calibrations": calibrations,
                    "calibration_type": calibration_type,
                    "change_conf": change_conf,
                    "change_detected": change_detected,
                    "collection_density_conf": collection_density_conf,
                    "collection_id": collection_id,
                    "collection_mode": collection_mode,
                    "corr_quality": corr_quality,
                    "end_time": end_time,
                    "gain": gain,
                    "id_elset": id_elset,
                    "id_sensor": id_sensor,
                    "los_declination_end": los_declination_end,
                    "los_declination_start": los_declination_start,
                    "msg_create_date": msg_create_date,
                    "num_spectral_filters": num_spectral_filters,
                    "optical_soi_observation_list": optical_soi_observation_list,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "percent_sat_threshold": percent_sat_threshold,
                    "periodicity_change_detected": periodicity_change_detected,
                    "periodicity_detection_conf": periodicity_detection_conf,
                    "periodicity_sampling_conf": periodicity_sampling_conf,
                    "pixel_array_height": pixel_array_height,
                    "pixel_array_width": pixel_array_width,
                    "pixel_max": pixel_max,
                    "pixel_min": pixel_min,
                    "pointing_angle_az_end": pointing_angle_az_end,
                    "pointing_angle_az_start": pointing_angle_az_start,
                    "pointing_angle_el_end": pointing_angle_el_end,
                    "pointing_angle_el_start": pointing_angle_el_start,
                    "polar_angle_end": polar_angle_end,
                    "polar_angle_start": polar_angle_start,
                    "radar_soi_observation_list": radar_soi_observation_list,
                    "reference_frame": reference_frame,
                    "satellite_name": satellite_name,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sen_reference_frame": sen_reference_frame,
                    "sensor_as_id": sensor_as_id,
                    "senvelx": senvelx,
                    "senvely": senvely,
                    "senvelz": senvelz,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "software_version": software_version,
                    "solar_mag": solar_mag,
                    "solar_phase_angle_brightness_change_detected": solar_phase_angle_brightness_change_detected,
                    "spectral_filters": spectral_filters,
                    "star_cat_name": star_cat_name,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "valid_calibrations": valid_calibrations,
                },
                soi_observation_set_create_params.SoiObservationSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
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
    ) -> AsyncPaginator[SoiObservationSetListResponse, AsyncOffsetPage[SoiObservationSetListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters.
        The query will return the SOI Observation Sets and not the associated SOI
        Observations. See the queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for
        more details on valid/required query parameter information.

        Args:
          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/soiobservationset",
            page=AsyncOffsetPage[SoiObservationSetListResponse],
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
                    soi_observation_set_list_params.SoiObservationSetListParams,
                ),
            ),
            model=SoiObservationSetListResponse,
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
          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/soiobservationset/count",
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
                    soi_observation_set_count_params.SoiObservationSetCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[soi_observation_set_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        SOIObservationSet records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/soiobservationset/createBulk",
            body=await async_maybe_transform(body, Iterable[soi_observation_set_create_bulk_params.Body]),
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
    ) -> SoiObservationSetFull:
        """
        Service operation to get a single SOIObservationSet by its unique ID passed as a
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
            f"/udl/soiobservationset/{id}",
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
                    soi_observation_set_get_params.SoiObservationSetGetParams,
                ),
            ),
            cast_to=SoiObservationSetFull,
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
            "/udl/soiobservationset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SoiObservationSetTupleResponse:
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

          start_time: Observation set detection start time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/soiobservationset/tuple",
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
                    soi_observation_set_tuple_params.SoiObservationSetTupleParams,
                ),
            ),
            cast_to=SoiObservationSetTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[soi_observation_set_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple SOIObservationSet records as a POST body and
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
            "/filedrop/udl-soiobservationset",
            body=await async_maybe_transform(body, Iterable[soi_observation_set_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SoiObservationSetResourceWithRawResponse:
    def __init__(self, soi_observation_set: SoiObservationSetResource) -> None:
        self._soi_observation_set = soi_observation_set

        self.create = to_raw_response_wrapper(
            soi_observation_set.create,
        )
        self.list = to_raw_response_wrapper(
            soi_observation_set.list,
        )
        self.count = to_raw_response_wrapper(
            soi_observation_set.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            soi_observation_set.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            soi_observation_set.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            soi_observation_set.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            soi_observation_set.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            soi_observation_set.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._soi_observation_set.history)


class AsyncSoiObservationSetResourceWithRawResponse:
    def __init__(self, soi_observation_set: AsyncSoiObservationSetResource) -> None:
        self._soi_observation_set = soi_observation_set

        self.create = async_to_raw_response_wrapper(
            soi_observation_set.create,
        )
        self.list = async_to_raw_response_wrapper(
            soi_observation_set.list,
        )
        self.count = async_to_raw_response_wrapper(
            soi_observation_set.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            soi_observation_set.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            soi_observation_set.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            soi_observation_set.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            soi_observation_set.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            soi_observation_set.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._soi_observation_set.history)


class SoiObservationSetResourceWithStreamingResponse:
    def __init__(self, soi_observation_set: SoiObservationSetResource) -> None:
        self._soi_observation_set = soi_observation_set

        self.create = to_streamed_response_wrapper(
            soi_observation_set.create,
        )
        self.list = to_streamed_response_wrapper(
            soi_observation_set.list,
        )
        self.count = to_streamed_response_wrapper(
            soi_observation_set.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            soi_observation_set.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            soi_observation_set.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            soi_observation_set.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            soi_observation_set.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            soi_observation_set.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._soi_observation_set.history)


class AsyncSoiObservationSetResourceWithStreamingResponse:
    def __init__(self, soi_observation_set: AsyncSoiObservationSetResource) -> None:
        self._soi_observation_set = soi_observation_set

        self.create = async_to_streamed_response_wrapper(
            soi_observation_set.create,
        )
        self.list = async_to_streamed_response_wrapper(
            soi_observation_set.list,
        )
        self.count = async_to_streamed_response_wrapper(
            soi_observation_set.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            soi_observation_set.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            soi_observation_set.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            soi_observation_set.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            soi_observation_set.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            soi_observation_set.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._soi_observation_set.history)
