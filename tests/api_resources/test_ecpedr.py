# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EcpedrListResponse,
    EcpedrTupleResponse,
    EcpedrQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEcpedr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
        )
        assert ecpedr is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                    "chan_energy_high": 0.003495,
                    "chan_energy_low": 58.4,
                    "chan_id": "H05E",
                    "chan_type": "INTEGRAL",
                    "chan_unit": "keV",
                    "msg_number": 21,
                    "ob_value": 31473.9,
                    "species": "ELECTRON",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            gen_system="cpuch2.aero.org",
            gen_time=parse_datetime("2025-03-13T18:00:00.123Z"),
            id_sensor="REACH-101",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="WSF-M SV1",
            orig_sensor_id="CEASE-3",
            sat_no=101,
            sen_pos=[5893.74, 1408.8, 3899.38],
            sen_reference_frame="TEME",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert ecpedr is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert ecpedr is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert ecpedr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert_matches_type(SyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert_matches_type(SyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ecpedr, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ecpedr, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert_matches_type(str, ecpedr, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert_matches_type(str, ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert ecpedr is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert ecpedr is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert ecpedr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.queryhelp()
        assert_matches_type(EcpedrQueryhelpResponse, ecpedr, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert_matches_type(EcpedrQueryhelpResponse, ecpedr, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert_matches_type(EcpedrQueryhelpResponse, ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        ecpedr = client.ecpedr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert ecpedr is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.ecpedr.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = response.parse()
        assert ecpedr is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.ecpedr.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = response.parse()
            assert ecpedr is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEcpedr:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
        )
        assert ecpedr is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                    "chan_energy_high": 0.003495,
                    "chan_energy_low": 58.4,
                    "chan_id": "H05E",
                    "chan_type": "INTEGRAL",
                    "chan_unit": "keV",
                    "msg_number": 21,
                    "ob_value": 31473.9,
                    "species": "ELECTRON",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            gen_system="cpuch2.aero.org",
            gen_time=parse_datetime("2025-03-13T18:00:00.123Z"),
            id_sensor="REACH-101",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="WSF-M SV1",
            orig_sensor_id="CEASE-3",
            sat_no=101,
            sen_pos=[5893.74, 1408.8, 3899.38],
            sen_reference_frame="TEME",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert ecpedr is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert ecpedr is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ecpedr_measurements=[
                {
                    "ob_type": "FLUX",
                    "ob_uo_m": "#/MeV/cm^2/sr/s",
                }
            ],
            ob_time=parse_datetime("2025-03-13T17:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert ecpedr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert_matches_type(AsyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert_matches_type(AsyncOffsetPage[EcpedrListResponse], ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ecpedr, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ecpedr, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert_matches_type(str, ecpedr, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert_matches_type(str, ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert ecpedr is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert ecpedr is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert ecpedr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.queryhelp()
        assert_matches_type(EcpedrQueryhelpResponse, ecpedr, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert_matches_type(EcpedrQueryhelpResponse, ecpedr, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert_matches_type(EcpedrQueryhelpResponse, ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert_matches_type(EcpedrTupleResponse, ecpedr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpedr = await async_client.ecpedr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert ecpedr is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpedr.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpedr = await response.parse()
        assert ecpedr is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpedr.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ecpedr_measurements": [
                        {
                            "ob_type": "FLUX",
                            "ob_uo_m": "#/MeV/cm^2/sr/s",
                        }
                    ],
                    "ob_time": parse_datetime("2025-03-13T17:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpedr = await response.parse()
            assert ecpedr is None

        assert cast(Any, response.is_closed) is True
