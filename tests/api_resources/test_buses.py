# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    BusFull,
    BusListResponse,
    BusTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )
        assert bus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            id="id",
            aocs_notes="aocsNotes",
            avg_dry_mass=0,
            avg_payload_mass=0,
            avg_payload_power=0,
            avg_spacecraft_power=0,
            avg_wet_mass=0,
            body_dimension_x=0,
            body_dimension_y=0,
            body_dimension_z=0,
            bus_kit_designer_org_id="busKitDesignerOrgId",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
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
            generic=True,
            id_entity="idEntity",
            launch_envelope_dimension_x=0,
            launch_envelope_dimension_y=0,
            launch_envelope_dimension_z=0,
            main_computer_manufacturer_org_id="mainComputerManufacturerOrgId",
            manufacturer_org_id="manufacturerOrgId",
            mass_category="massCategory",
            max_bol_power_lower=0,
            max_bol_power_upper=0,
            max_bol_station_mass=0,
            max_dry_mass=0,
            max_eol_power_lower=0,
            max_eol_power_upper=0,
            max_launch_mass_lower=0,
            max_launch_mass_upper=0,
            max_payload_mass=0,
            max_payload_power=0,
            max_spacecraft_power=0,
            max_wet_mass=0,
            median_dry_mass=0,
            median_wet_mass=0,
            min_dry_mass=0,
            min_wet_mass=0,
            num_orbit_type=0,
            oap_payload_power=0,
            oap_spacecraft_power=0,
            orbit_types=["string"],
            origin="origin",
            orig_network="origNetwork",
            payload_dimension_x=0,
            payload_dimension_y=0,
            payload_dimension_z=0,
            payload_volume=0,
            power_category="powerCategory",
            telemetry_tracking_manufacturer_org_id="telemetryTrackingManufacturerOrgId",
            type="type",
        )
        assert bus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.retrieve(
            "id",
        )
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(BusFull, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.buses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )
        assert bus is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            id_2="id",
            aocs_notes="aocsNotes",
            avg_dry_mass=0,
            avg_payload_mass=0,
            avg_payload_power=0,
            avg_spacecraft_power=0,
            avg_wet_mass=0,
            body_dimension_x=0,
            body_dimension_y=0,
            body_dimension_z=0,
            bus_kit_designer_org_id="busKitDesignerOrgId",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
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
            generic=True,
            id_entity="idEntity",
            launch_envelope_dimension_x=0,
            launch_envelope_dimension_y=0,
            launch_envelope_dimension_z=0,
            main_computer_manufacturer_org_id="mainComputerManufacturerOrgId",
            manufacturer_org_id="manufacturerOrgId",
            mass_category="massCategory",
            max_bol_power_lower=0,
            max_bol_power_upper=0,
            max_bol_station_mass=0,
            max_dry_mass=0,
            max_eol_power_lower=0,
            max_eol_power_upper=0,
            max_launch_mass_lower=0,
            max_launch_mass_upper=0,
            max_payload_mass=0,
            max_payload_power=0,
            max_spacecraft_power=0,
            max_wet_mass=0,
            median_dry_mass=0,
            median_wet_mass=0,
            min_dry_mass=0,
            min_wet_mass=0,
            num_orbit_type=0,
            oap_payload_power=0,
            oap_spacecraft_power=0,
            orbit_types=["string"],
            origin="origin",
            orig_network="origNetwork",
            payload_dimension_x=0,
            payload_dimension_y=0,
            payload_dimension_z=0,
            payload_volume=0,
            power_category="powerCategory",
            telemetry_tracking_manufacturer_org_id="telemetryTrackingManufacturerOrgId",
            type="type",
        )
        assert bus is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.buses.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                name="name",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.list()
        assert_matches_type(BusListResponse, bus, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(BusListResponse, bus, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(BusListResponse, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.delete(
            "id",
        )
        assert bus is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.buses.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.count()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(str, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.query_help()
        assert bus is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.tuple(
            columns="columns",
        )
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(BusTupleResponse, bus, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBuses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )
        assert bus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            id="id",
            aocs_notes="aocsNotes",
            avg_dry_mass=0,
            avg_payload_mass=0,
            avg_payload_power=0,
            avg_spacecraft_power=0,
            avg_wet_mass=0,
            body_dimension_x=0,
            body_dimension_y=0,
            body_dimension_z=0,
            bus_kit_designer_org_id="busKitDesignerOrgId",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
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
            generic=True,
            id_entity="idEntity",
            launch_envelope_dimension_x=0,
            launch_envelope_dimension_y=0,
            launch_envelope_dimension_z=0,
            main_computer_manufacturer_org_id="mainComputerManufacturerOrgId",
            manufacturer_org_id="manufacturerOrgId",
            mass_category="massCategory",
            max_bol_power_lower=0,
            max_bol_power_upper=0,
            max_bol_station_mass=0,
            max_dry_mass=0,
            max_eol_power_lower=0,
            max_eol_power_upper=0,
            max_launch_mass_lower=0,
            max_launch_mass_upper=0,
            max_payload_mass=0,
            max_payload_power=0,
            max_spacecraft_power=0,
            max_wet_mass=0,
            median_dry_mass=0,
            median_wet_mass=0,
            min_dry_mass=0,
            min_wet_mass=0,
            num_orbit_type=0,
            oap_payload_power=0,
            oap_spacecraft_power=0,
            orbit_types=["string"],
            origin="origin",
            orig_network="origNetwork",
            payload_dimension_x=0,
            payload_dimension_y=0,
            payload_dimension_z=0,
            payload_volume=0,
            power_category="powerCategory",
            telemetry_tracking_manufacturer_org_id="telemetryTrackingManufacturerOrgId",
            type="type",
        )
        assert bus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.retrieve(
            "id",
        )
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(BusFull, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.buses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )
        assert bus is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            id_2="id",
            aocs_notes="aocsNotes",
            avg_dry_mass=0,
            avg_payload_mass=0,
            avg_payload_power=0,
            avg_spacecraft_power=0,
            avg_wet_mass=0,
            body_dimension_x=0,
            body_dimension_y=0,
            body_dimension_z=0,
            bus_kit_designer_org_id="busKitDesignerOrgId",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
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
            generic=True,
            id_entity="idEntity",
            launch_envelope_dimension_x=0,
            launch_envelope_dimension_y=0,
            launch_envelope_dimension_z=0,
            main_computer_manufacturer_org_id="mainComputerManufacturerOrgId",
            manufacturer_org_id="manufacturerOrgId",
            mass_category="massCategory",
            max_bol_power_lower=0,
            max_bol_power_upper=0,
            max_bol_station_mass=0,
            max_dry_mass=0,
            max_eol_power_lower=0,
            max_eol_power_upper=0,
            max_launch_mass_lower=0,
            max_launch_mass_upper=0,
            max_payload_mass=0,
            max_payload_power=0,
            max_spacecraft_power=0,
            max_wet_mass=0,
            median_dry_mass=0,
            median_wet_mass=0,
            min_dry_mass=0,
            min_wet_mass=0,
            num_orbit_type=0,
            oap_payload_power=0,
            oap_spacecraft_power=0,
            orbit_types=["string"],
            origin="origin",
            orig_network="origNetwork",
            payload_dimension_x=0,
            payload_dimension_y=0,
            payload_dimension_z=0,
            payload_volume=0,
            power_category="powerCategory",
            telemetry_tracking_manufacturer_org_id="telemetryTrackingManufacturerOrgId",
            type="type",
        )
        assert bus is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.buses.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                name="name",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.list()
        assert_matches_type(BusListResponse, bus, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(BusListResponse, bus, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(BusListResponse, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.delete(
            "id",
        )
        assert bus is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.buses.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.count()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(str, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.query_help()
        assert bus is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.tuple(
            columns="columns",
        )
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(BusTupleResponse, bus, path=["response"])

        assert cast(Any, response.is_closed) is True
