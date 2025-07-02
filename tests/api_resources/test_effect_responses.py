# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EffectResponseListResponse,
    EffectResponseTupleResponse,
    EffectResponseRetrieveResponse,
    EffectResponseQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEffectResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
        )
        assert effect_response is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
            id="EFFECTRESPONSE-ID",
            actions_list=[
                {
                    "action_actor_src_id": "ACTIONACTORSRC-ID",
                    "action_actor_src_type": "AIRCRAFT",
                    "action_end_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "action_id": "ACTION-ID",
                    "action_metrics": [
                        {
                            "domain_value": 10.1,
                            "metric_type": "GoalAchievement",
                            "provenance": "Example metric",
                            "relative_value": 10.1,
                        }
                    ],
                    "action_start_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "actor_intercept_alt": 1.1,
                    "actor_intercept_lat": 45.1,
                    "actor_intercept_lon": 180.1,
                    "effector": "SENSOR1",
                    "summary": "Example summary",
                    "target_src_id": "TARGETSRC-ID",
                    "target_src_type": "POI",
                    "tot_end_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "tot_start_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "weapon_intercept_alt": 1.1,
                    "weapon_intercept_lat": 45.1,
                    "weapon_intercept_lon": 180.1,
                }
            ],
            actor_src_id="RC-ID",
            actor_src_type="AIRCRAFT",
            coa_metrics=[
                {
                    "domain_value": 10.1,
                    "metric_type": "GoalAchievement",
                    "provenance": "Example metric",
                    "relative_value": 10.1,
                }
            ],
            collateral_damage_est=0.5,
            decision_deadline=parse_datetime("2021-01-01T00:00:00.123456Z"),
            external_actions=["ACTION1", "ACTION2"],
            external_request_id="EXTERNALREQUEST-ID",
            id_effect_request="EFFECTREQUEST-ID",
            munition_id="MUNITION-ID",
            munition_type="Dummy",
            origin="THIRD_PARTY_DATASOURCE",
            probability_of_kill=0.7,
            red_target_src_id="REDTARGETSRC-ID",
            red_target_src_type="POI",
            red_time_to_overhead=parse_datetime("2021-01-01T00:00:00.123456Z"),
            shots_required=10,
        )
        assert effect_response is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert effect_response is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert effect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.retrieve(
            id="id",
        )
        assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.effect_responses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert_matches_type(SyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert_matches_type(SyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, effect_response, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, effect_response, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert_matches_type(str, effect_response, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert_matches_type(str, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )
        assert effect_response is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert effect_response is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert effect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.query_help()
        assert_matches_type(EffectResponseQueryHelpResponse, effect_response, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert_matches_type(EffectResponseQueryHelpResponse, effect_response, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert_matches_type(EffectResponseQueryHelpResponse, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        effect_response = client.effect_responses.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )
        assert effect_response is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.effect_responses.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = response.parse()
        assert effect_response is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.effect_responses.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = response.parse()
            assert effect_response is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEffectResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
        )
        assert effect_response is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
            id="EFFECTRESPONSE-ID",
            actions_list=[
                {
                    "action_actor_src_id": "ACTIONACTORSRC-ID",
                    "action_actor_src_type": "AIRCRAFT",
                    "action_end_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "action_id": "ACTION-ID",
                    "action_metrics": [
                        {
                            "domain_value": 10.1,
                            "metric_type": "GoalAchievement",
                            "provenance": "Example metric",
                            "relative_value": 10.1,
                        }
                    ],
                    "action_start_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "actor_intercept_alt": 1.1,
                    "actor_intercept_lat": 45.1,
                    "actor_intercept_lon": 180.1,
                    "effector": "SENSOR1",
                    "summary": "Example summary",
                    "target_src_id": "TARGETSRC-ID",
                    "target_src_type": "POI",
                    "tot_end_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "tot_start_time": parse_datetime("2021-01-01T00:00:00.123456Z"),
                    "weapon_intercept_alt": 1.1,
                    "weapon_intercept_lat": 45.1,
                    "weapon_intercept_lon": 180.1,
                }
            ],
            actor_src_id="RC-ID",
            actor_src_type="AIRCRAFT",
            coa_metrics=[
                {
                    "domain_value": 10.1,
                    "metric_type": "GoalAchievement",
                    "provenance": "Example metric",
                    "relative_value": 10.1,
                }
            ],
            collateral_damage_est=0.5,
            decision_deadline=parse_datetime("2021-01-01T00:00:00.123456Z"),
            external_actions=["ACTION1", "ACTION2"],
            external_request_id="EXTERNALREQUEST-ID",
            id_effect_request="EFFECTREQUEST-ID",
            munition_id="MUNITION-ID",
            munition_type="Dummy",
            origin="THIRD_PARTY_DATASOURCE",
            probability_of_kill=0.7,
            red_target_src_id="REDTARGETSRC-ID",
            red_target_src_type="POI",
            red_time_to_overhead=parse_datetime("2021-01-01T00:00:00.123456Z"),
            shots_required=10,
        )
        assert effect_response is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert effect_response is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="COA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert effect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.retrieve(
            id="id",
        )
        assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert_matches_type(EffectResponseRetrieveResponse, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.effect_responses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert_matches_type(AsyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert_matches_type(AsyncOffsetPage[EffectResponseListResponse], effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, effect_response, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, effect_response, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert_matches_type(str, effect_response, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert_matches_type(str, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )
        assert effect_response is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert effect_response is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert effect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.query_help()
        assert_matches_type(EffectResponseQueryHelpResponse, effect_response, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert_matches_type(EffectResponseQueryHelpResponse, effect_response, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert_matches_type(EffectResponseQueryHelpResponse, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert_matches_type(EffectResponseTupleResponse, effect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        effect_response = await async_client.effect_responses.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )
        assert effect_response is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.effect_responses.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        effect_response = await response.parse()
        assert effect_response is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.effect_responses.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "COA",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            effect_response = await response.parse()
            assert effect_response is None

        assert cast(Any, response.is_closed) is True
