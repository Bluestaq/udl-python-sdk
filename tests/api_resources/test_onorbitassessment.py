# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbitassessmentGetResponse,
    OnorbitassessmentListResponse,
    OnorbitassessmentTupleResponse,
    OnorbitassessmentQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbitassessment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert onorbitassessment is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            assessment="NOMINAL",
            assmt_details="This spacecraft appears to be in a stable, 3-axis controlled state",
            assmt_level="SIGNATURE",
            assmt_rot_period=72.5,
            assmt_sub_type="STABLE",
            assmt_url="https://unifieddatalibrary.com",
            auto_assmt=False,
            collection_url="https://unifieddatalibrary.com",
            components=["THRUSTER", "RWA-2"],
            id_on_orbit="25544",
            id_sensor="211",
            ob_duration=1.75,
            ob_time=parse_datetime("2025-08-09T23:27:55.862Z"),
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ISS",
            orig_sensor_id="ORIGSENSOR-ID",
            sat_no=25544,
            sig_data_type="PHOTOMETRY",
            src_ids=["49cf9dcf-e97e-43ed-8e21-22e2bb0e3da6", "da779fc4-3a37-4caa-a629-289671bc96e8"],
            src_typs=["EO", "SKYIMAGE"],
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert onorbitassessment is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert onorbitassessment is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert onorbitassessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert_matches_type(SyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, onorbitassessment, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbitassessment, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert_matches_type(str, onorbitassessment, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert_matches_type(str, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.create_bulk(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert onorbitassessment is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.create_bulk(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert onorbitassessment is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.create_bulk(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert onorbitassessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.get(
            id="id",
        )
        assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitassessment.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.queryhelp()
        assert_matches_type(OnorbitassessmentQueryhelpResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert_matches_type(OnorbitassessmentQueryhelpResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert_matches_type(OnorbitassessmentQueryhelpResponse, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        onorbitassessment = client.onorbitassessment.unvalidated_publish(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert onorbitassessment is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitassessment.with_raw_response.unvalidated_publish(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = response.parse()
        assert onorbitassessment is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.onorbitassessment.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = response.parse()
            assert onorbitassessment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOnorbitassessment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert onorbitassessment is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            assessment="NOMINAL",
            assmt_details="This spacecraft appears to be in a stable, 3-axis controlled state",
            assmt_level="SIGNATURE",
            assmt_rot_period=72.5,
            assmt_sub_type="STABLE",
            assmt_url="https://unifieddatalibrary.com",
            auto_assmt=False,
            collection_url="https://unifieddatalibrary.com",
            components=["THRUSTER", "RWA-2"],
            id_on_orbit="25544",
            id_sensor="211",
            ob_duration=1.75,
            ob_time=parse_datetime("2025-08-09T23:27:55.862Z"),
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ISS",
            orig_sensor_id="ORIGSENSOR-ID",
            sat_no=25544,
            sig_data_type="PHOTOMETRY",
            src_ids=["49cf9dcf-e97e-43ed-8e21-22e2bb0e3da6", "da779fc4-3a37-4caa-a629-289671bc96e8"],
            src_typs=["EO", "SKYIMAGE"],
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert onorbitassessment is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert onorbitassessment is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.create(
            assmt_time=parse_datetime("2025-08-10T02:44:02.000Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert onorbitassessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert_matches_type(AsyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.list(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert_matches_type(AsyncOffsetPage[OnorbitassessmentListResponse], onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, onorbitassessment, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbitassessment, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert_matches_type(str, onorbitassessment, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.count(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert_matches_type(str, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.create_bulk(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert onorbitassessment is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.create_bulk(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert onorbitassessment is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.create_bulk(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert onorbitassessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.get(
            id="id",
        )
        assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert_matches_type(OnorbitassessmentGetResponse, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitassessment.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.queryhelp()
        assert_matches_type(OnorbitassessmentQueryhelpResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert_matches_type(OnorbitassessmentQueryhelpResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert_matches_type(OnorbitassessmentQueryhelpResponse, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.tuple(
            assmt_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert_matches_type(OnorbitassessmentTupleResponse, onorbitassessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitassessment = await async_client.onorbitassessment.unvalidated_publish(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert onorbitassessment is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitassessment.with_raw_response.unvalidated_publish(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitassessment = await response.parse()
        assert onorbitassessment is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitassessment.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "assmt_time": parse_datetime("2025-08-10T02:44:02.000Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitassessment = await response.parse()
            assert onorbitassessment is None

        assert cast(Any, response.is_closed) is True
