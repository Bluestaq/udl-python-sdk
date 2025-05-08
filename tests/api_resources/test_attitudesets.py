# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.shared import AttitudesetFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttitudesets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        attitudeset = client.attitudesets.retrieve(
            id="id",
        )
        assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitudeset = client.attitudesets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.attitudesets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitudeset = response.parse()
        assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.attitudesets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitudeset = response.parse()
            assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.attitudesets.with_raw_response.retrieve(
                id="",
            )


class TestAsyncAttitudesets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitudeset = await async_client.attitudesets.retrieve(
            id="id",
        )
        assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitudeset = await async_client.attitudesets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitudesets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitudeset = await response.parse()
        assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitudesets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitudeset = await response.parse()
            assert_matches_type(AttitudesetFull, attitudeset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.attitudesets.with_raw_response.retrieve(
                id="",
            )
