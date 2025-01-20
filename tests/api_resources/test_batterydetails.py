# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    BatterydetailsFull,
    BatterydetailListResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatterydetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )
        assert batterydetail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
            id="id",
            capacity=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            discharge_depth=0,
            manufacturer_org_id="manufacturerOrgId",
            model="model",
            origin="origin",
            orig_network="origNetwork",
            tags=["string"],
            technology="technology",
        )
        assert batterydetail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.batterydetails.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = response.parse()
        assert batterydetail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.batterydetails.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = response.parse()
            assert batterydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.retrieve(
            "id",
        )
        assert_matches_type(BatterydetailsFull, batterydetail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.batterydetails.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = response.parse()
        assert_matches_type(BatterydetailsFull, batterydetail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.batterydetails.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = response.parse()
            assert_matches_type(BatterydetailsFull, batterydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.batterydetails.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )
        assert batterydetail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
            id_2="id",
            capacity=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            discharge_depth=0,
            manufacturer_org_id="manufacturerOrgId",
            model="model",
            origin="origin",
            orig_network="origNetwork",
            tags=["string"],
            technology="technology",
        )
        assert batterydetail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.batterydetails.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = response.parse()
        assert batterydetail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.batterydetails.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = response.parse()
            assert batterydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.batterydetails.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_battery="idBattery",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.list()
        assert_matches_type(BatterydetailListResponse, batterydetail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.batterydetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = response.parse()
        assert_matches_type(BatterydetailListResponse, batterydetail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.batterydetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = response.parse()
            assert_matches_type(BatterydetailListResponse, batterydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        batterydetail = client.batterydetails.delete(
            "id",
        )
        assert batterydetail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.batterydetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = response.parse()
        assert batterydetail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.batterydetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = response.parse()
            assert batterydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.batterydetails.with_raw_response.delete(
                "",
            )


class TestAsyncBatterydetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )
        assert batterydetail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
            id="id",
            capacity=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            discharge_depth=0,
            manufacturer_org_id="manufacturerOrgId",
            model="model",
            origin="origin",
            orig_network="origNetwork",
            tags=["string"],
            technology="technology",
        )
        assert batterydetail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batterydetails.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = await response.parse()
        assert batterydetail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batterydetails.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = await response.parse()
            assert batterydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.retrieve(
            "id",
        )
        assert_matches_type(BatterydetailsFull, batterydetail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batterydetails.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = await response.parse()
        assert_matches_type(BatterydetailsFull, batterydetail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batterydetails.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = await response.parse()
            assert_matches_type(BatterydetailsFull, batterydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.batterydetails.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )
        assert batterydetail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
            id_2="id",
            capacity=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            discharge_depth=0,
            manufacturer_org_id="manufacturerOrgId",
            model="model",
            origin="origin",
            orig_network="origNetwork",
            tags=["string"],
            technology="technology",
        )
        assert batterydetail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batterydetails.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = await response.parse()
        assert batterydetail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batterydetails.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_battery="idBattery",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = await response.parse()
            assert batterydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.batterydetails.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_battery="idBattery",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.list()
        assert_matches_type(BatterydetailListResponse, batterydetail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batterydetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = await response.parse()
        assert_matches_type(BatterydetailListResponse, batterydetail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batterydetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = await response.parse()
            assert_matches_type(BatterydetailListResponse, batterydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        batterydetail = await async_client.batterydetails.delete(
            "id",
        )
        assert batterydetail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batterydetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batterydetail = await response.parse()
        assert batterydetail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batterydetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batterydetail = await response.parse()
            assert batterydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.batterydetails.with_raw_response.delete(
                "",
            )
