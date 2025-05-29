# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ...types import (
    effect_response_list_params,
    effect_response_count_params,
    effect_response_tuple_params,
    effect_response_create_params,
    effect_response_retrieve_params,
    effect_response_create_bulk_params,
    effect_response_unvalidated_publish_params,
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
from ...types.effect_response_list_response import EffectResponseListResponse
from ...types.effect_response_tuple_response import EffectResponseTupleResponse
from ...types.effect_response_retrieve_response import EffectResponseRetrieveResponse
from ...types.effect_response_query_help_response import EffectResponseQueryHelpResponse

__all__ = ["EffectResponsesResource", "AsyncEffectResponsesResource"]


class EffectResponsesResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EffectResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EffectResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EffectResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EffectResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        actions_list: Iterable[effect_response_create_params.ActionsList] | NotGiven = NOT_GIVEN,
        actor_src_id: str | NotGiven = NOT_GIVEN,
        actor_src_type: str | NotGiven = NOT_GIVEN,
        coa_metrics: Iterable[effect_response_create_params.CoaMetric] | NotGiven = NOT_GIVEN,
        collateral_damage_est: float | NotGiven = NOT_GIVEN,
        decision_deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_actions: List[str] | NotGiven = NOT_GIVEN,
        external_request_id: str | NotGiven = NOT_GIVEN,
        id_effect_request: str | NotGiven = NOT_GIVEN,
        munition_id: str | NotGiven = NOT_GIVEN,
        munition_type: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        probability_of_kill: float | NotGiven = NOT_GIVEN,
        red_target_src_id: str | NotGiven = NOT_GIVEN,
        red_target_src_type: str | NotGiven = NOT_GIVEN,
        red_time_to_overhead: Union[str, datetime] | NotGiven = NOT_GIVEN,
        shots_required: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EffectResponse as a POST body and ingest into
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

          source: Source of the data.

          type: The type of response in this record (e.g. COA, SCORECARD, etc.).

          id: Unique identifier of the record, auto-generated by the system.

          actions_list: List of actions associated with this effect response.

          actor_src_id: The record ID, depending on the type identified in actorSrcType, of the
              requested asset.

          actor_src_type: The source type of the asset/actor identifier (AIRCRAFT, LANDCRAFT, SEACRAFT,
              TRACK).

          coa_metrics: List of COA metrics associated with this effect response.

          collateral_damage_est: The collateral damage estimate (CDE) of the munition being fired.

          decision_deadline: The deadline time to accept this COA before it's no longer valid, in ISO8601 UTC
              format.

          external_actions: List of external actions to be executed as part of this task.

          external_request_id: The external system identifier of the associated effect request. A human
              readable unique id.

          id_effect_request: Unique identifier of the EffectRequest associated with this response.

          munition_id: Unique identifier of the munition.

          munition_type: The type of munition being fired.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          probability_of_kill: The probability of kill (0-1) of the target being destroyed.

          red_target_src_id: The record ID, depending on the type identified in redTargetSrcType, of the red
              force target. If the redTargetSrcType is POI or TRACK, then this identifier
              corresponds to either poi.poiid or track.trkId from their respective schemas.

          red_target_src_type: The source type of the targetId identifier (POI, SITE, TRACK).

          red_time_to_overhead: The time to overhead for the red force to be over their target, in ISO8601 UTC
              format.

          shots_required: The number of shots required to destroy target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/effectresponse",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "type": type,
                    "id": id,
                    "actions_list": actions_list,
                    "actor_src_id": actor_src_id,
                    "actor_src_type": actor_src_type,
                    "coa_metrics": coa_metrics,
                    "collateral_damage_est": collateral_damage_est,
                    "decision_deadline": decision_deadline,
                    "external_actions": external_actions,
                    "external_request_id": external_request_id,
                    "id_effect_request": id_effect_request,
                    "munition_id": munition_id,
                    "munition_type": munition_type,
                    "origin": origin,
                    "probability_of_kill": probability_of_kill,
                    "red_target_src_id": red_target_src_id,
                    "red_target_src_type": red_target_src_type,
                    "red_time_to_overhead": red_time_to_overhead,
                    "shots_required": shots_required,
                },
                effect_response_create_params.EffectResponseCreateParams,
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
    ) -> EffectResponseRetrieveResponse:
        """
        Service operation to get a single EffectResponse by its unique ID passed as a
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
            f"/udl/effectresponse/{id}",
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
                    effect_response_retrieve_params.EffectResponseRetrieveParams,
                ),
            ),
            cast_to=EffectResponseRetrieveResponse,
        )

    def list(
        self,
        *,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EffectResponseListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/effectresponse",
            page=SyncOffsetPage[EffectResponseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    effect_response_list_params.EffectResponseListParams,
                ),
            ),
            model=EffectResponseListResponse,
        )

    def count(
        self,
        *,
        created_at: Union[str, date],
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
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/effectresponse/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    effect_response_count_params.EffectResponseCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[effect_response_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        EffectResponse records as a POST body and ingest into the database. This
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
            "/udl/effectresponse/createBulk",
            body=maybe_transform(body, Iterable[effect_response_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> EffectResponseQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/effectresponse/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EffectResponseQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EffectResponseTupleResponse:
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

          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/effectresponse/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    effect_response_tuple_params.EffectResponseTupleParams,
                ),
            ),
            cast_to=EffectResponseTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[effect_response_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple EffectResponses as a POST body and ingest
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
            "/filedrop/udl-effectresponse",
            body=maybe_transform(body, Iterable[effect_response_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEffectResponsesResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEffectResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEffectResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEffectResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEffectResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        actions_list: Iterable[effect_response_create_params.ActionsList] | NotGiven = NOT_GIVEN,
        actor_src_id: str | NotGiven = NOT_GIVEN,
        actor_src_type: str | NotGiven = NOT_GIVEN,
        coa_metrics: Iterable[effect_response_create_params.CoaMetric] | NotGiven = NOT_GIVEN,
        collateral_damage_est: float | NotGiven = NOT_GIVEN,
        decision_deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_actions: List[str] | NotGiven = NOT_GIVEN,
        external_request_id: str | NotGiven = NOT_GIVEN,
        id_effect_request: str | NotGiven = NOT_GIVEN,
        munition_id: str | NotGiven = NOT_GIVEN,
        munition_type: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        probability_of_kill: float | NotGiven = NOT_GIVEN,
        red_target_src_id: str | NotGiven = NOT_GIVEN,
        red_target_src_type: str | NotGiven = NOT_GIVEN,
        red_time_to_overhead: Union[str, datetime] | NotGiven = NOT_GIVEN,
        shots_required: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EffectResponse as a POST body and ingest into
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

          source: Source of the data.

          type: The type of response in this record (e.g. COA, SCORECARD, etc.).

          id: Unique identifier of the record, auto-generated by the system.

          actions_list: List of actions associated with this effect response.

          actor_src_id: The record ID, depending on the type identified in actorSrcType, of the
              requested asset.

          actor_src_type: The source type of the asset/actor identifier (AIRCRAFT, LANDCRAFT, SEACRAFT,
              TRACK).

          coa_metrics: List of COA metrics associated with this effect response.

          collateral_damage_est: The collateral damage estimate (CDE) of the munition being fired.

          decision_deadline: The deadline time to accept this COA before it's no longer valid, in ISO8601 UTC
              format.

          external_actions: List of external actions to be executed as part of this task.

          external_request_id: The external system identifier of the associated effect request. A human
              readable unique id.

          id_effect_request: Unique identifier of the EffectRequest associated with this response.

          munition_id: Unique identifier of the munition.

          munition_type: The type of munition being fired.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          probability_of_kill: The probability of kill (0-1) of the target being destroyed.

          red_target_src_id: The record ID, depending on the type identified in redTargetSrcType, of the red
              force target. If the redTargetSrcType is POI or TRACK, then this identifier
              corresponds to either poi.poiid or track.trkId from their respective schemas.

          red_target_src_type: The source type of the targetId identifier (POI, SITE, TRACK).

          red_time_to_overhead: The time to overhead for the red force to be over their target, in ISO8601 UTC
              format.

          shots_required: The number of shots required to destroy target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/effectresponse",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "type": type,
                    "id": id,
                    "actions_list": actions_list,
                    "actor_src_id": actor_src_id,
                    "actor_src_type": actor_src_type,
                    "coa_metrics": coa_metrics,
                    "collateral_damage_est": collateral_damage_est,
                    "decision_deadline": decision_deadline,
                    "external_actions": external_actions,
                    "external_request_id": external_request_id,
                    "id_effect_request": id_effect_request,
                    "munition_id": munition_id,
                    "munition_type": munition_type,
                    "origin": origin,
                    "probability_of_kill": probability_of_kill,
                    "red_target_src_id": red_target_src_id,
                    "red_target_src_type": red_target_src_type,
                    "red_time_to_overhead": red_time_to_overhead,
                    "shots_required": shots_required,
                },
                effect_response_create_params.EffectResponseCreateParams,
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
    ) -> EffectResponseRetrieveResponse:
        """
        Service operation to get a single EffectResponse by its unique ID passed as a
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
            f"/udl/effectresponse/{id}",
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
                    effect_response_retrieve_params.EffectResponseRetrieveParams,
                ),
            ),
            cast_to=EffectResponseRetrieveResponse,
        )

    def list(
        self,
        *,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EffectResponseListResponse, AsyncOffsetPage[EffectResponseListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/effectresponse",
            page=AsyncOffsetPage[EffectResponseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    effect_response_list_params.EffectResponseListParams,
                ),
            ),
            model=EffectResponseListResponse,
        )

    async def count(
        self,
        *,
        created_at: Union[str, date],
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
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/effectresponse/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    effect_response_count_params.EffectResponseCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[effect_response_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        EffectResponse records as a POST body and ingest into the database. This
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
            "/udl/effectresponse/createBulk",
            body=await async_maybe_transform(body, Iterable[effect_response_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> EffectResponseQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/effectresponse/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EffectResponseQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EffectResponseTupleResponse:
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

          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/effectresponse/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    effect_response_tuple_params.EffectResponseTupleParams,
                ),
            ),
            cast_to=EffectResponseTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[effect_response_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple EffectResponses as a POST body and ingest
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
            "/filedrop/udl-effectresponse",
            body=await async_maybe_transform(body, Iterable[effect_response_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EffectResponsesResourceWithRawResponse:
    def __init__(self, effect_responses: EffectResponsesResource) -> None:
        self._effect_responses = effect_responses

        self.create = to_raw_response_wrapper(
            effect_responses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            effect_responses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            effect_responses.list,
        )
        self.count = to_raw_response_wrapper(
            effect_responses.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            effect_responses.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            effect_responses.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            effect_responses.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            effect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._effect_responses.history)


class AsyncEffectResponsesResourceWithRawResponse:
    def __init__(self, effect_responses: AsyncEffectResponsesResource) -> None:
        self._effect_responses = effect_responses

        self.create = async_to_raw_response_wrapper(
            effect_responses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            effect_responses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            effect_responses.list,
        )
        self.count = async_to_raw_response_wrapper(
            effect_responses.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            effect_responses.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            effect_responses.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            effect_responses.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            effect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._effect_responses.history)


class EffectResponsesResourceWithStreamingResponse:
    def __init__(self, effect_responses: EffectResponsesResource) -> None:
        self._effect_responses = effect_responses

        self.create = to_streamed_response_wrapper(
            effect_responses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            effect_responses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            effect_responses.list,
        )
        self.count = to_streamed_response_wrapper(
            effect_responses.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            effect_responses.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            effect_responses.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            effect_responses.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            effect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._effect_responses.history)


class AsyncEffectResponsesResourceWithStreamingResponse:
    def __init__(self, effect_responses: AsyncEffectResponsesResource) -> None:
        self._effect_responses = effect_responses

        self.create = async_to_streamed_response_wrapper(
            effect_responses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            effect_responses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            effect_responses.list,
        )
        self.count = async_to_streamed_response_wrapper(
            effect_responses.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            effect_responses.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            effect_responses.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            effect_responses.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            effect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._effect_responses.history)
