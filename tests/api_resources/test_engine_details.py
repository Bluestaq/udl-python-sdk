# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import EngineDetailsFull
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngineDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )
        assert engine_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
            id="id",
            burn_time=0,
            chamber_pressure=0,
            characteristic_type="characteristicType",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cycle_type="cycleType",
            family="family",
            manufacturer_org_id="manufacturerOrgId",
            max_firings=0,
            notes="notes",
            nozzle_expansion_ratio=0,
            origin="origin",
            orig_network="origNetwork",
            oxidizer="oxidizer",
            propellant="propellant",
            sea_level_thrust=0,
            specific_impulse=0,
            tags=["string"],
            vacuum_thrust=0,
        )
        assert engine_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert engine_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.retrieve(
            "id",
        )
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.engine_details.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )
        assert engine_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
            id_2="id",
            burn_time=0,
            chamber_pressure=0,
            characteristic_type="characteristicType",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cycle_type="cycleType",
            family="family",
            manufacturer_org_id="manufacturerOrgId",
            max_firings=0,
            notes="notes",
            nozzle_expansion_ratio=0,
            origin="origin",
            orig_network="origNetwork",
            oxidizer="oxidizer",
            propellant="propellant",
            sea_level_thrust=0,
            specific_impulse=0,
            tags=["string"],
            vacuum_thrust=0,
        )
        assert engine_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert engine_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.engine_details.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_engine="idEngine",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.delete(
            "id",
        )
        assert engine_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert engine_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.engine_details.with_raw_response.delete(
                "",
            )


class TestAsyncEngineDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )
        assert engine_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
            id="id",
            burn_time=0,
            chamber_pressure=0,
            characteristic_type="characteristicType",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cycle_type="cycleType",
            family="family",
            manufacturer_org_id="manufacturerOrgId",
            max_firings=0,
            notes="notes",
            nozzle_expansion_ratio=0,
            origin="origin",
            orig_network="origNetwork",
            oxidizer="oxidizer",
            propellant="propellant",
            sea_level_thrust=0,
            specific_impulse=0,
            tags=["string"],
            vacuum_thrust=0,
        )
        assert engine_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert engine_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.retrieve(
            "id",
        )
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.engine_details.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )
        assert engine_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
            id_2="id",
            burn_time=0,
            chamber_pressure=0,
            characteristic_type="characteristicType",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cycle_type="cycleType",
            family="family",
            manufacturer_org_id="manufacturerOrgId",
            max_firings=0,
            notes="notes",
            nozzle_expansion_ratio=0,
            origin="origin",
            orig_network="origNetwork",
            oxidizer="oxidizer",
            propellant="propellant",
            sea_level_thrust=0,
            specific_impulse=0,
            tags=["string"],
            vacuum_thrust=0,
        )
        assert engine_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert engine_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_engine="idEngine",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.engine_details.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_engine="idEngine",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.delete(
            "id",
        )
        assert engine_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert engine_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.engine_details.with_raw_response.delete(
                "",
            )
