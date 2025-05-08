# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .dataowner import (
    DataownerResource,
    AsyncDataownerResource,
    DataownerResourceWithRawResponse,
    AsyncDataownerResourceWithRawResponse,
    DataownerResourceWithStreamingResponse,
    AsyncDataownerResourceWithStreamingResponse,
)
from .data_types import (
    DataTypesResource,
    AsyncDataTypesResource,
    DataTypesResourceWithRawResponse,
    AsyncDataTypesResourceWithRawResponse,
    DataTypesResourceWithStreamingResponse,
    AsyncDataTypesResourceWithStreamingResponse,
)
from .query_help import (
    QueryHelpResource,
    AsyncQueryHelpResource,
    QueryHelpResourceWithRawResponse,
    AsyncQueryHelpResourceWithRawResponse,
    QueryHelpResourceWithStreamingResponse,
    AsyncQueryHelpResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .dataowner_types import (
    DataownerTypesResource,
    AsyncDataownerTypesResource,
    DataownerTypesResourceWithRawResponse,
    AsyncDataownerTypesResourceWithRawResponse,
    DataownerTypesResourceWithStreamingResponse,
    AsyncDataownerTypesResourceWithStreamingResponse,
)
from .provider_metadata import (
    ProviderMetadataResource,
    AsyncProviderMetadataResource,
    ProviderMetadataResourceWithRawResponse,
    AsyncProviderMetadataResourceWithRawResponse,
    ProviderMetadataResourceWithStreamingResponse,
    AsyncProviderMetadataResourceWithStreamingResponse,
)

__all__ = ["SupportingDataResource", "AsyncSupportingDataResource"]


class SupportingDataResource(SyncAPIResource):
    @cached_property
    def data_types(self) -> DataTypesResource:
        return DataTypesResource(self._client)

    @cached_property
    def dataowner(self) -> DataownerResource:
        return DataownerResource(self._client)

    @cached_property
    def dataowner_types(self) -> DataownerTypesResource:
        return DataownerTypesResource(self._client)

    @cached_property
    def provider_metadata(self) -> ProviderMetadataResource:
        return ProviderMetadataResource(self._client)

    @cached_property
    def query_help(self) -> QueryHelpResource:
        return QueryHelpResource(self._client)

    @cached_property
    def with_raw_response(self) -> SupportingDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SupportingDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportingDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SupportingDataResourceWithStreamingResponse(self)


class AsyncSupportingDataResource(AsyncAPIResource):
    @cached_property
    def data_types(self) -> AsyncDataTypesResource:
        return AsyncDataTypesResource(self._client)

    @cached_property
    def dataowner(self) -> AsyncDataownerResource:
        return AsyncDataownerResource(self._client)

    @cached_property
    def dataowner_types(self) -> AsyncDataownerTypesResource:
        return AsyncDataownerTypesResource(self._client)

    @cached_property
    def provider_metadata(self) -> AsyncProviderMetadataResource:
        return AsyncProviderMetadataResource(self._client)

    @cached_property
    def query_help(self) -> AsyncQueryHelpResource:
        return AsyncQueryHelpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSupportingDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportingDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportingDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSupportingDataResourceWithStreamingResponse(self)


class SupportingDataResourceWithRawResponse:
    def __init__(self, supporting_data: SupportingDataResource) -> None:
        self._supporting_data = supporting_data

    @cached_property
    def data_types(self) -> DataTypesResourceWithRawResponse:
        return DataTypesResourceWithRawResponse(self._supporting_data.data_types)

    @cached_property
    def dataowner(self) -> DataownerResourceWithRawResponse:
        return DataownerResourceWithRawResponse(self._supporting_data.dataowner)

    @cached_property
    def dataowner_types(self) -> DataownerTypesResourceWithRawResponse:
        return DataownerTypesResourceWithRawResponse(self._supporting_data.dataowner_types)

    @cached_property
    def provider_metadata(self) -> ProviderMetadataResourceWithRawResponse:
        return ProviderMetadataResourceWithRawResponse(self._supporting_data.provider_metadata)

    @cached_property
    def query_help(self) -> QueryHelpResourceWithRawResponse:
        return QueryHelpResourceWithRawResponse(self._supporting_data.query_help)


class AsyncSupportingDataResourceWithRawResponse:
    def __init__(self, supporting_data: AsyncSupportingDataResource) -> None:
        self._supporting_data = supporting_data

    @cached_property
    def data_types(self) -> AsyncDataTypesResourceWithRawResponse:
        return AsyncDataTypesResourceWithRawResponse(self._supporting_data.data_types)

    @cached_property
    def dataowner(self) -> AsyncDataownerResourceWithRawResponse:
        return AsyncDataownerResourceWithRawResponse(self._supporting_data.dataowner)

    @cached_property
    def dataowner_types(self) -> AsyncDataownerTypesResourceWithRawResponse:
        return AsyncDataownerTypesResourceWithRawResponse(self._supporting_data.dataowner_types)

    @cached_property
    def provider_metadata(self) -> AsyncProviderMetadataResourceWithRawResponse:
        return AsyncProviderMetadataResourceWithRawResponse(self._supporting_data.provider_metadata)

    @cached_property
    def query_help(self) -> AsyncQueryHelpResourceWithRawResponse:
        return AsyncQueryHelpResourceWithRawResponse(self._supporting_data.query_help)


class SupportingDataResourceWithStreamingResponse:
    def __init__(self, supporting_data: SupportingDataResource) -> None:
        self._supporting_data = supporting_data

    @cached_property
    def data_types(self) -> DataTypesResourceWithStreamingResponse:
        return DataTypesResourceWithStreamingResponse(self._supporting_data.data_types)

    @cached_property
    def dataowner(self) -> DataownerResourceWithStreamingResponse:
        return DataownerResourceWithStreamingResponse(self._supporting_data.dataowner)

    @cached_property
    def dataowner_types(self) -> DataownerTypesResourceWithStreamingResponse:
        return DataownerTypesResourceWithStreamingResponse(self._supporting_data.dataowner_types)

    @cached_property
    def provider_metadata(self) -> ProviderMetadataResourceWithStreamingResponse:
        return ProviderMetadataResourceWithStreamingResponse(self._supporting_data.provider_metadata)

    @cached_property
    def query_help(self) -> QueryHelpResourceWithStreamingResponse:
        return QueryHelpResourceWithStreamingResponse(self._supporting_data.query_help)


class AsyncSupportingDataResourceWithStreamingResponse:
    def __init__(self, supporting_data: AsyncSupportingDataResource) -> None:
        self._supporting_data = supporting_data

    @cached_property
    def data_types(self) -> AsyncDataTypesResourceWithStreamingResponse:
        return AsyncDataTypesResourceWithStreamingResponse(self._supporting_data.data_types)

    @cached_property
    def dataowner(self) -> AsyncDataownerResourceWithStreamingResponse:
        return AsyncDataownerResourceWithStreamingResponse(self._supporting_data.dataowner)

    @cached_property
    def dataowner_types(self) -> AsyncDataownerTypesResourceWithStreamingResponse:
        return AsyncDataownerTypesResourceWithStreamingResponse(self._supporting_data.dataowner_types)

    @cached_property
    def provider_metadata(self) -> AsyncProviderMetadataResourceWithStreamingResponse:
        return AsyncProviderMetadataResourceWithStreamingResponse(self._supporting_data.provider_metadata)

    @cached_property
    def query_help(self) -> AsyncQueryHelpResourceWithStreamingResponse:
        return AsyncQueryHelpResourceWithStreamingResponse(self._supporting_data.query_help)
