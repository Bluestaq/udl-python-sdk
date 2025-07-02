# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    orbitdetermination_get_params,
    orbitdetermination_list_params,
    orbitdetermination_count_params,
    orbitdetermination_tuple_params,
    orbitdetermination_create_params,
    orbitdetermination_create_bulk_params,
    orbitdetermination_unvalidated_publish_params,
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
from ...types.orbitdetermination_get_response import OrbitdeterminationGetResponse
from ...types.orbitdetermination_list_response import OrbitdeterminationListResponse
from ...types.orbitdetermination_tuple_response import OrbitdeterminationTupleResponse
from ...types.orbitdetermination_queryhelp_response import OrbitdeterminationQueryhelpResponse

__all__ = ["OrbitdeterminationResource", "AsyncOrbitdeterminationResource"]


class OrbitdeterminationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrbitdeterminationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrbitdeterminationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrbitdeterminationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OrbitdeterminationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        initial_od: bool,
        method: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        accepted_ob_ids: List[str] | NotGiven = NOT_GIVEN,
        accepted_ob_typs: List[str] | NotGiven = NOT_GIVEN,
        agom_est: bool | NotGiven = NOT_GIVEN,
        agom_model: str | NotGiven = NOT_GIVEN,
        apriori_elset: orbitdetermination_create_params.AprioriElset | NotGiven = NOT_GIVEN,
        apriori_id_elset: str | NotGiven = NOT_GIVEN,
        apriori_id_state_vector: str | NotGiven = NOT_GIVEN,
        apriori_state_vector: orbitdetermination_create_params.AprioriStateVector | NotGiven = NOT_GIVEN,
        ballistic_coeff_est: bool | NotGiven = NOT_GIVEN,
        ballistic_coeff_model: str | NotGiven = NOT_GIVEN,
        best_pass_wrms: float | NotGiven = NOT_GIVEN,
        edr: float | NotGiven = NOT_GIVEN,
        effective_from: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        error_growth_rate: float | NotGiven = NOT_GIVEN,
        first_pass_wrms: float | NotGiven = NOT_GIVEN,
        fit_span: float | NotGiven = NOT_GIVEN,
        last_ob_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_ob_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        method_source: str | NotGiven = NOT_GIVEN,
        num_iterations: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        previous_wrms: float | NotGiven = NOT_GIVEN,
        rejected_ob_ids: List[str] | NotGiven = NOT_GIVEN,
        rejected_ob_typs: List[str] | NotGiven = NOT_GIVEN,
        rms_convergence_criteria: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sensor_ids: List[str] | NotGiven = NOT_GIVEN,
        time_span: float | NotGiven = NOT_GIVEN,
        wrms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OrbitDetermination record as a POST body and
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

          end_time: End time for OD solution in ISO 8601 UTC datetime format, with microsecond
              precision.

          initial_od: Flag indicating whether this is an initial orbit determination.

          method: Orbit determination method used to produce this record (e.g. BLS, KF, UKF,
              etc.).

          source: Source of the data.

          start_time: Start time for OD solution in ISO 8601 UTC datetime format, with microsecond
              precision.

          id: Unique identifier of the record, auto-generated by the system.

          accepted_ob_ids: Array of UDL data (observation) UUIDs that were accepted in this OD solution.
              See the associated acceptedObTyps array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          accepted_ob_typs: Array of UDL observation types (e.g. DOA, EO, RADAR, RF) of the observations
              that were accepted in this OD solution. See the associated acceptedObIds array
              for the records UUID(s), positionally corresponding to the record types in this
              array. The acceptedObTyps and acceptedObIds arrays must match in size.

          agom_est: Flag indicating whether the AGOM was estimated during this OD solution.

          agom_model: Model used to estimate the AGOM.

          apriori_elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          apriori_id_elset: Identifier of the element set used to seed this OD solution. This ID can be used
              to obtain additional information on an Elset object using the 'get by ID'
              operation (e.g. /udl/elset/{id}). For example, the Elset with idElset = abc
              would be queried as /udl/elset/abc.

          apriori_id_state_vector: Identifier of the state vector used to seed this OD solution. This ID can be
              used to obtain additional information on a StateVector object using the 'get by
              ID' operation (e.g. /udl/statevector/{id}). For example, the StateVector with
              idStateVector = abc would be queried as /udl/statevector/abc.

          apriori_state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          ballistic_coeff_est: Flag indicating whether the ballistic coefficient was estimated during this OD
              solution.

          ballistic_coeff_model: Model used to estimate the ballistic coefficient.

          best_pass_wrms: Lowest Weighted Root Mean Squared (RMS) value achieved for any single satellite
              pass during the observation span, indicating the pass with the highest quality
              OD solution.

          edr: Model parameter value for energy dissipation rate (EDR) in watts per kilogram.

          effective_from: Optional start time at which this OD solution is accurate, in ISO 8601 UTC
              datetime format with microsecond precision.

          effective_until: Optional end time at which this OD solution may no longer be accurate, in ISO
              8601 UTC datetime format with microsecond precision.

          error_growth_rate: Error growth rate of the OD solution in kilometers per day.

          first_pass_wrms: The Weighted Root Mean Squared (RMS) calculated for the first satellite pass in
              the observation span. Serves as the initial quality metric for the beginning of
              the observation period.

          fit_span: The fit span, in days, used in a Batch Least Squares (BLS) OD.

          last_ob_end: The end of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC datetime format with microsecond precision. For an
              exact observation time, the lastObStart and lastObEnd are the same.

          last_ob_start: The start of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC datetime format with microsecond precision. For an
              exact observation time, the lastObStart and lastObEnd are the same.

          method_source: Source of orbit determination method used to produce this record (e.g. ASW,
              ACTRAC, FreeFlyer, GEODYNE, GDTS, etc.).

          num_iterations: The number of iterations taken for the algorithm to converge on an OD solution.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the OD source to indicate the target on-orbit
              object of this OD solution. This may be an internal identifier and not
              necessarily map to a valid satellite number.

          previous_wrms: The Weighted Root Mean Squared (RMS) of the differential correction from the
              previous overhead pass of the satellite. Provides a point of comparison for
              assessing changes in the quality of the OD solution between consecutive passes.

          rejected_ob_ids: Array of UDL data (observation) UUIDs that were rejected in this OD solution.
              See the associated rejectedObTyps array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          rejected_ob_typs: Array of UDL observation types (e.g. DOA, EO, RADAR, RF) of the observations
              that were rejected in this OD solution. See the associated rejectedObIds array
              for the records UUID(s), positionally corresponding to the record types in this
              array. The rejectedObTyps and rejectedObIds arrays must match in size.

          rms_convergence_criteria: OD parameter value for the Root Mean Square (RMS) convergence criteria to
              successfully close the OD solution.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          sensor_ids: Array of UDL UUIDs (idSensor) of the sensors that contributed observations in
              this OD solution.

          time_span: The time span used for the OD of the object, in days.

          wrms: The Weighted Root Mean Squared (RMS) of the differential correction of the
              target object that produced this OD state. WRMS is a quality indicator of the OD
              update, with a value of 1.00 being optimal. WRMS applies to batch least squares
              (BLS) processes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/orbitdetermination",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "initial_od": initial_od,
                    "method": method,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "accepted_ob_ids": accepted_ob_ids,
                    "accepted_ob_typs": accepted_ob_typs,
                    "agom_est": agom_est,
                    "agom_model": agom_model,
                    "apriori_elset": apriori_elset,
                    "apriori_id_elset": apriori_id_elset,
                    "apriori_id_state_vector": apriori_id_state_vector,
                    "apriori_state_vector": apriori_state_vector,
                    "ballistic_coeff_est": ballistic_coeff_est,
                    "ballistic_coeff_model": ballistic_coeff_model,
                    "best_pass_wrms": best_pass_wrms,
                    "edr": edr,
                    "effective_from": effective_from,
                    "effective_until": effective_until,
                    "error_growth_rate": error_growth_rate,
                    "first_pass_wrms": first_pass_wrms,
                    "fit_span": fit_span,
                    "last_ob_end": last_ob_end,
                    "last_ob_start": last_ob_start,
                    "method_source": method_source,
                    "num_iterations": num_iterations,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "previous_wrms": previous_wrms,
                    "rejected_ob_ids": rejected_ob_ids,
                    "rejected_ob_typs": rejected_ob_typs,
                    "rms_convergence_criteria": rms_convergence_criteria,
                    "sat_no": sat_no,
                    "sensor_ids": sensor_ids,
                    "time_span": time_span,
                    "wrms": wrms,
                },
                orbitdetermination_create_params.OrbitdeterminationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[OrbitdeterminationListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/orbitdetermination",
            page=SyncOffsetPage[OrbitdeterminationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    orbitdetermination_list_params.OrbitdeterminationListParams,
                ),
            ),
            model=OrbitdeterminationListResponse,
        )

    def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/orbitdetermination/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    orbitdetermination_count_params.OrbitdeterminationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[orbitdetermination_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        OrbitDetermination records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into the UDL. Data
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
            "/udl/orbitdetermination/createBulk",
            body=maybe_transform(body, Iterable[orbitdetermination_create_bulk_params.Body]),
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
    ) -> OrbitdeterminationGetResponse:
        """
        Service operation to get a single OrbitDetermination record by its unique ID
        passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/orbitdetermination/{id}",
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
                    orbitdetermination_get_params.OrbitdeterminationGetParams,
                ),
            ),
            cast_to=OrbitdeterminationGetResponse,
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
    ) -> OrbitdeterminationQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/orbitdetermination/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrbitdeterminationQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrbitdeterminationTupleResponse:
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

          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/orbitdetermination/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    orbitdetermination_tuple_params.OrbitdeterminationTupleParams,
                ),
            ),
            cast_to=OrbitdeterminationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[orbitdetermination_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple OrbitDetermination records as a POST body and
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
            "/filedrop/udl-orbitdetermination",
            body=maybe_transform(body, Iterable[orbitdetermination_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrbitdeterminationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrbitdeterminationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrbitdeterminationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrbitdeterminationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOrbitdeterminationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        initial_od: bool,
        method: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        accepted_ob_ids: List[str] | NotGiven = NOT_GIVEN,
        accepted_ob_typs: List[str] | NotGiven = NOT_GIVEN,
        agom_est: bool | NotGiven = NOT_GIVEN,
        agom_model: str | NotGiven = NOT_GIVEN,
        apriori_elset: orbitdetermination_create_params.AprioriElset | NotGiven = NOT_GIVEN,
        apriori_id_elset: str | NotGiven = NOT_GIVEN,
        apriori_id_state_vector: str | NotGiven = NOT_GIVEN,
        apriori_state_vector: orbitdetermination_create_params.AprioriStateVector | NotGiven = NOT_GIVEN,
        ballistic_coeff_est: bool | NotGiven = NOT_GIVEN,
        ballistic_coeff_model: str | NotGiven = NOT_GIVEN,
        best_pass_wrms: float | NotGiven = NOT_GIVEN,
        edr: float | NotGiven = NOT_GIVEN,
        effective_from: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        error_growth_rate: float | NotGiven = NOT_GIVEN,
        first_pass_wrms: float | NotGiven = NOT_GIVEN,
        fit_span: float | NotGiven = NOT_GIVEN,
        last_ob_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_ob_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        method_source: str | NotGiven = NOT_GIVEN,
        num_iterations: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        previous_wrms: float | NotGiven = NOT_GIVEN,
        rejected_ob_ids: List[str] | NotGiven = NOT_GIVEN,
        rejected_ob_typs: List[str] | NotGiven = NOT_GIVEN,
        rms_convergence_criteria: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sensor_ids: List[str] | NotGiven = NOT_GIVEN,
        time_span: float | NotGiven = NOT_GIVEN,
        wrms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OrbitDetermination record as a POST body and
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

          end_time: End time for OD solution in ISO 8601 UTC datetime format, with microsecond
              precision.

          initial_od: Flag indicating whether this is an initial orbit determination.

          method: Orbit determination method used to produce this record (e.g. BLS, KF, UKF,
              etc.).

          source: Source of the data.

          start_time: Start time for OD solution in ISO 8601 UTC datetime format, with microsecond
              precision.

          id: Unique identifier of the record, auto-generated by the system.

          accepted_ob_ids: Array of UDL data (observation) UUIDs that were accepted in this OD solution.
              See the associated acceptedObTyps array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          accepted_ob_typs: Array of UDL observation types (e.g. DOA, EO, RADAR, RF) of the observations
              that were accepted in this OD solution. See the associated acceptedObIds array
              for the records UUID(s), positionally corresponding to the record types in this
              array. The acceptedObTyps and acceptedObIds arrays must match in size.

          agom_est: Flag indicating whether the AGOM was estimated during this OD solution.

          agom_model: Model used to estimate the AGOM.

          apriori_elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          apriori_id_elset: Identifier of the element set used to seed this OD solution. This ID can be used
              to obtain additional information on an Elset object using the 'get by ID'
              operation (e.g. /udl/elset/{id}). For example, the Elset with idElset = abc
              would be queried as /udl/elset/abc.

          apriori_id_state_vector: Identifier of the state vector used to seed this OD solution. This ID can be
              used to obtain additional information on a StateVector object using the 'get by
              ID' operation (e.g. /udl/statevector/{id}). For example, the StateVector with
              idStateVector = abc would be queried as /udl/statevector/abc.

          apriori_state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          ballistic_coeff_est: Flag indicating whether the ballistic coefficient was estimated during this OD
              solution.

          ballistic_coeff_model: Model used to estimate the ballistic coefficient.

          best_pass_wrms: Lowest Weighted Root Mean Squared (RMS) value achieved for any single satellite
              pass during the observation span, indicating the pass with the highest quality
              OD solution.

          edr: Model parameter value for energy dissipation rate (EDR) in watts per kilogram.

          effective_from: Optional start time at which this OD solution is accurate, in ISO 8601 UTC
              datetime format with microsecond precision.

          effective_until: Optional end time at which this OD solution may no longer be accurate, in ISO
              8601 UTC datetime format with microsecond precision.

          error_growth_rate: Error growth rate of the OD solution in kilometers per day.

          first_pass_wrms: The Weighted Root Mean Squared (RMS) calculated for the first satellite pass in
              the observation span. Serves as the initial quality metric for the beginning of
              the observation period.

          fit_span: The fit span, in days, used in a Batch Least Squares (BLS) OD.

          last_ob_end: The end of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC datetime format with microsecond precision. For an
              exact observation time, the lastObStart and lastObEnd are the same.

          last_ob_start: The start of the time interval containing the time of the last accepted
              observation, in ISO 8601 UTC datetime format with microsecond precision. For an
              exact observation time, the lastObStart and lastObEnd are the same.

          method_source: Source of orbit determination method used to produce this record (e.g. ASW,
              ACTRAC, FreeFlyer, GEODYNE, GDTS, etc.).

          num_iterations: The number of iterations taken for the algorithm to converge on an OD solution.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the OD source to indicate the target on-orbit
              object of this OD solution. This may be an internal identifier and not
              necessarily map to a valid satellite number.

          previous_wrms: The Weighted Root Mean Squared (RMS) of the differential correction from the
              previous overhead pass of the satellite. Provides a point of comparison for
              assessing changes in the quality of the OD solution between consecutive passes.

          rejected_ob_ids: Array of UDL data (observation) UUIDs that were rejected in this OD solution.
              See the associated rejectedObTyps array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          rejected_ob_typs: Array of UDL observation types (e.g. DOA, EO, RADAR, RF) of the observations
              that were rejected in this OD solution. See the associated rejectedObIds array
              for the records UUID(s), positionally corresponding to the record types in this
              array. The rejectedObTyps and rejectedObIds arrays must match in size.

          rms_convergence_criteria: OD parameter value for the Root Mean Square (RMS) convergence criteria to
              successfully close the OD solution.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          sensor_ids: Array of UDL UUIDs (idSensor) of the sensors that contributed observations in
              this OD solution.

          time_span: The time span used for the OD of the object, in days.

          wrms: The Weighted Root Mean Squared (RMS) of the differential correction of the
              target object that produced this OD state. WRMS is a quality indicator of the OD
              update, with a value of 1.00 being optimal. WRMS applies to batch least squares
              (BLS) processes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/orbitdetermination",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "initial_od": initial_od,
                    "method": method,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "accepted_ob_ids": accepted_ob_ids,
                    "accepted_ob_typs": accepted_ob_typs,
                    "agom_est": agom_est,
                    "agom_model": agom_model,
                    "apriori_elset": apriori_elset,
                    "apriori_id_elset": apriori_id_elset,
                    "apriori_id_state_vector": apriori_id_state_vector,
                    "apriori_state_vector": apriori_state_vector,
                    "ballistic_coeff_est": ballistic_coeff_est,
                    "ballistic_coeff_model": ballistic_coeff_model,
                    "best_pass_wrms": best_pass_wrms,
                    "edr": edr,
                    "effective_from": effective_from,
                    "effective_until": effective_until,
                    "error_growth_rate": error_growth_rate,
                    "first_pass_wrms": first_pass_wrms,
                    "fit_span": fit_span,
                    "last_ob_end": last_ob_end,
                    "last_ob_start": last_ob_start,
                    "method_source": method_source,
                    "num_iterations": num_iterations,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "previous_wrms": previous_wrms,
                    "rejected_ob_ids": rejected_ob_ids,
                    "rejected_ob_typs": rejected_ob_typs,
                    "rms_convergence_criteria": rms_convergence_criteria,
                    "sat_no": sat_no,
                    "sensor_ids": sensor_ids,
                    "time_span": time_span,
                    "wrms": wrms,
                },
                orbitdetermination_create_params.OrbitdeterminationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrbitdeterminationListResponse, AsyncOffsetPage[OrbitdeterminationListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/orbitdetermination",
            page=AsyncOffsetPage[OrbitdeterminationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    orbitdetermination_list_params.OrbitdeterminationListParams,
                ),
            ),
            model=OrbitdeterminationListResponse,
        )

    async def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/orbitdetermination/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    orbitdetermination_count_params.OrbitdeterminationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[orbitdetermination_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        OrbitDetermination records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into the UDL. Data
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
            "/udl/orbitdetermination/createBulk",
            body=await async_maybe_transform(body, Iterable[orbitdetermination_create_bulk_params.Body]),
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
    ) -> OrbitdeterminationGetResponse:
        """
        Service operation to get a single OrbitDetermination record by its unique ID
        passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/orbitdetermination/{id}",
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
                    orbitdetermination_get_params.OrbitdeterminationGetParams,
                ),
            ),
            cast_to=OrbitdeterminationGetResponse,
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
    ) -> OrbitdeterminationQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/orbitdetermination/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrbitdeterminationQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrbitdeterminationTupleResponse:
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

          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/orbitdetermination/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    orbitdetermination_tuple_params.OrbitdeterminationTupleParams,
                ),
            ),
            cast_to=OrbitdeterminationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[orbitdetermination_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple OrbitDetermination records as a POST body and
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
            "/filedrop/udl-orbitdetermination",
            body=await async_maybe_transform(body, Iterable[orbitdetermination_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrbitdeterminationResourceWithRawResponse:
    def __init__(self, orbitdetermination: OrbitdeterminationResource) -> None:
        self._orbitdetermination = orbitdetermination

        self.create = to_raw_response_wrapper(
            orbitdetermination.create,
        )
        self.list = to_raw_response_wrapper(
            orbitdetermination.list,
        )
        self.count = to_raw_response_wrapper(
            orbitdetermination.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            orbitdetermination.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            orbitdetermination.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            orbitdetermination.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            orbitdetermination.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            orbitdetermination.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._orbitdetermination.history)


class AsyncOrbitdeterminationResourceWithRawResponse:
    def __init__(self, orbitdetermination: AsyncOrbitdeterminationResource) -> None:
        self._orbitdetermination = orbitdetermination

        self.create = async_to_raw_response_wrapper(
            orbitdetermination.create,
        )
        self.list = async_to_raw_response_wrapper(
            orbitdetermination.list,
        )
        self.count = async_to_raw_response_wrapper(
            orbitdetermination.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            orbitdetermination.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            orbitdetermination.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            orbitdetermination.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            orbitdetermination.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            orbitdetermination.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._orbitdetermination.history)


class OrbitdeterminationResourceWithStreamingResponse:
    def __init__(self, orbitdetermination: OrbitdeterminationResource) -> None:
        self._orbitdetermination = orbitdetermination

        self.create = to_streamed_response_wrapper(
            orbitdetermination.create,
        )
        self.list = to_streamed_response_wrapper(
            orbitdetermination.list,
        )
        self.count = to_streamed_response_wrapper(
            orbitdetermination.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            orbitdetermination.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            orbitdetermination.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            orbitdetermination.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            orbitdetermination.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            orbitdetermination.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._orbitdetermination.history)


class AsyncOrbitdeterminationResourceWithStreamingResponse:
    def __init__(self, orbitdetermination: AsyncOrbitdeterminationResource) -> None:
        self._orbitdetermination = orbitdetermination

        self.create = async_to_streamed_response_wrapper(
            orbitdetermination.create,
        )
        self.list = async_to_streamed_response_wrapper(
            orbitdetermination.list,
        )
        self.count = async_to_streamed_response_wrapper(
            orbitdetermination.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            orbitdetermination.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            orbitdetermination.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            orbitdetermination.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            orbitdetermination.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            orbitdetermination.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._orbitdetermination.history)
