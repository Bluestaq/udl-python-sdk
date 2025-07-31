# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbitthrusterstatusListResponse,
    OnorbitthrusterstatusTupleResponse,
    OnorbitthrusterstatusQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import OnorbitthrusterstatusFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbitthrusterstatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
        )
        assert onorbitthrusterstatus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            id="af103c-1f917dc-002c1bd",
            est_delta_v=10.1,
            fuel_mass=100.1,
            fuel_mass_unc=10.1,
            isp=300.1,
            max_delta_v=100.1,
            min_delta_v=0.1,
            name="REA1",
            operational=True,
            origin="THIRD_PARTY_DATASOURCE",
            prop_mass_avg=907.6,
            prop_mass_max=2333.3,
            prop_mass_median=200.1,
            prop_mass_min=0.1,
            thrust_max=22.1,
            total_delta_v=100.1,
        )
        assert onorbitthrusterstatus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert onorbitthrusterstatus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert onorbitthrusterstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.list()
        assert_matches_type(SyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.list(
            first_result=0,
            id_onorbit_thruster="idOnorbitThruster",
            max_results=0,
            status_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert_matches_type(
                SyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.delete(
            "id",
        )
        assert onorbitthrusterstatus is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert onorbitthrusterstatus is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert onorbitthrusterstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitthrusterstatus.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.count()
        assert_matches_type(str, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.count(
            first_result=0,
            id_onorbit_thruster="idOnorbitThruster",
            max_results=0,
            status_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert_matches_type(str, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert_matches_type(str, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_onorbit_thruster": "ff7dc909-e8b4-4a54-8529-1963d4e9b353",
                    "source": "Bluestaq",
                    "status_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
        )
        assert onorbitthrusterstatus is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_onorbit_thruster": "ff7dc909-e8b4-4a54-8529-1963d4e9b353",
                    "source": "Bluestaq",
                    "status_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert onorbitthrusterstatus is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_onorbit_thruster": "ff7dc909-e8b4-4a54-8529-1963d4e9b353",
                    "source": "Bluestaq",
                    "status_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert onorbitthrusterstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.get(
            id="id",
        )
        assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitthrusterstatus.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.queryhelp()
        assert_matches_type(OnorbitthrusterstatusQueryhelpResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert_matches_type(OnorbitthrusterstatusQueryhelpResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert_matches_type(OnorbitthrusterstatusQueryhelpResponse, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitthrusterstatus = client.onorbitthrusterstatus.tuple(
            columns="columns",
            first_result=0,
            id_onorbit_thruster="idOnorbitThruster",
            max_results=0,
            status_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitthrusterstatus.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = response.parse()
        assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.onorbitthrusterstatus.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = response.parse()
            assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnorbitthrusterstatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
        )
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            id="af103c-1f917dc-002c1bd",
            est_delta_v=10.1,
            fuel_mass=100.1,
            fuel_mass_unc=10.1,
            isp=300.1,
            max_delta_v=100.1,
            min_delta_v=0.1,
            name="REA1",
            operational=True,
            origin="THIRD_PARTY_DATASOURCE",
            prop_mass_avg=907.6,
            prop_mass_max=2333.3,
            prop_mass_median=200.1,
            prop_mass_min=0.1,
            thrust_max=22.1,
            total_delta_v=100.1,
        )
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_onorbit_thruster="ff7dc909-e8b4-4a54-8529-1963d4e9b353",
            source="Bluestaq",
            status_time=parse_datetime("2024-01-01T16:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert onorbitthrusterstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.list()
        assert_matches_type(
            AsyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.list(
            first_result=0,
            id_onorbit_thruster="idOnorbitThruster",
            max_results=0,
            status_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            AsyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[OnorbitthrusterstatusListResponse], onorbitthrusterstatus, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.delete(
            "id",
        )
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert onorbitthrusterstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitthrusterstatus.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.count()
        assert_matches_type(str, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.count(
            first_result=0,
            id_onorbit_thruster="idOnorbitThruster",
            max_results=0,
            status_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert_matches_type(str, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert_matches_type(str, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_onorbit_thruster": "ff7dc909-e8b4-4a54-8529-1963d4e9b353",
                    "source": "Bluestaq",
                    "status_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
        )
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_onorbit_thruster": "ff7dc909-e8b4-4a54-8529-1963d4e9b353",
                    "source": "Bluestaq",
                    "status_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert onorbitthrusterstatus is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_onorbit_thruster": "ff7dc909-e8b4-4a54-8529-1963d4e9b353",
                    "source": "Bluestaq",
                    "status_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert onorbitthrusterstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.get(
            id="id",
        )
        assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert_matches_type(OnorbitthrusterstatusFull, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitthrusterstatus.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.queryhelp()
        assert_matches_type(OnorbitthrusterstatusQueryhelpResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert_matches_type(OnorbitthrusterstatusQueryhelpResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert_matches_type(OnorbitthrusterstatusQueryhelpResponse, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitthrusterstatus = await async_client.onorbitthrusterstatus.tuple(
            columns="columns",
            first_result=0,
            id_onorbit_thruster="idOnorbitThruster",
            max_results=0,
            status_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitthrusterstatus.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitthrusterstatus = await response.parse()
        assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitthrusterstatus.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitthrusterstatus = await response.parse()
            assert_matches_type(OnorbitthrusterstatusTupleResponse, onorbitthrusterstatus, path=["response"])

        assert cast(Any, response.is_closed) is True
