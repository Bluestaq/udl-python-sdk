# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.types.mission_ops import (
    EffectRequestListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEffectRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        effect_request = client.mission_ops.effect_requests.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
        )
        assert effect_request is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_request = client.mission_ops.effect_requests.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
            id="EFFECTREQUEST-ID",
            context="Example Notes",
            deadline_type="NoLaterThan",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            external_request_id="EXTERNALREQUEST-ID",
            metric_types=["COST", "RISK"],
            metric_weights=[0.5, 0.6],
            model_class="Preference model",
            origin="THIRD_PARTY_DATASOURCE",
            priority="LOW",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            state="CREATED",
            target_src_id="TARGETSRC-ID",
            target_src_type="POI",
        )
        assert effect_request is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.mission_ops.effect_requests.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert effect_request is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.mission_ops.effect_requests.with_streaming_response.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert effect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        effect_request = client.mission_ops.effect_requests.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(EffectRequestListResponse, effect_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.mission_ops.effect_requests.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert_matches_type(EffectRequestListResponse, effect_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.mission_ops.effect_requests.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = response.parse()
            assert_matches_type(EffectRequestListResponse, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEffectRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.mission_ops.effect_requests.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
        )
        assert effect_request is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.mission_ops.effect_requests.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
            id="EFFECTREQUEST-ID",
            context="Example Notes",
            deadline_type="NoLaterThan",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            external_request_id="EXTERNALREQUEST-ID",
            metric_types=["COST", "RISK"],
            metric_weights=[0.5, 0.6],
            model_class="Preference model",
            origin="THIRD_PARTY_DATASOURCE",
            priority="LOW",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            state="CREATED",
            target_src_id="TARGETSRC-ID",
            target_src_type="POI",
        )
        assert effect_request is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mission_ops.effect_requests.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert effect_request is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mission_ops.effect_requests.with_streaming_response.create(
            classification_marking="U",
            data_mode="REAL",
            effect_list=["COVER", "DECEIVE"],
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert effect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.mission_ops.effect_requests.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(EffectRequestListResponse, effect_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mission_ops.effect_requests.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert_matches_type(EffectRequestListResponse, effect_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mission_ops.effect_requests.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_request = await response.parse()
            assert_matches_type(EffectRequestListResponse, effect_request, path=["response"])

        assert cast(Any, response.is_closed) is True
