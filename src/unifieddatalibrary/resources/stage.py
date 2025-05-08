# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    stage_get_params,
    stage_list_params,
    stage_count_params,
    stage_tuple_params,
    stage_create_params,
    stage_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.stage_get_response import StageGetResponse
from ..types.stage_list_response import StageListResponse
from ..types.stage_tuple_response import StageTupleResponse

__all__ = ["StageResource", "AsyncStageResource"]


class StageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return StageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return StageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_engine: str,
        id_launch_vehicle: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        avionics_notes: str | NotGiven = NOT_GIVEN,
        burn_time: float | NotGiven = NOT_GIVEN,
        control_thruster1: str | NotGiven = NOT_GIVEN,
        control_thruster2: str | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_burns: int | NotGiven = NOT_GIVEN,
        num_control_thruster1: int | NotGiven = NOT_GIVEN,
        num_control_thruster2: int | NotGiven = NOT_GIVEN,
        num_engines: int | NotGiven = NOT_GIVEN,
        num_stage_elements: int | NotGiven = NOT_GIVEN,
        num_vernier: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        photo_urls: List[str] | NotGiven = NOT_GIVEN,
        restartable: bool | NotGiven = NOT_GIVEN,
        reusable: bool | NotGiven = NOT_GIVEN,
        stage_number: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        thrust_sea_level: float | NotGiven = NOT_GIVEN,
        thrust_vacuum: float | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        vernier: str | NotGiven = NOT_GIVEN,
        vernier_burn_time: float | NotGiven = NOT_GIVEN,
        vernier_num_burns: int | NotGiven = NOT_GIVEN,
        vernier_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        vernier_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Stage as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance. A Stage represents various stages of a
        particular launch vehicle, compiled by a particular source. A vehicle may have
        multiple stage records.

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

          id_engine: Identifier of the Engine record for this stage.

          id_launch_vehicle: Identifier of the launch vehicle record for this stage.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          avionics_notes: Description/notes of the stage avionics.

          burn_time: Total burn time of the stage engines in seconds.

          control_thruster1: Control thruster 1 type.

          control_thruster2: Control thruster 2 type.

          diameter: Stage maximum external diameter in meters.

          length: Stage length in meters.

          main_engine_thrust_sea_level: Thrust of the stage main engine at sea level in kN.

          main_engine_thrust_vacuum: Thrust of the stage main engine in a vacuum in kN.

          manufacturer_org_id: ID of the organization that manufactures this launch stage.

          mass: Stage gross mass in kg.

          notes: Description/notes of the stage.

          num_burns: Number of burns for the stage engines.

          num_control_thruster1: Number of type control thruster 1.

          num_control_thruster2: Number of type control thruster 2.

          num_engines: The number of the specified engines on this launch stage.

          num_stage_elements: Number of launch stage elements used in this stage.

          num_vernier: Number of vernier or additional engines.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          photo_urls: Array of URLs of photos of the stage.

          restartable: Boolean indicating if this launch stage can be restarted.

          reusable: Boolean indicating if this launch stage is reusable.

          stage_number: The stage number of this launch stage.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          thrust_sea_level: Total thrust of the stage at sea level in kN.

          thrust_vacuum: Total thrust of the stage in a vacuum in kN.

          type: Engine cycle type (e.g. Electrostatic Ion, Pressure Fed, Hall, Catalytic
              Decomposition, etc.).

          vernier: Engine vernier or additional engine type.

          vernier_burn_time: Total burn time of the vernier or additional stage engines in seconds.

          vernier_num_burns: Total number of burns of the vernier or additional stage engines.

          vernier_thrust_sea_level: Total thrust of one of the vernier or additional engines at sea level in kN.

          vernier_thrust_vacuum: Total thrust of one of the vernier or additional engines in a vacuum in kN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/stage",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "id": id,
                    "avionics_notes": avionics_notes,
                    "burn_time": burn_time,
                    "control_thruster1": control_thruster1,
                    "control_thruster2": control_thruster2,
                    "diameter": diameter,
                    "length": length,
                    "main_engine_thrust_sea_level": main_engine_thrust_sea_level,
                    "main_engine_thrust_vacuum": main_engine_thrust_vacuum,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass": mass,
                    "notes": notes,
                    "num_burns": num_burns,
                    "num_control_thruster1": num_control_thruster1,
                    "num_control_thruster2": num_control_thruster2,
                    "num_engines": num_engines,
                    "num_stage_elements": num_stage_elements,
                    "num_vernier": num_vernier,
                    "origin": origin,
                    "photo_urls": photo_urls,
                    "restartable": restartable,
                    "reusable": reusable,
                    "stage_number": stage_number,
                    "tags": tags,
                    "thrust_sea_level": thrust_sea_level,
                    "thrust_vacuum": thrust_vacuum,
                    "type": type,
                    "vernier": vernier,
                    "vernier_burn_time": vernier_burn_time,
                    "vernier_num_burns": vernier_num_burns,
                    "vernier_thrust_sea_level": vernier_thrust_sea_level,
                    "vernier_thrust_vacuum": vernier_thrust_vacuum,
                },
                stage_create_params.StageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_engine: str,
        id_launch_vehicle: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        avionics_notes: str | NotGiven = NOT_GIVEN,
        burn_time: float | NotGiven = NOT_GIVEN,
        control_thruster1: str | NotGiven = NOT_GIVEN,
        control_thruster2: str | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_burns: int | NotGiven = NOT_GIVEN,
        num_control_thruster1: int | NotGiven = NOT_GIVEN,
        num_control_thruster2: int | NotGiven = NOT_GIVEN,
        num_engines: int | NotGiven = NOT_GIVEN,
        num_stage_elements: int | NotGiven = NOT_GIVEN,
        num_vernier: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        photo_urls: List[str] | NotGiven = NOT_GIVEN,
        restartable: bool | NotGiven = NOT_GIVEN,
        reusable: bool | NotGiven = NOT_GIVEN,
        stage_number: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        thrust_sea_level: float | NotGiven = NOT_GIVEN,
        thrust_vacuum: float | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        vernier: str | NotGiven = NOT_GIVEN,
        vernier_burn_time: float | NotGiven = NOT_GIVEN,
        vernier_num_burns: int | NotGiven = NOT_GIVEN,
        vernier_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        vernier_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Stage.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance. A
        Stage represents various stages of a particular launch vehicle, compiled by a
        particular source. A vehicle may have multiple stage records.

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

          id_engine: Identifier of the Engine record for this stage.

          id_launch_vehicle: Identifier of the launch vehicle record for this stage.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          avionics_notes: Description/notes of the stage avionics.

          burn_time: Total burn time of the stage engines in seconds.

          control_thruster1: Control thruster 1 type.

          control_thruster2: Control thruster 2 type.

          diameter: Stage maximum external diameter in meters.

          length: Stage length in meters.

          main_engine_thrust_sea_level: Thrust of the stage main engine at sea level in kN.

          main_engine_thrust_vacuum: Thrust of the stage main engine in a vacuum in kN.

          manufacturer_org_id: ID of the organization that manufactures this launch stage.

          mass: Stage gross mass in kg.

          notes: Description/notes of the stage.

          num_burns: Number of burns for the stage engines.

          num_control_thruster1: Number of type control thruster 1.

          num_control_thruster2: Number of type control thruster 2.

          num_engines: The number of the specified engines on this launch stage.

          num_stage_elements: Number of launch stage elements used in this stage.

          num_vernier: Number of vernier or additional engines.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          photo_urls: Array of URLs of photos of the stage.

          restartable: Boolean indicating if this launch stage can be restarted.

          reusable: Boolean indicating if this launch stage is reusable.

          stage_number: The stage number of this launch stage.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          thrust_sea_level: Total thrust of the stage at sea level in kN.

          thrust_vacuum: Total thrust of the stage in a vacuum in kN.

          type: Engine cycle type (e.g. Electrostatic Ion, Pressure Fed, Hall, Catalytic
              Decomposition, etc.).

          vernier: Engine vernier or additional engine type.

          vernier_burn_time: Total burn time of the vernier or additional stage engines in seconds.

          vernier_num_burns: Total number of burns of the vernier or additional stage engines.

          vernier_thrust_sea_level: Total thrust of one of the vernier or additional engines at sea level in kN.

          vernier_thrust_vacuum: Total thrust of one of the vernier or additional engines in a vacuum in kN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/stage/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "body_id": body_id,
                    "avionics_notes": avionics_notes,
                    "burn_time": burn_time,
                    "control_thruster1": control_thruster1,
                    "control_thruster2": control_thruster2,
                    "diameter": diameter,
                    "length": length,
                    "main_engine_thrust_sea_level": main_engine_thrust_sea_level,
                    "main_engine_thrust_vacuum": main_engine_thrust_vacuum,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass": mass,
                    "notes": notes,
                    "num_burns": num_burns,
                    "num_control_thruster1": num_control_thruster1,
                    "num_control_thruster2": num_control_thruster2,
                    "num_engines": num_engines,
                    "num_stage_elements": num_stage_elements,
                    "num_vernier": num_vernier,
                    "origin": origin,
                    "photo_urls": photo_urls,
                    "restartable": restartable,
                    "reusable": reusable,
                    "stage_number": stage_number,
                    "tags": tags,
                    "thrust_sea_level": thrust_sea_level,
                    "thrust_vacuum": thrust_vacuum,
                    "type": type,
                    "vernier": vernier,
                    "vernier_burn_time": vernier_burn_time,
                    "vernier_num_burns": vernier_num_burns,
                    "vernier_thrust_sea_level": vernier_thrust_sea_level,
                    "vernier_thrust_vacuum": vernier_thrust_vacuum,
                },
                stage_update_params.StageUpdateParams,
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
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[StageListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/stage",
            page=SyncOffsetPage[StageListResponse],
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
                    stage_list_params.StageListParams,
                ),
            ),
            model=StageListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete a Stage object specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance. A Stage represents various stages of a
        particular launch vehicle, compiled by a particular source. A vehicle may have
        multiple stage records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/udl/stage/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/stage/count",
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
                    stage_count_params.StageCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> StageGetResponse:
        """
        Service operation to get a single Stage record by its unique ID passed as a path
        parameter. A Stage represents various stages of a particular launch vehicle,
        compiled by a particular source. A vehicle may have multiple stage records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/stage/{id}",
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
                    stage_get_params.StageGetParams,
                ),
            ),
            cast_to=StageGetResponse,
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
            "/udl/stage/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StageTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/stage/tuple",
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
                    },
                    stage_tuple_params.StageTupleParams,
                ),
            ),
            cast_to=StageTupleResponse,
        )


class AsyncStageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncStageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_engine: str,
        id_launch_vehicle: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        avionics_notes: str | NotGiven = NOT_GIVEN,
        burn_time: float | NotGiven = NOT_GIVEN,
        control_thruster1: str | NotGiven = NOT_GIVEN,
        control_thruster2: str | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_burns: int | NotGiven = NOT_GIVEN,
        num_control_thruster1: int | NotGiven = NOT_GIVEN,
        num_control_thruster2: int | NotGiven = NOT_GIVEN,
        num_engines: int | NotGiven = NOT_GIVEN,
        num_stage_elements: int | NotGiven = NOT_GIVEN,
        num_vernier: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        photo_urls: List[str] | NotGiven = NOT_GIVEN,
        restartable: bool | NotGiven = NOT_GIVEN,
        reusable: bool | NotGiven = NOT_GIVEN,
        stage_number: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        thrust_sea_level: float | NotGiven = NOT_GIVEN,
        thrust_vacuum: float | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        vernier: str | NotGiven = NOT_GIVEN,
        vernier_burn_time: float | NotGiven = NOT_GIVEN,
        vernier_num_burns: int | NotGiven = NOT_GIVEN,
        vernier_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        vernier_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Stage as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance. A Stage represents various stages of a
        particular launch vehicle, compiled by a particular source. A vehicle may have
        multiple stage records.

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

          id_engine: Identifier of the Engine record for this stage.

          id_launch_vehicle: Identifier of the launch vehicle record for this stage.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          avionics_notes: Description/notes of the stage avionics.

          burn_time: Total burn time of the stage engines in seconds.

          control_thruster1: Control thruster 1 type.

          control_thruster2: Control thruster 2 type.

          diameter: Stage maximum external diameter in meters.

          length: Stage length in meters.

          main_engine_thrust_sea_level: Thrust of the stage main engine at sea level in kN.

          main_engine_thrust_vacuum: Thrust of the stage main engine in a vacuum in kN.

          manufacturer_org_id: ID of the organization that manufactures this launch stage.

          mass: Stage gross mass in kg.

          notes: Description/notes of the stage.

          num_burns: Number of burns for the stage engines.

          num_control_thruster1: Number of type control thruster 1.

          num_control_thruster2: Number of type control thruster 2.

          num_engines: The number of the specified engines on this launch stage.

          num_stage_elements: Number of launch stage elements used in this stage.

          num_vernier: Number of vernier or additional engines.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          photo_urls: Array of URLs of photos of the stage.

          restartable: Boolean indicating if this launch stage can be restarted.

          reusable: Boolean indicating if this launch stage is reusable.

          stage_number: The stage number of this launch stage.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          thrust_sea_level: Total thrust of the stage at sea level in kN.

          thrust_vacuum: Total thrust of the stage in a vacuum in kN.

          type: Engine cycle type (e.g. Electrostatic Ion, Pressure Fed, Hall, Catalytic
              Decomposition, etc.).

          vernier: Engine vernier or additional engine type.

          vernier_burn_time: Total burn time of the vernier or additional stage engines in seconds.

          vernier_num_burns: Total number of burns of the vernier or additional stage engines.

          vernier_thrust_sea_level: Total thrust of one of the vernier or additional engines at sea level in kN.

          vernier_thrust_vacuum: Total thrust of one of the vernier or additional engines in a vacuum in kN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/stage",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "id": id,
                    "avionics_notes": avionics_notes,
                    "burn_time": burn_time,
                    "control_thruster1": control_thruster1,
                    "control_thruster2": control_thruster2,
                    "diameter": diameter,
                    "length": length,
                    "main_engine_thrust_sea_level": main_engine_thrust_sea_level,
                    "main_engine_thrust_vacuum": main_engine_thrust_vacuum,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass": mass,
                    "notes": notes,
                    "num_burns": num_burns,
                    "num_control_thruster1": num_control_thruster1,
                    "num_control_thruster2": num_control_thruster2,
                    "num_engines": num_engines,
                    "num_stage_elements": num_stage_elements,
                    "num_vernier": num_vernier,
                    "origin": origin,
                    "photo_urls": photo_urls,
                    "restartable": restartable,
                    "reusable": reusable,
                    "stage_number": stage_number,
                    "tags": tags,
                    "thrust_sea_level": thrust_sea_level,
                    "thrust_vacuum": thrust_vacuum,
                    "type": type,
                    "vernier": vernier,
                    "vernier_burn_time": vernier_burn_time,
                    "vernier_num_burns": vernier_num_burns,
                    "vernier_thrust_sea_level": vernier_thrust_sea_level,
                    "vernier_thrust_vacuum": vernier_thrust_vacuum,
                },
                stage_create_params.StageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_engine: str,
        id_launch_vehicle: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        avionics_notes: str | NotGiven = NOT_GIVEN,
        burn_time: float | NotGiven = NOT_GIVEN,
        control_thruster1: str | NotGiven = NOT_GIVEN,
        control_thruster2: str | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        main_engine_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_burns: int | NotGiven = NOT_GIVEN,
        num_control_thruster1: int | NotGiven = NOT_GIVEN,
        num_control_thruster2: int | NotGiven = NOT_GIVEN,
        num_engines: int | NotGiven = NOT_GIVEN,
        num_stage_elements: int | NotGiven = NOT_GIVEN,
        num_vernier: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        photo_urls: List[str] | NotGiven = NOT_GIVEN,
        restartable: bool | NotGiven = NOT_GIVEN,
        reusable: bool | NotGiven = NOT_GIVEN,
        stage_number: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        thrust_sea_level: float | NotGiven = NOT_GIVEN,
        thrust_vacuum: float | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        vernier: str | NotGiven = NOT_GIVEN,
        vernier_burn_time: float | NotGiven = NOT_GIVEN,
        vernier_num_burns: int | NotGiven = NOT_GIVEN,
        vernier_thrust_sea_level: float | NotGiven = NOT_GIVEN,
        vernier_thrust_vacuum: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Stage.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance. A
        Stage represents various stages of a particular launch vehicle, compiled by a
        particular source. A vehicle may have multiple stage records.

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

          id_engine: Identifier of the Engine record for this stage.

          id_launch_vehicle: Identifier of the launch vehicle record for this stage.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          avionics_notes: Description/notes of the stage avionics.

          burn_time: Total burn time of the stage engines in seconds.

          control_thruster1: Control thruster 1 type.

          control_thruster2: Control thruster 2 type.

          diameter: Stage maximum external diameter in meters.

          length: Stage length in meters.

          main_engine_thrust_sea_level: Thrust of the stage main engine at sea level in kN.

          main_engine_thrust_vacuum: Thrust of the stage main engine in a vacuum in kN.

          manufacturer_org_id: ID of the organization that manufactures this launch stage.

          mass: Stage gross mass in kg.

          notes: Description/notes of the stage.

          num_burns: Number of burns for the stage engines.

          num_control_thruster1: Number of type control thruster 1.

          num_control_thruster2: Number of type control thruster 2.

          num_engines: The number of the specified engines on this launch stage.

          num_stage_elements: Number of launch stage elements used in this stage.

          num_vernier: Number of vernier or additional engines.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          photo_urls: Array of URLs of photos of the stage.

          restartable: Boolean indicating if this launch stage can be restarted.

          reusable: Boolean indicating if this launch stage is reusable.

          stage_number: The stage number of this launch stage.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          thrust_sea_level: Total thrust of the stage at sea level in kN.

          thrust_vacuum: Total thrust of the stage in a vacuum in kN.

          type: Engine cycle type (e.g. Electrostatic Ion, Pressure Fed, Hall, Catalytic
              Decomposition, etc.).

          vernier: Engine vernier or additional engine type.

          vernier_burn_time: Total burn time of the vernier or additional stage engines in seconds.

          vernier_num_burns: Total number of burns of the vernier or additional stage engines.

          vernier_thrust_sea_level: Total thrust of one of the vernier or additional engines at sea level in kN.

          vernier_thrust_vacuum: Total thrust of one of the vernier or additional engines in a vacuum in kN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/stage/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "body_id": body_id,
                    "avionics_notes": avionics_notes,
                    "burn_time": burn_time,
                    "control_thruster1": control_thruster1,
                    "control_thruster2": control_thruster2,
                    "diameter": diameter,
                    "length": length,
                    "main_engine_thrust_sea_level": main_engine_thrust_sea_level,
                    "main_engine_thrust_vacuum": main_engine_thrust_vacuum,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass": mass,
                    "notes": notes,
                    "num_burns": num_burns,
                    "num_control_thruster1": num_control_thruster1,
                    "num_control_thruster2": num_control_thruster2,
                    "num_engines": num_engines,
                    "num_stage_elements": num_stage_elements,
                    "num_vernier": num_vernier,
                    "origin": origin,
                    "photo_urls": photo_urls,
                    "restartable": restartable,
                    "reusable": reusable,
                    "stage_number": stage_number,
                    "tags": tags,
                    "thrust_sea_level": thrust_sea_level,
                    "thrust_vacuum": thrust_vacuum,
                    "type": type,
                    "vernier": vernier,
                    "vernier_burn_time": vernier_burn_time,
                    "vernier_num_burns": vernier_num_burns,
                    "vernier_thrust_sea_level": vernier_thrust_sea_level,
                    "vernier_thrust_vacuum": vernier_thrust_vacuum,
                },
                stage_update_params.StageUpdateParams,
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
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[StageListResponse, AsyncOffsetPage[StageListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/stage",
            page=AsyncOffsetPage[StageListResponse],
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
                    stage_list_params.StageListParams,
                ),
            ),
            model=StageListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete a Stage object specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance. A Stage represents various stages of a
        particular launch vehicle, compiled by a particular source. A vehicle may have
        multiple stage records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/udl/stage/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/stage/count",
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
                    stage_count_params.StageCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> StageGetResponse:
        """
        Service operation to get a single Stage record by its unique ID passed as a path
        parameter. A Stage represents various stages of a particular launch vehicle,
        compiled by a particular source. A vehicle may have multiple stage records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/stage/{id}",
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
                    stage_get_params.StageGetParams,
                ),
            ),
            cast_to=StageGetResponse,
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
            "/udl/stage/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StageTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/stage/tuple",
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
                    },
                    stage_tuple_params.StageTupleParams,
                ),
            ),
            cast_to=StageTupleResponse,
        )


class StageResourceWithRawResponse:
    def __init__(self, stage: StageResource) -> None:
        self._stage = stage

        self.create = to_raw_response_wrapper(
            stage.create,
        )
        self.update = to_raw_response_wrapper(
            stage.update,
        )
        self.list = to_raw_response_wrapper(
            stage.list,
        )
        self.delete = to_raw_response_wrapper(
            stage.delete,
        )
        self.count = to_raw_response_wrapper(
            stage.count,
        )
        self.get = to_raw_response_wrapper(
            stage.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            stage.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            stage.tuple,
        )


class AsyncStageResourceWithRawResponse:
    def __init__(self, stage: AsyncStageResource) -> None:
        self._stage = stage

        self.create = async_to_raw_response_wrapper(
            stage.create,
        )
        self.update = async_to_raw_response_wrapper(
            stage.update,
        )
        self.list = async_to_raw_response_wrapper(
            stage.list,
        )
        self.delete = async_to_raw_response_wrapper(
            stage.delete,
        )
        self.count = async_to_raw_response_wrapper(
            stage.count,
        )
        self.get = async_to_raw_response_wrapper(
            stage.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            stage.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            stage.tuple,
        )


class StageResourceWithStreamingResponse:
    def __init__(self, stage: StageResource) -> None:
        self._stage = stage

        self.create = to_streamed_response_wrapper(
            stage.create,
        )
        self.update = to_streamed_response_wrapper(
            stage.update,
        )
        self.list = to_streamed_response_wrapper(
            stage.list,
        )
        self.delete = to_streamed_response_wrapper(
            stage.delete,
        )
        self.count = to_streamed_response_wrapper(
            stage.count,
        )
        self.get = to_streamed_response_wrapper(
            stage.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            stage.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            stage.tuple,
        )


class AsyncStageResourceWithStreamingResponse:
    def __init__(self, stage: AsyncStageResource) -> None:
        self._stage = stage

        self.create = async_to_streamed_response_wrapper(
            stage.create,
        )
        self.update = async_to_streamed_response_wrapper(
            stage.update,
        )
        self.list = async_to_streamed_response_wrapper(
            stage.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            stage.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            stage.count,
        )
        self.get = async_to_streamed_response_wrapper(
            stage.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            stage.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            stage.tuple,
        )
