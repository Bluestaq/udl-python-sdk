# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftSortyTupleResponse,
    AircraftSortyQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.types.shared import AircraftsortieFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftSorties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.retrieve(
            id="id",
        )
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraft_sorties.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
        )
        assert aircraft_sorty is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            body_id="AIRCRAFTSORTIE-ID",
            actual_arr_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            actual_block_in_time=parse_datetime("2021-01-01T01:06:01.123Z"),
            actual_block_out_time=parse_datetime("2021-01-01T00:55:01.123Z"),
            actual_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            aircraft_adsb="AE123C",
            aircraft_alt_id="ALT-AIRCRAFT-ID",
            aircraft_event="Example event",
            aircraft_mds="C017A",
            aircraft_remarks="Some remark about aircraft A",
            alert_status=22,
            alert_status_code="C1",
            amc_msn_num="AJM512571333",
            amc_msn_type="SAAM",
            arr_faa="FAA1",
            arr_iata="AAA",
            arr_icao="KCOS",
            arr_itinerary=101,
            arr_purpose_code="O",
            call_sign="BAKER",
            cargo_config="C-1",
            commander_name="Smith",
            current_state="Park",
            delay_code="500",
            dep_faa="FAA1",
            dep_iata="AAA",
            dep_icao="KCOS",
            dep_itinerary=100,
            dep_purpose_code="P",
            dhd=parse_datetime("2021-01-03T01:01:01.123Z"),
            dhd_reason="Due for maintenance",
            est_arr_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            est_block_in_time=parse_datetime("2021-01-01T01:06:01.123Z"),
            est_block_out_time=parse_datetime("2021-01-01T00:55:01.123Z"),
            est_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            flight_time=104.5,
            fm_desk_num="7198675309",
            fm_name="Smith",
            fuel_req=20000.1,
            gnd_time=387.8,
            id_aircraft="REF-AIRCRAFT-ID",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            jcs_priority="1A3",
            leg_num=14,
            line_number=99,
            mission_id="ABLE",
            mission_update=parse_datetime("2024-09-09T01:01:01.123Z"),
            objective_remarks="Some objective remark about aircraft A",
            origin="THIRD_PARTY_DATASOURCE",
            orig_sortie_id="A0640",
            oxy_on_crew=12.3,
            oxy_on_pax=12.3,
            oxy_req_crew=12.3,
            oxy_req_pax=12.3,
            parking_loc="KCOS",
            passengers=17,
            planned_arr_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            ppr_status="PENDING",
            primary_scl="ABC",
            req_config="C-1",
            result_remarks="Some remark about aircraft A",
            rvn_req="R",
            schedule_remarks="Some schedule remark about aircraft A",
            secondary_scl="ABC",
            soe="OPS",
            sortie_date=parse_date("2021-01-01"),
            tail_number="Tail_1",
        )
        assert aircraft_sorty is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert aircraft_sorty is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.aircraft_sorties.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.queryhelp()
        assert_matches_type(AircraftSortyQueryhelpResponse, aircraft_sorty, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert_matches_type(AircraftSortyQueryhelpResponse, aircraft_sorty, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert_matches_type(AircraftSortyQueryhelpResponse, aircraft_sorty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAircraftSorties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.retrieve(
            id="id",
        )
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraft_sorties.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
        )
        assert aircraft_sorty is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            body_id="AIRCRAFTSORTIE-ID",
            actual_arr_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            actual_block_in_time=parse_datetime("2021-01-01T01:06:01.123Z"),
            actual_block_out_time=parse_datetime("2021-01-01T00:55:01.123Z"),
            actual_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            aircraft_adsb="AE123C",
            aircraft_alt_id="ALT-AIRCRAFT-ID",
            aircraft_event="Example event",
            aircraft_mds="C017A",
            aircraft_remarks="Some remark about aircraft A",
            alert_status=22,
            alert_status_code="C1",
            amc_msn_num="AJM512571333",
            amc_msn_type="SAAM",
            arr_faa="FAA1",
            arr_iata="AAA",
            arr_icao="KCOS",
            arr_itinerary=101,
            arr_purpose_code="O",
            call_sign="BAKER",
            cargo_config="C-1",
            commander_name="Smith",
            current_state="Park",
            delay_code="500",
            dep_faa="FAA1",
            dep_iata="AAA",
            dep_icao="KCOS",
            dep_itinerary=100,
            dep_purpose_code="P",
            dhd=parse_datetime("2021-01-03T01:01:01.123Z"),
            dhd_reason="Due for maintenance",
            est_arr_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            est_block_in_time=parse_datetime("2021-01-01T01:06:01.123Z"),
            est_block_out_time=parse_datetime("2021-01-01T00:55:01.123Z"),
            est_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            flight_time=104.5,
            fm_desk_num="7198675309",
            fm_name="Smith",
            fuel_req=20000.1,
            gnd_time=387.8,
            id_aircraft="REF-AIRCRAFT-ID",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            jcs_priority="1A3",
            leg_num=14,
            line_number=99,
            mission_id="ABLE",
            mission_update=parse_datetime("2024-09-09T01:01:01.123Z"),
            objective_remarks="Some objective remark about aircraft A",
            origin="THIRD_PARTY_DATASOURCE",
            orig_sortie_id="A0640",
            oxy_on_crew=12.3,
            oxy_on_pax=12.3,
            oxy_req_crew=12.3,
            oxy_req_pax=12.3,
            parking_loc="KCOS",
            passengers=17,
            planned_arr_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            ppr_status="PENDING",
            primary_scl="ABC",
            req_config="C-1",
            result_remarks="Some remark about aircraft A",
            rvn_req="R",
            schedule_remarks="Some schedule remark about aircraft A",
            secondary_scl="ABC",
            soe="OPS",
            sortie_date=parse_date("2021-01-01"),
            tail_number="Tail_1",
        )
        assert aircraft_sorty is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert aircraft_sorty is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.aircraft_sorties.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                planned_dep_time=parse_datetime("2021-01-01T01:01:01.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.queryhelp()
        assert_matches_type(AircraftSortyQueryhelpResponse, aircraft_sorty, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert_matches_type(AircraftSortyQueryhelpResponse, aircraft_sorty, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert_matches_type(AircraftSortyQueryhelpResponse, aircraft_sorty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert_matches_type(AircraftSortyTupleResponse, aircraft_sorty, path=["response"])

        assert cast(Any, response.is_closed) is True
