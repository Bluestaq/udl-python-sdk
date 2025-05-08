# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.supporting_data import ProviderMetadataRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviderMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        provider_metadata = client.supporting_data.provider_metadata.retrieve()
        assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        provider_metadata = client.supporting_data.provider_metadata.retrieve(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.supporting_data.provider_metadata.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_metadata = response.parse()
        assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.supporting_data.provider_metadata.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_metadata = response.parse()
            assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProviderMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        provider_metadata = await async_client.supporting_data.provider_metadata.retrieve()
        assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        provider_metadata = await async_client.supporting_data.provider_metadata.retrieve(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.supporting_data.provider_metadata.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_metadata = await response.parse()
        assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.supporting_data.provider_metadata.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_metadata = await response.parse()
            assert_matches_type(ProviderMetadataRetrieveResponse, provider_metadata, path=["response"])

        assert cast(Any, response.is_closed) is True
