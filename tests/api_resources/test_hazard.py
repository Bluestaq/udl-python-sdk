# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    HazardGetResponse,
    HazardListResponse,
    HazardTupleResponse,
    HazardQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHazard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
        )
        assert hazard is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
            id="HAZARD-ID",
            a=238,
            activity=120.1,
            bottle_id="6264",
            cas_rn="64-17-5",
            channel="Skin",
            ctrn_time=1.077,
            density=18900.2,
            dep=1.084,
            dep_ctrn=86.1,
            dose=1.12,
            dose_rate=1.0000001865,
            duration=14400,
            g_bar=2.5,
            harmful=False,
            h_bar=3.1,
            id_poi="POI-ID",
            id_track="TRACK-ID",
            mass_frac=0.029,
            mat_cat=3,
            mat_class="Nerve Agent",
            mat_name="VX",
            mat_type="21",
            origin="THIRD_PARTY_DATASOURCE",
            ppm=27129,
            rad_ctrn=1.31,
            readings=["Rad1", "Rad2"],
            reading_units=["Gray", "Gray"],
            reading_values=[107.2, 124.1],
            z=92,
        )
        assert hazard is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert hazard is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert hazard is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[HazardListResponse], hazard, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[HazardListResponse], hazard, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert_matches_type(SyncOffsetPage[HazardListResponse], hazard, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert_matches_type(SyncOffsetPage[HazardListResponse], hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, hazard, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, hazard, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert_matches_type(str, hazard, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert_matches_type(str, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.create_bulk(
            body=[
                {
                    "alarms": ["Alarm1", "Alarm2"],
                    "alarm_values": [2.7, 2.9],
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "detect_time": parse_datetime("2022-03-07T14:51:39.653Z"),
                    "detect_type": "Chemical",
                    "source": "Bluestaq",
                }
            ],
        )
        assert hazard is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.create_bulk(
            body=[
                {
                    "alarms": ["Alarm1", "Alarm2"],
                    "alarm_values": [2.7, 2.9],
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "detect_time": parse_datetime("2022-03-07T14:51:39.653Z"),
                    "detect_type": "Chemical",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert hazard is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.create_bulk(
            body=[
                {
                    "alarms": ["Alarm1", "Alarm2"],
                    "alarm_values": [2.7, 2.9],
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "detect_time": parse_datetime("2022-03-07T14:51:39.653Z"),
                    "detect_type": "Chemical",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert hazard is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.get(
            id="id",
        )
        assert_matches_type(HazardGetResponse, hazard, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HazardGetResponse, hazard, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert_matches_type(HazardGetResponse, hazard, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert_matches_type(HazardGetResponse, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.hazard.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.queryhelp()
        assert_matches_type(HazardQueryhelpResponse, hazard, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert_matches_type(HazardQueryhelpResponse, hazard, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert_matches_type(HazardQueryhelpResponse, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(HazardTupleResponse, hazard, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        hazard = client.hazard.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HazardTupleResponse, hazard, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.hazard.with_raw_response.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = response.parse()
        assert_matches_type(HazardTupleResponse, hazard, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.hazard.with_streaming_response.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = response.parse()
            assert_matches_type(HazardTupleResponse, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHazard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
        )
        assert hazard is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
            id="HAZARD-ID",
            a=238,
            activity=120.1,
            bottle_id="6264",
            cas_rn="64-17-5",
            channel="Skin",
            ctrn_time=1.077,
            density=18900.2,
            dep=1.084,
            dep_ctrn=86.1,
            dose=1.12,
            dose_rate=1.0000001865,
            duration=14400,
            g_bar=2.5,
            harmful=False,
            h_bar=3.1,
            id_poi="POI-ID",
            id_track="TRACK-ID",
            mass_frac=0.029,
            mat_cat=3,
            mat_class="Nerve Agent",
            mat_name="VX",
            mat_type="21",
            origin="THIRD_PARTY_DATASOURCE",
            ppm=27129,
            rad_ctrn=1.31,
            readings=["Rad1", "Rad2"],
            reading_units=["Gray", "Gray"],
            reading_values=[107.2, 124.1],
            z=92,
        )
        assert hazard is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert hazard is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.create(
            alarms=["Alarm1", "Alarm2"],
            alarm_values=[2.7, 2.9],
            classification_marking="U",
            data_mode="TEST",
            detect_time=parse_datetime("2022-03-07T14:51:39.653Z"),
            detect_type="Chemical",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert hazard is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[HazardListResponse], hazard, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[HazardListResponse], hazard, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert_matches_type(AsyncOffsetPage[HazardListResponse], hazard, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.list(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert_matches_type(AsyncOffsetPage[HazardListResponse], hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, hazard, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, hazard, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert_matches_type(str, hazard, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.count(
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert_matches_type(str, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.create_bulk(
            body=[
                {
                    "alarms": ["Alarm1", "Alarm2"],
                    "alarm_values": [2.7, 2.9],
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "detect_time": parse_datetime("2022-03-07T14:51:39.653Z"),
                    "detect_type": "Chemical",
                    "source": "Bluestaq",
                }
            ],
        )
        assert hazard is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.create_bulk(
            body=[
                {
                    "alarms": ["Alarm1", "Alarm2"],
                    "alarm_values": [2.7, 2.9],
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "detect_time": parse_datetime("2022-03-07T14:51:39.653Z"),
                    "detect_type": "Chemical",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert hazard is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.create_bulk(
            body=[
                {
                    "alarms": ["Alarm1", "Alarm2"],
                    "alarm_values": [2.7, 2.9],
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "detect_time": parse_datetime("2022-03-07T14:51:39.653Z"),
                    "detect_type": "Chemical",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert hazard is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.get(
            id="id",
        )
        assert_matches_type(HazardGetResponse, hazard, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HazardGetResponse, hazard, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert_matches_type(HazardGetResponse, hazard, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert_matches_type(HazardGetResponse, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.hazard.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.queryhelp()
        assert_matches_type(HazardQueryhelpResponse, hazard, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert_matches_type(HazardQueryhelpResponse, hazard, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert_matches_type(HazardQueryhelpResponse, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(HazardTupleResponse, hazard, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        hazard = await async_client.hazard.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HazardTupleResponse, hazard, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.hazard.with_raw_response.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hazard = await response.parse()
        assert_matches_type(HazardTupleResponse, hazard, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.hazard.with_streaming_response.tuple(
            columns="columns",
            detect_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hazard = await response.parse()
            assert_matches_type(HazardTupleResponse, hazard, path=["response"])

        assert cast(Any, response.is_closed) is True
