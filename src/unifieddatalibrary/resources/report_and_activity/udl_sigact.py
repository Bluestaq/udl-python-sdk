# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ..._base_client import make_request_options
from ...types.report_and_activity import udl_sigact_file_get_params, udl_sigact_unvalidated_publish_params

__all__ = ["UdlSigactResource", "AsyncUdlSigactResource"]


class UdlSigactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UdlSigactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UdlSigactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UdlSigactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return UdlSigactResourceWithStreamingResponse(self)

    def file_get(
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
        Service operation to get a single SigAct text file by its unique ID passed as a
        path parameter. The text file is returned as an attachment Content-Disposition.

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
            f"/udl/sigact/getFile/{id}",
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
                    udl_sigact_file_get_params.UdlSigactFileGetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[udl_sigact_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of SigAct as a POST body and ingest into the
        database. A SigAct provides data for Report and Activity information. Requires a
        specific role, please contact the UDL team to gain access. This operation is
        intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-sigact",
            body=maybe_transform(body, Iterable[udl_sigact_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUdlSigactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUdlSigactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUdlSigactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUdlSigactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncUdlSigactResourceWithStreamingResponse(self)

    async def file_get(
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
        Service operation to get a single SigAct text file by its unique ID passed as a
        path parameter. The text file is returned as an attachment Content-Disposition.

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
            f"/udl/sigact/getFile/{id}",
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
                    udl_sigact_file_get_params.UdlSigactFileGetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[udl_sigact_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of SigAct as a POST body and ingest into the
        database. A SigAct provides data for Report and Activity information. Requires a
        specific role, please contact the UDL team to gain access. This operation is
        intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-sigact",
            body=await async_maybe_transform(body, Iterable[udl_sigact_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UdlSigactResourceWithRawResponse:
    def __init__(self, udl_sigact: UdlSigactResource) -> None:
        self._udl_sigact = udl_sigact

        self.file_get = to_custom_raw_response_wrapper(
            udl_sigact.file_get,
            BinaryAPIResponse,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            udl_sigact.unvalidated_publish,
        )


class AsyncUdlSigactResourceWithRawResponse:
    def __init__(self, udl_sigact: AsyncUdlSigactResource) -> None:
        self._udl_sigact = udl_sigact

        self.file_get = async_to_custom_raw_response_wrapper(
            udl_sigact.file_get,
            AsyncBinaryAPIResponse,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            udl_sigact.unvalidated_publish,
        )


class UdlSigactResourceWithStreamingResponse:
    def __init__(self, udl_sigact: UdlSigactResource) -> None:
        self._udl_sigact = udl_sigact

        self.file_get = to_custom_streamed_response_wrapper(
            udl_sigact.file_get,
            StreamedBinaryAPIResponse,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            udl_sigact.unvalidated_publish,
        )


class AsyncUdlSigactResourceWithStreamingResponse:
    def __init__(self, udl_sigact: AsyncUdlSigactResource) -> None:
        self._udl_sigact = udl_sigact

        self.file_get = async_to_custom_streamed_response_wrapper(
            udl_sigact.file_get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            udl_sigact.unvalidated_publish,
        )
