# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    state_vector_get_params,
    state_vector_list_params,
    state_vector_count_params,
    state_vector_tuple_params,
    state_vector_create_params,
)
from .current import (
    CurrentResource,
    AsyncCurrentResource,
    CurrentResourceWithRawResponse,
    AsyncCurrentResourceWithRawResponse,
    CurrentResourceWithStreamingResponse,
    AsyncCurrentResourceWithStreamingResponse,
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
from ...types.state_vector_abridged import StateVectorAbridged
from ...types.shared.state_vector_full import StateVectorFull
from ...types.state_vector_ingest_param import StateVectorIngestParam
from ...types.state_vector_tuple_response import StateVectorTupleResponse
from ...types.state_vector_queryhelp_response import StateVectorQueryhelpResponse

__all__ = ["StateVectorResource", "AsyncStateVectorResource"]


class StateVectorResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def current(self) -> CurrentResource:
        return CurrentResource(self._client)

    @cached_property
    def with_raw_response(self) -> StateVectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return StateVectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StateVectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return StateVectorResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        epoch: Union[str, datetime],
        source: str,
        actual_od_span: float | NotGiven = NOT_GIVEN,
        algorithm: str | NotGiven = NOT_GIVEN,
        alt1_reference_frame: str | NotGiven = NOT_GIVEN,
        alt2_reference_frame: str | NotGiven = NOT_GIVEN,
        area: float | NotGiven = NOT_GIVEN,
        b_dot: float | NotGiven = NOT_GIVEN,
        cm_offset: float | NotGiven = NOT_GIVEN,
        cov: Iterable[float] | NotGiven = NOT_GIVEN,
        cov_method: str | NotGiven = NOT_GIVEN,
        cov_reference_frame: Literal["J2000", "UVW", "EFG/TDR", "TEME", "GCRF"] | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        drag_area: float | NotGiven = NOT_GIVEN,
        drag_coeff: float | NotGiven = NOT_GIVEN,
        drag_model: str | NotGiven = NOT_GIVEN,
        edr: float | NotGiven = NOT_GIVEN,
        eq_cov: Iterable[float] | NotGiven = NOT_GIVEN,
        error_control: float | NotGiven = NOT_GIVEN,
        fixed_step: bool | NotGiven = NOT_GIVEN,
        geopotential_model: str | NotGiven = NOT_GIVEN,
        iau1980_terms: int | NotGiven = NOT_GIVEN,
        id_orbit_determination: str | NotGiven = NOT_GIVEN,
        id_state_vector: str | NotGiven = NOT_GIVEN,
        integrator_mode: str | NotGiven = NOT_GIVEN,
        in_track_thrust: bool | NotGiven = NOT_GIVEN,
        last_ob_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_ob_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        leap_second_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        lunar_solar: bool | NotGiven = NOT_GIVEN,
        mass: float | NotGiven = NOT_GIVEN,
        obs_available: int | NotGiven = NOT_GIVEN,
        obs_used: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        partials: str | NotGiven = NOT_GIVEN,
        pedigree: str | NotGiven = NOT_GIVEN,
        polar_motion_x: float | NotGiven = NOT_GIVEN,
        polar_motion_y: float | NotGiven = NOT_GIVEN,
        pos_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rec_od_span: float | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        residuals_acc: float | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        rms: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sigma_pos_uvw: Iterable[float] | NotGiven = NOT_GIVEN,
        sigma_vel_uvw: Iterable[float] | NotGiven = NOT_GIVEN,
        solar_flux_ap_avg: float | NotGiven = NOT_GIVEN,
        solar_flux_f10: float | NotGiven = NOT_GIVEN,
        solar_flux_f10_avg: float | NotGiven = NOT_GIVEN,
        solar_rad_press: bool | NotGiven = NOT_GIVEN,
        solar_rad_press_coeff: float | NotGiven = NOT_GIVEN,
        solid_earth_tides: bool | NotGiven = NOT_GIVEN,
        sourced_data: List[str] | NotGiven = NOT_GIVEN,
        sourced_data_types: List[Literal["EO", "RADAR", "RF", "DOA", "ELSET", "SV"]] | NotGiven = NOT_GIVEN,
        srp_area: float | NotGiven = NOT_GIVEN,
        step_mode: str | NotGiven = NOT_GIVEN,
        step_size: float | NotGiven = NOT_GIVEN,
        step_size_selection: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        tai_utc: float | NotGiven = NOT_GIVEN,
        thrust_accel: float | NotGiven = NOT_GIVEN,
        tracks_avail: int | NotGiven = NOT_GIVEN,
        tracks_used: int | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        ut1_rate: float | NotGiven = NOT_GIVEN,
        ut1_utc: float | NotGiven = NOT_GIVEN,
        vel_unc: float | NotGiven = NOT_GIVEN,
        xaccel: float | NotGiven = NOT_GIVEN,
        xpos: float | NotGiven = NOT_GIVEN,
        xpos_alt1: float | NotGiven = NOT_GIVEN,
        xpos_alt2: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        xvel_alt1: float | NotGiven = NOT_GIVEN,
        xvel_alt2: float | NotGiven = NOT_GIVEN,
        yaccel: float | NotGiven = NOT_GIVEN,
        ypos: float | NotGiven = NOT_GIVEN,
        ypos_alt1: float | NotGiven = NOT_GIVEN,
        ypos_alt2: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        yvel_alt1: float | NotGiven = NOT_GIVEN,
        yvel_alt2: float | NotGiven = NOT_GIVEN,
        zaccel: float | NotGiven = NOT_GIVEN,
        zpos: float | NotGiven = NOT_GIVEN,
        zpos_alt1: float | NotGiven = NOT_GIVEN,
        zpos_alt2: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        zvel_alt1: float | NotGiven = NOT_GIVEN,
        zvel_alt2: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single state vector as a POST body and ingest into
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

          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision.

          source: Source of the data.

          actual_od_span: The actual time span used for the OD of the object, expressed in days.

          algorithm: Optional algorithm used to produce this record.

          alt1_reference_frame: The reference frame of the alternate1 (Alt1) cartesian orbital state.

          alt2_reference_frame: The reference frame of the alternate2 (Alt2) cartesian orbital state.

          area: The actual area of the object at it's largest cross-section, expressed in
              meters^2.

          b_dot: First derivative of drag/ballistic coefficient (m2/kg-s).

          cm_offset: Model parameter value for center of mass offset (m).

          cov: Covariance matrix, in kilometer and second based units, in the specified
              covReferenceFrame. If the covReferenceFrame is null it is assumed to be J2000.
              The array values (1-21) represent the lower triangular half of the
              position-velocity covariance matrix. The size of the covariance matrix is
              dynamic, depending on whether the covariance for position only or position &
              velocity. The covariance elements are position dependent within the array with
              values ordered as follows:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;&nbsp;x'&nbsp;&nbsp;&nbsp;&nbsp;y'&nbsp;&nbsp;&nbsp;&nbsp;z'&nbsp;&nbsp;&nbsp;&nbsp;DRG&nbsp;&nbsp;&nbsp;&nbsp;SRP&nbsp;&nbsp;&nbsp;&nbsp;THR&nbsp;&nbsp;

              x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1

              y&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;3

              z&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;6

              x'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;10

              y'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11&nbsp;&nbsp;12&nbsp;&nbsp;13&nbsp;&nbsp;14&nbsp;&nbsp;15

              z'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16&nbsp;&nbsp;17&nbsp;&nbsp;18&nbsp;&nbsp;19&nbsp;&nbsp;20&nbsp;&nbsp;&nbsp;21&nbsp;

              The cov array should contain only the lower left triangle values from top left
              down to bottom right, in order.

              If additional covariance terms are included for DRAG, SRP, and/or THRUST, the
              matrix can be extended with the following order of elements:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;&nbsp;x'&nbsp;&nbsp;&nbsp;&nbsp;y'&nbsp;&nbsp;&nbsp;&nbsp;z'&nbsp;&nbsp;&nbsp;&nbsp;DRG&nbsp;&nbsp;&nbsp;&nbsp;SRP&nbsp;&nbsp;&nbsp;&nbsp;THR

              DRG&nbsp;&nbsp;&nbsp;22&nbsp;&nbsp;23&nbsp;&nbsp;24&nbsp;&nbsp;25&nbsp;&nbsp;26&nbsp;&nbsp;&nbsp;27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28&nbsp;&nbsp;

              SRP&nbsp;&nbsp;&nbsp;29&nbsp;&nbsp;30&nbsp;&nbsp;31&nbsp;&nbsp;32&nbsp;&nbsp;33&nbsp;&nbsp;&nbsp;34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36&nbsp;&nbsp;

              THR&nbsp;&nbsp;&nbsp;37&nbsp;&nbsp;38&nbsp;&nbsp;39&nbsp;&nbsp;40&nbsp;&nbsp;41&nbsp;&nbsp;&nbsp;42&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;43&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;45&nbsp;

          cov_method: The method used to generate the covariance during the orbit determination (OD)
              that produced the state vector, or whether an arbitrary, non-calculated default
              value was used (CALCULATED, DEFAULT).

          cov_reference_frame: The reference frame of the covariance matrix elements. If the covReferenceFrame
              is null it is assumed to be J2000.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          drag_area: The effective area of the object exposed to atmospheric drag, expressed in
              meters^2.

          drag_coeff: Area-to-mass ratio coefficient for atmospheric ballistic drag (m2/kg).

          drag_model: The Drag Model used for this vector (e.g. HARRIS-PRIESTER, JAC70, JBH09, MSIS90,
              NONE, etc.).

          edr: Model parameter value for energy dissipation rate (EDR) (w/kg).

          eq_cov: The covariance matrix values represent the lower triangular half of the
              covariance matrix in terms of equinoctial elements.&nbsp; The size of the
              covariance matrix is dynamic.&nbsp; The values are outputted in order across
              each row, i.e.:

              1&nbsp;&nbsp; 2&nbsp;&nbsp; 3&nbsp;&nbsp; 4&nbsp;&nbsp; 5

              6&nbsp;&nbsp; 7&nbsp;&nbsp; 8&nbsp;&nbsp; 9&nbsp; 10

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              51&nbsp; 52&nbsp; 53&nbsp; 54&nbsp; 55

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              The ordering of values is as follows:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Af&nbsp;&nbsp;
              Ag&nbsp;&nbsp; L&nbsp;&nbsp;&nbsp; N&nbsp;&nbsp; Chi&nbsp; Psi&nbsp;&nbsp;
              B&nbsp;&nbsp; BDOT AGOM&nbsp; T&nbsp;&nbsp; C1&nbsp;&nbsp; C2&nbsp; ...

              Af&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1

              Ag&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 3

              L&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              4&nbsp;&nbsp;&nbsp; 5&nbsp;&nbsp;&nbsp; 6

              N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              7&nbsp;&nbsp;&nbsp; 8&nbsp;&nbsp;&nbsp; 9&nbsp;&nbsp; 10

              Chi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 11&nbsp;&nbsp; 12&nbsp;&nbsp;
              13&nbsp;&nbsp; 14&nbsp;&nbsp; 15

              Psi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16&nbsp;&nbsp; 17&nbsp;&nbsp;
              18&nbsp;&nbsp; 19&nbsp;&nbsp; 20&nbsp;&nbsp; 21

              B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 22&nbsp;&nbsp;
              23&nbsp;&nbsp; 24 &nbsp;&nbsp;25&nbsp;&nbsp; 26&nbsp;&nbsp; 27&nbsp;&nbsp; 28

              BDOT&nbsp;&nbsp; 29&nbsp;&nbsp; 30&nbsp;&nbsp; 31&nbsp;&nbsp; 32&nbsp;&nbsp;
              33&nbsp;&nbsp; 34&nbsp;&nbsp; 35&nbsp;&nbsp; 36

              AGOM&nbsp; 37&nbsp;&nbsp; 38&nbsp;&nbsp; 39&nbsp;&nbsp; 40&nbsp;&nbsp;
              41&nbsp;&nbsp; 42&nbsp;&nbsp; 43&nbsp;&nbsp; 44&nbsp;&nbsp; 45

              T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 46&nbsp;&nbsp;
              47&nbsp;&nbsp; 48&nbsp;&nbsp; 49&nbsp;&nbsp; 50&nbsp;&nbsp; 51&nbsp;&nbsp;
              52&nbsp;&nbsp; 53&nbsp;&nbsp; 54&nbsp;&nbsp; 55

              C1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 56&nbsp;&nbsp; 57&nbsp;&nbsp;
              58&nbsp;&nbsp; 59&nbsp;&nbsp; 60&nbsp;&nbsp; 61&nbsp;&nbsp; 62&nbsp;&nbsp;
              63&nbsp;&nbsp; 64&nbsp;&nbsp; 65&nbsp;&nbsp; 66

              C2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 67&nbsp;&nbsp; 68&nbsp;&nbsp;
              69&nbsp;&nbsp; 70&nbsp;&nbsp; 71&nbsp; &nbsp;72&nbsp;&nbsp; 73&nbsp;&nbsp;
              74&nbsp;&nbsp; 75&nbsp;&nbsp; 76&nbsp;&nbsp; 77&nbsp;&nbsp; 78

              :

              :

              where C1, C2, etc, are the "consider parameters" that may be added to the
              covariance matrix.&nbsp; The covariance matrix will be as large as the last
              element/model parameter needed.&nbsp; In other words, if the DC solved for all 6
              elements plus AGOM, the covariance matrix will be 9x9 (and the rows for B and
              BDOT will be all zeros).&nbsp; If the covariance matrix is unavailable, the size
              will be set to 0x0, and no data will follow.&nbsp; The cov field should contain
              only the lower left triangle values from top left down to bottom right, in
              order.

          error_control: Integrator error control.

          fixed_step: Boolean indicating use of fixed step size for this vector.

          geopotential_model: Geopotential model used for this vector (e.g. EGM-96, WGS-84, WGS-72, JGM-2, or
              GEM-T3), including mm degree zonals, nn degree/order tesserals. E.g. EGM-96
              24Z,24T.

          iau1980_terms: Number of terms used in the IAU 1980 nutation model (4, 50, or 106).

          id_orbit_determination: Unique identifier of the OD solution record that produced this state vector.
              This ID can be used to obtain additional information on an OrbitDetermination
              object using the 'get by ID' operation (e.g. /udl/orbitdetermination/{id}). For
              example, the OrbitDetermination with idOrbitDetermination = abc would be queries
              as /udl/orbitdetermination/abc.

          id_state_vector: Unique identifier of the record, auto-generated by the system.

          integrator_mode: Integrator Mode.

          in_track_thrust: Boolean indicating use of in-track thrust perturbations for this vector.

          last_ob_end: The end of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC format with microsecond precision. For an exact
              observation time, the firstObTime and lastObTime are the same.

          last_ob_start: The start of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC format with microsecond precision. For an exact
              observation time, the firstObTime and lastObTime are the same.

          leap_second_time: Time of the next leap second after epoch in ISO 8601 UTC time. If the next leap
              second is not known, the time of the previous leap second is used.

          lunar_solar: Boolean indicating use of lunar/solar perturbations for this vector.

          mass: The mass of the object, in kilograms.

          obs_available: The number of observations available for the OD of the object.

          obs_used: The number of observations accepted for the OD of the object.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by state vector source to indicate the target
              onorbit object of this state vector. This may be an internal identifier and not
              necessarily map to a valid satellite number.

          partials: Type of partial derivatives used (ANALYTIC, FULL NUM, or FAST NUM).

          pedigree: The pedigree of state vector, or methods used for its generation to include
              state update/orbit determination, propagation from another state, or a state
              from a calibration satellite (e.g. ORBIT_UPDATE, PROPAGATION, CALIBRATION,
              CONJUNCTION, FLIGHT_PLAN).

          polar_motion_x: Polar Wander Motion X (arc seconds).

          polar_motion_y: Polar Wander Motion Y (arc seconds).

          pos_unc: One sigma position uncertainty, in kilometers.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rec_od_span: The recommended OD time span calculated for the object, expressed in days.

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          residuals_acc: The percentage of residuals accepted in the OD of the object.

          rev_no: Epoch revolution number.

          rms: The Weighted Root Mean Squared (RMS) of the differential correction on the
              target object that produced this vector. WRMS is a quality indicator of the
              state vector update, with a value of 1.00 being optimal. WRMS applies to Batch
              Least Squares (BLS) processes.

          sat_no: Satellite/Catalog number of the target OnOrbit object.

          sigma_pos_uvw: Array containing the standard deviation of error in target object position, U, V
              and W direction respectively (km).

          sigma_vel_uvw: Array containing the standard deviation of error in target object velocity, U, V
              and W direction respectively (km/sec).

          solar_flux_ap_avg: Average solar flux geomagnetic index.

          solar_flux_f10: F10 (10.7 cm) solar flux value.

          solar_flux_f10_avg: F10 (10.7 cm) solar flux 81-day average value.

          solar_rad_press: Boolean indicating use of solar radiation pressure perturbations for this
              vector.

          solar_rad_press_coeff: Area-to-mass ratio coefficient for solar radiation pressure.

          solid_earth_tides: Boolean indicating use of solid earth tide perturbations for this vector.

          sourced_data: Optional array of UDL data (observation) UUIDs used to build this state vector.
              See the associated sourcedDataTypes array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          sourced_data_types: Optional array of UDL observation data types used to build this state vector
              (e.g. EO, RADAR, RF, DOA). See the associated sourcedData array for the specific
              UUIDs of observations for the positionally corresponding data types in this
              array (the two arrays must match in size).

          srp_area: The effective area of the object exposed to solar radiation pressure, expressed
              in meters^2.

          step_mode: Integrator step mode (AUTO, TIME, or S).

          step_size: Initial integration step size (seconds).

          step_size_selection: Initial step size selection (AUTO or MANUAL).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          tai_utc: TAI (Temps Atomique International) minus UTC (Universal Time Coordinates) offset
              in seconds.

          thrust_accel: Model parameter value for thrust acceleration (m/s2).

          tracks_avail: The number of sensor tracks available for the OD of the object.

          tracks_used: The number of sensor tracks accepted for the OD of the object.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this state vector was unable to be correlated to a known
              object. This flag should only be set to true by data providers after an attempt
              to correlate to an OnOrbit object was made and failed. If unable to correlate,
              the 'origObjectId' field may be populated with an internal data provider
              specific identifier.

          ut1_rate: Rate of change of UT1 (milliseconds/day) - first derivative of ut1Utc.

          ut1_utc: Universal Time-1 (UT1) minus UTC offset, in seconds.

          vel_unc: One sigma velocity uncertainty, in kilometers/second.

          xaccel: Cartesian X acceleration of target, in kilometers/second^2, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          xpos: Cartesian X position of the target, in kilometers, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          xpos_alt1: Cartesian X position of the target, in kilometers, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          xpos_alt2: Cartesian X position of the target, in kilometers, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          xvel: Cartesian X velocity of target, in kilometers/second, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          xvel_alt1: Cartesian X velocity of the target, in kilometers/second, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          xvel_alt2: Cartesian X velocity of the target, in kilometers/second, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          yaccel: Cartesian Y acceleration of target, in kilometers/second^2, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          ypos: Cartesian Y position of the target, in kilometers, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          ypos_alt1: Cartesian Y position of the target, in kilometers, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          ypos_alt2: Cartesian Y position of the target, in kilometers, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          yvel: Cartesian Y velocity of target, in kilometers/second, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          yvel_alt1: Cartesian Y velocity of the target, in kilometers/second, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          yvel_alt2: Cartesian Y velocity of the target, in kilometers/second, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zaccel: Cartesian Z acceleration of target, in kilometers/second^2, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          zpos: Cartesian Z position of the target, in kilometers, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          zpos_alt1: Cartesian Z position of the target, in kilometers, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zpos_alt2: Cartesian Z position of the target, in kilometers, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zvel: Cartesian Z velocity of target, in kilometers/second, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          zvel_alt1: Cartesian Z velocity of the target, in kilometers/second, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zvel_alt2: Cartesian Z velocity of the target, in kilometers/second, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/statevector",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "epoch": epoch,
                    "source": source,
                    "actual_od_span": actual_od_span,
                    "algorithm": algorithm,
                    "alt1_reference_frame": alt1_reference_frame,
                    "alt2_reference_frame": alt2_reference_frame,
                    "area": area,
                    "b_dot": b_dot,
                    "cm_offset": cm_offset,
                    "cov": cov,
                    "cov_method": cov_method,
                    "cov_reference_frame": cov_reference_frame,
                    "descriptor": descriptor,
                    "drag_area": drag_area,
                    "drag_coeff": drag_coeff,
                    "drag_model": drag_model,
                    "edr": edr,
                    "eq_cov": eq_cov,
                    "error_control": error_control,
                    "fixed_step": fixed_step,
                    "geopotential_model": geopotential_model,
                    "iau1980_terms": iau1980_terms,
                    "id_orbit_determination": id_orbit_determination,
                    "id_state_vector": id_state_vector,
                    "integrator_mode": integrator_mode,
                    "in_track_thrust": in_track_thrust,
                    "last_ob_end": last_ob_end,
                    "last_ob_start": last_ob_start,
                    "leap_second_time": leap_second_time,
                    "lunar_solar": lunar_solar,
                    "mass": mass,
                    "obs_available": obs_available,
                    "obs_used": obs_used,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "partials": partials,
                    "pedigree": pedigree,
                    "polar_motion_x": polar_motion_x,
                    "polar_motion_y": polar_motion_y,
                    "pos_unc": pos_unc,
                    "raw_file_uri": raw_file_uri,
                    "rec_od_span": rec_od_span,
                    "reference_frame": reference_frame,
                    "residuals_acc": residuals_acc,
                    "rev_no": rev_no,
                    "rms": rms,
                    "sat_no": sat_no,
                    "sigma_pos_uvw": sigma_pos_uvw,
                    "sigma_vel_uvw": sigma_vel_uvw,
                    "solar_flux_ap_avg": solar_flux_ap_avg,
                    "solar_flux_f10": solar_flux_f10,
                    "solar_flux_f10_avg": solar_flux_f10_avg,
                    "solar_rad_press": solar_rad_press,
                    "solar_rad_press_coeff": solar_rad_press_coeff,
                    "solid_earth_tides": solid_earth_tides,
                    "sourced_data": sourced_data,
                    "sourced_data_types": sourced_data_types,
                    "srp_area": srp_area,
                    "step_mode": step_mode,
                    "step_size": step_size,
                    "step_size_selection": step_size_selection,
                    "tags": tags,
                    "tai_utc": tai_utc,
                    "thrust_accel": thrust_accel,
                    "tracks_avail": tracks_avail,
                    "tracks_used": tracks_used,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "ut1_rate": ut1_rate,
                    "ut1_utc": ut1_utc,
                    "vel_unc": vel_unc,
                    "xaccel": xaccel,
                    "xpos": xpos,
                    "xpos_alt1": xpos_alt1,
                    "xpos_alt2": xpos_alt2,
                    "xvel": xvel,
                    "xvel_alt1": xvel_alt1,
                    "xvel_alt2": xvel_alt2,
                    "yaccel": yaccel,
                    "ypos": ypos,
                    "ypos_alt1": ypos_alt1,
                    "ypos_alt2": ypos_alt2,
                    "yvel": yvel,
                    "yvel_alt1": yvel_alt1,
                    "yvel_alt2": yvel_alt2,
                    "zaccel": zaccel,
                    "zpos": zpos,
                    "zpos_alt1": zpos_alt1,
                    "zpos_alt2": zpos_alt2,
                    "zvel": zvel,
                    "zvel_alt1": zvel_alt1,
                    "zvel_alt2": zvel_alt2,
                },
                state_vector_create_params.StateVectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[StateVectorAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/statevector",
            page=SyncOffsetPage[StateVectorAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    state_vector_list_params.StateVectorListParams,
                ),
            ),
            model=StateVectorAbridged,
        )

    def count(
        self,
        *,
        epoch: Union[str, datetime],
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
          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/statevector/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    state_vector_count_params.StateVectorCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[StateVectorIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of state
        vectors as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/statevector/createBulk",
            body=maybe_transform(body, Iterable[StateVectorIngestParam]),
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
    ) -> StateVectorFull:
        """
        Service operation to get a single state vector by its unique ID passed as a path
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
            f"/udl/statevector/{id}",
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
                    state_vector_get_params.StateVectorGetParams,
                ),
            ),
            cast_to=StateVectorFull,
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
    ) -> StateVectorQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/statevector/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateVectorQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StateVectorTupleResponse:
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

          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/statevector/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    state_vector_tuple_params.StateVectorTupleParams,
                ),
            ),
            cast_to=StateVectorTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[StateVectorIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple state vectors as a POST body and ingest into
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
            "/filedrop/udl-sv",
            body=maybe_transform(body, Iterable[StateVectorIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncStateVectorResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def current(self) -> AsyncCurrentResource:
        return AsyncCurrentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStateVectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStateVectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStateVectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncStateVectorResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        epoch: Union[str, datetime],
        source: str,
        actual_od_span: float | NotGiven = NOT_GIVEN,
        algorithm: str | NotGiven = NOT_GIVEN,
        alt1_reference_frame: str | NotGiven = NOT_GIVEN,
        alt2_reference_frame: str | NotGiven = NOT_GIVEN,
        area: float | NotGiven = NOT_GIVEN,
        b_dot: float | NotGiven = NOT_GIVEN,
        cm_offset: float | NotGiven = NOT_GIVEN,
        cov: Iterable[float] | NotGiven = NOT_GIVEN,
        cov_method: str | NotGiven = NOT_GIVEN,
        cov_reference_frame: Literal["J2000", "UVW", "EFG/TDR", "TEME", "GCRF"] | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        drag_area: float | NotGiven = NOT_GIVEN,
        drag_coeff: float | NotGiven = NOT_GIVEN,
        drag_model: str | NotGiven = NOT_GIVEN,
        edr: float | NotGiven = NOT_GIVEN,
        eq_cov: Iterable[float] | NotGiven = NOT_GIVEN,
        error_control: float | NotGiven = NOT_GIVEN,
        fixed_step: bool | NotGiven = NOT_GIVEN,
        geopotential_model: str | NotGiven = NOT_GIVEN,
        iau1980_terms: int | NotGiven = NOT_GIVEN,
        id_orbit_determination: str | NotGiven = NOT_GIVEN,
        id_state_vector: str | NotGiven = NOT_GIVEN,
        integrator_mode: str | NotGiven = NOT_GIVEN,
        in_track_thrust: bool | NotGiven = NOT_GIVEN,
        last_ob_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_ob_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        leap_second_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        lunar_solar: bool | NotGiven = NOT_GIVEN,
        mass: float | NotGiven = NOT_GIVEN,
        obs_available: int | NotGiven = NOT_GIVEN,
        obs_used: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        partials: str | NotGiven = NOT_GIVEN,
        pedigree: str | NotGiven = NOT_GIVEN,
        polar_motion_x: float | NotGiven = NOT_GIVEN,
        polar_motion_y: float | NotGiven = NOT_GIVEN,
        pos_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rec_od_span: float | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        residuals_acc: float | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        rms: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sigma_pos_uvw: Iterable[float] | NotGiven = NOT_GIVEN,
        sigma_vel_uvw: Iterable[float] | NotGiven = NOT_GIVEN,
        solar_flux_ap_avg: float | NotGiven = NOT_GIVEN,
        solar_flux_f10: float | NotGiven = NOT_GIVEN,
        solar_flux_f10_avg: float | NotGiven = NOT_GIVEN,
        solar_rad_press: bool | NotGiven = NOT_GIVEN,
        solar_rad_press_coeff: float | NotGiven = NOT_GIVEN,
        solid_earth_tides: bool | NotGiven = NOT_GIVEN,
        sourced_data: List[str] | NotGiven = NOT_GIVEN,
        sourced_data_types: List[Literal["EO", "RADAR", "RF", "DOA", "ELSET", "SV"]] | NotGiven = NOT_GIVEN,
        srp_area: float | NotGiven = NOT_GIVEN,
        step_mode: str | NotGiven = NOT_GIVEN,
        step_size: float | NotGiven = NOT_GIVEN,
        step_size_selection: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        tai_utc: float | NotGiven = NOT_GIVEN,
        thrust_accel: float | NotGiven = NOT_GIVEN,
        tracks_avail: int | NotGiven = NOT_GIVEN,
        tracks_used: int | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        ut1_rate: float | NotGiven = NOT_GIVEN,
        ut1_utc: float | NotGiven = NOT_GIVEN,
        vel_unc: float | NotGiven = NOT_GIVEN,
        xaccel: float | NotGiven = NOT_GIVEN,
        xpos: float | NotGiven = NOT_GIVEN,
        xpos_alt1: float | NotGiven = NOT_GIVEN,
        xpos_alt2: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        xvel_alt1: float | NotGiven = NOT_GIVEN,
        xvel_alt2: float | NotGiven = NOT_GIVEN,
        yaccel: float | NotGiven = NOT_GIVEN,
        ypos: float | NotGiven = NOT_GIVEN,
        ypos_alt1: float | NotGiven = NOT_GIVEN,
        ypos_alt2: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        yvel_alt1: float | NotGiven = NOT_GIVEN,
        yvel_alt2: float | NotGiven = NOT_GIVEN,
        zaccel: float | NotGiven = NOT_GIVEN,
        zpos: float | NotGiven = NOT_GIVEN,
        zpos_alt1: float | NotGiven = NOT_GIVEN,
        zpos_alt2: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        zvel_alt1: float | NotGiven = NOT_GIVEN,
        zvel_alt2: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single state vector as a POST body and ingest into
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

          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision.

          source: Source of the data.

          actual_od_span: The actual time span used for the OD of the object, expressed in days.

          algorithm: Optional algorithm used to produce this record.

          alt1_reference_frame: The reference frame of the alternate1 (Alt1) cartesian orbital state.

          alt2_reference_frame: The reference frame of the alternate2 (Alt2) cartesian orbital state.

          area: The actual area of the object at it's largest cross-section, expressed in
              meters^2.

          b_dot: First derivative of drag/ballistic coefficient (m2/kg-s).

          cm_offset: Model parameter value for center of mass offset (m).

          cov: Covariance matrix, in kilometer and second based units, in the specified
              covReferenceFrame. If the covReferenceFrame is null it is assumed to be J2000.
              The array values (1-21) represent the lower triangular half of the
              position-velocity covariance matrix. The size of the covariance matrix is
              dynamic, depending on whether the covariance for position only or position &
              velocity. The covariance elements are position dependent within the array with
              values ordered as follows:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;&nbsp;x'&nbsp;&nbsp;&nbsp;&nbsp;y'&nbsp;&nbsp;&nbsp;&nbsp;z'&nbsp;&nbsp;&nbsp;&nbsp;DRG&nbsp;&nbsp;&nbsp;&nbsp;SRP&nbsp;&nbsp;&nbsp;&nbsp;THR&nbsp;&nbsp;

              x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1

              y&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;3

              z&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;6

              x'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;10

              y'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11&nbsp;&nbsp;12&nbsp;&nbsp;13&nbsp;&nbsp;14&nbsp;&nbsp;15

              z'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16&nbsp;&nbsp;17&nbsp;&nbsp;18&nbsp;&nbsp;19&nbsp;&nbsp;20&nbsp;&nbsp;&nbsp;21&nbsp;

              The cov array should contain only the lower left triangle values from top left
              down to bottom right, in order.

              If additional covariance terms are included for DRAG, SRP, and/or THRUST, the
              matrix can be extended with the following order of elements:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;&nbsp;x'&nbsp;&nbsp;&nbsp;&nbsp;y'&nbsp;&nbsp;&nbsp;&nbsp;z'&nbsp;&nbsp;&nbsp;&nbsp;DRG&nbsp;&nbsp;&nbsp;&nbsp;SRP&nbsp;&nbsp;&nbsp;&nbsp;THR

              DRG&nbsp;&nbsp;&nbsp;22&nbsp;&nbsp;23&nbsp;&nbsp;24&nbsp;&nbsp;25&nbsp;&nbsp;26&nbsp;&nbsp;&nbsp;27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28&nbsp;&nbsp;

              SRP&nbsp;&nbsp;&nbsp;29&nbsp;&nbsp;30&nbsp;&nbsp;31&nbsp;&nbsp;32&nbsp;&nbsp;33&nbsp;&nbsp;&nbsp;34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36&nbsp;&nbsp;

              THR&nbsp;&nbsp;&nbsp;37&nbsp;&nbsp;38&nbsp;&nbsp;39&nbsp;&nbsp;40&nbsp;&nbsp;41&nbsp;&nbsp;&nbsp;42&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;43&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;45&nbsp;

          cov_method: The method used to generate the covariance during the orbit determination (OD)
              that produced the state vector, or whether an arbitrary, non-calculated default
              value was used (CALCULATED, DEFAULT).

          cov_reference_frame: The reference frame of the covariance matrix elements. If the covReferenceFrame
              is null it is assumed to be J2000.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          drag_area: The effective area of the object exposed to atmospheric drag, expressed in
              meters^2.

          drag_coeff: Area-to-mass ratio coefficient for atmospheric ballistic drag (m2/kg).

          drag_model: The Drag Model used for this vector (e.g. HARRIS-PRIESTER, JAC70, JBH09, MSIS90,
              NONE, etc.).

          edr: Model parameter value for energy dissipation rate (EDR) (w/kg).

          eq_cov: The covariance matrix values represent the lower triangular half of the
              covariance matrix in terms of equinoctial elements.&nbsp; The size of the
              covariance matrix is dynamic.&nbsp; The values are outputted in order across
              each row, i.e.:

              1&nbsp;&nbsp; 2&nbsp;&nbsp; 3&nbsp;&nbsp; 4&nbsp;&nbsp; 5

              6&nbsp;&nbsp; 7&nbsp;&nbsp; 8&nbsp;&nbsp; 9&nbsp; 10

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              51&nbsp; 52&nbsp; 53&nbsp; 54&nbsp; 55

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :&nbsp;&nbsp; :

              The ordering of values is as follows:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Af&nbsp;&nbsp;
              Ag&nbsp;&nbsp; L&nbsp;&nbsp;&nbsp; N&nbsp;&nbsp; Chi&nbsp; Psi&nbsp;&nbsp;
              B&nbsp;&nbsp; BDOT AGOM&nbsp; T&nbsp;&nbsp; C1&nbsp;&nbsp; C2&nbsp; ...

              Af&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1

              Ag&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 3

              L&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              4&nbsp;&nbsp;&nbsp; 5&nbsp;&nbsp;&nbsp; 6

              N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              7&nbsp;&nbsp;&nbsp; 8&nbsp;&nbsp;&nbsp; 9&nbsp;&nbsp; 10

              Chi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 11&nbsp;&nbsp; 12&nbsp;&nbsp;
              13&nbsp;&nbsp; 14&nbsp;&nbsp; 15

              Psi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16&nbsp;&nbsp; 17&nbsp;&nbsp;
              18&nbsp;&nbsp; 19&nbsp;&nbsp; 20&nbsp;&nbsp; 21

              B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 22&nbsp;&nbsp;
              23&nbsp;&nbsp; 24 &nbsp;&nbsp;25&nbsp;&nbsp; 26&nbsp;&nbsp; 27&nbsp;&nbsp; 28

              BDOT&nbsp;&nbsp; 29&nbsp;&nbsp; 30&nbsp;&nbsp; 31&nbsp;&nbsp; 32&nbsp;&nbsp;
              33&nbsp;&nbsp; 34&nbsp;&nbsp; 35&nbsp;&nbsp; 36

              AGOM&nbsp; 37&nbsp;&nbsp; 38&nbsp;&nbsp; 39&nbsp;&nbsp; 40&nbsp;&nbsp;
              41&nbsp;&nbsp; 42&nbsp;&nbsp; 43&nbsp;&nbsp; 44&nbsp;&nbsp; 45

              T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 46&nbsp;&nbsp;
              47&nbsp;&nbsp; 48&nbsp;&nbsp; 49&nbsp;&nbsp; 50&nbsp;&nbsp; 51&nbsp;&nbsp;
              52&nbsp;&nbsp; 53&nbsp;&nbsp; 54&nbsp;&nbsp; 55

              C1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 56&nbsp;&nbsp; 57&nbsp;&nbsp;
              58&nbsp;&nbsp; 59&nbsp;&nbsp; 60&nbsp;&nbsp; 61&nbsp;&nbsp; 62&nbsp;&nbsp;
              63&nbsp;&nbsp; 64&nbsp;&nbsp; 65&nbsp;&nbsp; 66

              C2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 67&nbsp;&nbsp; 68&nbsp;&nbsp;
              69&nbsp;&nbsp; 70&nbsp;&nbsp; 71&nbsp; &nbsp;72&nbsp;&nbsp; 73&nbsp;&nbsp;
              74&nbsp;&nbsp; 75&nbsp;&nbsp; 76&nbsp;&nbsp; 77&nbsp;&nbsp; 78

              :

              :

              where C1, C2, etc, are the "consider parameters" that may be added to the
              covariance matrix.&nbsp; The covariance matrix will be as large as the last
              element/model parameter needed.&nbsp; In other words, if the DC solved for all 6
              elements plus AGOM, the covariance matrix will be 9x9 (and the rows for B and
              BDOT will be all zeros).&nbsp; If the covariance matrix is unavailable, the size
              will be set to 0x0, and no data will follow.&nbsp; The cov field should contain
              only the lower left triangle values from top left down to bottom right, in
              order.

          error_control: Integrator error control.

          fixed_step: Boolean indicating use of fixed step size for this vector.

          geopotential_model: Geopotential model used for this vector (e.g. EGM-96, WGS-84, WGS-72, JGM-2, or
              GEM-T3), including mm degree zonals, nn degree/order tesserals. E.g. EGM-96
              24Z,24T.

          iau1980_terms: Number of terms used in the IAU 1980 nutation model (4, 50, or 106).

          id_orbit_determination: Unique identifier of the OD solution record that produced this state vector.
              This ID can be used to obtain additional information on an OrbitDetermination
              object using the 'get by ID' operation (e.g. /udl/orbitdetermination/{id}). For
              example, the OrbitDetermination with idOrbitDetermination = abc would be queries
              as /udl/orbitdetermination/abc.

          id_state_vector: Unique identifier of the record, auto-generated by the system.

          integrator_mode: Integrator Mode.

          in_track_thrust: Boolean indicating use of in-track thrust perturbations for this vector.

          last_ob_end: The end of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC format with microsecond precision. For an exact
              observation time, the firstObTime and lastObTime are the same.

          last_ob_start: The start of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC format with microsecond precision. For an exact
              observation time, the firstObTime and lastObTime are the same.

          leap_second_time: Time of the next leap second after epoch in ISO 8601 UTC time. If the next leap
              second is not known, the time of the previous leap second is used.

          lunar_solar: Boolean indicating use of lunar/solar perturbations for this vector.

          mass: The mass of the object, in kilograms.

          obs_available: The number of observations available for the OD of the object.

          obs_used: The number of observations accepted for the OD of the object.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by state vector source to indicate the target
              onorbit object of this state vector. This may be an internal identifier and not
              necessarily map to a valid satellite number.

          partials: Type of partial derivatives used (ANALYTIC, FULL NUM, or FAST NUM).

          pedigree: The pedigree of state vector, or methods used for its generation to include
              state update/orbit determination, propagation from another state, or a state
              from a calibration satellite (e.g. ORBIT_UPDATE, PROPAGATION, CALIBRATION,
              CONJUNCTION, FLIGHT_PLAN).

          polar_motion_x: Polar Wander Motion X (arc seconds).

          polar_motion_y: Polar Wander Motion Y (arc seconds).

          pos_unc: One sigma position uncertainty, in kilometers.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rec_od_span: The recommended OD time span calculated for the object, expressed in days.

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          residuals_acc: The percentage of residuals accepted in the OD of the object.

          rev_no: Epoch revolution number.

          rms: The Weighted Root Mean Squared (RMS) of the differential correction on the
              target object that produced this vector. WRMS is a quality indicator of the
              state vector update, with a value of 1.00 being optimal. WRMS applies to Batch
              Least Squares (BLS) processes.

          sat_no: Satellite/Catalog number of the target OnOrbit object.

          sigma_pos_uvw: Array containing the standard deviation of error in target object position, U, V
              and W direction respectively (km).

          sigma_vel_uvw: Array containing the standard deviation of error in target object velocity, U, V
              and W direction respectively (km/sec).

          solar_flux_ap_avg: Average solar flux geomagnetic index.

          solar_flux_f10: F10 (10.7 cm) solar flux value.

          solar_flux_f10_avg: F10 (10.7 cm) solar flux 81-day average value.

          solar_rad_press: Boolean indicating use of solar radiation pressure perturbations for this
              vector.

          solar_rad_press_coeff: Area-to-mass ratio coefficient for solar radiation pressure.

          solid_earth_tides: Boolean indicating use of solid earth tide perturbations for this vector.

          sourced_data: Optional array of UDL data (observation) UUIDs used to build this state vector.
              See the associated sourcedDataTypes array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          sourced_data_types: Optional array of UDL observation data types used to build this state vector
              (e.g. EO, RADAR, RF, DOA). See the associated sourcedData array for the specific
              UUIDs of observations for the positionally corresponding data types in this
              array (the two arrays must match in size).

          srp_area: The effective area of the object exposed to solar radiation pressure, expressed
              in meters^2.

          step_mode: Integrator step mode (AUTO, TIME, or S).

          step_size: Initial integration step size (seconds).

          step_size_selection: Initial step size selection (AUTO or MANUAL).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          tai_utc: TAI (Temps Atomique International) minus UTC (Universal Time Coordinates) offset
              in seconds.

          thrust_accel: Model parameter value for thrust acceleration (m/s2).

          tracks_avail: The number of sensor tracks available for the OD of the object.

          tracks_used: The number of sensor tracks accepted for the OD of the object.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this state vector was unable to be correlated to a known
              object. This flag should only be set to true by data providers after an attempt
              to correlate to an OnOrbit object was made and failed. If unable to correlate,
              the 'origObjectId' field may be populated with an internal data provider
              specific identifier.

          ut1_rate: Rate of change of UT1 (milliseconds/day) - first derivative of ut1Utc.

          ut1_utc: Universal Time-1 (UT1) minus UTC offset, in seconds.

          vel_unc: One sigma velocity uncertainty, in kilometers/second.

          xaccel: Cartesian X acceleration of target, in kilometers/second^2, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          xpos: Cartesian X position of the target, in kilometers, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          xpos_alt1: Cartesian X position of the target, in kilometers, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          xpos_alt2: Cartesian X position of the target, in kilometers, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          xvel: Cartesian X velocity of target, in kilometers/second, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          xvel_alt1: Cartesian X velocity of the target, in kilometers/second, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          xvel_alt2: Cartesian X velocity of the target, in kilometers/second, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          yaccel: Cartesian Y acceleration of target, in kilometers/second^2, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          ypos: Cartesian Y position of the target, in kilometers, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          ypos_alt1: Cartesian Y position of the target, in kilometers, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          ypos_alt2: Cartesian Y position of the target, in kilometers, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          yvel: Cartesian Y velocity of target, in kilometers/second, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          yvel_alt1: Cartesian Y velocity of the target, in kilometers/second, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          yvel_alt2: Cartesian Y velocity of the target, in kilometers/second, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zaccel: Cartesian Z acceleration of target, in kilometers/second^2, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          zpos: Cartesian Z position of the target, in kilometers, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          zpos_alt1: Cartesian Z position of the target, in kilometers, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zpos_alt2: Cartesian Z position of the target, in kilometers, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zvel: Cartesian Z velocity of target, in kilometers/second, in the specified
              referenceFrame. If referenceFrame is null then J2K should be assumed.

          zvel_alt1: Cartesian Z velocity of the target, in kilometers/second, in the specified
              alt1ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          zvel_alt2: Cartesian Z velocity of the target, in kilometers/second, in the specified
              alt2ReferenceFrame. Alternate reference frames are optional and are intended to
              allow a data source to provide an equivalent vector in a different cartesian
              frame than the primary vector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/statevector",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "epoch": epoch,
                    "source": source,
                    "actual_od_span": actual_od_span,
                    "algorithm": algorithm,
                    "alt1_reference_frame": alt1_reference_frame,
                    "alt2_reference_frame": alt2_reference_frame,
                    "area": area,
                    "b_dot": b_dot,
                    "cm_offset": cm_offset,
                    "cov": cov,
                    "cov_method": cov_method,
                    "cov_reference_frame": cov_reference_frame,
                    "descriptor": descriptor,
                    "drag_area": drag_area,
                    "drag_coeff": drag_coeff,
                    "drag_model": drag_model,
                    "edr": edr,
                    "eq_cov": eq_cov,
                    "error_control": error_control,
                    "fixed_step": fixed_step,
                    "geopotential_model": geopotential_model,
                    "iau1980_terms": iau1980_terms,
                    "id_orbit_determination": id_orbit_determination,
                    "id_state_vector": id_state_vector,
                    "integrator_mode": integrator_mode,
                    "in_track_thrust": in_track_thrust,
                    "last_ob_end": last_ob_end,
                    "last_ob_start": last_ob_start,
                    "leap_second_time": leap_second_time,
                    "lunar_solar": lunar_solar,
                    "mass": mass,
                    "obs_available": obs_available,
                    "obs_used": obs_used,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "partials": partials,
                    "pedigree": pedigree,
                    "polar_motion_x": polar_motion_x,
                    "polar_motion_y": polar_motion_y,
                    "pos_unc": pos_unc,
                    "raw_file_uri": raw_file_uri,
                    "rec_od_span": rec_od_span,
                    "reference_frame": reference_frame,
                    "residuals_acc": residuals_acc,
                    "rev_no": rev_no,
                    "rms": rms,
                    "sat_no": sat_no,
                    "sigma_pos_uvw": sigma_pos_uvw,
                    "sigma_vel_uvw": sigma_vel_uvw,
                    "solar_flux_ap_avg": solar_flux_ap_avg,
                    "solar_flux_f10": solar_flux_f10,
                    "solar_flux_f10_avg": solar_flux_f10_avg,
                    "solar_rad_press": solar_rad_press,
                    "solar_rad_press_coeff": solar_rad_press_coeff,
                    "solid_earth_tides": solid_earth_tides,
                    "sourced_data": sourced_data,
                    "sourced_data_types": sourced_data_types,
                    "srp_area": srp_area,
                    "step_mode": step_mode,
                    "step_size": step_size,
                    "step_size_selection": step_size_selection,
                    "tags": tags,
                    "tai_utc": tai_utc,
                    "thrust_accel": thrust_accel,
                    "tracks_avail": tracks_avail,
                    "tracks_used": tracks_used,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "ut1_rate": ut1_rate,
                    "ut1_utc": ut1_utc,
                    "vel_unc": vel_unc,
                    "xaccel": xaccel,
                    "xpos": xpos,
                    "xpos_alt1": xpos_alt1,
                    "xpos_alt2": xpos_alt2,
                    "xvel": xvel,
                    "xvel_alt1": xvel_alt1,
                    "xvel_alt2": xvel_alt2,
                    "yaccel": yaccel,
                    "ypos": ypos,
                    "ypos_alt1": ypos_alt1,
                    "ypos_alt2": ypos_alt2,
                    "yvel": yvel,
                    "yvel_alt1": yvel_alt1,
                    "yvel_alt2": yvel_alt2,
                    "zaccel": zaccel,
                    "zpos": zpos,
                    "zpos_alt1": zpos_alt1,
                    "zpos_alt2": zpos_alt2,
                    "zvel": zvel,
                    "zvel_alt1": zvel_alt1,
                    "zvel_alt2": zvel_alt2,
                },
                state_vector_create_params.StateVectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[StateVectorAbridged, AsyncOffsetPage[StateVectorAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/statevector",
            page=AsyncOffsetPage[StateVectorAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    state_vector_list_params.StateVectorListParams,
                ),
            ),
            model=StateVectorAbridged,
        )

    async def count(
        self,
        *,
        epoch: Union[str, datetime],
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
          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/statevector/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    state_vector_count_params.StateVectorCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[StateVectorIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of state
        vectors as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/statevector/createBulk",
            body=await async_maybe_transform(body, Iterable[StateVectorIngestParam]),
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
    ) -> StateVectorFull:
        """
        Service operation to get a single state vector by its unique ID passed as a path
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
            f"/udl/statevector/{id}",
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
                    state_vector_get_params.StateVectorGetParams,
                ),
            ),
            cast_to=StateVectorFull,
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
    ) -> StateVectorQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/statevector/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateVectorQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StateVectorTupleResponse:
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

          epoch: Time of validity for state vector in ISO 8601 UTC datetime format, with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/statevector/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    state_vector_tuple_params.StateVectorTupleParams,
                ),
            ),
            cast_to=StateVectorTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[StateVectorIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple state vectors as a POST body and ingest into
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
            "/filedrop/udl-sv",
            body=await async_maybe_transform(body, Iterable[StateVectorIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class StateVectorResourceWithRawResponse:
    def __init__(self, state_vector: StateVectorResource) -> None:
        self._state_vector = state_vector

        self.create = to_raw_response_wrapper(
            state_vector.create,
        )
        self.list = to_raw_response_wrapper(
            state_vector.list,
        )
        self.count = to_raw_response_wrapper(
            state_vector.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            state_vector.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            state_vector.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            state_vector.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            state_vector.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            state_vector.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._state_vector.history)

    @cached_property
    def current(self) -> CurrentResourceWithRawResponse:
        return CurrentResourceWithRawResponse(self._state_vector.current)


class AsyncStateVectorResourceWithRawResponse:
    def __init__(self, state_vector: AsyncStateVectorResource) -> None:
        self._state_vector = state_vector

        self.create = async_to_raw_response_wrapper(
            state_vector.create,
        )
        self.list = async_to_raw_response_wrapper(
            state_vector.list,
        )
        self.count = async_to_raw_response_wrapper(
            state_vector.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            state_vector.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            state_vector.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            state_vector.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            state_vector.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            state_vector.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._state_vector.history)

    @cached_property
    def current(self) -> AsyncCurrentResourceWithRawResponse:
        return AsyncCurrentResourceWithRawResponse(self._state_vector.current)


class StateVectorResourceWithStreamingResponse:
    def __init__(self, state_vector: StateVectorResource) -> None:
        self._state_vector = state_vector

        self.create = to_streamed_response_wrapper(
            state_vector.create,
        )
        self.list = to_streamed_response_wrapper(
            state_vector.list,
        )
        self.count = to_streamed_response_wrapper(
            state_vector.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            state_vector.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            state_vector.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            state_vector.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            state_vector.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            state_vector.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._state_vector.history)

    @cached_property
    def current(self) -> CurrentResourceWithStreamingResponse:
        return CurrentResourceWithStreamingResponse(self._state_vector.current)


class AsyncStateVectorResourceWithStreamingResponse:
    def __init__(self, state_vector: AsyncStateVectorResource) -> None:
        self._state_vector = state_vector

        self.create = async_to_streamed_response_wrapper(
            state_vector.create,
        )
        self.list = async_to_streamed_response_wrapper(
            state_vector.list,
        )
        self.count = async_to_streamed_response_wrapper(
            state_vector.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            state_vector.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            state_vector.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            state_vector.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            state_vector.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            state_vector.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._state_vector.history)

    @cached_property
    def current(self) -> AsyncCurrentResourceWithStreamingResponse:
        return AsyncCurrentResourceWithStreamingResponse(self._state_vector.current)
