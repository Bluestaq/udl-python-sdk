# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime

import httpx

from ..types import cot_create_params
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
from .._base_client import make_request_options

__all__ = ["CotsResource", "AsyncCotsResource"]


class CotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CotsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        lat: float,
        lon: float,
        alt: float | NotGiven = NOT_GIVEN,
        call_signs: List[str] | NotGiven = NOT_GIVEN,
        ce: float | NotGiven = NOT_GIVEN,
        cot_chat_data: cot_create_params.CotChatData | NotGiven = NOT_GIVEN,
        cot_position_data: cot_create_params.CotPositionData | NotGiven = NOT_GIVEN,
        groups: List[str] | NotGiven = NOT_GIVEN,
        how: str | NotGiven = NOT_GIVEN,
        le: float | NotGiven = NOT_GIVEN,
        sender_uid: str | NotGiven = NOT_GIVEN,
        stale: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        uids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This service enables posting CoT messages to the UDL TAK server.

        CoT data will
        be persisted in the UDL POI schema as well as federated to connected TAK
        servers.

        Args:
          lat: WGS-84 latitude of the POI, in degrees (+N, -S), -90 to 90.

          lon: WGS-84 longitude of the POI, in degrees (+E, -W), -180 to 180.

          alt: Point height above ellipsoid (WGS-84), in meters.

          call_signs: Optional list of call signs to send message to directly.

          ce: Radius of circular area about lat/lon point, in meters (1-sigma, if representing
              error).

          cot_chat_data: Schema for the CotChatData to post.

          cot_position_data: Schema for the CotPositionData to post.

          groups: Optional set of groups to send message to specifically. If not specified, the
              message will be sent to the default _ANON_ group.

          how: How the event point was generated, in CoT object heirarchy notation (optional,
              CoT).

          le: Height above lat/lon point, in meters (1-sigma, if representing linear error).

          sender_uid: Identifier of the sender of the cot message which should remain the same on
              subsequent POI records of the same point of interest.

          stale: Stale timestamp (optional), in ISO8601 UTC format.

          start: Start time of event validity (optional), in ISO8601 UTC format.

          type: Event type, in CoT object heirarchy notation (optional, CoT).

          uids: Optional list of TAK user ids to send message to directly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/cot",
            body=maybe_transform(
                {
                    "lat": lat,
                    "lon": lon,
                    "alt": alt,
                    "call_signs": call_signs,
                    "ce": ce,
                    "cot_chat_data": cot_chat_data,
                    "cot_position_data": cot_position_data,
                    "groups": groups,
                    "how": how,
                    "le": le,
                    "sender_uid": sender_uid,
                    "stale": stale,
                    "start": start,
                    "type": type,
                    "uids": uids,
                },
                cot_create_params.CotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCotsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        lat: float,
        lon: float,
        alt: float | NotGiven = NOT_GIVEN,
        call_signs: List[str] | NotGiven = NOT_GIVEN,
        ce: float | NotGiven = NOT_GIVEN,
        cot_chat_data: cot_create_params.CotChatData | NotGiven = NOT_GIVEN,
        cot_position_data: cot_create_params.CotPositionData | NotGiven = NOT_GIVEN,
        groups: List[str] | NotGiven = NOT_GIVEN,
        how: str | NotGiven = NOT_GIVEN,
        le: float | NotGiven = NOT_GIVEN,
        sender_uid: str | NotGiven = NOT_GIVEN,
        stale: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        uids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This service enables posting CoT messages to the UDL TAK server.

        CoT data will
        be persisted in the UDL POI schema as well as federated to connected TAK
        servers.

        Args:
          lat: WGS-84 latitude of the POI, in degrees (+N, -S), -90 to 90.

          lon: WGS-84 longitude of the POI, in degrees (+E, -W), -180 to 180.

          alt: Point height above ellipsoid (WGS-84), in meters.

          call_signs: Optional list of call signs to send message to directly.

          ce: Radius of circular area about lat/lon point, in meters (1-sigma, if representing
              error).

          cot_chat_data: Schema for the CotChatData to post.

          cot_position_data: Schema for the CotPositionData to post.

          groups: Optional set of groups to send message to specifically. If not specified, the
              message will be sent to the default _ANON_ group.

          how: How the event point was generated, in CoT object heirarchy notation (optional,
              CoT).

          le: Height above lat/lon point, in meters (1-sigma, if representing linear error).

          sender_uid: Identifier of the sender of the cot message which should remain the same on
              subsequent POI records of the same point of interest.

          stale: Stale timestamp (optional), in ISO8601 UTC format.

          start: Start time of event validity (optional), in ISO8601 UTC format.

          type: Event type, in CoT object heirarchy notation (optional, CoT).

          uids: Optional list of TAK user ids to send message to directly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/cot",
            body=await async_maybe_transform(
                {
                    "lat": lat,
                    "lon": lon,
                    "alt": alt,
                    "call_signs": call_signs,
                    "ce": ce,
                    "cot_chat_data": cot_chat_data,
                    "cot_position_data": cot_position_data,
                    "groups": groups,
                    "how": how,
                    "le": le,
                    "sender_uid": sender_uid,
                    "stale": stale,
                    "start": start,
                    "type": type,
                    "uids": uids,
                },
                cot_create_params.CotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CotsResourceWithRawResponse:
    def __init__(self, cots: CotsResource) -> None:
        self._cots = cots

        self.create = to_raw_response_wrapper(
            cots.create,
        )


class AsyncCotsResourceWithRawResponse:
    def __init__(self, cots: AsyncCotsResource) -> None:
        self._cots = cots

        self.create = async_to_raw_response_wrapper(
            cots.create,
        )


class CotsResourceWithStreamingResponse:
    def __init__(self, cots: CotsResource) -> None:
        self._cots = cots

        self.create = to_streamed_response_wrapper(
            cots.create,
        )


class AsyncCotsResourceWithStreamingResponse:
    def __init__(self, cots: AsyncCotsResource) -> None:
        self._cots = cots

        self.create = async_to_streamed_response_wrapper(
            cots.create,
        )
