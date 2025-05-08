# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.scs.classification_marking_list_response import ClassificationMarkingListResponse

__all__ = ["ClassificationMarkingsResource", "AsyncClassificationMarkingsResource"]


class ClassificationMarkingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassificationMarkingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ClassificationMarkingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassificationMarkingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ClassificationMarkingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassificationMarkingListResponse:
        """Returns a list of all classification markings appropriate to the current user."""
        return self._get(
            "/scs/getClassificationMarkings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationMarkingListResponse,
        )


class AsyncClassificationMarkingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassificationMarkingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClassificationMarkingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassificationMarkingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncClassificationMarkingsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassificationMarkingListResponse:
        """Returns a list of all classification markings appropriate to the current user."""
        return await self._get(
            "/scs/getClassificationMarkings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationMarkingListResponse,
        )


class ClassificationMarkingsResourceWithRawResponse:
    def __init__(self, classification_markings: ClassificationMarkingsResource) -> None:
        self._classification_markings = classification_markings

        self.list = to_raw_response_wrapper(
            classification_markings.list,
        )


class AsyncClassificationMarkingsResourceWithRawResponse:
    def __init__(self, classification_markings: AsyncClassificationMarkingsResource) -> None:
        self._classification_markings = classification_markings

        self.list = async_to_raw_response_wrapper(
            classification_markings.list,
        )


class ClassificationMarkingsResourceWithStreamingResponse:
    def __init__(self, classification_markings: ClassificationMarkingsResource) -> None:
        self._classification_markings = classification_markings

        self.list = to_streamed_response_wrapper(
            classification_markings.list,
        )


class AsyncClassificationMarkingsResourceWithStreamingResponse:
    def __init__(self, classification_markings: AsyncClassificationMarkingsResource) -> None:
        self._classification_markings = classification_markings

        self.list = async_to_streamed_response_wrapper(
            classification_markings.list,
        )
