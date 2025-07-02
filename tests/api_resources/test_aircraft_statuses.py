# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftstatusAbridged,
    AircraftStatusTupleResponse,
    AircraftStatusQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AircraftstatusFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )
        assert aircraft_status is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            additional_sys=["ATOMS", "TUDL", "BLOS1"],
            air_to_air_status="OPERATIONAL",
            air_to_ground_status="OPERATIONAL",
            alpha_status_code="A2",
            alt_aircraft_id="ORIG-AIRCRAFT-ID",
            contamination_status="CLEAR",
            current_icao="KCHS",
            current_state="AVAILABLE",
            earliest_ta_end_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            flight_phase="Landing",
            fuel=10,
            fuel_function="Burn",
            fuel_status="DELIVERED",
            geo_loc="AJJY",
            ground_status="ALERT",
            gun_capable=True,
            gun_rds_max=550,
            gun_rds_min=150,
            gun_rds_type="7.62 MM",
            id_airfield="b89430e3-97d9-408c-9c89-fd3840c4b84d",
            id_poi="0e52f081-a2e3-4b73-b822-88b882232691",
            inventory=["AIM-9 SIDEWINDER", "AIM-120 AMRAAM"],
            inventory_max=[2, 2],
            inventory_min=[1, 2],
            last_inspection_date=parse_datetime("2024-09-09T16:00:00.123Z"),
            last_updated_by="some.user",
            maint_poc="PSUP NIGHT SHIFT 800-555-4412",
            maint_priority="1",
            maint_status="maintenance status",
            maint_status_driver="SCREW STUCK IN LEFT NLG TIRE",
            maint_status_update=parse_datetime("2022-01-01T16:00:00.123Z"),
            mission_readiness="ABLE",
            mx_remark="COM2 INOP",
            next_icao="PHNL",
            notes="Some notes for aircraft A",
            origin="THIRD_PARTY_DATASOURCE",
            park_location="B1",
            park_location_system="GDSS",
            previous_icao="EGLL",
            ta_start_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            troubleshoot_etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            unavailable_sys=["CMDS", "AOC"],
        )
        assert aircraft_status is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert aircraft_status is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.retrieve(
            id="id",
        )
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraft_statuses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )
        assert aircraft_status is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            additional_sys=["ATOMS", "TUDL", "BLOS1"],
            air_to_air_status="OPERATIONAL",
            air_to_ground_status="OPERATIONAL",
            alpha_status_code="A2",
            alt_aircraft_id="ORIG-AIRCRAFT-ID",
            contamination_status="CLEAR",
            current_icao="KCHS",
            current_state="AVAILABLE",
            earliest_ta_end_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            flight_phase="Landing",
            fuel=10,
            fuel_function="Burn",
            fuel_status="DELIVERED",
            geo_loc="AJJY",
            ground_status="ALERT",
            gun_capable=True,
            gun_rds_max=550,
            gun_rds_min=150,
            gun_rds_type="7.62 MM",
            id_airfield="b89430e3-97d9-408c-9c89-fd3840c4b84d",
            id_poi="0e52f081-a2e3-4b73-b822-88b882232691",
            inventory=["AIM-9 SIDEWINDER", "AIM-120 AMRAAM"],
            inventory_max=[2, 2],
            inventory_min=[1, 2],
            last_inspection_date=parse_datetime("2024-09-09T16:00:00.123Z"),
            last_updated_by="some.user",
            maint_poc="PSUP NIGHT SHIFT 800-555-4412",
            maint_priority="1",
            maint_status="maintenance status",
            maint_status_driver="SCREW STUCK IN LEFT NLG TIRE",
            maint_status_update=parse_datetime("2022-01-01T16:00:00.123Z"),
            mission_readiness="ABLE",
            mx_remark="COM2 INOP",
            next_icao="PHNL",
            notes="Some notes for aircraft A",
            origin="THIRD_PARTY_DATASOURCE",
            park_location="B1",
            park_location_system="GDSS",
            previous_icao="EGLL",
            ta_start_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            troubleshoot_etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            unavailable_sys=["CMDS", "AOC"],
        )
        assert aircraft_status is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert aircraft_status is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.aircraft_statuses.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.list()
        assert_matches_type(SyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(SyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert_matches_type(SyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.delete(
            "id",
        )
        assert aircraft_status is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert aircraft_status is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraft_statuses.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.count()
        assert_matches_type(str, aircraft_status, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(str, aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert_matches_type(str, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.queryhelp()
        assert_matches_type(AircraftStatusQueryhelpResponse, aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(AircraftStatusQueryhelpResponse, aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert_matches_type(AircraftStatusQueryhelpResponse, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.tuple(
            columns="columns",
        )
        assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAircraftStatuses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )
        assert aircraft_status is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            additional_sys=["ATOMS", "TUDL", "BLOS1"],
            air_to_air_status="OPERATIONAL",
            air_to_ground_status="OPERATIONAL",
            alpha_status_code="A2",
            alt_aircraft_id="ORIG-AIRCRAFT-ID",
            contamination_status="CLEAR",
            current_icao="KCHS",
            current_state="AVAILABLE",
            earliest_ta_end_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            flight_phase="Landing",
            fuel=10,
            fuel_function="Burn",
            fuel_status="DELIVERED",
            geo_loc="AJJY",
            ground_status="ALERT",
            gun_capable=True,
            gun_rds_max=550,
            gun_rds_min=150,
            gun_rds_type="7.62 MM",
            id_airfield="b89430e3-97d9-408c-9c89-fd3840c4b84d",
            id_poi="0e52f081-a2e3-4b73-b822-88b882232691",
            inventory=["AIM-9 SIDEWINDER", "AIM-120 AMRAAM"],
            inventory_max=[2, 2],
            inventory_min=[1, 2],
            last_inspection_date=parse_datetime("2024-09-09T16:00:00.123Z"),
            last_updated_by="some.user",
            maint_poc="PSUP NIGHT SHIFT 800-555-4412",
            maint_priority="1",
            maint_status="maintenance status",
            maint_status_driver="SCREW STUCK IN LEFT NLG TIRE",
            maint_status_update=parse_datetime("2022-01-01T16:00:00.123Z"),
            mission_readiness="ABLE",
            mx_remark="COM2 INOP",
            next_icao="PHNL",
            notes="Some notes for aircraft A",
            origin="THIRD_PARTY_DATASOURCE",
            park_location="B1",
            park_location_system="GDSS",
            previous_icao="EGLL",
            ta_start_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            troubleshoot_etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            unavailable_sys=["CMDS", "AOC"],
        )
        assert aircraft_status is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert aircraft_status is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.retrieve(
            id="id",
        )
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraft_statuses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )
        assert aircraft_status is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            additional_sys=["ATOMS", "TUDL", "BLOS1"],
            air_to_air_status="OPERATIONAL",
            air_to_ground_status="OPERATIONAL",
            alpha_status_code="A2",
            alt_aircraft_id="ORIG-AIRCRAFT-ID",
            contamination_status="CLEAR",
            current_icao="KCHS",
            current_state="AVAILABLE",
            earliest_ta_end_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            flight_phase="Landing",
            fuel=10,
            fuel_function="Burn",
            fuel_status="DELIVERED",
            geo_loc="AJJY",
            ground_status="ALERT",
            gun_capable=True,
            gun_rds_max=550,
            gun_rds_min=150,
            gun_rds_type="7.62 MM",
            id_airfield="b89430e3-97d9-408c-9c89-fd3840c4b84d",
            id_poi="0e52f081-a2e3-4b73-b822-88b882232691",
            inventory=["AIM-9 SIDEWINDER", "AIM-120 AMRAAM"],
            inventory_max=[2, 2],
            inventory_min=[1, 2],
            last_inspection_date=parse_datetime("2024-09-09T16:00:00.123Z"),
            last_updated_by="some.user",
            maint_poc="PSUP NIGHT SHIFT 800-555-4412",
            maint_priority="1",
            maint_status="maintenance status",
            maint_status_driver="SCREW STUCK IN LEFT NLG TIRE",
            maint_status_update=parse_datetime("2022-01-01T16:00:00.123Z"),
            mission_readiness="ABLE",
            mx_remark="COM2 INOP",
            next_icao="PHNL",
            notes="Some notes for aircraft A",
            origin="THIRD_PARTY_DATASOURCE",
            park_location="B1",
            park_location_system="GDSS",
            previous_icao="EGLL",
            ta_start_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            troubleshoot_etic=parse_datetime("2022-01-01T16:00:00.123Z"),
            unavailable_sys=["CMDS", "AOC"],
        )
        assert aircraft_status is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert aircraft_status is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.aircraft_statuses.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_aircraft="29232269-e4c2-45c9-aa21-039a33209340",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.list()
        assert_matches_type(AsyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(AsyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert_matches_type(AsyncOffsetPage[AircraftstatusAbridged], aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.delete(
            "id",
        )
        assert aircraft_status is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert aircraft_status is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraft_statuses.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.count()
        assert_matches_type(str, aircraft_status, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(str, aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert_matches_type(str, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.queryhelp()
        assert_matches_type(AircraftStatusQueryhelpResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(AircraftStatusQueryhelpResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert_matches_type(AircraftStatusQueryhelpResponse, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.tuple(
            columns="columns",
        )
        assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert_matches_type(AircraftStatusTupleResponse, aircraft_status, path=["response"])

        assert cast(Any, response.is_closed) is True
