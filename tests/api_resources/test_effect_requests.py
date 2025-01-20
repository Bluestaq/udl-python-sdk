# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EffectRequestTupleResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.types.mission_ops import EffectRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEffectRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        effect_request = client.effect_requests.retrieve(
            "id",
        )
        assert_matches_type(EffectRequest, effect_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.effect_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert_matches_type(EffectRequest, effect_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.effect_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert_matches_type(EffectRequest, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.effect_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        effect_request = client.effect_requests.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.effect_requests.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.effect_requests.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert_matches_type(str, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        effect_request = client.effect_requests.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "effect_list": ["string"],
                    "source": "source",
                }
            ],
        )
        assert effect_request is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.effect_requests.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "effect_list": ["string"],
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert effect_request is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.effect_requests.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "effect_list": ["string"],
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert effect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history_count(self, client: Unifieddatalibrary) -> None:
        effect_request = client.effect_requests.history_count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    def test_raw_response_history_count(self, client: Unifieddatalibrary) -> None:
        response = client.effect_requests.with_raw_response.history_count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    def test_streaming_response_history_count(self, client: Unifieddatalibrary) -> None:
        with client.effect_requests.with_streaming_response.history_count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert_matches_type(str, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        effect_request = client.effect_requests.query_help()
        assert effect_request is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.effect_requests.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert effect_request is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.effect_requests.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert effect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        effect_request = client.effect_requests.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(EffectRequestTupleResponse, effect_request, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.effect_requests.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert_matches_type(EffectRequestTupleResponse, effect_request, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.effect_requests.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert_matches_type(EffectRequestTupleResponse, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEffectRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.effect_requests.retrieve(
            "id",
        )
        assert_matches_type(EffectRequest, effect_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert_matches_type(EffectRequest, effect_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert_matches_type(EffectRequest, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.effect_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.effect_requests.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_requests.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_requests.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert_matches_type(str, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.effect_requests.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "effect_list": ["string"],
                    "source": "source",
                }
            ],
        )
        assert effect_request is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_requests.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "effect_list": ["string"],
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert effect_request is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_requests.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "effect_list": ["string"],
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert effect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.effect_requests.history_count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    async def test_raw_response_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_requests.with_raw_response.history_count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert_matches_type(str, effect_request, path=["response"])

    @parametrize
    async def test_streaming_response_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_requests.with_streaming_response.history_count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert_matches_type(str, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.effect_requests.query_help()
        assert effect_request is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_requests.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert effect_request is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_requests.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert effect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.effect_requests.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(EffectRequestTupleResponse, effect_request, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_requests.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert_matches_type(EffectRequestTupleResponse, effect_request, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_requests.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert_matches_type(EffectRequestTupleResponse, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True
