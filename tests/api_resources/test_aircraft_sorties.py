# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftSortyTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.types.air_operations import AircraftsortieFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftSorties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.retrieve(
            "id",
        )
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert aircraft_sorty is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id_2="id",
            actual_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            actual_block_in_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            actual_block_out_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            actual_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            aircraft_adsb="aircraftADSB",
            aircraft_alt_id="aircraftAltId",
            aircraft_event="aircraftEvent",
            aircraft_mds="aircraftMDS",
            aircraft_remarks="aircraftRemarks",
            alert_status=0,
            alert_status_code="alertStatusCode",
            amc_msn_num="amcMsnNum",
            amc_msn_type="amcMsnType",
            arr_faa="arrFAA",
            arr_iata="arrIATA",
            arr_icao="arrICAO",
            arr_itinerary=0,
            arr_purpose_code="arrPurposeCode",
            call_sign="callSign",
            cargo_config="cargoConfig",
            commander_name="commanderName",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            current_state="currentState",
            delay_code="delayCode",
            dep_faa="depFAA",
            dep_iata="depIATA",
            dep_icao="depICAO",
            dep_itinerary=0,
            dep_purpose_code="depPurposeCode",
            dhd=parse_datetime("2019-12-27T18:11:19.117Z"),
            dhd_reason="dhdReason",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_block_in_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_block_out_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            filesize=0,
            flight_time=0,
            fm_desk_num="fmDeskNum",
            fm_name="fmName",
            fuel_req=0,
            gnd_time=0,
            id_aircraft="idAircraft",
            id_mission="idMission",
            jcs_priority="jcsPriority",
            leg_num=0,
            line_number=0,
            mission_id="missionId",
            mission_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            objective_remarks="objectiveRemarks",
            origin="origin",
            orig_network="origNetwork",
            orig_sortie_id="origSortieId",
            oxy_on_crew=0,
            oxy_on_pax=0,
            oxy_req_crew=0,
            oxy_req_pax=0,
            paper_status="paperStatus",
            papers_version="papersVersion",
            parking_loc="parkingLoc",
            passengers=0,
            planned_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            ppr_status="pprStatus",
            primary_scl="primarySCL",
            raw_file_uri="rawFileURI",
            req_config="reqConfig",
            result_remarks="resultRemarks",
            rvn_req="rvnReq",
            schedule_remarks="scheduleRemarks",
            secondary_scl="secondarySCL",
            soe="soe",
            sortie_date=parse_date("2019-12-27"),
            source_dl="sourceDL",
            tail_number="tailNumber",
        )
        assert aircraft_sorty is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert aircraft_sorty is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.aircraft_sorties.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.queryhelp()
        assert aircraft_sorty is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_sorties.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert aircraft_sorty is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_sorties.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.aircraft_sorties.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.retrieve(
            "id",
        )
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert_matches_type(AircraftsortieFull, aircraft_sorty, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert aircraft_sorty is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id_2="id",
            actual_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            actual_block_in_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            actual_block_out_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            actual_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            aircraft_adsb="aircraftADSB",
            aircraft_alt_id="aircraftAltId",
            aircraft_event="aircraftEvent",
            aircraft_mds="aircraftMDS",
            aircraft_remarks="aircraftRemarks",
            alert_status=0,
            alert_status_code="alertStatusCode",
            amc_msn_num="amcMsnNum",
            amc_msn_type="amcMsnType",
            arr_faa="arrFAA",
            arr_iata="arrIATA",
            arr_icao="arrICAO",
            arr_itinerary=0,
            arr_purpose_code="arrPurposeCode",
            call_sign="callSign",
            cargo_config="cargoConfig",
            commander_name="commanderName",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            current_state="currentState",
            delay_code="delayCode",
            dep_faa="depFAA",
            dep_iata="depIATA",
            dep_icao="depICAO",
            dep_itinerary=0,
            dep_purpose_code="depPurposeCode",
            dhd=parse_datetime("2019-12-27T18:11:19.117Z"),
            dhd_reason="dhdReason",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_block_in_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_block_out_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            filesize=0,
            flight_time=0,
            fm_desk_num="fmDeskNum",
            fm_name="fmName",
            fuel_req=0,
            gnd_time=0,
            id_aircraft="idAircraft",
            id_mission="idMission",
            jcs_priority="jcsPriority",
            leg_num=0,
            line_number=0,
            mission_id="missionId",
            mission_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            objective_remarks="objectiveRemarks",
            origin="origin",
            orig_network="origNetwork",
            orig_sortie_id="origSortieId",
            oxy_on_crew=0,
            oxy_on_pax=0,
            oxy_req_crew=0,
            oxy_req_pax=0,
            paper_status="paperStatus",
            papers_version="papersVersion",
            parking_loc="parkingLoc",
            passengers=0,
            planned_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            ppr_status="pprStatus",
            primary_scl="primarySCL",
            raw_file_uri="rawFileURI",
            req_config="reqConfig",
            result_remarks="resultRemarks",
            rvn_req="rvnReq",
            schedule_remarks="scheduleRemarks",
            secondary_scl="secondarySCL",
            soe="soe",
            sortie_date=parse_date("2019-12-27"),
            source_dl="sourceDL",
            tail_number="tailNumber",
        )
        assert aircraft_sorty is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert aircraft_sorty is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.aircraft_sorties.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.queryhelp()
        assert aircraft_sorty is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_sorties.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert aircraft_sorty is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_sorties.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.aircraft_sorties.tuple(
            columns="columns",
            planned_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
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
