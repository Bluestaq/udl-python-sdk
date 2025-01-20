# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirfieldstatusFull,
    AirfieldStatusTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfieldStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airfield_status = client.airfield_status.retrieve(
            "id",
        )
        assert_matches_type(AirfieldstatusFull, airfield_status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_status.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = response.parse()
        assert_matches_type(AirfieldstatusFull, airfield_status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airfield_status.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = response.parse()
            assert_matches_type(AirfieldstatusFull, airfield_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfield_status.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        airfield_status = client.airfield_status.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )
        assert airfield_status is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_status = client.airfield_status.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
            id_2="id",
            alt_airfield_id="altAirfieldId",
            arff_cat="arffCat",
            cargo_mog=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            fleet_service_mog=0,
            fuel_mog=0,
            fuel_qtys=[0],
            fuel_types=["string"],
            gse_time=0,
            med_cap="medCap",
            message="message",
            mhe_qtys=[0],
            mhe_types=["string"],
            mx_mog=0,
            narrow_parking_mog=0,
            narrow_working_mog=0,
            num_cog=0,
            operating_mog=0,
            origin="origin",
            orig_network="origNetwork",
            passenger_service_mog=0,
            pri_freq=0,
            pri_rwy_num="priRwyNum",
            rwy_cond_reading=0,
            rwy_friction_factor=0,
            rwy_markings=["string"],
            slot_types_req=["string"],
            source_dl="sourceDL",
            wide_parking_mog=0,
            wide_working_mog=0,
        )
        assert airfield_status is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_status.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = response.parse()
        assert airfield_status is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.airfield_status.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = response.parse()
            assert airfield_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.airfield_status.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_airfield="idAirfield",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        airfield_status = client.airfield_status.delete(
            "id",
        )
        assert airfield_status is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_status.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = response.parse()
        assert airfield_status is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.airfield_status.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = response.parse()
            assert airfield_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfield_status.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        airfield_status = client.airfield_status.tuple(
            columns="columns",
        )
        assert_matches_type(AirfieldStatusTupleResponse, airfield_status, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_status.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = response.parse()
        assert_matches_type(AirfieldStatusTupleResponse, airfield_status, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.airfield_status.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = response.parse()
            assert_matches_type(AirfieldStatusTupleResponse, airfield_status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirfieldStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_status = await async_client.airfield_status.retrieve(
            "id",
        )
        assert_matches_type(AirfieldstatusFull, airfield_status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_status.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = await response.parse()
        assert_matches_type(AirfieldstatusFull, airfield_status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_status.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = await response.parse()
            assert_matches_type(AirfieldstatusFull, airfield_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfield_status.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_status = await async_client.airfield_status.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )
        assert airfield_status is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_status = await async_client.airfield_status.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
            id_2="id",
            alt_airfield_id="altAirfieldId",
            arff_cat="arffCat",
            cargo_mog=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            fleet_service_mog=0,
            fuel_mog=0,
            fuel_qtys=[0],
            fuel_types=["string"],
            gse_time=0,
            med_cap="medCap",
            message="message",
            mhe_qtys=[0],
            mhe_types=["string"],
            mx_mog=0,
            narrow_parking_mog=0,
            narrow_working_mog=0,
            num_cog=0,
            operating_mog=0,
            origin="origin",
            orig_network="origNetwork",
            passenger_service_mog=0,
            pri_freq=0,
            pri_rwy_num="priRwyNum",
            rwy_cond_reading=0,
            rwy_friction_factor=0,
            rwy_markings=["string"],
            slot_types_req=["string"],
            source_dl="sourceDL",
            wide_parking_mog=0,
            wide_working_mog=0,
        )
        assert airfield_status is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_status.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = await response.parse()
        assert airfield_status is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_status.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = await response.parse()
            assert airfield_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.airfield_status.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_airfield="idAirfield",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_status = await async_client.airfield_status.delete(
            "id",
        )
        assert airfield_status is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_status.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = await response.parse()
        assert airfield_status is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_status.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = await response.parse()
            assert airfield_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfield_status.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_status = await async_client.airfield_status.tuple(
            columns="columns",
        )
        assert_matches_type(AirfieldStatusTupleResponse, airfield_status, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_status.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_status = await response.parse()
        assert_matches_type(AirfieldStatusTupleResponse, airfield_status, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_status.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_status = await response.parse()
            assert_matches_type(AirfieldStatusTupleResponse, airfield_status, path=["response"])

        assert cast(Any, response.is_closed) is True
