# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    onorbitthrusterstatus_get_params,
    onorbitthrusterstatus_list_params,
    onorbitthrusterstatus_count_params,
    onorbitthrusterstatus_tuple_params,
    onorbitthrusterstatus_create_params,
    onorbitthrusterstatus_create_bulk_params,
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
from ...types.onorbitthrusterstatus_list_response import OnorbitthrusterstatusListResponse
from ...types.onorbitthrusterstatus_tuple_response import OnorbitthrusterstatusTupleResponse
from ...types.onorbitthrusterstatus_queryhelp_response import OnorbitthrusterstatusQueryhelpResponse
from ...types.onorbitthrusterstatus.onorbitthrusterstatus_full import OnorbitthrusterstatusFull

__all__ = ["OnorbitthrusterstatusResource", "AsyncOnorbitthrusterstatusResource"]


class OnorbitthrusterstatusResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnorbitthrusterstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnorbitthrusterstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbitthrusterstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnorbitthrusterstatusResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_onorbit_thruster: str,
        source: str,
        status_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        est_delta_v: float | NotGiven = NOT_GIVEN,
        fuel_mass: float | NotGiven = NOT_GIVEN,
        fuel_mass_unc: float | NotGiven = NOT_GIVEN,
        isp: float | NotGiven = NOT_GIVEN,
        max_delta_v: float | NotGiven = NOT_GIVEN,
        min_delta_v: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        operational: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        prop_mass_avg: float | NotGiven = NOT_GIVEN,
        prop_mass_max: float | NotGiven = NOT_GIVEN,
        prop_mass_median: float | NotGiven = NOT_GIVEN,
        prop_mass_min: float | NotGiven = NOT_GIVEN,
        thrust_max: float | NotGiven = NOT_GIVEN,
        total_delta_v: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitThrusterStatus record as a POST body
        and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          id_onorbit_thruster: ID of the associated OnorbitThruster record. This ID can be used to obtain
              additional information on an onorbit thruster object using the 'get by ID'
              operation (e.g. /udl/onorbitthruster/{id}). For example, the OnorbitThruster
              object with idOnorbitThruster = abc would be queried as
              /udl/onorbitthruster/abc.

          source: Source of the data.

          status_time: Datetime of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          est_delta_v: Estimated available delta-velocity for this thruster, in meters per second.

          fuel_mass: Total fuel mass available for this thruster's type, in kilograms.

          fuel_mass_unc: 1-sigma uncertainty of the total fuel mass available for this thruster type, in
              kilograms.

          isp: Specific impulse for this thruster, in seconds.

          max_delta_v: Maximum available delta-velocity for this thruster, in meters per second.

          min_delta_v: Minimum available delta-velocity for this thruster, in meters per second.

          name: Identifier of this thruster.

          operational: Flag indicating if this thruster is operational.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          prop_mass_avg: Average available propellant mass for this thruster's type, in kilograms.

          prop_mass_max: Maximum available propellant mass for this thruster's type, in kilograms.

          prop_mass_median: Median available propellant mass for this thruster's type, in kilograms.

          prop_mass_min: Minimum available propellant mass for this thruster's type, in kilograms.

          thrust_max: Maximum available thrust for this thruster, in newtons.

          total_delta_v: Total delta-velocity available for this thruster's type, in meters per second.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/onorbitthrusterstatus",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_onorbit_thruster": id_onorbit_thruster,
                    "source": source,
                    "status_time": status_time,
                    "id": id,
                    "est_delta_v": est_delta_v,
                    "fuel_mass": fuel_mass,
                    "fuel_mass_unc": fuel_mass_unc,
                    "isp": isp,
                    "max_delta_v": max_delta_v,
                    "min_delta_v": min_delta_v,
                    "name": name,
                    "operational": operational,
                    "origin": origin,
                    "prop_mass_avg": prop_mass_avg,
                    "prop_mass_max": prop_mass_max,
                    "prop_mass_median": prop_mass_median,
                    "prop_mass_min": prop_mass_min,
                    "thrust_max": thrust_max,
                    "total_delta_v": total_delta_v,
                },
                onorbitthrusterstatus_create_params.OnorbitthrusterstatusCreateParams,
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
        id_onorbit_thruster: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        status_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[OnorbitthrusterstatusListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_onorbit_thruster: (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
              associated OnorbitThruster record. This ID can be used to obtain additional
              information on an onorbit thruster object using the 'get by ID' operation (e.g.
              /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
              idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.

          status_time: (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
              of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/onorbitthrusterstatus",
            page=SyncOffsetPage[OnorbitthrusterstatusListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_onorbit_thruster": id_onorbit_thruster,
                        "max_results": max_results,
                        "status_time": status_time,
                    },
                    onorbitthrusterstatus_list_params.OnorbitthrusterstatusListParams,
                ),
            ),
            model=OnorbitthrusterstatusListResponse,
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
        Service operation to delete a OnorbitThrusterStatus record specified by the
        passed ID path parameter. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/onorbitthrusterstatus/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_onorbit_thruster: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        status_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          id_onorbit_thruster: (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
              associated OnorbitThruster record. This ID can be used to obtain additional
              information on an onorbit thruster object using the 'get by ID' operation (e.g.
              /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
              idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.

          status_time: (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
              of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/onorbitthrusterstatus/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_onorbit_thruster": id_onorbit_thruster,
                        "max_results": max_results,
                        "status_time": status_time,
                    },
                    onorbitthrusterstatus_count_params.OnorbitthrusterstatusCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[onorbitthrusterstatus_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        onorbitthrusterstatus records as a POST body and ingest into the database. This
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
            "/udl/onorbitthrusterstatus/createBulk",
            body=maybe_transform(body, Iterable[onorbitthrusterstatus_create_bulk_params.Body]),
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
    ) -> OnorbitthrusterstatusFull:
        """
        Service operation to get a single OnorbitThrusterStatus record by its unique ID
        passed as a path parameter. OnorbitThrusterStatus records are information for
        OnorbitThruster objects.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/onorbitthrusterstatus/{id}",
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
                    onorbitthrusterstatus_get_params.OnorbitthrusterstatusGetParams,
                ),
            ),
            cast_to=OnorbitthrusterstatusFull,
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
    ) -> OnorbitthrusterstatusQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/onorbitthrusterstatus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnorbitthrusterstatusQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        id_onorbit_thruster: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        status_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnorbitthrusterstatusTupleResponse:
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

          id_onorbit_thruster: (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
              associated OnorbitThruster record. This ID can be used to obtain additional
              information on an onorbit thruster object using the 'get by ID' operation (e.g.
              /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
              idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.

          status_time: (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
              of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/onorbitthrusterstatus/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_onorbit_thruster": id_onorbit_thruster,
                        "max_results": max_results,
                        "status_time": status_time,
                    },
                    onorbitthrusterstatus_tuple_params.OnorbitthrusterstatusTupleParams,
                ),
            ),
            cast_to=OnorbitthrusterstatusTupleResponse,
        )


class AsyncOnorbitthrusterstatusResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnorbitthrusterstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbitthrusterstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnorbitthrusterstatusResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_onorbit_thruster: str,
        source: str,
        status_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        est_delta_v: float | NotGiven = NOT_GIVEN,
        fuel_mass: float | NotGiven = NOT_GIVEN,
        fuel_mass_unc: float | NotGiven = NOT_GIVEN,
        isp: float | NotGiven = NOT_GIVEN,
        max_delta_v: float | NotGiven = NOT_GIVEN,
        min_delta_v: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        operational: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        prop_mass_avg: float | NotGiven = NOT_GIVEN,
        prop_mass_max: float | NotGiven = NOT_GIVEN,
        prop_mass_median: float | NotGiven = NOT_GIVEN,
        prop_mass_min: float | NotGiven = NOT_GIVEN,
        thrust_max: float | NotGiven = NOT_GIVEN,
        total_delta_v: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitThrusterStatus record as a POST body
        and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          id_onorbit_thruster: ID of the associated OnorbitThruster record. This ID can be used to obtain
              additional information on an onorbit thruster object using the 'get by ID'
              operation (e.g. /udl/onorbitthruster/{id}). For example, the OnorbitThruster
              object with idOnorbitThruster = abc would be queried as
              /udl/onorbitthruster/abc.

          source: Source of the data.

          status_time: Datetime of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          est_delta_v: Estimated available delta-velocity for this thruster, in meters per second.

          fuel_mass: Total fuel mass available for this thruster's type, in kilograms.

          fuel_mass_unc: 1-sigma uncertainty of the total fuel mass available for this thruster type, in
              kilograms.

          isp: Specific impulse for this thruster, in seconds.

          max_delta_v: Maximum available delta-velocity for this thruster, in meters per second.

          min_delta_v: Minimum available delta-velocity for this thruster, in meters per second.

          name: Identifier of this thruster.

          operational: Flag indicating if this thruster is operational.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          prop_mass_avg: Average available propellant mass for this thruster's type, in kilograms.

          prop_mass_max: Maximum available propellant mass for this thruster's type, in kilograms.

          prop_mass_median: Median available propellant mass for this thruster's type, in kilograms.

          prop_mass_min: Minimum available propellant mass for this thruster's type, in kilograms.

          thrust_max: Maximum available thrust for this thruster, in newtons.

          total_delta_v: Total delta-velocity available for this thruster's type, in meters per second.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/onorbitthrusterstatus",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_onorbit_thruster": id_onorbit_thruster,
                    "source": source,
                    "status_time": status_time,
                    "id": id,
                    "est_delta_v": est_delta_v,
                    "fuel_mass": fuel_mass,
                    "fuel_mass_unc": fuel_mass_unc,
                    "isp": isp,
                    "max_delta_v": max_delta_v,
                    "min_delta_v": min_delta_v,
                    "name": name,
                    "operational": operational,
                    "origin": origin,
                    "prop_mass_avg": prop_mass_avg,
                    "prop_mass_max": prop_mass_max,
                    "prop_mass_median": prop_mass_median,
                    "prop_mass_min": prop_mass_min,
                    "thrust_max": thrust_max,
                    "total_delta_v": total_delta_v,
                },
                onorbitthrusterstatus_create_params.OnorbitthrusterstatusCreateParams,
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
        id_onorbit_thruster: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        status_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OnorbitthrusterstatusListResponse, AsyncOffsetPage[OnorbitthrusterstatusListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_onorbit_thruster: (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
              associated OnorbitThruster record. This ID can be used to obtain additional
              information on an onorbit thruster object using the 'get by ID' operation (e.g.
              /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
              idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.

          status_time: (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
              of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/onorbitthrusterstatus",
            page=AsyncOffsetPage[OnorbitthrusterstatusListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_onorbit_thruster": id_onorbit_thruster,
                        "max_results": max_results,
                        "status_time": status_time,
                    },
                    onorbitthrusterstatus_list_params.OnorbitthrusterstatusListParams,
                ),
            ),
            model=OnorbitthrusterstatusListResponse,
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
        Service operation to delete a OnorbitThrusterStatus record specified by the
        passed ID path parameter. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/onorbitthrusterstatus/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_onorbit_thruster: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        status_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          id_onorbit_thruster: (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
              associated OnorbitThruster record. This ID can be used to obtain additional
              information on an onorbit thruster object using the 'get by ID' operation (e.g.
              /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
              idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.

          status_time: (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
              of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/onorbitthrusterstatus/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "id_onorbit_thruster": id_onorbit_thruster,
                        "max_results": max_results,
                        "status_time": status_time,
                    },
                    onorbitthrusterstatus_count_params.OnorbitthrusterstatusCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[onorbitthrusterstatus_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        onorbitthrusterstatus records as a POST body and ingest into the database. This
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
            "/udl/onorbitthrusterstatus/createBulk",
            body=await async_maybe_transform(body, Iterable[onorbitthrusterstatus_create_bulk_params.Body]),
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
    ) -> OnorbitthrusterstatusFull:
        """
        Service operation to get a single OnorbitThrusterStatus record by its unique ID
        passed as a path parameter. OnorbitThrusterStatus records are information for
        OnorbitThruster objects.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/onorbitthrusterstatus/{id}",
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
                    onorbitthrusterstatus_get_params.OnorbitthrusterstatusGetParams,
                ),
            ),
            cast_to=OnorbitthrusterstatusFull,
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
    ) -> OnorbitthrusterstatusQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/onorbitthrusterstatus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnorbitthrusterstatusQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        id_onorbit_thruster: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        status_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnorbitthrusterstatusTupleResponse:
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

          id_onorbit_thruster: (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
              associated OnorbitThruster record. This ID can be used to obtain additional
              information on an onorbit thruster object using the 'get by ID' operation (e.g.
              /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
              idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.

          status_time: (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
              of the thruster status observation in ISO 8601 UTC datetime format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/onorbitthrusterstatus/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_onorbit_thruster": id_onorbit_thruster,
                        "max_results": max_results,
                        "status_time": status_time,
                    },
                    onorbitthrusterstatus_tuple_params.OnorbitthrusterstatusTupleParams,
                ),
            ),
            cast_to=OnorbitthrusterstatusTupleResponse,
        )


class OnorbitthrusterstatusResourceWithRawResponse:
    def __init__(self, onorbitthrusterstatus: OnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

        self.create = to_raw_response_wrapper(
            onorbitthrusterstatus.create,
        )
        self.list = to_raw_response_wrapper(
            onorbitthrusterstatus.list,
        )
        self.delete = to_raw_response_wrapper(
            onorbitthrusterstatus.delete,
        )
        self.count = to_raw_response_wrapper(
            onorbitthrusterstatus.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            onorbitthrusterstatus.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            onorbitthrusterstatus.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            onorbitthrusterstatus.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            onorbitthrusterstatus.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._onorbitthrusterstatus.history)


class AsyncOnorbitthrusterstatusResourceWithRawResponse:
    def __init__(self, onorbitthrusterstatus: AsyncOnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

        self.create = async_to_raw_response_wrapper(
            onorbitthrusterstatus.create,
        )
        self.list = async_to_raw_response_wrapper(
            onorbitthrusterstatus.list,
        )
        self.delete = async_to_raw_response_wrapper(
            onorbitthrusterstatus.delete,
        )
        self.count = async_to_raw_response_wrapper(
            onorbitthrusterstatus.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            onorbitthrusterstatus.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            onorbitthrusterstatus.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            onorbitthrusterstatus.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            onorbitthrusterstatus.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._onorbitthrusterstatus.history)


class OnorbitthrusterstatusResourceWithStreamingResponse:
    def __init__(self, onorbitthrusterstatus: OnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

        self.create = to_streamed_response_wrapper(
            onorbitthrusterstatus.create,
        )
        self.list = to_streamed_response_wrapper(
            onorbitthrusterstatus.list,
        )
        self.delete = to_streamed_response_wrapper(
            onorbitthrusterstatus.delete,
        )
        self.count = to_streamed_response_wrapper(
            onorbitthrusterstatus.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            onorbitthrusterstatus.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            onorbitthrusterstatus.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            onorbitthrusterstatus.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            onorbitthrusterstatus.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._onorbitthrusterstatus.history)


class AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
    def __init__(self, onorbitthrusterstatus: AsyncOnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

        self.create = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.create,
        )
        self.list = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            onorbitthrusterstatus.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._onorbitthrusterstatus.history)
