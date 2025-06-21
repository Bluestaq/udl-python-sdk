# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaunchVehicleGetResponse,
    LaunchVehicleListResponse,
    LaunchVehicleTupleResponse,
    LaunchVehicleQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchVehicle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )
        assert launch_vehicle is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
            id="LAUNCHVEHICLE-ID",
            origin="THIRD_PARTY_DATASOURCE",
            type="Example-vehicle-type",
        )
        assert launch_vehicle is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert launch_vehicle is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert launch_vehicle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )
        assert launch_vehicle is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
            body_id="LAUNCHVEHICLE-ID",
            origin="THIRD_PARTY_DATASOURCE",
            type="Example-vehicle-type",
        )
        assert launch_vehicle is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert launch_vehicle is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert launch_vehicle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.launch_vehicle.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example-name",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.list()
        assert_matches_type(SyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert_matches_type(SyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert_matches_type(SyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.delete(
            "id",
        )
        assert launch_vehicle is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert launch_vehicle is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert launch_vehicle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_vehicle.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.count()
        assert_matches_type(str, launch_vehicle, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, launch_vehicle, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert_matches_type(str, launch_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert_matches_type(str, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.get(
            id="id",
        )
        assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_vehicle.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.queryhelp()
        assert_matches_type(LaunchVehicleQueryhelpResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert_matches_type(LaunchVehicleQueryhelpResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert_matches_type(LaunchVehicleQueryhelpResponse, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.tuple(
            columns="columns",
        )
        assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle = client.launch_vehicle.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = response.parse()
        assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = response.parse()
            assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLaunchVehicle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )
        assert launch_vehicle is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
            id="LAUNCHVEHICLE-ID",
            origin="THIRD_PARTY_DATASOURCE",
            type="Example-vehicle-type",
        )
        assert launch_vehicle is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert launch_vehicle is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert launch_vehicle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )
        assert launch_vehicle is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
            body_id="LAUNCHVEHICLE-ID",
            origin="THIRD_PARTY_DATASOURCE",
            type="Example-vehicle-type",
        )
        assert launch_vehicle is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert launch_vehicle is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example-name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert launch_vehicle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.launch_vehicle.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example-name",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.list()
        assert_matches_type(AsyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert_matches_type(AsyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert_matches_type(AsyncOffsetPage[LaunchVehicleListResponse], launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.delete(
            "id",
        )
        assert launch_vehicle is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert launch_vehicle is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert launch_vehicle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_vehicle.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.count()
        assert_matches_type(str, launch_vehicle, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, launch_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert_matches_type(str, launch_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert_matches_type(str, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.get(
            id="id",
        )
        assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert_matches_type(LaunchVehicleGetResponse, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_vehicle.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.queryhelp()
        assert_matches_type(LaunchVehicleQueryhelpResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert_matches_type(LaunchVehicleQueryhelpResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert_matches_type(LaunchVehicleQueryhelpResponse, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.tuple(
            columns="columns",
        )
        assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle = await async_client.launch_vehicle.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle = await response.parse()
        assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle = await response.parse()
            assert_matches_type(LaunchVehicleTupleResponse, launch_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True
