# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftStatusListResponse,
    AircraftStatusTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.shared import AircraftstatusFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )
        assert aircraft_status is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
            id="id",
            additional_sys=["string"],
            air_to_air_status="airToAirStatus",
            air_to_ground_status="airToGroundStatus",
            alpha_status_code="alphaStatusCode",
            alt_aircraft_id="altAircraftId",
            contamination_status="contaminationStatus",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            current_icao="currentICAO",
            current_state="currentState",
            earliest_ta_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            flight_phase="flightPhase",
            fuel=0,
            fuel_function="fuelFunction",
            fuel_status="fuelStatus",
            geo_loc="geoLoc",
            ground_status="groundStatus",
            gun_capable=True,
            gun_rds_max=0,
            gun_rds_min=0,
            gun_rds_type="gunRdsType",
            id_airfield="idAirfield",
            id_poi="idPOI",
            inventory=["string"],
            inventory_max=[0],
            inventory_min=[0],
            last_inspection_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_updated_by="lastUpdatedBy",
            maint_poc="maintPoc",
            maint_priority="maintPriority",
            maint_status="maintStatus",
            maint_status_driver="maintStatusDriver",
            maint_status_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mission_readiness="missionReadiness",
            mx_remark="mxRemark",
            next_icao="nextICAO",
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            park_location="parkLocation",
            park_location_system="parkLocationSystem",
            previous_icao="previousICAO",
            source_dl="sourceDL",
            ta_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            troubleshoot_etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            unavailable_sys=["string"],
        )
        assert aircraft_status is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert aircraft_status is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.retrieve(
            "id",
        )
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )
        assert aircraft_status is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
            id_2="id",
            additional_sys=["string"],
            air_to_air_status="airToAirStatus",
            air_to_ground_status="airToGroundStatus",
            alpha_status_code="alphaStatusCode",
            alt_aircraft_id="altAircraftId",
            contamination_status="contaminationStatus",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            current_icao="currentICAO",
            current_state="currentState",
            earliest_ta_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            flight_phase="flightPhase",
            fuel=0,
            fuel_function="fuelFunction",
            fuel_status="fuelStatus",
            geo_loc="geoLoc",
            ground_status="groundStatus",
            gun_capable=True,
            gun_rds_max=0,
            gun_rds_min=0,
            gun_rds_type="gunRdsType",
            id_airfield="idAirfield",
            id_poi="idPOI",
            inventory=["string"],
            inventory_max=[0],
            inventory_min=[0],
            last_inspection_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_updated_by="lastUpdatedBy",
            maint_poc="maintPoc",
            maint_priority="maintPriority",
            maint_status="maintStatus",
            maint_status_driver="maintStatusDriver",
            maint_status_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mission_readiness="missionReadiness",
            mx_remark="mxRemark",
            next_icao="nextICAO",
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            park_location="parkLocation",
            park_location_system="parkLocationSystem",
            previous_icao="previousICAO",
            source_dl="sourceDL",
            ta_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            troubleshoot_etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            unavailable_sys=["string"],
        )
        assert aircraft_status is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert aircraft_status is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.aircraft_statuses.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_aircraft="idAircraft",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.list()
        assert_matches_type(AircraftStatusListResponse, aircraft_status, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert_matches_type(AircraftStatusListResponse, aircraft_status, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert_matches_type(AircraftStatusListResponse, aircraft_status, path=["response"])

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
        assert aircraft_status is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_statuses.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = response.parse()
        assert aircraft_status is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_statuses.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        aircraft_status = client.aircraft_statuses.tuple(
            columns="columns",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )
        assert aircraft_status is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
            id="id",
            additional_sys=["string"],
            air_to_air_status="airToAirStatus",
            air_to_ground_status="airToGroundStatus",
            alpha_status_code="alphaStatusCode",
            alt_aircraft_id="altAircraftId",
            contamination_status="contaminationStatus",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            current_icao="currentICAO",
            current_state="currentState",
            earliest_ta_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            flight_phase="flightPhase",
            fuel=0,
            fuel_function="fuelFunction",
            fuel_status="fuelStatus",
            geo_loc="geoLoc",
            ground_status="groundStatus",
            gun_capable=True,
            gun_rds_max=0,
            gun_rds_min=0,
            gun_rds_type="gunRdsType",
            id_airfield="idAirfield",
            id_poi="idPOI",
            inventory=["string"],
            inventory_max=[0],
            inventory_min=[0],
            last_inspection_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_updated_by="lastUpdatedBy",
            maint_poc="maintPoc",
            maint_priority="maintPriority",
            maint_status="maintStatus",
            maint_status_driver="maintStatusDriver",
            maint_status_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mission_readiness="missionReadiness",
            mx_remark="mxRemark",
            next_icao="nextICAO",
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            park_location="parkLocation",
            park_location_system="parkLocationSystem",
            previous_icao="previousICAO",
            source_dl="sourceDL",
            ta_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            troubleshoot_etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            unavailable_sys=["string"],
        )
        assert aircraft_status is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert aircraft_status is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.retrieve(
            "id",
        )
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(AircraftstatusFull, aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )
        assert aircraft_status is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
            id_2="id",
            additional_sys=["string"],
            air_to_air_status="airToAirStatus",
            air_to_ground_status="airToGroundStatus",
            alpha_status_code="alphaStatusCode",
            alt_aircraft_id="altAircraftId",
            contamination_status="contaminationStatus",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            current_icao="currentICAO",
            current_state="currentState",
            earliest_ta_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            flight_phase="flightPhase",
            fuel=0,
            fuel_function="fuelFunction",
            fuel_status="fuelStatus",
            geo_loc="geoLoc",
            ground_status="groundStatus",
            gun_capable=True,
            gun_rds_max=0,
            gun_rds_min=0,
            gun_rds_type="gunRdsType",
            id_airfield="idAirfield",
            id_poi="idPOI",
            inventory=["string"],
            inventory_max=[0],
            inventory_min=[0],
            last_inspection_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_updated_by="lastUpdatedBy",
            maint_poc="maintPoc",
            maint_priority="maintPriority",
            maint_status="maintStatus",
            maint_status_driver="maintStatusDriver",
            maint_status_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mission_readiness="missionReadiness",
            mx_remark="mxRemark",
            next_icao="nextICAO",
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            park_location="parkLocation",
            park_location_system="parkLocationSystem",
            previous_icao="previousICAO",
            source_dl="sourceDL",
            ta_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            troubleshoot_etic=parse_datetime("2019-12-27T18:11:19.117Z"),
            unavailable_sys=["string"],
        )
        assert aircraft_status is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert aircraft_status is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_aircraft="idAircraft",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.aircraft_statuses.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_aircraft="idAircraft",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.list()
        assert_matches_type(AircraftStatusListResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert_matches_type(AircraftStatusListResponse, aircraft_status, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert_matches_type(AircraftStatusListResponse, aircraft_status, path=["response"])

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
        assert aircraft_status is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_statuses.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status = await response.parse()
        assert aircraft_status is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_statuses.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status = await response.parse()
            assert aircraft_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status = await async_client.aircraft_statuses.tuple(
            columns="columns",
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
