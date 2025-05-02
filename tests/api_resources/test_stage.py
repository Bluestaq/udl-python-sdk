# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    StageGetResponse,
    StageListResponse,
    StageTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert stage is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            id="STAGE-ID",
            avionics_notes="Sample Notes",
            burn_time=256.3,
            control_thruster1="controlThruster1",
            control_thruster2="controlThruster2",
            diameter=3.95,
            length=25.13,
            main_engine_thrust_sea_level=733.4,
            main_engine_thrust_vacuum=733.4,
            manufacturer_org_id="5feed5d7-d131-57e5-a3fd-acc173bca736",
            mass=9956.1,
            notes="Sample Notes",
            num_burns=1,
            num_control_thruster1=1,
            num_control_thruster2=1,
            num_engines=1,
            num_stage_elements=2,
            num_vernier=3,
            origin="THIRD_PARTY_DATASOURCE",
            photo_urls=["photoURL"],
            restartable=True,
            reusable=True,
            stage_number=2,
            tags=["TAG1", "TAG2"],
            thrust_sea_level=733.4,
            thrust_vacuum=733.4,
            type="Electrostatic Ion",
            vernier="vernier",
            vernier_burn_time=1.1,
            vernier_num_burns=4,
            vernier_thrust_sea_level=4.1,
            vernier_thrust_vacuum=3.2,
        )
        assert stage is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert stage is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert stage is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            body_id="STAGE-ID",
            avionics_notes="Sample Notes",
            burn_time=256.3,
            control_thruster1="controlThruster1",
            control_thruster2="controlThruster2",
            diameter=3.95,
            length=25.13,
            main_engine_thrust_sea_level=733.4,
            main_engine_thrust_vacuum=733.4,
            manufacturer_org_id="5feed5d7-d131-57e5-a3fd-acc173bca736",
            mass=9956.1,
            notes="Sample Notes",
            num_burns=1,
            num_control_thruster1=1,
            num_control_thruster2=1,
            num_engines=1,
            num_stage_elements=2,
            num_vernier=3,
            origin="THIRD_PARTY_DATASOURCE",
            photo_urls=["photoURL"],
            restartable=True,
            reusable=True,
            stage_number=2,
            tags=["TAG1", "TAG2"],
            thrust_sea_level=733.4,
            thrust_vacuum=733.4,
            type="Electrostatic Ion",
            vernier="vernier",
            vernier_burn_time=1.1,
            vernier_num_burns=4,
            vernier_thrust_sea_level=4.1,
            vernier_thrust_vacuum=3.2,
        )
        assert stage is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert stage is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.stage.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_engine="ENGINE-ID",
                id_launch_vehicle="LAUNCHVEHICLE-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.list()
        assert_matches_type(SyncOffsetPage[StageListResponse], stage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[StageListResponse], stage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert_matches_type(SyncOffsetPage[StageListResponse], stage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert_matches_type(SyncOffsetPage[StageListResponse], stage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.delete(
            "id",
        )
        assert stage is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert stage is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stage.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.count()
        assert_matches_type(str, stage, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, stage, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert_matches_type(str, stage, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert_matches_type(str, stage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.get(
            id="id",
        )
        assert_matches_type(StageGetResponse, stage, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StageGetResponse, stage, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert_matches_type(StageGetResponse, stage, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert_matches_type(StageGetResponse, stage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stage.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.queryhelp()
        assert stage is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert stage is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.tuple(
            columns="columns",
        )
        assert_matches_type(StageTupleResponse, stage, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        stage = client.stage.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StageTupleResponse, stage, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.stage.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = response.parse()
        assert_matches_type(StageTupleResponse, stage, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.stage.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = response.parse()
            assert_matches_type(StageTupleResponse, stage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert stage is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            id="STAGE-ID",
            avionics_notes="Sample Notes",
            burn_time=256.3,
            control_thruster1="controlThruster1",
            control_thruster2="controlThruster2",
            diameter=3.95,
            length=25.13,
            main_engine_thrust_sea_level=733.4,
            main_engine_thrust_vacuum=733.4,
            manufacturer_org_id="5feed5d7-d131-57e5-a3fd-acc173bca736",
            mass=9956.1,
            notes="Sample Notes",
            num_burns=1,
            num_control_thruster1=1,
            num_control_thruster2=1,
            num_engines=1,
            num_stage_elements=2,
            num_vernier=3,
            origin="THIRD_PARTY_DATASOURCE",
            photo_urls=["photoURL"],
            restartable=True,
            reusable=True,
            stage_number=2,
            tags=["TAG1", "TAG2"],
            thrust_sea_level=733.4,
            thrust_vacuum=733.4,
            type="Electrostatic Ion",
            vernier="vernier",
            vernier_burn_time=1.1,
            vernier_num_burns=4,
            vernier_thrust_sea_level=4.1,
            vernier_thrust_vacuum=3.2,
        )
        assert stage is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert stage is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert stage is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            body_id="STAGE-ID",
            avionics_notes="Sample Notes",
            burn_time=256.3,
            control_thruster1="controlThruster1",
            control_thruster2="controlThruster2",
            diameter=3.95,
            length=25.13,
            main_engine_thrust_sea_level=733.4,
            main_engine_thrust_vacuum=733.4,
            manufacturer_org_id="5feed5d7-d131-57e5-a3fd-acc173bca736",
            mass=9956.1,
            notes="Sample Notes",
            num_burns=1,
            num_control_thruster1=1,
            num_control_thruster2=1,
            num_engines=1,
            num_stage_elements=2,
            num_vernier=3,
            origin="THIRD_PARTY_DATASOURCE",
            photo_urls=["photoURL"],
            restartable=True,
            reusable=True,
            stage_number=2,
            tags=["TAG1", "TAG2"],
            thrust_sea_level=733.4,
            thrust_vacuum=733.4,
            type="Electrostatic Ion",
            vernier="vernier",
            vernier_burn_time=1.1,
            vernier_num_burns=4,
            vernier_thrust_sea_level=4.1,
            vernier_thrust_vacuum=3.2,
        )
        assert stage is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert stage is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.stage.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_engine="ENGINE-ID",
                id_launch_vehicle="LAUNCHVEHICLE-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.list()
        assert_matches_type(AsyncOffsetPage[StageListResponse], stage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[StageListResponse], stage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert_matches_type(AsyncOffsetPage[StageListResponse], stage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert_matches_type(AsyncOffsetPage[StageListResponse], stage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.delete(
            "id",
        )
        assert stage is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert stage is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stage.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.count()
        assert_matches_type(str, stage, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, stage, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert_matches_type(str, stage, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert_matches_type(str, stage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.get(
            id="id",
        )
        assert_matches_type(StageGetResponse, stage, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StageGetResponse, stage, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert_matches_type(StageGetResponse, stage, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert_matches_type(StageGetResponse, stage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stage.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.queryhelp()
        assert stage is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert stage is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert stage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.tuple(
            columns="columns",
        )
        assert_matches_type(StageTupleResponse, stage, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        stage = await async_client.stage.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StageTupleResponse, stage, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.stage.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stage = await response.parse()
        assert_matches_type(StageTupleResponse, stage, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.stage.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stage = await response.parse()
            assert_matches_type(StageTupleResponse, stage, path=["response"])

        assert cast(Any, response.is_closed) is True
