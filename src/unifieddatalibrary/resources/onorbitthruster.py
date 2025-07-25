# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    onorbitthruster_get_params,
    onorbitthruster_list_params,
    onorbitthruster_create_params,
    onorbitthruster_update_params,
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
from ..types.onorbitthruster_get_response import OnorbitthrusterGetResponse
from ..types.onorbitthruster_list_response import OnorbitthrusterListResponse

__all__ = ["OnorbitthrusterResource", "AsyncOnorbitthrusterResource"]


class OnorbitthrusterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnorbitthrusterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnorbitthrusterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbitthrusterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnorbitthrusterResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_engine: str,
        id_on_orbit: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        engine: onorbitthruster_create_params.Engine | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitThruster as a POST body and ingest
        into the database. An OnorbitThruster is the association between an on-orbit
        spacecraft's engine and a particular on-orbit spacecraft. An Engine type may be
        associated with many different on-orbit spacecraft. A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          id_engine: ID of the Engine.

          id_on_orbit: ID of the on-orbit object.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          engine: Known launch vehicle engines and their performance characteristics and limits. A
              launch vehicle has 1 to many engines per stage.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          quantity: The number of engines/thrusters on the spacecraft of the type identified by
              idEngine.

          type: The type of thruster associated with this record (e.g. LAE, Hydrazine REA,
              etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/onorbitthruster",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "id": id,
                    "engine": engine,
                    "origin": origin,
                    "quantity": quantity,
                    "type": type,
                },
                onorbitthruster_create_params.OnorbitthrusterCreateParams,
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
        id_on_orbit: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        engine: onorbitthruster_update_params.Engine | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single OnorbitThruster.

        An OnorbitThruster is the
        association between an on-orbit spacecraft's engine and a particular on-orbit
        spacecraft. An Engine type may be associated with many different on-orbit
        spacecraft. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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

          id_engine: ID of the Engine.

          id_on_orbit: ID of the on-orbit object.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          engine: Known launch vehicle engines and their performance characteristics and limits. A
              launch vehicle has 1 to many engines per stage.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          quantity: The number of engines/thrusters on the spacecraft of the type identified by
              idEngine.

          type: The type of thruster associated with this record (e.g. LAE, Hydrazine REA,
              etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/onorbitthruster/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "body_id": body_id,
                    "engine": engine,
                    "origin": origin,
                    "quantity": quantity,
                    "type": type,
                },
                onorbitthruster_update_params.OnorbitthrusterUpdateParams,
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
    ) -> SyncOffsetPage[OnorbitthrusterListResponse]:
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
            "/udl/onorbitthruster",
            page=SyncOffsetPage[OnorbitthrusterListResponse],
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
                    onorbitthruster_list_params.OnorbitthrusterListParams,
                ),
            ),
            model=OnorbitthrusterListResponse,
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
        Service operation to delete a OnorbitThruster object specified by the passed ID
        path parameter. An OnorbitThruster is the association between an on-orbit
        spacecraft's engine and a particular on-orbit spacecraft. An Engine type may be
        associated with many different on-orbit spacecraft. A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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
            f"/udl/onorbitthruster/{id}",
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
    ) -> OnorbitthrusterGetResponse:
        """
        Service operation to get a single OnorbitThruster record by its unique ID passed
        as a path parameter. An OnorbitThruster is the association between an on-orbit
        spacecraft's engine and a particular on-orbit spacecraft. An Engine type may be
        associated with many different on-orbit spacecraft.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/onorbitthruster/{id}",
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
                    onorbitthruster_get_params.OnorbitthrusterGetParams,
                ),
            ),
            cast_to=OnorbitthrusterGetResponse,
        )


class AsyncOnorbitthrusterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnorbitthrusterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbitthrusterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbitthrusterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnorbitthrusterResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_engine: str,
        id_on_orbit: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        engine: onorbitthruster_create_params.Engine | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitThruster as a POST body and ingest
        into the database. An OnorbitThruster is the association between an on-orbit
        spacecraft's engine and a particular on-orbit spacecraft. An Engine type may be
        associated with many different on-orbit spacecraft. A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          id_engine: ID of the Engine.

          id_on_orbit: ID of the on-orbit object.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          engine: Known launch vehicle engines and their performance characteristics and limits. A
              launch vehicle has 1 to many engines per stage.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          quantity: The number of engines/thrusters on the spacecraft of the type identified by
              idEngine.

          type: The type of thruster associated with this record (e.g. LAE, Hydrazine REA,
              etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/onorbitthruster",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "id": id,
                    "engine": engine,
                    "origin": origin,
                    "quantity": quantity,
                    "type": type,
                },
                onorbitthruster_create_params.OnorbitthrusterCreateParams,
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
        id_on_orbit: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        engine: onorbitthruster_update_params.Engine | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single OnorbitThruster.

        An OnorbitThruster is the
        association between an on-orbit spacecraft's engine and a particular on-orbit
        spacecraft. An Engine type may be associated with many different on-orbit
        spacecraft. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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

          id_engine: ID of the Engine.

          id_on_orbit: ID of the on-orbit object.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          engine: Known launch vehicle engines and their performance characteristics and limits. A
              launch vehicle has 1 to many engines per stage.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          quantity: The number of engines/thrusters on the spacecraft of the type identified by
              idEngine.

          type: The type of thruster associated with this record (e.g. LAE, Hydrazine REA,
              etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/onorbitthruster/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_engine": id_engine,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "body_id": body_id,
                    "engine": engine,
                    "origin": origin,
                    "quantity": quantity,
                    "type": type,
                },
                onorbitthruster_update_params.OnorbitthrusterUpdateParams,
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
    ) -> AsyncPaginator[OnorbitthrusterListResponse, AsyncOffsetPage[OnorbitthrusterListResponse]]:
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
            "/udl/onorbitthruster",
            page=AsyncOffsetPage[OnorbitthrusterListResponse],
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
                    onorbitthruster_list_params.OnorbitthrusterListParams,
                ),
            ),
            model=OnorbitthrusterListResponse,
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
        Service operation to delete a OnorbitThruster object specified by the passed ID
        path parameter. An OnorbitThruster is the association between an on-orbit
        spacecraft's engine and a particular on-orbit spacecraft. An Engine type may be
        associated with many different on-orbit spacecraft. A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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
            f"/udl/onorbitthruster/{id}",
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
    ) -> OnorbitthrusterGetResponse:
        """
        Service operation to get a single OnorbitThruster record by its unique ID passed
        as a path parameter. An OnorbitThruster is the association between an on-orbit
        spacecraft's engine and a particular on-orbit spacecraft. An Engine type may be
        associated with many different on-orbit spacecraft.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/onorbitthruster/{id}",
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
                    onorbitthruster_get_params.OnorbitthrusterGetParams,
                ),
            ),
            cast_to=OnorbitthrusterGetResponse,
        )


class OnorbitthrusterResourceWithRawResponse:
    def __init__(self, onorbitthruster: OnorbitthrusterResource) -> None:
        self._onorbitthruster = onorbitthruster

        self.create = to_raw_response_wrapper(
            onorbitthruster.create,
        )
        self.update = to_raw_response_wrapper(
            onorbitthruster.update,
        )
        self.list = to_raw_response_wrapper(
            onorbitthruster.list,
        )
        self.delete = to_raw_response_wrapper(
            onorbitthruster.delete,
        )
        self.get = to_raw_response_wrapper(
            onorbitthruster.get,
        )


class AsyncOnorbitthrusterResourceWithRawResponse:
    def __init__(self, onorbitthruster: AsyncOnorbitthrusterResource) -> None:
        self._onorbitthruster = onorbitthruster

        self.create = async_to_raw_response_wrapper(
            onorbitthruster.create,
        )
        self.update = async_to_raw_response_wrapper(
            onorbitthruster.update,
        )
        self.list = async_to_raw_response_wrapper(
            onorbitthruster.list,
        )
        self.delete = async_to_raw_response_wrapper(
            onorbitthruster.delete,
        )
        self.get = async_to_raw_response_wrapper(
            onorbitthruster.get,
        )


class OnorbitthrusterResourceWithStreamingResponse:
    def __init__(self, onorbitthruster: OnorbitthrusterResource) -> None:
        self._onorbitthruster = onorbitthruster

        self.create = to_streamed_response_wrapper(
            onorbitthruster.create,
        )
        self.update = to_streamed_response_wrapper(
            onorbitthruster.update,
        )
        self.list = to_streamed_response_wrapper(
            onorbitthruster.list,
        )
        self.delete = to_streamed_response_wrapper(
            onorbitthruster.delete,
        )
        self.get = to_streamed_response_wrapper(
            onorbitthruster.get,
        )


class AsyncOnorbitthrusterResourceWithStreamingResponse:
    def __init__(self, onorbitthruster: AsyncOnorbitthrusterResource) -> None:
        self._onorbitthruster = onorbitthruster

        self.create = async_to_streamed_response_wrapper(
            onorbitthruster.create,
        )
        self.update = async_to_streamed_response_wrapper(
            onorbitthruster.update,
        )
        self.list = async_to_streamed_response_wrapper(
            onorbitthruster.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            onorbitthruster.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            onorbitthruster.get,
        )
