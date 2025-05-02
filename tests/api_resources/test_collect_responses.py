# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    CollectResponseAbridged,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import CollectResponseFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollectResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
        )
        assert collect_response is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
            id="COLLECTRESPONSE-ID",
            actual_end_time=parse_datetime("2018-01-01T18:00:00.123456Z"),
            actual_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            alt_end_time=parse_datetime("2018-01-01T18:00:00.123456Z"),
            alt_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            err_code="ERROR CODE",
            external_id="EXTERNAL-ID",
            id_plan="REF-PLAN-ID",
            id_sensor="REF-SENSOR-ID",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            sat_no=101,
            src_ids=["DOA_ID", "DWELL_ID"],
            src_typs=["DOA", "DWELL"],
            status="ACCEPTED",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
        )
        assert collect_response is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert collect_response is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.retrieve(
            id="id",
        )
        assert_matches_type(CollectResponseFull, collect_response, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CollectResponseFull, collect_response, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert_matches_type(CollectResponseFull, collect_response, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert_matches_type(CollectResponseFull, collect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collect_responses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert_matches_type(SyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert_matches_type(SyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, collect_response, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, collect_response, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert_matches_type(str, collect_response, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert_matches_type(str, collect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )
        assert collect_response is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert collect_response is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.query_help()
        assert collect_response is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert collect_response is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        collect_response = client.collect_responses.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )
        assert collect_response is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = response.parse()
        assert collect_response is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCollectResponses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
        )
        assert collect_response is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
            id="COLLECTRESPONSE-ID",
            actual_end_time=parse_datetime("2018-01-01T18:00:00.123456Z"),
            actual_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            alt_end_time=parse_datetime("2018-01-01T18:00:00.123456Z"),
            alt_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            err_code="ERROR CODE",
            external_id="EXTERNAL-ID",
            id_plan="REF-PLAN-ID",
            id_sensor="REF-SENSOR-ID",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            sat_no=101,
            src_ids=["DOA_ID", "DWELL_ID"],
            src_typs=["DOA", "DWELL"],
            status="ACCEPTED",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
        )
        assert collect_response is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert collect_response is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_request="REF-REQUEST-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.retrieve(
            id="id",
        )
        assert_matches_type(CollectResponseFull, collect_response, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CollectResponseFull, collect_response, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert_matches_type(CollectResponseFull, collect_response, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert_matches_type(CollectResponseFull, collect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collect_responses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert_matches_type(AsyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert_matches_type(AsyncOffsetPage[CollectResponseAbridged], collect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, collect_response, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, collect_response, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert_matches_type(str, collect_response, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert_matches_type(str, collect_response, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )
        assert collect_response is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert collect_response is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.query_help()
        assert collect_response is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert collect_response is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_response = await async_client.collect_responses.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )
        assert collect_response is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_response = await response.parse()
        assert collect_response is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_request": "REF-REQUEST-ID",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_response = await response.parse()
            assert collect_response is None

        assert cast(Any, response.is_closed) is True
