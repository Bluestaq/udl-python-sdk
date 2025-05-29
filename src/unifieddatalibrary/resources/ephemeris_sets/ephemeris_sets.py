# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    ephemeris_set_list_params,
    ephemeris_set_count_params,
    ephemeris_set_tuple_params,
    ephemeris_set_create_params,
    ephemeris_set_retrieve_params,
    ephemeris_set_file_retrieve_params,
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
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ephemeris_set import EphemerisSet
from ...types.ephemeris_set_abridged import EphemerisSetAbridged
from ...types.ephemeris_set_tuple_response import EphemerisSetTupleResponse
from ...types.ephemeris_set_queryhelp_response import EphemerisSetQueryhelpResponse

__all__ = ["EphemerisSetsResource", "AsyncEphemerisSetsResource"]


class EphemerisSetsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EphemerisSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EphemerisSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EphemerisSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EphemerisSetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        num_points: int,
        point_end_time: Union[str, datetime],
        point_start_time: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        b_dot: float | NotGiven = NOT_GIVEN,
        cent_body: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        cov_reference_frame: Literal["J2000", "UVW", "EFG/TDR", "TEME", "GCRF"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        drag_model: str | NotGiven = NOT_GIVEN,
        edr: float | NotGiven = NOT_GIVEN,
        ephemeris_list: Iterable[ephemeris_set_create_params.EphemerisList] | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        geopotential_model: str | NotGiven = NOT_GIVEN,
        has_accel: bool | NotGiven = NOT_GIVEN,
        has_cov: bool | NotGiven = NOT_GIVEN,
        has_mnvr: bool | NotGiven = NOT_GIVEN,
        id_maneuvers: List[str] | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        id_state_vector: str | NotGiven = NOT_GIVEN,
        integrator: str | NotGiven = NOT_GIVEN,
        interpolation: str | NotGiven = NOT_GIVEN,
        interpolation_degree: int | NotGiven = NOT_GIVEN,
        lunar_solar: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        pedigree: str | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        solid_earth_tides: bool | NotGiven = NOT_GIVEN,
        step_size: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        usable_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        usable_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation intended for initial integration only.

        Takes a single
        EphemerisSet as a POST body and ingest into the database. This operation does
        not persist any Ephemeris Points that may be present in the body of the request.
        This operation is not intended to be used for automated feeds into UDL.A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        The following rules apply to this operation:

        <h3>
         * Ephemeris Set numPoints value must correspond exactly to the number of Ephemeris states associated with that Ephemeris Set.  The numPoints value is checked against the actual posted number of states and mismatch will result in the post being rejected.
         * Ephemeris Set pointStartTime and pointEndTime must correspond to the earliest and latest state times, respectively, of the associated Ephemeris states.
         * Either satNo, idOnOrbit, or origObjectId must be provided.  The preferred option is to post with satNo for a cataloged object, and with (only) origObjectId for an unknown, uncatalogued, or internal/test object.  There are several cases for the logic associated with these fields:
           + If satNo is provided and correlates to a known UDL sat number then the idOnOrbit will be populated appropriately in addition to the satNo.
           + If satNo is provided and does not correlate to a known UDL sat number then the provided satNo value will be moved to the origObjectId field and satNo left null.
           + If origObjectId and a valid satNo or idOnOrbit are provided then both the satNo/idOnOrbit and origObjectId will maintain the provided values.
           + If only origObjectId is provided then origObjectId will be populated with the posted value.  In this case, no checks are made against existing UDL sat numbers.
        </h3>

        Args:
          category: The source category of the ephemeris (e.g. OWNER_OPERATOR, ANALYST, EXTERNAL).

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

          num_points: Number of points contained in the ephemeris.

          point_end_time: End time/last time point of the ephemeris, in ISO 8601 UTC format.

          point_start_time: Start time/first time point of the ephemeris, in ISO 8601 UTC format.

          source: Source of the data.

          type: The type/purpose of the ephemeris (e.g., CALIBRATION, LAUNCH, MNVR_PLAN,
              ROUTINE, SCREENING).

          id: Unique identifier of the record, auto-generated by the system.

          b_dot: First derivative of ballistic coefficient (m^2/kg-s).

          cent_body: The Central Body of the ephemeris. Assumed to be Earth, unless otherwise
              indicated.

          comments: Additional source provided comments associated with the ephemeris.

          cov_reference_frame: The reference frame of the covariance matrix elements. If the covReferenceFrame
              is null it is assumed to be J2000.

          description: Notes/description of the provided ephemeris. A value of DSTOP signifies the
              ephemeris were generated using the last observation available.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          drag_model: Drag model used in ephemeris generation (e.g. JAC70, MSIS90, NONE, etc.).

          edr: Model parameter value for energy dissipation rate (EDR), expressed in w/kg.

          ephemeris_list: The list of ephemeris states belonging to the EphemerisSet. Each ephemeris point
              is associated with a parent Ephemeris Set via the EphemerisSet ID (esId).

          filename: Filename of the raw file used to provide the ephemeris data including filetype
              extension, if applicable. This file may be retrieved using the 'getFile'
              operation as specified in the 'EphemerisSet' OpenAPI docs.

          geopotential_model: Geopotential model used in ephemeris generation (e.g. EGM-96, WGS-84, WGS-72,
              JGM-2, GEM-T3), including mm degree zonals, nn degree/order tesserals (e.g.
              EGM-96 24Z,24T).

          has_accel: Boolean indicating whether acceleration data is provided with the ephemeris.

          has_cov: Boolean indicating whether covariance data is provided with the ephemeris.

          has_mnvr: Boolean indicating whether maneuver(s) are incorporated into the ephemeris.

          id_maneuvers: Array of the maneuver IDs of all maneuvers incorporated in the ephemeris.

          id_on_orbit: Unique identifier of the primary satellite on-orbit object.

          id_state_vector: ID of the State Vector used to generate the ephemeris.

          integrator: Integrator used in ephemeris generation (e.g. RK7(8), RK8(9), COWELL, TWO-BODY).

          interpolation: The recommended interpolation method for the ephemeris data.

          interpolation_degree: The recommended interpolation degree for the ephemeris data.

          lunar_solar: Boolean indicating use of lunar/solar data in ephemeris generation.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by ephemeris source to indicate the target object
              of this ephemeris. This may be an internal identifier and not necessarily map to
              a valid satellite number.

          pedigree: The pedigree of the ephemeris or source data used for ephemeris generation (e.g.
              DOPPLER, GPS, HYBRID, PROPAGATED, RANGING, SLR).

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          sat_no: Satellite/catalog number of the target on-orbit object.

          solid_earth_tides: Boolean indicating use of solid earth tide data in ephemeris generation.

          step_size: Ephemeris step size, in seconds.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          usable_end_time: Optional end time of the usable time span for the ephemeris data, in ISO 8601
              UTC format with microsecond precision.

          usable_start_time: Optional start time of the usable time span for the ephemeris data, in ISO 8601
              UTC format with microsecond precision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/ephemerisset",
            body=maybe_transform(
                {
                    "category": category,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "num_points": num_points,
                    "point_end_time": point_end_time,
                    "point_start_time": point_start_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "b_dot": b_dot,
                    "cent_body": cent_body,
                    "comments": comments,
                    "cov_reference_frame": cov_reference_frame,
                    "description": description,
                    "descriptor": descriptor,
                    "drag_model": drag_model,
                    "edr": edr,
                    "ephemeris_list": ephemeris_list,
                    "filename": filename,
                    "geopotential_model": geopotential_model,
                    "has_accel": has_accel,
                    "has_cov": has_cov,
                    "has_mnvr": has_mnvr,
                    "id_maneuvers": id_maneuvers,
                    "id_on_orbit": id_on_orbit,
                    "id_state_vector": id_state_vector,
                    "integrator": integrator,
                    "interpolation": interpolation,
                    "interpolation_degree": interpolation_degree,
                    "lunar_solar": lunar_solar,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "pedigree": pedigree,
                    "reference_frame": reference_frame,
                    "sat_no": sat_no,
                    "solid_earth_tides": solid_earth_tides,
                    "step_size": step_size,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "usable_end_time": usable_end_time,
                    "usable_start_time": usable_start_time,
                },
                ephemeris_set_create_params.EphemerisSetCreateParams,
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
    ) -> EphemerisSet:
        """
        Service operation to get a single Ephemeris Set by its unique ID passed as a
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
            f"/udl/ephemerisset/{id}",
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
                    ephemeris_set_retrieve_params.EphemerisSetRetrieveParams,
                ),
            ),
            cast_to=EphemerisSet,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        point_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        point_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EphemerisSetAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          point_end_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) End
              time/last time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          point_start_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
              time/first time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ephemerisset",
            page=SyncOffsetPage[EphemerisSetAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                        "point_end_time": point_end_time,
                        "point_start_time": point_start_time,
                    },
                    ephemeris_set_list_params.EphemerisSetListParams,
                ),
            ),
            model=EphemerisSetAbridged,
        )

    def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        point_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        point_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          point_end_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) End
              time/last time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          point_start_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
              time/first time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/ephemerisset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                        "point_end_time": point_end_time,
                        "point_start_time": point_start_time,
                    },
                    ephemeris_set_count_params.EphemerisSetCountParams,
                ),
            ),
            cast_to=str,
        )

    def file_retrieve(
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
    ) -> BinaryAPIResponse:
        """
        Service operation to get the original raw flat file, if any, associated with the
        EphemerisSet. The file is returned as an attachment Content-Disposition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/udl/ephemerisset/getFile/{id}",
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
                    ephemeris_set_file_retrieve_params.EphemerisSetFileRetrieveParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
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
    ) -> EphemerisSetQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/ephemerisset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EphemerisSetQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        point_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        point_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EphemerisSetTupleResponse:
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

          point_end_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) End
              time/last time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          point_start_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
              time/first time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/ephemerisset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "point_end_time": point_end_time,
                        "point_start_time": point_start_time,
                    },
                    ephemeris_set_tuple_params.EphemerisSetTupleParams,
                ),
            ),
            cast_to=EphemerisSetTupleResponse,
        )


class AsyncEphemerisSetsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEphemerisSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEphemerisSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEphemerisSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEphemerisSetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        num_points: int,
        point_end_time: Union[str, datetime],
        point_start_time: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        b_dot: float | NotGiven = NOT_GIVEN,
        cent_body: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        cov_reference_frame: Literal["J2000", "UVW", "EFG/TDR", "TEME", "GCRF"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        drag_model: str | NotGiven = NOT_GIVEN,
        edr: float | NotGiven = NOT_GIVEN,
        ephemeris_list: Iterable[ephemeris_set_create_params.EphemerisList] | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        geopotential_model: str | NotGiven = NOT_GIVEN,
        has_accel: bool | NotGiven = NOT_GIVEN,
        has_cov: bool | NotGiven = NOT_GIVEN,
        has_mnvr: bool | NotGiven = NOT_GIVEN,
        id_maneuvers: List[str] | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        id_state_vector: str | NotGiven = NOT_GIVEN,
        integrator: str | NotGiven = NOT_GIVEN,
        interpolation: str | NotGiven = NOT_GIVEN,
        interpolation_degree: int | NotGiven = NOT_GIVEN,
        lunar_solar: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        pedigree: str | NotGiven = NOT_GIVEN,
        reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        solid_earth_tides: bool | NotGiven = NOT_GIVEN,
        step_size: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        usable_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        usable_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation intended for initial integration only.

        Takes a single
        EphemerisSet as a POST body and ingest into the database. This operation does
        not persist any Ephemeris Points that may be present in the body of the request.
        This operation is not intended to be used for automated feeds into UDL.A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        The following rules apply to this operation:

        <h3>
         * Ephemeris Set numPoints value must correspond exactly to the number of Ephemeris states associated with that Ephemeris Set.  The numPoints value is checked against the actual posted number of states and mismatch will result in the post being rejected.
         * Ephemeris Set pointStartTime and pointEndTime must correspond to the earliest and latest state times, respectively, of the associated Ephemeris states.
         * Either satNo, idOnOrbit, or origObjectId must be provided.  The preferred option is to post with satNo for a cataloged object, and with (only) origObjectId for an unknown, uncatalogued, or internal/test object.  There are several cases for the logic associated with these fields:
           + If satNo is provided and correlates to a known UDL sat number then the idOnOrbit will be populated appropriately in addition to the satNo.
           + If satNo is provided and does not correlate to a known UDL sat number then the provided satNo value will be moved to the origObjectId field and satNo left null.
           + If origObjectId and a valid satNo or idOnOrbit are provided then both the satNo/idOnOrbit and origObjectId will maintain the provided values.
           + If only origObjectId is provided then origObjectId will be populated with the posted value.  In this case, no checks are made against existing UDL sat numbers.
        </h3>

        Args:
          category: The source category of the ephemeris (e.g. OWNER_OPERATOR, ANALYST, EXTERNAL).

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

          num_points: Number of points contained in the ephemeris.

          point_end_time: End time/last time point of the ephemeris, in ISO 8601 UTC format.

          point_start_time: Start time/first time point of the ephemeris, in ISO 8601 UTC format.

          source: Source of the data.

          type: The type/purpose of the ephemeris (e.g., CALIBRATION, LAUNCH, MNVR_PLAN,
              ROUTINE, SCREENING).

          id: Unique identifier of the record, auto-generated by the system.

          b_dot: First derivative of ballistic coefficient (m^2/kg-s).

          cent_body: The Central Body of the ephemeris. Assumed to be Earth, unless otherwise
              indicated.

          comments: Additional source provided comments associated with the ephemeris.

          cov_reference_frame: The reference frame of the covariance matrix elements. If the covReferenceFrame
              is null it is assumed to be J2000.

          description: Notes/description of the provided ephemeris. A value of DSTOP signifies the
              ephemeris were generated using the last observation available.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          drag_model: Drag model used in ephemeris generation (e.g. JAC70, MSIS90, NONE, etc.).

          edr: Model parameter value for energy dissipation rate (EDR), expressed in w/kg.

          ephemeris_list: The list of ephemeris states belonging to the EphemerisSet. Each ephemeris point
              is associated with a parent Ephemeris Set via the EphemerisSet ID (esId).

          filename: Filename of the raw file used to provide the ephemeris data including filetype
              extension, if applicable. This file may be retrieved using the 'getFile'
              operation as specified in the 'EphemerisSet' OpenAPI docs.

          geopotential_model: Geopotential model used in ephemeris generation (e.g. EGM-96, WGS-84, WGS-72,
              JGM-2, GEM-T3), including mm degree zonals, nn degree/order tesserals (e.g.
              EGM-96 24Z,24T).

          has_accel: Boolean indicating whether acceleration data is provided with the ephemeris.

          has_cov: Boolean indicating whether covariance data is provided with the ephemeris.

          has_mnvr: Boolean indicating whether maneuver(s) are incorporated into the ephemeris.

          id_maneuvers: Array of the maneuver IDs of all maneuvers incorporated in the ephemeris.

          id_on_orbit: Unique identifier of the primary satellite on-orbit object.

          id_state_vector: ID of the State Vector used to generate the ephemeris.

          integrator: Integrator used in ephemeris generation (e.g. RK7(8), RK8(9), COWELL, TWO-BODY).

          interpolation: The recommended interpolation method for the ephemeris data.

          interpolation_degree: The recommended interpolation degree for the ephemeris data.

          lunar_solar: Boolean indicating use of lunar/solar data in ephemeris generation.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by ephemeris source to indicate the target object
              of this ephemeris. This may be an internal identifier and not necessarily map to
              a valid satellite number.

          pedigree: The pedigree of the ephemeris or source data used for ephemeris generation (e.g.
              DOPPLER, GPS, HYBRID, PROPAGATED, RANGING, SLR).

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          sat_no: Satellite/catalog number of the target on-orbit object.

          solid_earth_tides: Boolean indicating use of solid earth tide data in ephemeris generation.

          step_size: Ephemeris step size, in seconds.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          usable_end_time: Optional end time of the usable time span for the ephemeris data, in ISO 8601
              UTC format with microsecond precision.

          usable_start_time: Optional start time of the usable time span for the ephemeris data, in ISO 8601
              UTC format with microsecond precision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/ephemerisset",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "num_points": num_points,
                    "point_end_time": point_end_time,
                    "point_start_time": point_start_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "b_dot": b_dot,
                    "cent_body": cent_body,
                    "comments": comments,
                    "cov_reference_frame": cov_reference_frame,
                    "description": description,
                    "descriptor": descriptor,
                    "drag_model": drag_model,
                    "edr": edr,
                    "ephemeris_list": ephemeris_list,
                    "filename": filename,
                    "geopotential_model": geopotential_model,
                    "has_accel": has_accel,
                    "has_cov": has_cov,
                    "has_mnvr": has_mnvr,
                    "id_maneuvers": id_maneuvers,
                    "id_on_orbit": id_on_orbit,
                    "id_state_vector": id_state_vector,
                    "integrator": integrator,
                    "interpolation": interpolation,
                    "interpolation_degree": interpolation_degree,
                    "lunar_solar": lunar_solar,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "pedigree": pedigree,
                    "reference_frame": reference_frame,
                    "sat_no": sat_no,
                    "solid_earth_tides": solid_earth_tides,
                    "step_size": step_size,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "usable_end_time": usable_end_time,
                    "usable_start_time": usable_start_time,
                },
                ephemeris_set_create_params.EphemerisSetCreateParams,
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
    ) -> EphemerisSet:
        """
        Service operation to get a single Ephemeris Set by its unique ID passed as a
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
            f"/udl/ephemerisset/{id}",
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
                    ephemeris_set_retrieve_params.EphemerisSetRetrieveParams,
                ),
            ),
            cast_to=EphemerisSet,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        point_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        point_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EphemerisSetAbridged, AsyncOffsetPage[EphemerisSetAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          point_end_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) End
              time/last time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          point_start_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
              time/first time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ephemerisset",
            page=AsyncOffsetPage[EphemerisSetAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                        "point_end_time": point_end_time,
                        "point_start_time": point_start_time,
                    },
                    ephemeris_set_list_params.EphemerisSetListParams,
                ),
            ),
            model=EphemerisSetAbridged,
        )

    async def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        point_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        point_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          point_end_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) End
              time/last time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          point_start_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
              time/first time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/ephemerisset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                        "point_end_time": point_end_time,
                        "point_start_time": point_start_time,
                    },
                    ephemeris_set_count_params.EphemerisSetCountParams,
                ),
            ),
            cast_to=str,
        )

    async def file_retrieve(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Service operation to get the original raw flat file, if any, associated with the
        EphemerisSet. The file is returned as an attachment Content-Disposition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/udl/ephemerisset/getFile/{id}",
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
                    ephemeris_set_file_retrieve_params.EphemerisSetFileRetrieveParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
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
    ) -> EphemerisSetQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/ephemerisset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EphemerisSetQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        point_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        point_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EphemerisSetTupleResponse:
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

          point_end_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) End
              time/last time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          point_start_time: (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
              time/first time point of the ephemeris, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/ephemerisset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "point_end_time": point_end_time,
                        "point_start_time": point_start_time,
                    },
                    ephemeris_set_tuple_params.EphemerisSetTupleParams,
                ),
            ),
            cast_to=EphemerisSetTupleResponse,
        )


class EphemerisSetsResourceWithRawResponse:
    def __init__(self, ephemeris_sets: EphemerisSetsResource) -> None:
        self._ephemeris_sets = ephemeris_sets

        self.create = to_raw_response_wrapper(
            ephemeris_sets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ephemeris_sets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ephemeris_sets.list,
        )
        self.count = to_raw_response_wrapper(
            ephemeris_sets.count,
        )
        self.file_retrieve = to_custom_raw_response_wrapper(
            ephemeris_sets.file_retrieve,
            BinaryAPIResponse,
        )
        self.queryhelp = to_raw_response_wrapper(
            ephemeris_sets.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            ephemeris_sets.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._ephemeris_sets.history)


class AsyncEphemerisSetsResourceWithRawResponse:
    def __init__(self, ephemeris_sets: AsyncEphemerisSetsResource) -> None:
        self._ephemeris_sets = ephemeris_sets

        self.create = async_to_raw_response_wrapper(
            ephemeris_sets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ephemeris_sets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ephemeris_sets.list,
        )
        self.count = async_to_raw_response_wrapper(
            ephemeris_sets.count,
        )
        self.file_retrieve = async_to_custom_raw_response_wrapper(
            ephemeris_sets.file_retrieve,
            AsyncBinaryAPIResponse,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            ephemeris_sets.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            ephemeris_sets.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._ephemeris_sets.history)


class EphemerisSetsResourceWithStreamingResponse:
    def __init__(self, ephemeris_sets: EphemerisSetsResource) -> None:
        self._ephemeris_sets = ephemeris_sets

        self.create = to_streamed_response_wrapper(
            ephemeris_sets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ephemeris_sets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ephemeris_sets.list,
        )
        self.count = to_streamed_response_wrapper(
            ephemeris_sets.count,
        )
        self.file_retrieve = to_custom_streamed_response_wrapper(
            ephemeris_sets.file_retrieve,
            StreamedBinaryAPIResponse,
        )
        self.queryhelp = to_streamed_response_wrapper(
            ephemeris_sets.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            ephemeris_sets.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._ephemeris_sets.history)


class AsyncEphemerisSetsResourceWithStreamingResponse:
    def __init__(self, ephemeris_sets: AsyncEphemerisSetsResource) -> None:
        self._ephemeris_sets = ephemeris_sets

        self.create = async_to_streamed_response_wrapper(
            ephemeris_sets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ephemeris_sets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ephemeris_sets.list,
        )
        self.count = async_to_streamed_response_wrapper(
            ephemeris_sets.count,
        )
        self.file_retrieve = async_to_custom_streamed_response_wrapper(
            ephemeris_sets.file_retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            ephemeris_sets.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            ephemeris_sets.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._ephemeris_sets.history)
