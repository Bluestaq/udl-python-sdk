# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ephemeride_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["EphemeridesResource", "AsyncEphemeridesResource"]


class EphemeridesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EphemeridesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return EphemeridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EphemeridesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return EphemeridesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: str,
        classification: str,
        data_mode: str,
        ephem_format_type: str,
        has_mnvr: bool,
        sat_no: int,
        source: str,
        type: str,
        body: str,
        origin: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to post/store Ephemeris data.

        This operation is intended to be
        used for automated feeds into UDL. The payload is in Ephemeris format as
        described by the "Flight Safety Handbook" published by 18th Space Command. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        **Example:**
        /filedrop/ephem?classification=U&dataMode=TEST&source=Bluestaq&satNo=25544&ephemFormatType=NASA&hasMnvr=false&type=ROUTINE&category=EXTERNAL&origin=NASA&tags=tag1,tag2

        Args:
          category: Ephemeris category.

          classification: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          ephem_format_type: Ephemeris format as documented in Flight Safety Handbook.

          has_mnvr: Boolean indicating whether maneuver(s) are incorporated into the ephemeris.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          source: Source of the Ephemeris data.

          type: Ephemeris type.

          origin: Optional origin of the Ephemeris.

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
            "/filedrop/ephem",
            body=maybe_transform(body, ephemeride_create_params.EphemerideCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "classification": classification,
                        "data_mode": data_mode,
                        "ephem_format_type": ephem_format_type,
                        "has_mnvr": has_mnvr,
                        "sat_no": sat_no,
                        "source": source,
                        "type": type,
                        "origin": origin,
                        "tags": tags,
                    },
                    ephemeride_create_params.EphemerideCreateParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncEphemeridesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEphemeridesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEphemeridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEphemeridesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncEphemeridesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: str,
        classification: str,
        data_mode: str,
        ephem_format_type: str,
        has_mnvr: bool,
        sat_no: int,
        source: str,
        type: str,
        body: str,
        origin: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to post/store Ephemeris data.

        This operation is intended to be
        used for automated feeds into UDL. The payload is in Ephemeris format as
        described by the "Flight Safety Handbook" published by 18th Space Command. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        **Example:**
        /filedrop/ephem?classification=U&dataMode=TEST&source=Bluestaq&satNo=25544&ephemFormatType=NASA&hasMnvr=false&type=ROUTINE&category=EXTERNAL&origin=NASA&tags=tag1,tag2

        Args:
          category: Ephemeris category.

          classification: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          ephem_format_type: Ephemeris format as documented in Flight Safety Handbook.

          has_mnvr: Boolean indicating whether maneuver(s) are incorporated into the ephemeris.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          source: Source of the Ephemeris data.

          type: Ephemeris type.

          origin: Optional origin of the Ephemeris.

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
            "/filedrop/ephem",
            body=await async_maybe_transform(body, ephemeride_create_params.EphemerideCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "classification": classification,
                        "data_mode": data_mode,
                        "ephem_format_type": ephem_format_type,
                        "has_mnvr": has_mnvr,
                        "sat_no": sat_no,
                        "source": source,
                        "type": type,
                        "origin": origin,
                        "tags": tags,
                    },
                    ephemeride_create_params.EphemerideCreateParams,
                ),
            ),
            cast_to=NoneType,
        )


class EphemeridesResourceWithRawResponse:
    def __init__(self, ephemerides: EphemeridesResource) -> None:
        self._ephemerides = ephemerides

        self.create = to_raw_response_wrapper(
            ephemerides.create,
        )


class AsyncEphemeridesResourceWithRawResponse:
    def __init__(self, ephemerides: AsyncEphemeridesResource) -> None:
        self._ephemerides = ephemerides

        self.create = async_to_raw_response_wrapper(
            ephemerides.create,
        )


class EphemeridesResourceWithStreamingResponse:
    def __init__(self, ephemerides: EphemeridesResource) -> None:
        self._ephemerides = ephemerides

        self.create = to_streamed_response_wrapper(
            ephemerides.create,
        )


class AsyncEphemeridesResourceWithStreamingResponse:
    def __init__(self, ephemerides: AsyncEphemeridesResource) -> None:
        self._ephemerides = ephemerides

        self.create = async_to_streamed_response_wrapper(
            ephemerides.create,
        )
