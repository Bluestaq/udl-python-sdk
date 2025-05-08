# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SiteGetResponse,
    SiteListResponse,
    SiteTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSite:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        site = client.site.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )
        assert site is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        site = client.site.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
            id="SITE-ID",
            activity="OCC",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            be_number="0427RT1030",
            cat_code="20345",
            cat_text="Radar Facility, General",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
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
            eval=7,
            faa="FAA1",
            fpa="EOB",
            funct_primary="JG",
            geo_area="E2",
            geoidal_msl_sep=12.34,
            grade=5,
            iata="AAA",
            icao="ICA1",
            ident="FRIEND",
            id_entity="ENTITY-ID",
            id_parent_site="ID-Parent-Site",
            lz_usage="AF",
            max_runway_length=1000,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="AA",
            msn_primary_spec="AB",
            notes="Example Notes",
            nuc_cap="A",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            orig_lz_id="ORIG-LZ-ID",
            orig_site_id="ORIG-SITE-ID",
            osuffix="BB002",
            pin="25200",
            pol_subdiv="IZO7",
            pop_area=True,
            pop_area_prox=12.345,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            runways=5,
            sym_code="SOGPU----------",
            type="AIRBASE",
            usage="MILITARY",
            utm="19P4390691376966",
            veg_ht=3,
            veg_type="FR",
            wac="0427",
        )
        assert site is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert site is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        site = client.site.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )
        assert site is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        site = client.site.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
            body_id="SITE-ID",
            activity="OCC",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            be_number="0427RT1030",
            cat_code="20345",
            cat_text="Radar Facility, General",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
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
            eval=7,
            faa="FAA1",
            fpa="EOB",
            funct_primary="JG",
            geo_area="E2",
            geoidal_msl_sep=12.34,
            grade=5,
            iata="AAA",
            icao="ICA1",
            ident="FRIEND",
            id_entity="ENTITY-ID",
            id_parent_site="ID-Parent-Site",
            lz_usage="AF",
            max_runway_length=1000,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="AA",
            msn_primary_spec="AB",
            notes="Example Notes",
            nuc_cap="A",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            orig_lz_id="ORIG-LZ-ID",
            orig_site_id="ORIG-SITE-ID",
            osuffix="BB002",
            pin="25200",
            pol_subdiv="IZO7",
            pop_area=True,
            pop_area_prox=12.345,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            runways=5,
            sym_code="SOGPU----------",
            type="AIRBASE",
            usage="MILITARY",
            utm="19P4390691376966",
            veg_ht=3,
            veg_type="FR",
            wac="0427",
        )
        assert site is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert site is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.site.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Site Name",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        site = client.site.list()
        assert_matches_type(SyncOffsetPage[SiteListResponse], site, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        site = client.site.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SiteListResponse], site, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(SyncOffsetPage[SiteListResponse], site, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(SyncOffsetPage[SiteListResponse], site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        site = client.site.count()
        assert_matches_type(str, site, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        site = client.site.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, site, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(str, site, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(str, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        site = client.site.get(
            id="id",
        )
        assert_matches_type(SiteGetResponse, site, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        site = client.site.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteGetResponse, site, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(SiteGetResponse, site, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(SiteGetResponse, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.site.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        site = client.site.queryhelp()
        assert site is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert site is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        site = client.site.tuple(
            columns="columns",
        )
        assert_matches_type(SiteTupleResponse, site, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        site = client.site.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteTupleResponse, site, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.site.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(SiteTupleResponse, site, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.site.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(SiteTupleResponse, site, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSite:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )
        assert site is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
            id="SITE-ID",
            activity="OCC",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            be_number="0427RT1030",
            cat_code="20345",
            cat_text="Radar Facility, General",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
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
            eval=7,
            faa="FAA1",
            fpa="EOB",
            funct_primary="JG",
            geo_area="E2",
            geoidal_msl_sep=12.34,
            grade=5,
            iata="AAA",
            icao="ICA1",
            ident="FRIEND",
            id_entity="ENTITY-ID",
            id_parent_site="ID-Parent-Site",
            lz_usage="AF",
            max_runway_length=1000,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="AA",
            msn_primary_spec="AB",
            notes="Example Notes",
            nuc_cap="A",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            orig_lz_id="ORIG-LZ-ID",
            orig_site_id="ORIG-SITE-ID",
            osuffix="BB002",
            pin="25200",
            pol_subdiv="IZO7",
            pop_area=True,
            pop_area_prox=12.345,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            runways=5,
            sym_code="SOGPU----------",
            type="AIRBASE",
            usage="MILITARY",
            utm="19P4390691376966",
            veg_ht=3,
            veg_type="FR",
            wac="0427",
        )
        assert site is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert site is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )
        assert site is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
            body_id="SITE-ID",
            activity="OCC",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            be_number="0427RT1030",
            cat_code="20345",
            cat_text="Radar Facility, General",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
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
            eval=7,
            faa="FAA1",
            fpa="EOB",
            funct_primary="JG",
            geo_area="E2",
            geoidal_msl_sep=12.34,
            grade=5,
            iata="AAA",
            icao="ICA1",
            ident="FRIEND",
            id_entity="ENTITY-ID",
            id_parent_site="ID-Parent-Site",
            lz_usage="AF",
            max_runway_length=1000,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="AA",
            msn_primary_spec="AB",
            notes="Example Notes",
            nuc_cap="A",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            orig_lz_id="ORIG-LZ-ID",
            orig_site_id="ORIG-SITE-ID",
            osuffix="BB002",
            pin="25200",
            pol_subdiv="IZO7",
            pop_area=True,
            pop_area_prox=12.345,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            runways=5,
            sym_code="SOGPU----------",
            type="AIRBASE",
            usage="MILITARY",
            utm="19P4390691376966",
            veg_ht=3,
            veg_type="FR",
            wac="0427",
        )
        assert site is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert site is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Site Name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.site.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Site Name",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.list()
        assert_matches_type(AsyncOffsetPage[SiteListResponse], site, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SiteListResponse], site, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(AsyncOffsetPage[SiteListResponse], site, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(AsyncOffsetPage[SiteListResponse], site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.count()
        assert_matches_type(str, site, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, site, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(str, site, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(str, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.get(
            id="id",
        )
        assert_matches_type(SiteGetResponse, site, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteGetResponse, site, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(SiteGetResponse, site, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(SiteGetResponse, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.site.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.queryhelp()
        assert site is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert site is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.tuple(
            columns="columns",
        )
        assert_matches_type(SiteTupleResponse, site, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site = await async_client.site.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteTupleResponse, site, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(SiteTupleResponse, site, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(SiteTupleResponse, site, path=["response"])

        assert cast(Any, response.is_closed) is True
