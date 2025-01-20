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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
        )
        assert effect_request is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_request = client.mission_ops.effect_requests.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
            id="id",
            context="context",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            deadline_type="deadlineType",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_request_id="externalRequestId",
            metric_types=["string"],
            metric_weights=[0],
            model_class="modelClass",
            origin="origin",
            orig_network="origNetwork",
            priority="priority",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            state="state",
            target_src_id="targetSrcId",
            target_src_type="targetSrcType",
        )
        assert effect_request is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.mission_ops.effect_requests.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = response.parse()
        assert effect_request is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.mission_ops.effect_requests.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
        )
        assert effect_request is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_request = await async_client.mission_ops.effect_requests.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
            id="id",
            context="context",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            deadline_type="deadlineType",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_request_id="externalRequestId",
            metric_types=["string"],
            metric_weights=[0],
            model_class="modelClass",
            origin="origin",
            orig_network="origNetwork",
            priority="priority",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            state="state",
            target_src_id="targetSrcId",
            target_src_type="targetSrcType",
        )
        assert effect_request is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mission_ops.effect_requests.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_request = await response.parse()
        assert effect_request is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mission_ops.effect_requests.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            effect_list=["string"],
            source="source",
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
