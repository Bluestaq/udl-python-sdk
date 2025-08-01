# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftAbridged,
    AircraftQueryhelpResponse,
    AircraftTupleQueryResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AircraftFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert aircraft is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            category="M",
            command="HQACC",
            cruise_speed=915,
            dtd="005",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            max_speed=2655.1,
            min_req_runway_ft=3000,
            min_req_runway_m=1000,
            nominal_ta_time=500,
            notes="Notes for this aircraft",
            origin="THIRD_PARTY_DATASOURCE",
            owner="437AW",
            serial_number="7007187",
            tail_number="N702JG",
        )
        assert aircraft is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert aircraft is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.retrieve(
            id="id",
        )
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert_matches_type(AircraftFull, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraft.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert aircraft is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            category="M",
            command="HQACC",
            cruise_speed=915,
            dtd="005",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            max_speed=2655.1,
            min_req_runway_ft=3000,
            min_req_runway_m=1000,
            nominal_ta_time=500,
            notes="Notes for this aircraft",
            origin="THIRD_PARTY_DATASOURCE",
            owner="437AW",
            serial_number="7007187",
            tail_number="N702JG",
        )
        assert aircraft is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert aircraft is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.aircraft.with_raw_response.update(
                path_id="",
                aircraft_mds="E-2C HAWKEYE",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.list()
        assert_matches_type(SyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(SyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert_matches_type(SyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.count()
        assert_matches_type(str, aircraft, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aircraft, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(str, aircraft, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert_matches_type(str, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.queryhelp()
        assert_matches_type(AircraftQueryhelpResponse, aircraft, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(AircraftQueryhelpResponse, aircraft, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert_matches_type(AircraftQueryhelpResponse, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple_query(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.tuple_query(
            columns="columns",
        )
        assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

    @parametrize
    def test_method_tuple_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.tuple_query(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

    @parametrize
    def test_raw_response_tuple_query(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.tuple_query(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

    @parametrize
    def test_streaming_response_tuple_query(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.tuple_query(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAircraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert aircraft is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            category="M",
            command="HQACC",
            cruise_speed=915,
            dtd="005",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            max_speed=2655.1,
            min_req_runway_ft=3000,
            min_req_runway_m=1000,
            nominal_ta_time=500,
            notes="Notes for this aircraft",
            origin="THIRD_PARTY_DATASOURCE",
            owner="437AW",
            serial_number="7007187",
            tail_number="N702JG",
        )
        assert aircraft is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert aircraft is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.create(
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.retrieve(
            id="id",
        )
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert_matches_type(AircraftFull, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraft.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert aircraft is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            category="M",
            command="HQACC",
            cruise_speed=915,
            dtd="005",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            max_speed=2655.1,
            min_req_runway_ft=3000,
            min_req_runway_m=1000,
            nominal_ta_time=500,
            notes="Notes for this aircraft",
            origin="THIRD_PARTY_DATASOURCE",
            owner="437AW",
            serial_number="7007187",
            tail_number="N702JG",
        )
        assert aircraft is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert aircraft is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.update(
            path_id="id",
            aircraft_mds="E-2C HAWKEYE",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.aircraft.with_raw_response.update(
                path_id="",
                aircraft_mds="E-2C HAWKEYE",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.list()
        assert_matches_type(AsyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(AsyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert_matches_type(AsyncOffsetPage[AircraftAbridged], aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.count()
        assert_matches_type(str, aircraft, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aircraft, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(str, aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert_matches_type(str, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.queryhelp()
        assert_matches_type(AircraftQueryhelpResponse, aircraft, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(AircraftQueryhelpResponse, aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert_matches_type(AircraftQueryhelpResponse, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.tuple_query(
            columns="columns",
        )
        assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

    @parametrize
    async def test_method_tuple_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.tuple_query(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

    @parametrize
    async def test_raw_response_tuple_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.tuple_query(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_tuple_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.tuple_query(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert_matches_type(AircraftTupleQueryResponse, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True
