# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirfieldslotconsumptionFull,
    AirfieldslotconsumptionAbridged,
    AirfieldSlotConsumptionTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfieldSlotConsumptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_arr_sortie_id="ALT-SORTIE-ID",
            alt_dep_sortie_id="ALT-SORTIE-ID",
            app_comment="The request was denied due to inoperable fuel pumps.",
            app_initials="CB",
            app_org="KCHS/BOPS",
            call_signs=["RCH123", "ABC123", "LLS442"],
            consumer="APRON1-230401001",
            end_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            id_arr_sortie="be831d39-1822-da9f-7ace-6cc5643397dc",
            id_dep_sortie="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            mission_id="AJM123456123",
            occ_aircraft_mds="C017A",
            occ_start_time=parse_datetime("2023-01-01T01:01:03.123Z"),
            occ_tail_number="N702JG",
            occupied=True,
            origin="THIRD_PARTY_DATASOURCE",
            req_comment="Sorry for the late notice.",
            req_initials="CB",
            req_org="TACC",
            res_aircraft_mds="C017A",
            res_mission_id="AJM123456123",
            res_reason="Maintenance needed",
            res_tail_number="N702JG",
            res_type="M",
            status="APPROVED",
            target_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.retrieve(
            id="id",
        )
        assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfield_slot_consumptions.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            body_id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_arr_sortie_id="ALT-SORTIE-ID",
            alt_dep_sortie_id="ALT-SORTIE-ID",
            app_comment="The request was denied due to inoperable fuel pumps.",
            app_initials="CB",
            app_org="KCHS/BOPS",
            call_signs=["RCH123", "ABC123", "LLS442"],
            consumer="APRON1-230401001",
            end_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            id_arr_sortie="be831d39-1822-da9f-7ace-6cc5643397dc",
            id_dep_sortie="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            mission_id="AJM123456123",
            occ_aircraft_mds="C017A",
            occ_start_time=parse_datetime("2023-01-01T01:01:03.123Z"),
            occ_tail_number="N702JG",
            occupied=True,
            origin="THIRD_PARTY_DATASOURCE",
            req_comment="Sorry for the late notice.",
            req_initials="CB",
            req_org="TACC",
            res_aircraft_mds="C017A",
            res_mission_id="AJM123456123",
            res_reason="Maintenance needed",
            res_tail_number="N702JG",
            res_type="M",
            status="APPROVED",
            target_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.airfield_slot_consumptions.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
                num_aircraft=1,
                source="Bluestaq",
                start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            SyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            SyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert_matches_type(
            SyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert_matches_type(
                SyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.delete(
            "id",
        )
        assert airfield_slot_consumption is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfield_slot_consumptions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert_matches_type(str, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert_matches_type(str, airfield_slot_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.queryhelp()
        assert airfield_slot_consumption is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot_consumption = client.airfield_slot_consumptions.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slot_consumptions.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = response.parse()
        assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slot_consumptions.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = response.parse()
            assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirfieldSlotConsumptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_arr_sortie_id="ALT-SORTIE-ID",
            alt_dep_sortie_id="ALT-SORTIE-ID",
            app_comment="The request was denied due to inoperable fuel pumps.",
            app_initials="CB",
            app_org="KCHS/BOPS",
            call_signs=["RCH123", "ABC123", "LLS442"],
            consumer="APRON1-230401001",
            end_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            id_arr_sortie="be831d39-1822-da9f-7ace-6cc5643397dc",
            id_dep_sortie="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            mission_id="AJM123456123",
            occ_aircraft_mds="C017A",
            occ_start_time=parse_datetime("2023-01-01T01:01:03.123Z"),
            occ_tail_number="N702JG",
            occupied=True,
            origin="THIRD_PARTY_DATASOURCE",
            req_comment="Sorry for the late notice.",
            req_initials="CB",
            req_org="TACC",
            res_aircraft_mds="C017A",
            res_mission_id="AJM123456123",
            res_reason="Maintenance needed",
            res_tail_number="N702JG",
            res_type="M",
            status="APPROVED",
            target_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.retrieve(
            id="id",
        )
        assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert_matches_type(AirfieldslotconsumptionFull, airfield_slot_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfield_slot_consumptions.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            body_id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_arr_sortie_id="ALT-SORTIE-ID",
            alt_dep_sortie_id="ALT-SORTIE-ID",
            app_comment="The request was denied due to inoperable fuel pumps.",
            app_initials="CB",
            app_org="KCHS/BOPS",
            call_signs=["RCH123", "ABC123", "LLS442"],
            consumer="APRON1-230401001",
            end_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            id_arr_sortie="be831d39-1822-da9f-7ace-6cc5643397dc",
            id_dep_sortie="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            mission_id="AJM123456123",
            occ_aircraft_mds="C017A",
            occ_start_time=parse_datetime("2023-01-01T01:01:03.123Z"),
            occ_tail_number="N702JG",
            occupied=True,
            origin="THIRD_PARTY_DATASOURCE",
            req_comment="Sorry for the late notice.",
            req_initials="CB",
            req_org="TACC",
            res_aircraft_mds="C017A",
            res_mission_id="AJM123456123",
            res_reason="Maintenance needed",
            res_tail_number="N702JG",
            res_type="M",
            status="APPROVED",
            target_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )
        assert airfield_slot_consumption is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
            num_aircraft=1,
            source="Bluestaq",
            start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.airfield_slot_consumptions.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_airfield_slot="3136498f-2969-3535-1432-e984b2e2e686",
                num_aircraft=1,
                source="Bluestaq",
                start_time=parse_datetime("2023-01-01T01:01:01.123Z"),
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            AsyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            AsyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[AirfieldslotconsumptionAbridged], airfield_slot_consumption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.delete(
            "id",
        )
        assert airfield_slot_consumption is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfield_slot_consumptions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert_matches_type(str, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert_matches_type(str, airfield_slot_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.queryhelp()
        assert airfield_slot_consumption is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert airfield_slot_consumption is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert airfield_slot_consumption is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot_consumption = await async_client.airfield_slot_consumptions.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slot_consumptions.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot_consumption = await response.parse()
        assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slot_consumptions.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot_consumption = await response.parse()
            assert_matches_type(AirfieldSlotConsumptionTupleResponse, airfield_slot_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True
