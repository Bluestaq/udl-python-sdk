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
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.observations import (
    eo_observation_list_params,
    eo_observation_count_params,
    eo_observation_tuple_params,
    eo_observation_create_params,
    eo_observation_retrieve_params,
    eo_observation_create_bulk_params,
    eo_observation_unvalidated_publish_params,
)
from ....types.shared.eo_observation_full import EoObservationFull
from ....types.observations.eo_observation_abridged import EoObservationAbridged
from ....types.observations.eo_observation_tuple_response import EoObservationTupleResponse
from ....types.observations.eo_observation_queryhelp_response import EoObservationQueryhelpResponse

__all__ = ["EoObservationsResource", "AsyncEoObservationsResource"]


class EoObservationsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EoObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EoObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EoObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EoObservationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_bias: float | NotGiven = NOT_GIVEN,
        azimuth_measured: bool | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        bg_intensity: float | NotGiven = NOT_GIVEN,
        collect_method: str | NotGiven = NOT_GIVEN,
        corr_quality: float | NotGiven = NOT_GIVEN,
        declination: float | NotGiven = NOT_GIVEN,
        declination_bias: float | NotGiven = NOT_GIVEN,
        declination_measured: bool | NotGiven = NOT_GIVEN,
        declination_rate: float | NotGiven = NOT_GIVEN,
        declination_unc: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_bias: float | NotGiven = NOT_GIVEN,
        elevation_measured: bool | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        eoobservation_details: eo_observation_create_params.EoobservationDetails | NotGiven = NOT_GIVEN,
        exp_duration: float | NotGiven = NOT_GIVEN,
        fov_count: int | NotGiven = NOT_GIVEN,
        fov_count_uct: int | NotGiven = NOT_GIVEN,
        geoalt: float | NotGiven = NOT_GIVEN,
        geolat: float | NotGiven = NOT_GIVEN,
        geolon: float | NotGiven = NOT_GIVEN,
        georange: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_sky_imagery: str | NotGiven = NOT_GIVEN,
        intensity: float | NotGiven = NOT_GIVEN,
        los_unc: float | NotGiven = NOT_GIVEN,
        losx: float | NotGiven = NOT_GIVEN,
        losxvel: float | NotGiven = NOT_GIVEN,
        losy: float | NotGiven = NOT_GIVEN,
        losyvel: float | NotGiven = NOT_GIVEN,
        losz: float | NotGiven = NOT_GIVEN,
        loszvel: float | NotGiven = NOT_GIVEN,
        mag: float | NotGiven = NOT_GIVEN,
        mag_norm_range: float | NotGiven = NOT_GIVEN,
        mag_unc: float | NotGiven = NOT_GIVEN,
        net_obj_sig: float | NotGiven = NOT_GIVEN,
        net_obj_sig_unc: float | NotGiven = NOT_GIVEN,
        ob_position: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        penumbra: bool | NotGiven = NOT_GIVEN,
        primary_extinction: float | NotGiven = NOT_GIVEN,
        primary_extinction_unc: float | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        ra_bias: float | NotGiven = NOT_GIVEN,
        ra_measured: bool | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        range_bias: float | NotGiven = NOT_GIVEN,
        range_measured: bool | NotGiven = NOT_GIVEN,
        range_rate: float | NotGiven = NOT_GIVEN,
        range_rate_measured: bool | NotGiven = NOT_GIVEN,
        range_rate_unc: float | NotGiven = NOT_GIVEN,
        range_unc: float | NotGiven = NOT_GIVEN,
        ra_rate: float | NotGiven = NOT_GIVEN,
        ra_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "GCRF", "ITRF", "TEME"] | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        sen_quat: Iterable[float] | NotGiven = NOT_GIVEN,
        sen_reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        senvelx: float | NotGiven = NOT_GIVEN,
        senvely: float | NotGiven = NOT_GIVEN,
        senvelz: float | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        shutter_delay: float | NotGiven = NOT_GIVEN,
        sky_bkgrnd: float | NotGiven = NOT_GIVEN,
        solar_dec_angle: float | NotGiven = NOT_GIVEN,
        solar_eq_phase_angle: float | NotGiven = NOT_GIVEN,
        solar_phase_angle: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        timing_bias: float | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        umbra: bool | NotGiven = NOT_GIVEN,
        zeroptd: float | NotGiven = NOT_GIVEN,
        zero_ptd_unc: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EO observation as a POST body and ingest into
        the database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          azimuth: Line of sight azimuth angle in degrees and topocentric frame. Reported value
              should include all applicable corrections as specified on the source provider
              data card. If uncertain, consumers should contact the provider for details on
              the applied corrections.

          azimuth_bias: Sensor line of sight azimuth angle bias in degrees.

          azimuth_measured: Optional flag indicating whether the azimuth value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          azimuth_rate: Rate of change of the line of sight azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the line of sight azimuth angle, in degrees.

          bg_intensity: Background intensity for IR observations, in kw/sr/um.

          collect_method: Method indicating telescope movement during collection (AUTOTRACK, MANUAL
              AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).

          corr_quality: Object Correlation Quality score of the observation when compared to a known
              orbit state, (non-standardized). Users should consult data providers regarding
              the expected range of values.

          declination: Line of sight declination, in degrees, in the specified referenceFrame. If
              referenceFrame is null then J2K should be assumed. Reported value should include
              all applicable corrections as specified on the source provider data card. If
              uncertain, consumers should contact the provider for details on the applied
              corrections.

          declination_bias: Sensor line of sight declination angle bias in degrees.

          declination_measured: Optional flag indicating whether the declination value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          declination_rate: Line of sight declination rate of change, in degrees/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          declination_unc: One sigma uncertainty in the line of sight declination angle, in degrees.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          elevation: Line of sight elevation in degrees and topocentric frame. Reported value should
              include all applicable corrections as specified on the source provider data
              card. If uncertain, consumers should contact the provider for details on the
              applied corrections.

          elevation_bias: Sensor line of sight elevation bias in degrees.

          elevation_measured: Optional flag indicating whether the elevation value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          elevation_rate: Rate of change of the line of sight elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the line of sight elevation angle, in degrees.

          eoobservation_details: Model representation of additional detailed observation data for electro-optical
              based sensor phenomenologies.

          exp_duration: Image exposure duration in seconds. For observations performed using frame
              stacking or synthetic tracking methods, the exposure duration should be the
              total integration time. This field is highly recommended / required if the
              observations are going to be used for photometric processing.

          fov_count: The number of RSOs detected in the sensor field of view.

          fov_count_uct: The number of uncorrelated tracks in the field of view.

          geoalt: For GEO detections, the altitude in km.

          geolat: For GEO detections, the latitude in degrees north.

          geolon: For GEO detections, the longitude in degrees east.

          georange: For GEO detections, the range in km.

          id_sensor: Unique identifier of the reporting sensor.

          id_sky_imagery: Unique identifier of the Sky Imagery.

          intensity: Intensity of the target for IR observations, in kw/sr/um.

          los_unc: One sigma uncertainty in the line of sight pointing in micro-radians.

          losx: Line-of-sight cartesian X position of the target, in km, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losxvel: Line-of-sight cartesian X velocity of target, in km/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losy: Line-of-sight cartesian Y position of the target, in km, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losyvel: Line-of-sight cartesian Y velocity of target, in km/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losz: Line-of-sight cartesian Z position of the target, in km, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          loszvel: Line-of-sight cartesian Z velocity of target, in km/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          mag: Measure of observed brightness calibrated against the Gaia G-band in units of
              magnitudes.

          mag_norm_range: Formula: mag - 5.0 \\** log_10(geo_range / 1000000.0).

          mag_unc: Uncertainty of the observed brightness in units of magnitudes.

          net_obj_sig: Net object signature = counts / expDuration.

          net_obj_sig_unc: Net object signature uncertainty = counts uncertainty / expDuration.

          ob_position: The position of this observation within a track (FENCE, FIRST, IN, LAST,
              SINGLE). This identifier is optional and, if null, no assumption should be made
              regarding whether other observations may or may not exist to compose a track.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          penumbra: Boolean indicating that the target object was in a penumbral eclipse at the time
              of this observation.

          primary_extinction: Primary Extinction Coefficient, in Magnitudes. Primary Extinction is the
              coefficient applied to the airmass to determine how much the observed visual
              magnitude has been attenuated by the atmosphere. Extinction, in general,
              describes the absorption and scattering of electromagnetic radiation by dust and
              gas between an emitting astronomical object and the observer. See the
              EOObservationDetails API for specification of extinction coefficients for
              multiple spectral filters.

          primary_extinction_unc: Primary Extinction Coefficient Uncertainty, in Magnitudes.

          ra: Line of sight right ascension, in degrees, in the specified referenceFrame. If
              referenceFrame is null then J2K should be assumed. Reported value should include
              all applicable corrections as specified on the source provider data card. If
              uncertain, consumers should contact the provider for details on the applied
              corrections.

          ra_bias: Sensor line of sight right ascension bias in degrees.

          ra_measured: Optional flag indicating whether the ra value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range: Line of sight range in km. If referenceFrame is null then J2K should be assumed.
              Reported value should include all applicable corrections as specified on the
              source provider data card. If uncertain, consumers should contact the provider
              for details on the applied corrections.

          range_bias: Sensor line of sight range bias in km.

          range_measured: Optional flag indicating whether the range value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range_rate: Range rate in km/s. If referenceFrame is null then J2K should be assumed.
              Reported value should include all applicable corrections as specified on the
              source provider data card. If uncertain, consumers should contact the provider
              for details on the applied corrections.

          range_rate_measured: Optional flag indicating whether the rangeRate value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          range_rate_unc: One sigma uncertainty in the line of sight range rate, in kilometers/second.

          range_unc: One sigma uncertainty in the line of sight range, in kilometers.

          ra_rate: Line of sight right ascension rate of change, in degrees/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          ra_unc: One sigma uncertainty in the line of sight right ascension angle, in degrees.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          reference_frame: The reference frame of the EOObservation measurements. If the referenceFrame is
              null it is assumed to be J2000.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          senalt: Sensor altitude at obTime (if mobile/onorbit) in km.

          senlat: Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -180 to 180 degrees (negative values west of Prime
              Meridian).

          sen_quat: The quaternion describing the rotation of the sensor in relation to the
              body-fixed frame used for this system into the local geodetic frame, at
              observation time (obTime). The array element order convention is scalar
              component first, followed by the three vector components (qc, q1, q2, q3).

          sen_reference_frame: The reference frame of the observing sensor state. If the senReferenceFrame is
              null it is assumed to be J2000.

          senvelx: Cartesian X velocity of the observing mobile/onorbit sensor at obTime, in
              km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
              J2K should be assumed.

          senvely: Cartesian Y velocity of the observing mobile/onorbit sensor at obTime, in
              km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
              J2K should be assumed.

          senvelz: Cartesian Z velocity of the observing mobile/onorbit sensor at obTime, in
              km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
              J2K should be assumed.

          senx: Cartesian X position of the observing mobile/onorbit sensor at obTime, in km, in
              the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
              assumed.

          seny: Cartesian Y position of the observing mobile/onorbit sensor at obTime, in km, in
              the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
              assumed.

          senz: Cartesian Z position of the observing mobile/onorbit sensor at obTime, in km, in
              the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
              assumed.

          shutter_delay: Shutter delay in seconds.

          sky_bkgrnd: Average Sky Background signal, in Magnitudes. Sky Background refers to the
              incoming light from an apparently empty part of the night sky.

          solar_dec_angle: Angle from the sun to the equatorial plane.

          solar_eq_phase_angle: The angle, in degrees, between the projections of the target-to-observer vector
              and the target-to-sun vector onto the equatorial plane. The angle is represented
              as negative when closing (i.e. before the opposition) and positive when opening
              (after the opposition).

          solar_phase_angle: The angle, in degrees, between the target-to-observer vector and the
              target-to-sun vector.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          timing_bias: Sensor timing bias in seconds.

          track_id: Optional identifier of the track to which this observation belongs.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          umbra: Boolean indicating that the target object was in umbral eclipse at the time of
              this observation.

          zeroptd: Formula: 2.5 \\** log_10 (zero_mag_counts / expDuration).

          zero_ptd_unc: This is the uncertainty in the zero point for the filter used for this
              observation/row in units of mag. For use with differential photometry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/eoobservation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "azimuth": azimuth,
                    "azimuth_bias": azimuth_bias,
                    "azimuth_measured": azimuth_measured,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "bg_intensity": bg_intensity,
                    "collect_method": collect_method,
                    "corr_quality": corr_quality,
                    "declination": declination,
                    "declination_bias": declination_bias,
                    "declination_measured": declination_measured,
                    "declination_rate": declination_rate,
                    "declination_unc": declination_unc,
                    "descriptor": descriptor,
                    "elevation": elevation,
                    "elevation_bias": elevation_bias,
                    "elevation_measured": elevation_measured,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "eoobservation_details": eoobservation_details,
                    "exp_duration": exp_duration,
                    "fov_count": fov_count,
                    "fov_count_uct": fov_count_uct,
                    "geoalt": geoalt,
                    "geolat": geolat,
                    "geolon": geolon,
                    "georange": georange,
                    "id_sensor": id_sensor,
                    "id_sky_imagery": id_sky_imagery,
                    "intensity": intensity,
                    "los_unc": los_unc,
                    "losx": losx,
                    "losxvel": losxvel,
                    "losy": losy,
                    "losyvel": losyvel,
                    "losz": losz,
                    "loszvel": loszvel,
                    "mag": mag,
                    "mag_norm_range": mag_norm_range,
                    "mag_unc": mag_unc,
                    "net_obj_sig": net_obj_sig,
                    "net_obj_sig_unc": net_obj_sig_unc,
                    "ob_position": ob_position,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "penumbra": penumbra,
                    "primary_extinction": primary_extinction,
                    "primary_extinction_unc": primary_extinction_unc,
                    "ra": ra,
                    "ra_bias": ra_bias,
                    "ra_measured": ra_measured,
                    "range": range,
                    "range_bias": range_bias,
                    "range_measured": range_measured,
                    "range_rate": range_rate,
                    "range_rate_measured": range_rate_measured,
                    "range_rate_unc": range_rate_unc,
                    "range_unc": range_unc,
                    "ra_rate": ra_rate,
                    "ra_unc": ra_unc,
                    "raw_file_uri": raw_file_uri,
                    "reference_frame": reference_frame,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sen_quat": sen_quat,
                    "sen_reference_frame": sen_reference_frame,
                    "senvelx": senvelx,
                    "senvely": senvely,
                    "senvelz": senvelz,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "shutter_delay": shutter_delay,
                    "sky_bkgrnd": sky_bkgrnd,
                    "solar_dec_angle": solar_dec_angle,
                    "solar_eq_phase_angle": solar_eq_phase_angle,
                    "solar_phase_angle": solar_phase_angle,
                    "tags": tags,
                    "task_id": task_id,
                    "timing_bias": timing_bias,
                    "track_id": track_id,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "umbra": umbra,
                    "zeroptd": zeroptd,
                    "zero_ptd_unc": zero_ptd_unc,
                },
                eo_observation_create_params.EoObservationCreateParams,
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
    ) -> EoObservationFull:
        """
        Service operation to get a single EO observation by its unique ID passed as a
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
            f"/udl/eoobservation/{id}",
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
                    eo_observation_retrieve_params.EoObservationRetrieveParams,
                ),
            ),
            cast_to=EoObservationFull,
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
    ) -> SyncOffsetPage[EoObservationAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eoobservation",
            page=SyncOffsetPage[EoObservationAbridged],
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
                    eo_observation_list_params.EoObservationListParams,
                ),
            ),
            model=EoObservationAbridged,
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
          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/eoobservation/count",
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
                    eo_observation_count_params.EoObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[eo_observation_create_bulk_params.Body],
        convert_to_j2_k: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of EO
        observations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          convert_to_j2_k: Flag to convert observation reference frame into J2000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/eoobservation/createBulk",
            body=maybe_transform(body, Iterable[eo_observation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"convert_to_j2_k": convert_to_j2_k},
                    eo_observation_create_bulk_params.EoObservationCreateBulkParams,
                ),
            ),
            cast_to=NoneType,
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
    ) -> EoObservationQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/eoobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EoObservationQueryhelpResponse,
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
    ) -> EoObservationTupleResponse:
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

          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/eoobservation/tuple",
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
                    eo_observation_tuple_params.EoObservationTupleParams,
                ),
            ),
            cast_to=EoObservationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[eo_observation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple EO observations as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-eo",
            body=maybe_transform(body, Iterable[eo_observation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEoObservationsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEoObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEoObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEoObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEoObservationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_bias: float | NotGiven = NOT_GIVEN,
        azimuth_measured: bool | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        bg_intensity: float | NotGiven = NOT_GIVEN,
        collect_method: str | NotGiven = NOT_GIVEN,
        corr_quality: float | NotGiven = NOT_GIVEN,
        declination: float | NotGiven = NOT_GIVEN,
        declination_bias: float | NotGiven = NOT_GIVEN,
        declination_measured: bool | NotGiven = NOT_GIVEN,
        declination_rate: float | NotGiven = NOT_GIVEN,
        declination_unc: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_bias: float | NotGiven = NOT_GIVEN,
        elevation_measured: bool | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        eoobservation_details: eo_observation_create_params.EoobservationDetails | NotGiven = NOT_GIVEN,
        exp_duration: float | NotGiven = NOT_GIVEN,
        fov_count: int | NotGiven = NOT_GIVEN,
        fov_count_uct: int | NotGiven = NOT_GIVEN,
        geoalt: float | NotGiven = NOT_GIVEN,
        geolat: float | NotGiven = NOT_GIVEN,
        geolon: float | NotGiven = NOT_GIVEN,
        georange: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_sky_imagery: str | NotGiven = NOT_GIVEN,
        intensity: float | NotGiven = NOT_GIVEN,
        los_unc: float | NotGiven = NOT_GIVEN,
        losx: float | NotGiven = NOT_GIVEN,
        losxvel: float | NotGiven = NOT_GIVEN,
        losy: float | NotGiven = NOT_GIVEN,
        losyvel: float | NotGiven = NOT_GIVEN,
        losz: float | NotGiven = NOT_GIVEN,
        loszvel: float | NotGiven = NOT_GIVEN,
        mag: float | NotGiven = NOT_GIVEN,
        mag_norm_range: float | NotGiven = NOT_GIVEN,
        mag_unc: float | NotGiven = NOT_GIVEN,
        net_obj_sig: float | NotGiven = NOT_GIVEN,
        net_obj_sig_unc: float | NotGiven = NOT_GIVEN,
        ob_position: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        penumbra: bool | NotGiven = NOT_GIVEN,
        primary_extinction: float | NotGiven = NOT_GIVEN,
        primary_extinction_unc: float | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        ra_bias: float | NotGiven = NOT_GIVEN,
        ra_measured: bool | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        range_bias: float | NotGiven = NOT_GIVEN,
        range_measured: bool | NotGiven = NOT_GIVEN,
        range_rate: float | NotGiven = NOT_GIVEN,
        range_rate_measured: bool | NotGiven = NOT_GIVEN,
        range_rate_unc: float | NotGiven = NOT_GIVEN,
        range_unc: float | NotGiven = NOT_GIVEN,
        ra_rate: float | NotGiven = NOT_GIVEN,
        ra_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "GCRF", "ITRF", "TEME"] | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        sen_quat: Iterable[float] | NotGiven = NOT_GIVEN,
        sen_reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        senvelx: float | NotGiven = NOT_GIVEN,
        senvely: float | NotGiven = NOT_GIVEN,
        senvelz: float | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        shutter_delay: float | NotGiven = NOT_GIVEN,
        sky_bkgrnd: float | NotGiven = NOT_GIVEN,
        solar_dec_angle: float | NotGiven = NOT_GIVEN,
        solar_eq_phase_angle: float | NotGiven = NOT_GIVEN,
        solar_phase_angle: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        timing_bias: float | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        umbra: bool | NotGiven = NOT_GIVEN,
        zeroptd: float | NotGiven = NOT_GIVEN,
        zero_ptd_unc: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EO observation as a POST body and ingest into
        the database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          azimuth: Line of sight azimuth angle in degrees and topocentric frame. Reported value
              should include all applicable corrections as specified on the source provider
              data card. If uncertain, consumers should contact the provider for details on
              the applied corrections.

          azimuth_bias: Sensor line of sight azimuth angle bias in degrees.

          azimuth_measured: Optional flag indicating whether the azimuth value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          azimuth_rate: Rate of change of the line of sight azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the line of sight azimuth angle, in degrees.

          bg_intensity: Background intensity for IR observations, in kw/sr/um.

          collect_method: Method indicating telescope movement during collection (AUTOTRACK, MANUAL
              AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).

          corr_quality: Object Correlation Quality score of the observation when compared to a known
              orbit state, (non-standardized). Users should consult data providers regarding
              the expected range of values.

          declination: Line of sight declination, in degrees, in the specified referenceFrame. If
              referenceFrame is null then J2K should be assumed. Reported value should include
              all applicable corrections as specified on the source provider data card. If
              uncertain, consumers should contact the provider for details on the applied
              corrections.

          declination_bias: Sensor line of sight declination angle bias in degrees.

          declination_measured: Optional flag indicating whether the declination value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          declination_rate: Line of sight declination rate of change, in degrees/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          declination_unc: One sigma uncertainty in the line of sight declination angle, in degrees.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          elevation: Line of sight elevation in degrees and topocentric frame. Reported value should
              include all applicable corrections as specified on the source provider data
              card. If uncertain, consumers should contact the provider for details on the
              applied corrections.

          elevation_bias: Sensor line of sight elevation bias in degrees.

          elevation_measured: Optional flag indicating whether the elevation value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          elevation_rate: Rate of change of the line of sight elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the line of sight elevation angle, in degrees.

          eoobservation_details: Model representation of additional detailed observation data for electro-optical
              based sensor phenomenologies.

          exp_duration: Image exposure duration in seconds. For observations performed using frame
              stacking or synthetic tracking methods, the exposure duration should be the
              total integration time. This field is highly recommended / required if the
              observations are going to be used for photometric processing.

          fov_count: The number of RSOs detected in the sensor field of view.

          fov_count_uct: The number of uncorrelated tracks in the field of view.

          geoalt: For GEO detections, the altitude in km.

          geolat: For GEO detections, the latitude in degrees north.

          geolon: For GEO detections, the longitude in degrees east.

          georange: For GEO detections, the range in km.

          id_sensor: Unique identifier of the reporting sensor.

          id_sky_imagery: Unique identifier of the Sky Imagery.

          intensity: Intensity of the target for IR observations, in kw/sr/um.

          los_unc: One sigma uncertainty in the line of sight pointing in micro-radians.

          losx: Line-of-sight cartesian X position of the target, in km, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losxvel: Line-of-sight cartesian X velocity of target, in km/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losy: Line-of-sight cartesian Y position of the target, in km, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losyvel: Line-of-sight cartesian Y velocity of target, in km/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          losz: Line-of-sight cartesian Z position of the target, in km, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          loszvel: Line-of-sight cartesian Z velocity of target, in km/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          mag: Measure of observed brightness calibrated against the Gaia G-band in units of
              magnitudes.

          mag_norm_range: Formula: mag - 5.0 \\** log_10(geo_range / 1000000.0).

          mag_unc: Uncertainty of the observed brightness in units of magnitudes.

          net_obj_sig: Net object signature = counts / expDuration.

          net_obj_sig_unc: Net object signature uncertainty = counts uncertainty / expDuration.

          ob_position: The position of this observation within a track (FENCE, FIRST, IN, LAST,
              SINGLE). This identifier is optional and, if null, no assumption should be made
              regarding whether other observations may or may not exist to compose a track.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          penumbra: Boolean indicating that the target object was in a penumbral eclipse at the time
              of this observation.

          primary_extinction: Primary Extinction Coefficient, in Magnitudes. Primary Extinction is the
              coefficient applied to the airmass to determine how much the observed visual
              magnitude has been attenuated by the atmosphere. Extinction, in general,
              describes the absorption and scattering of electromagnetic radiation by dust and
              gas between an emitting astronomical object and the observer. See the
              EOObservationDetails API for specification of extinction coefficients for
              multiple spectral filters.

          primary_extinction_unc: Primary Extinction Coefficient Uncertainty, in Magnitudes.

          ra: Line of sight right ascension, in degrees, in the specified referenceFrame. If
              referenceFrame is null then J2K should be assumed. Reported value should include
              all applicable corrections as specified on the source provider data card. If
              uncertain, consumers should contact the provider for details on the applied
              corrections.

          ra_bias: Sensor line of sight right ascension bias in degrees.

          ra_measured: Optional flag indicating whether the ra value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range: Line of sight range in km. If referenceFrame is null then J2K should be assumed.
              Reported value should include all applicable corrections as specified on the
              source provider data card. If uncertain, consumers should contact the provider
              for details on the applied corrections.

          range_bias: Sensor line of sight range bias in km.

          range_measured: Optional flag indicating whether the range value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range_rate: Range rate in km/s. If referenceFrame is null then J2K should be assumed.
              Reported value should include all applicable corrections as specified on the
              source provider data card. If uncertain, consumers should contact the provider
              for details on the applied corrections.

          range_rate_measured: Optional flag indicating whether the rangeRate value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          range_rate_unc: One sigma uncertainty in the line of sight range rate, in kilometers/second.

          range_unc: One sigma uncertainty in the line of sight range, in kilometers.

          ra_rate: Line of sight right ascension rate of change, in degrees/sec, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          ra_unc: One sigma uncertainty in the line of sight right ascension angle, in degrees.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          reference_frame: The reference frame of the EOObservation measurements. If the referenceFrame is
              null it is assumed to be J2000.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          senalt: Sensor altitude at obTime (if mobile/onorbit) in km.

          senlat: Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -180 to 180 degrees (negative values west of Prime
              Meridian).

          sen_quat: The quaternion describing the rotation of the sensor in relation to the
              body-fixed frame used for this system into the local geodetic frame, at
              observation time (obTime). The array element order convention is scalar
              component first, followed by the three vector components (qc, q1, q2, q3).

          sen_reference_frame: The reference frame of the observing sensor state. If the senReferenceFrame is
              null it is assumed to be J2000.

          senvelx: Cartesian X velocity of the observing mobile/onorbit sensor at obTime, in
              km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
              J2K should be assumed.

          senvely: Cartesian Y velocity of the observing mobile/onorbit sensor at obTime, in
              km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
              J2K should be assumed.

          senvelz: Cartesian Z velocity of the observing mobile/onorbit sensor at obTime, in
              km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
              J2K should be assumed.

          senx: Cartesian X position of the observing mobile/onorbit sensor at obTime, in km, in
              the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
              assumed.

          seny: Cartesian Y position of the observing mobile/onorbit sensor at obTime, in km, in
              the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
              assumed.

          senz: Cartesian Z position of the observing mobile/onorbit sensor at obTime, in km, in
              the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
              assumed.

          shutter_delay: Shutter delay in seconds.

          sky_bkgrnd: Average Sky Background signal, in Magnitudes. Sky Background refers to the
              incoming light from an apparently empty part of the night sky.

          solar_dec_angle: Angle from the sun to the equatorial plane.

          solar_eq_phase_angle: The angle, in degrees, between the projections of the target-to-observer vector
              and the target-to-sun vector onto the equatorial plane. The angle is represented
              as negative when closing (i.e. before the opposition) and positive when opening
              (after the opposition).

          solar_phase_angle: The angle, in degrees, between the target-to-observer vector and the
              target-to-sun vector.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          timing_bias: Sensor timing bias in seconds.

          track_id: Optional identifier of the track to which this observation belongs.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          umbra: Boolean indicating that the target object was in umbral eclipse at the time of
              this observation.

          zeroptd: Formula: 2.5 \\** log_10 (zero_mag_counts / expDuration).

          zero_ptd_unc: This is the uncertainty in the zero point for the filter used for this
              observation/row in units of mag. For use with differential photometry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/eoobservation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "azimuth": azimuth,
                    "azimuth_bias": azimuth_bias,
                    "azimuth_measured": azimuth_measured,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "bg_intensity": bg_intensity,
                    "collect_method": collect_method,
                    "corr_quality": corr_quality,
                    "declination": declination,
                    "declination_bias": declination_bias,
                    "declination_measured": declination_measured,
                    "declination_rate": declination_rate,
                    "declination_unc": declination_unc,
                    "descriptor": descriptor,
                    "elevation": elevation,
                    "elevation_bias": elevation_bias,
                    "elevation_measured": elevation_measured,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "eoobservation_details": eoobservation_details,
                    "exp_duration": exp_duration,
                    "fov_count": fov_count,
                    "fov_count_uct": fov_count_uct,
                    "geoalt": geoalt,
                    "geolat": geolat,
                    "geolon": geolon,
                    "georange": georange,
                    "id_sensor": id_sensor,
                    "id_sky_imagery": id_sky_imagery,
                    "intensity": intensity,
                    "los_unc": los_unc,
                    "losx": losx,
                    "losxvel": losxvel,
                    "losy": losy,
                    "losyvel": losyvel,
                    "losz": losz,
                    "loszvel": loszvel,
                    "mag": mag,
                    "mag_norm_range": mag_norm_range,
                    "mag_unc": mag_unc,
                    "net_obj_sig": net_obj_sig,
                    "net_obj_sig_unc": net_obj_sig_unc,
                    "ob_position": ob_position,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "penumbra": penumbra,
                    "primary_extinction": primary_extinction,
                    "primary_extinction_unc": primary_extinction_unc,
                    "ra": ra,
                    "ra_bias": ra_bias,
                    "ra_measured": ra_measured,
                    "range": range,
                    "range_bias": range_bias,
                    "range_measured": range_measured,
                    "range_rate": range_rate,
                    "range_rate_measured": range_rate_measured,
                    "range_rate_unc": range_rate_unc,
                    "range_unc": range_unc,
                    "ra_rate": ra_rate,
                    "ra_unc": ra_unc,
                    "raw_file_uri": raw_file_uri,
                    "reference_frame": reference_frame,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sen_quat": sen_quat,
                    "sen_reference_frame": sen_reference_frame,
                    "senvelx": senvelx,
                    "senvely": senvely,
                    "senvelz": senvelz,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "shutter_delay": shutter_delay,
                    "sky_bkgrnd": sky_bkgrnd,
                    "solar_dec_angle": solar_dec_angle,
                    "solar_eq_phase_angle": solar_eq_phase_angle,
                    "solar_phase_angle": solar_phase_angle,
                    "tags": tags,
                    "task_id": task_id,
                    "timing_bias": timing_bias,
                    "track_id": track_id,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "umbra": umbra,
                    "zeroptd": zeroptd,
                    "zero_ptd_unc": zero_ptd_unc,
                },
                eo_observation_create_params.EoObservationCreateParams,
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
    ) -> EoObservationFull:
        """
        Service operation to get a single EO observation by its unique ID passed as a
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
            f"/udl/eoobservation/{id}",
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
                    eo_observation_retrieve_params.EoObservationRetrieveParams,
                ),
            ),
            cast_to=EoObservationFull,
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
    ) -> AsyncPaginator[EoObservationAbridged, AsyncOffsetPage[EoObservationAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eoobservation",
            page=AsyncOffsetPage[EoObservationAbridged],
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
                    eo_observation_list_params.EoObservationListParams,
                ),
            ),
            model=EoObservationAbridged,
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
          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/eoobservation/count",
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
                    eo_observation_count_params.EoObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[eo_observation_create_bulk_params.Body],
        convert_to_j2_k: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of EO
        observations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          convert_to_j2_k: Flag to convert observation reference frame into J2000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/eoobservation/createBulk",
            body=await async_maybe_transform(body, Iterable[eo_observation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"convert_to_j2_k": convert_to_j2_k},
                    eo_observation_create_bulk_params.EoObservationCreateBulkParams,
                ),
            ),
            cast_to=NoneType,
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
    ) -> EoObservationQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/eoobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EoObservationQueryhelpResponse,
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
    ) -> EoObservationTupleResponse:
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

          ob_time: Ob detection time in ISO 8601 UTC, up to microsecond precision. Consumers should
              contact the provider for details on their obTime specifications.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/eoobservation/tuple",
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
                    eo_observation_tuple_params.EoObservationTupleParams,
                ),
            ),
            cast_to=EoObservationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[eo_observation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple EO observations as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-eo",
            body=await async_maybe_transform(body, Iterable[eo_observation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EoObservationsResourceWithRawResponse:
    def __init__(self, eo_observations: EoObservationsResource) -> None:
        self._eo_observations = eo_observations

        self.create = to_raw_response_wrapper(
            eo_observations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            eo_observations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            eo_observations.list,
        )
        self.count = to_raw_response_wrapper(
            eo_observations.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            eo_observations.create_bulk,
        )
        self.queryhelp = to_raw_response_wrapper(
            eo_observations.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            eo_observations.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            eo_observations.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._eo_observations.history)


class AsyncEoObservationsResourceWithRawResponse:
    def __init__(self, eo_observations: AsyncEoObservationsResource) -> None:
        self._eo_observations = eo_observations

        self.create = async_to_raw_response_wrapper(
            eo_observations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            eo_observations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            eo_observations.list,
        )
        self.count = async_to_raw_response_wrapper(
            eo_observations.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            eo_observations.create_bulk,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            eo_observations.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            eo_observations.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            eo_observations.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._eo_observations.history)


class EoObservationsResourceWithStreamingResponse:
    def __init__(self, eo_observations: EoObservationsResource) -> None:
        self._eo_observations = eo_observations

        self.create = to_streamed_response_wrapper(
            eo_observations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            eo_observations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            eo_observations.list,
        )
        self.count = to_streamed_response_wrapper(
            eo_observations.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            eo_observations.create_bulk,
        )
        self.queryhelp = to_streamed_response_wrapper(
            eo_observations.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            eo_observations.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            eo_observations.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._eo_observations.history)


class AsyncEoObservationsResourceWithStreamingResponse:
    def __init__(self, eo_observations: AsyncEoObservationsResource) -> None:
        self._eo_observations = eo_observations

        self.create = async_to_streamed_response_wrapper(
            eo_observations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            eo_observations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            eo_observations.list,
        )
        self.count = async_to_streamed_response_wrapper(
            eo_observations.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            eo_observations.create_bulk,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            eo_observations.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            eo_observations.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            eo_observations.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._eo_observations.history)
