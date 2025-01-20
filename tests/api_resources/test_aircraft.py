# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftFull,
    AircraftListResponse,
    AircraftTupleQueryResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert aircraft is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id="id",
            category="category",
            command="command",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cruise_speed=0,
            dtd="dtd",
            entity={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "name": "name",
                "source": "source",
                "type": "type",
                "country_code": "countryCode",
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "id_entity": "idEntity",
                "id_location": "idLocation",
                "id_on_orbit": "idOnOrbit",
                "id_operating_unit": "idOperatingUnit",
                "location": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "name": "name",
                    "source": "source",
                    "altitude": 0,
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "id_location": "idLocation",
                    "lat": 0,
                    "lon": 0,
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "on_orbit": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "sat_no": 0,
                    "source": "source",
                    "alt_name": "altName",
                    "category": "category",
                    "common_name": "commonName",
                    "constellation": "constellation",
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "decay_date": "2019-12-27T18:11:19.117Z",
                    "id_on_orbit": "idOnOrbit",
                    "intl_des": "intlDes",
                    "launch_date": "2019-12-27",
                    "launch_site_id": "launchSiteId",
                    "lifetime_years": 0,
                    "mission_number": "missionNumber",
                    "object_type": "objectType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "origin": "origin",
                "orig_network": "origNetwork",
                "owner_type": "ownerType",
                "taskable": True,
                "urls": ["string"],
            },
            id_entity="idEntity",
            max_speed=0,
            min_req_runway_ft=0,
            min_req_runway_m=0,
            nominal_ta_time=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            owner="owner",
            serial_number="serialNumber",
            source_dl="sourceDL",
            tail_number="tailNumber",
        )
        assert aircraft is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert aircraft is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.retrieve(
            "id",
        )
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert aircraft is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id_2="id",
            category="category",
            command="command",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cruise_speed=0,
            dtd="dtd",
            entity={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "name": "name",
                "source": "source",
                "type": "type",
                "country_code": "countryCode",
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "id_entity": "idEntity",
                "id_location": "idLocation",
                "id_on_orbit": "idOnOrbit",
                "id_operating_unit": "idOperatingUnit",
                "location": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "name": "name",
                    "source": "source",
                    "altitude": 0,
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "id_location": "idLocation",
                    "lat": 0,
                    "lon": 0,
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "on_orbit": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "sat_no": 0,
                    "source": "source",
                    "alt_name": "altName",
                    "category": "category",
                    "common_name": "commonName",
                    "constellation": "constellation",
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "decay_date": "2019-12-27T18:11:19.117Z",
                    "id_on_orbit": "idOnOrbit",
                    "intl_des": "intlDes",
                    "launch_date": "2019-12-27",
                    "launch_site_id": "launchSiteId",
                    "lifetime_years": 0,
                    "mission_number": "missionNumber",
                    "object_type": "objectType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "origin": "origin",
                "orig_network": "origNetwork",
                "owner_type": "ownerType",
                "taskable": True,
                "urls": ["string"],
            },
            id_entity="idEntity",
            max_speed=0,
            min_req_runway_ft=0,
            min_req_runway_m=0,
            nominal_ta_time=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            owner="owner",
            serial_number="serialNumber",
            source_dl="sourceDL",
            tail_number="tailNumber",
        )
        assert aircraft is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert aircraft is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.aircraft.with_raw_response.update(
                id_1="",
                aircraft_mds="aircraftMDS",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.list()
        assert_matches_type(AircraftListResponse, aircraft, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert_matches_type(AircraftListResponse, aircraft, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert_matches_type(AircraftListResponse, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.count()
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
        assert aircraft is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = response.parse()
        assert aircraft is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple_query(self, client: Unifieddatalibrary) -> None:
        aircraft = client.aircraft.tuple_query(
            columns="columns",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert aircraft is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id="id",
            category="category",
            command="command",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cruise_speed=0,
            dtd="dtd",
            entity={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "name": "name",
                "source": "source",
                "type": "type",
                "country_code": "countryCode",
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "id_entity": "idEntity",
                "id_location": "idLocation",
                "id_on_orbit": "idOnOrbit",
                "id_operating_unit": "idOperatingUnit",
                "location": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "name": "name",
                    "source": "source",
                    "altitude": 0,
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "id_location": "idLocation",
                    "lat": 0,
                    "lon": 0,
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "on_orbit": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "sat_no": 0,
                    "source": "source",
                    "alt_name": "altName",
                    "category": "category",
                    "common_name": "commonName",
                    "constellation": "constellation",
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "decay_date": "2019-12-27T18:11:19.117Z",
                    "id_on_orbit": "idOnOrbit",
                    "intl_des": "intlDes",
                    "launch_date": "2019-12-27",
                    "launch_site_id": "launchSiteId",
                    "lifetime_years": 0,
                    "mission_number": "missionNumber",
                    "object_type": "objectType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "origin": "origin",
                "orig_network": "origNetwork",
                "owner_type": "ownerType",
                "taskable": True,
                "urls": ["string"],
            },
            id_entity="idEntity",
            max_speed=0,
            min_req_runway_ft=0,
            min_req_runway_m=0,
            nominal_ta_time=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            owner="owner",
            serial_number="serialNumber",
            source_dl="sourceDL",
            tail_number="tailNumber",
        )
        assert aircraft is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert aircraft is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.create(
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.retrieve(
            "id",
        )
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(AircraftFull, aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert aircraft is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id_2="id",
            category="category",
            command="command",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cruise_speed=0,
            dtd="dtd",
            entity={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "name": "name",
                "source": "source",
                "type": "type",
                "country_code": "countryCode",
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "id_entity": "idEntity",
                "id_location": "idLocation",
                "id_on_orbit": "idOnOrbit",
                "id_operating_unit": "idOperatingUnit",
                "location": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "name": "name",
                    "source": "source",
                    "altitude": 0,
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "id_location": "idLocation",
                    "lat": 0,
                    "lon": 0,
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "on_orbit": {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "sat_no": 0,
                    "source": "source",
                    "alt_name": "altName",
                    "category": "category",
                    "common_name": "commonName",
                    "constellation": "constellation",
                    "country_code": "countryCode",
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "decay_date": "2019-12-27T18:11:19.117Z",
                    "id_on_orbit": "idOnOrbit",
                    "intl_des": "intlDes",
                    "launch_date": "2019-12-27",
                    "launch_site_id": "launchSiteId",
                    "lifetime_years": 0,
                    "mission_number": "missionNumber",
                    "object_type": "objectType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                },
                "origin": "origin",
                "orig_network": "origNetwork",
                "owner_type": "ownerType",
                "taskable": True,
                "urls": ["string"],
            },
            id_entity="idEntity",
            max_speed=0,
            min_req_runway_ft=0,
            min_req_runway_m=0,
            nominal_ta_time=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            owner="owner",
            serial_number="serialNumber",
            source_dl="sourceDL",
            tail_number="tailNumber",
        )
        assert aircraft is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert aircraft is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.update(
            id_1="id",
            aircraft_mds="aircraftMDS",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.aircraft.with_raw_response.update(
                id_1="",
                aircraft_mds="aircraftMDS",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.list()
        assert_matches_type(AircraftListResponse, aircraft, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert_matches_type(AircraftListResponse, aircraft, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert_matches_type(AircraftListResponse, aircraft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.count()
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
        assert aircraft is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft = await response.parse()
        assert aircraft is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft = await response.parse()
            assert aircraft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft = await async_client.aircraft.tuple_query(
            columns="columns",
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
