# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.diplomatic_clearance import (
    CountryListResponse,
    CountryTupleResponse,
    CountryRetrieveResponse,
    CountryQueryHelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCountry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert country is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            accepts_dms=True,
            accepts_email=True,
            accepts_fax=True,
            accepts_sipr_net=False,
            agency="TACC",
            alt_country_code="IZ",
            close_time="16:00",
            country_id="GDSSBL010412140742262246",
            country_name="NETHERLANDS",
            country_remark="Amsterdam airport EHAM will not accept hazardous cargo.",
            diplomatic_clearance_country_contacts=[
                {
                    "ah_num": "256039858",
                    "ah_spd_dial_code": "75",
                    "comm_num": "904716104",
                    "comm_spd_dial_code": "74",
                    "contact_id": "GDSSMC112108191329534522",
                    "contact_name": "John Smith",
                    "contact_remark": "Contact remark",
                    "dsn_num": "513827215",
                    "dsn_spd_dial_code": "94",
                    "fax_num": "571654897",
                    "nipr_num": "525574441",
                    "sipr_num": "546144352",
                }
            ],
            diplomatic_clearance_country_entry_exit_points=[
                {
                    "is_entry": True,
                    "is_exit": True,
                    "point_name": "BATEL",
                }
            ],
            diplomatic_clearance_country_profiles=[
                {
                    "cargo_pax_remark": "Cargo passenger remark",
                    "clearance_id": "MDCNPER231360050AAR",
                    "crew_info_remark": "Crew info remark",
                    "def_clearance_status": "R",
                    "def_entry_remark": "Default entry remark",
                    "def_entry_time": "15:00",
                    "def_exit_remark": "Default exit remark",
                    "def_exit_time": "17:00",
                    "flt_info_remark": "Flight info remark",
                    "haz_info_remark": "Hazmat remark",
                    "land_def_prof": True,
                    "land_lead_time": 7,
                    "land_lead_time_remark": "Landing lead time remark",
                    "land_lead_time_unit": "Day",
                    "land_valid_period_minus": 0,
                    "land_valid_period_plus": 72,
                    "land_valid_period_remark": "Landing valid period remark",
                    "land_valid_period_unit": "Hour",
                    "overfly_def_prof": True,
                    "overfly_lead_time": 7,
                    "overfly_lead_time_remark": "Overfly remark",
                    "overfly_lead_time_unit": "Day",
                    "overfly_valid_period_minus": 0,
                    "overfly_valid_period_plus": 72,
                    "overfly_valid_period_remark": "Overfly valid period remark",
                    "overfly_valid_period_unit": "Hour",
                    "profile": "Netherlands Non Haz Landing",
                    "profile_agency": "USAFE",
                    "profile_id": "GDSSBL010412140742262247",
                    "profile_remark": "Profile remark",
                    "req_ac_alt_name": False,
                    "req_all_haz_info": False,
                    "req_amc_std_info": False,
                    "req_cargo_list": False,
                    "req_cargo_pax": False,
                    "req_class1_info": False,
                    "req_class9_info": False,
                    "req_crew_comp": False,
                    "req_crew_detail": False,
                    "req_crew_info": False,
                    "req_div1_info": False,
                    "req_dv": False,
                    "req_entry_exit_coord": False,
                    "req_flt_info": False,
                    "req_flt_plan_route": False,
                    "req_fund_source": False,
                    "req_haz_info": False,
                    "req_icao": False,
                    "req_passport_info": False,
                    "req_raven": False,
                    "req_rep_change": False,
                    "req_tail_num": False,
                    "req_weapons_info": False,
                    "undefined_crew_reporting": False,
                }
            ],
            existing_profile=True,
            gmt_offset="-04:30",
            office_name="DAO.EU",
            office_poc="John Smith",
            office_remark="Diplomatic clearance office remark",
            open_fri=True,
            open_mon=True,
            open_sat=False,
            open_sun=False,
            open_thu=True,
            open_time="07:00",
            open_tue=True,
            open_wed=True,
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert country is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert country is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.retrieve(
            id="id",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryRetrieveResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.diplomatic_clearance.country.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert country is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            accepts_dms=True,
            accepts_email=True,
            accepts_fax=True,
            accepts_sipr_net=False,
            agency="TACC",
            alt_country_code="IZ",
            close_time="16:00",
            country_id="GDSSBL010412140742262246",
            country_name="NETHERLANDS",
            country_remark="Amsterdam airport EHAM will not accept hazardous cargo.",
            diplomatic_clearance_country_contacts=[
                {
                    "ah_num": "256039858",
                    "ah_spd_dial_code": "75",
                    "comm_num": "904716104",
                    "comm_spd_dial_code": "74",
                    "contact_id": "GDSSMC112108191329534522",
                    "contact_name": "John Smith",
                    "contact_remark": "Contact remark",
                    "dsn_num": "513827215",
                    "dsn_spd_dial_code": "94",
                    "fax_num": "571654897",
                    "nipr_num": "525574441",
                    "sipr_num": "546144352",
                }
            ],
            diplomatic_clearance_country_entry_exit_points=[
                {
                    "is_entry": True,
                    "is_exit": True,
                    "point_name": "BATEL",
                }
            ],
            diplomatic_clearance_country_profiles=[
                {
                    "cargo_pax_remark": "Cargo passenger remark",
                    "clearance_id": "MDCNPER231360050AAR",
                    "crew_info_remark": "Crew info remark",
                    "def_clearance_status": "R",
                    "def_entry_remark": "Default entry remark",
                    "def_entry_time": "15:00",
                    "def_exit_remark": "Default exit remark",
                    "def_exit_time": "17:00",
                    "flt_info_remark": "Flight info remark",
                    "haz_info_remark": "Hazmat remark",
                    "land_def_prof": True,
                    "land_lead_time": 7,
                    "land_lead_time_remark": "Landing lead time remark",
                    "land_lead_time_unit": "Day",
                    "land_valid_period_minus": 0,
                    "land_valid_period_plus": 72,
                    "land_valid_period_remark": "Landing valid period remark",
                    "land_valid_period_unit": "Hour",
                    "overfly_def_prof": True,
                    "overfly_lead_time": 7,
                    "overfly_lead_time_remark": "Overfly remark",
                    "overfly_lead_time_unit": "Day",
                    "overfly_valid_period_minus": 0,
                    "overfly_valid_period_plus": 72,
                    "overfly_valid_period_remark": "Overfly valid period remark",
                    "overfly_valid_period_unit": "Hour",
                    "profile": "Netherlands Non Haz Landing",
                    "profile_agency": "USAFE",
                    "profile_id": "GDSSBL010412140742262247",
                    "profile_remark": "Profile remark",
                    "req_ac_alt_name": False,
                    "req_all_haz_info": False,
                    "req_amc_std_info": False,
                    "req_cargo_list": False,
                    "req_cargo_pax": False,
                    "req_class1_info": False,
                    "req_class9_info": False,
                    "req_crew_comp": False,
                    "req_crew_detail": False,
                    "req_crew_info": False,
                    "req_div1_info": False,
                    "req_dv": False,
                    "req_entry_exit_coord": False,
                    "req_flt_info": False,
                    "req_flt_plan_route": False,
                    "req_fund_source": False,
                    "req_haz_info": False,
                    "req_icao": False,
                    "req_passport_info": False,
                    "req_raven": False,
                    "req_rep_change": False,
                    "req_tail_num": False,
                    "req_weapons_info": False,
                    "undefined_crew_reporting": False,
                }
            ],
            existing_profile=True,
            gmt_offset="-04:30",
            office_name="DAO.EU",
            office_poc="John Smith",
            office_remark="Diplomatic clearance office remark",
            open_fri=True,
            open_mon=True,
            open_sat=False,
            open_sun=False,
            open_thu=True,
            open_time="07:00",
            open_tue=True,
            open_wed=True,
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert country is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert country is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.diplomatic_clearance.country.with_raw_response.update(
                path_id="",
                classification_marking="U",
                country_code="NL",
                data_mode="TEST",
                last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.list()
        assert_matches_type(SyncOffsetPage[CountryListResponse], country, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[CountryListResponse], country, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(SyncOffsetPage[CountryListResponse], country, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(SyncOffsetPage[CountryListResponse], country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.delete(
            "id",
        )
        assert country is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert country is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.diplomatic_clearance.country.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.count()
        assert_matches_type(str, country, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, country, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(str, country, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(str, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert country is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert country is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.query_help()
        assert_matches_type(CountryQueryHelpResponse, country, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryQueryHelpResponse, country, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryQueryHelpResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.tuple(
            columns="columns",
        )
        assert_matches_type(CountryTupleResponse, country, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CountryTupleResponse, country, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryTupleResponse, country, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryTupleResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        country = client.diplomatic_clearance.country.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert country is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.country.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert country is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.country.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCountry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert country is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            accepts_dms=True,
            accepts_email=True,
            accepts_fax=True,
            accepts_sipr_net=False,
            agency="TACC",
            alt_country_code="IZ",
            close_time="16:00",
            country_id="GDSSBL010412140742262246",
            country_name="NETHERLANDS",
            country_remark="Amsterdam airport EHAM will not accept hazardous cargo.",
            diplomatic_clearance_country_contacts=[
                {
                    "ah_num": "256039858",
                    "ah_spd_dial_code": "75",
                    "comm_num": "904716104",
                    "comm_spd_dial_code": "74",
                    "contact_id": "GDSSMC112108191329534522",
                    "contact_name": "John Smith",
                    "contact_remark": "Contact remark",
                    "dsn_num": "513827215",
                    "dsn_spd_dial_code": "94",
                    "fax_num": "571654897",
                    "nipr_num": "525574441",
                    "sipr_num": "546144352",
                }
            ],
            diplomatic_clearance_country_entry_exit_points=[
                {
                    "is_entry": True,
                    "is_exit": True,
                    "point_name": "BATEL",
                }
            ],
            diplomatic_clearance_country_profiles=[
                {
                    "cargo_pax_remark": "Cargo passenger remark",
                    "clearance_id": "MDCNPER231360050AAR",
                    "crew_info_remark": "Crew info remark",
                    "def_clearance_status": "R",
                    "def_entry_remark": "Default entry remark",
                    "def_entry_time": "15:00",
                    "def_exit_remark": "Default exit remark",
                    "def_exit_time": "17:00",
                    "flt_info_remark": "Flight info remark",
                    "haz_info_remark": "Hazmat remark",
                    "land_def_prof": True,
                    "land_lead_time": 7,
                    "land_lead_time_remark": "Landing lead time remark",
                    "land_lead_time_unit": "Day",
                    "land_valid_period_minus": 0,
                    "land_valid_period_plus": 72,
                    "land_valid_period_remark": "Landing valid period remark",
                    "land_valid_period_unit": "Hour",
                    "overfly_def_prof": True,
                    "overfly_lead_time": 7,
                    "overfly_lead_time_remark": "Overfly remark",
                    "overfly_lead_time_unit": "Day",
                    "overfly_valid_period_minus": 0,
                    "overfly_valid_period_plus": 72,
                    "overfly_valid_period_remark": "Overfly valid period remark",
                    "overfly_valid_period_unit": "Hour",
                    "profile": "Netherlands Non Haz Landing",
                    "profile_agency": "USAFE",
                    "profile_id": "GDSSBL010412140742262247",
                    "profile_remark": "Profile remark",
                    "req_ac_alt_name": False,
                    "req_all_haz_info": False,
                    "req_amc_std_info": False,
                    "req_cargo_list": False,
                    "req_cargo_pax": False,
                    "req_class1_info": False,
                    "req_class9_info": False,
                    "req_crew_comp": False,
                    "req_crew_detail": False,
                    "req_crew_info": False,
                    "req_div1_info": False,
                    "req_dv": False,
                    "req_entry_exit_coord": False,
                    "req_flt_info": False,
                    "req_flt_plan_route": False,
                    "req_fund_source": False,
                    "req_haz_info": False,
                    "req_icao": False,
                    "req_passport_info": False,
                    "req_raven": False,
                    "req_rep_change": False,
                    "req_tail_num": False,
                    "req_weapons_info": False,
                    "undefined_crew_reporting": False,
                }
            ],
            existing_profile=True,
            gmt_offset="-04:30",
            office_name="DAO.EU",
            office_poc="John Smith",
            office_remark="Diplomatic clearance office remark",
            open_fri=True,
            open_mon=True,
            open_sat=False,
            open_sun=False,
            open_thu=True,
            open_time="07:00",
            open_tue=True,
            open_wed=True,
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert country is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert country is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.create(
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.retrieve(
            id="id",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryRetrieveResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.diplomatic_clearance.country.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert country is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            accepts_dms=True,
            accepts_email=True,
            accepts_fax=True,
            accepts_sipr_net=False,
            agency="TACC",
            alt_country_code="IZ",
            close_time="16:00",
            country_id="GDSSBL010412140742262246",
            country_name="NETHERLANDS",
            country_remark="Amsterdam airport EHAM will not accept hazardous cargo.",
            diplomatic_clearance_country_contacts=[
                {
                    "ah_num": "256039858",
                    "ah_spd_dial_code": "75",
                    "comm_num": "904716104",
                    "comm_spd_dial_code": "74",
                    "contact_id": "GDSSMC112108191329534522",
                    "contact_name": "John Smith",
                    "contact_remark": "Contact remark",
                    "dsn_num": "513827215",
                    "dsn_spd_dial_code": "94",
                    "fax_num": "571654897",
                    "nipr_num": "525574441",
                    "sipr_num": "546144352",
                }
            ],
            diplomatic_clearance_country_entry_exit_points=[
                {
                    "is_entry": True,
                    "is_exit": True,
                    "point_name": "BATEL",
                }
            ],
            diplomatic_clearance_country_profiles=[
                {
                    "cargo_pax_remark": "Cargo passenger remark",
                    "clearance_id": "MDCNPER231360050AAR",
                    "crew_info_remark": "Crew info remark",
                    "def_clearance_status": "R",
                    "def_entry_remark": "Default entry remark",
                    "def_entry_time": "15:00",
                    "def_exit_remark": "Default exit remark",
                    "def_exit_time": "17:00",
                    "flt_info_remark": "Flight info remark",
                    "haz_info_remark": "Hazmat remark",
                    "land_def_prof": True,
                    "land_lead_time": 7,
                    "land_lead_time_remark": "Landing lead time remark",
                    "land_lead_time_unit": "Day",
                    "land_valid_period_minus": 0,
                    "land_valid_period_plus": 72,
                    "land_valid_period_remark": "Landing valid period remark",
                    "land_valid_period_unit": "Hour",
                    "overfly_def_prof": True,
                    "overfly_lead_time": 7,
                    "overfly_lead_time_remark": "Overfly remark",
                    "overfly_lead_time_unit": "Day",
                    "overfly_valid_period_minus": 0,
                    "overfly_valid_period_plus": 72,
                    "overfly_valid_period_remark": "Overfly valid period remark",
                    "overfly_valid_period_unit": "Hour",
                    "profile": "Netherlands Non Haz Landing",
                    "profile_agency": "USAFE",
                    "profile_id": "GDSSBL010412140742262247",
                    "profile_remark": "Profile remark",
                    "req_ac_alt_name": False,
                    "req_all_haz_info": False,
                    "req_amc_std_info": False,
                    "req_cargo_list": False,
                    "req_cargo_pax": False,
                    "req_class1_info": False,
                    "req_class9_info": False,
                    "req_crew_comp": False,
                    "req_crew_detail": False,
                    "req_crew_info": False,
                    "req_div1_info": False,
                    "req_dv": False,
                    "req_entry_exit_coord": False,
                    "req_flt_info": False,
                    "req_flt_plan_route": False,
                    "req_fund_source": False,
                    "req_haz_info": False,
                    "req_icao": False,
                    "req_passport_info": False,
                    "req_raven": False,
                    "req_rep_change": False,
                    "req_tail_num": False,
                    "req_weapons_info": False,
                    "undefined_crew_reporting": False,
                }
            ],
            existing_profile=True,
            gmt_offset="-04:30",
            office_name="DAO.EU",
            office_poc="John Smith",
            office_remark="Diplomatic clearance office remark",
            open_fri=True,
            open_mon=True,
            open_sat=False,
            open_sun=False,
            open_thu=True,
            open_time="07:00",
            open_tue=True,
            open_wed=True,
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert country is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert country is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            country_code="NL",
            data_mode="TEST",
            last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.diplomatic_clearance.country.with_raw_response.update(
                path_id="",
                classification_marking="U",
                country_code="NL",
                data_mode="TEST",
                last_changed_date=parse_datetime("2024-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.list()
        assert_matches_type(AsyncOffsetPage[CountryListResponse], country, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[CountryListResponse], country, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(AsyncOffsetPage[CountryListResponse], country, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(AsyncOffsetPage[CountryListResponse], country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.delete(
            "id",
        )
        assert country is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert country is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.diplomatic_clearance.country.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.count()
        assert_matches_type(str, country, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, country, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(str, country, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(str, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert country is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert country is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.query_help()
        assert_matches_type(CountryQueryHelpResponse, country, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryQueryHelpResponse, country, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryQueryHelpResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.tuple(
            columns="columns",
        )
        assert_matches_type(CountryTupleResponse, country, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CountryTupleResponse, country, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryTupleResponse, country, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryTupleResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        country = await async_client.diplomatic_clearance.country.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert country is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.country.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert country is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.country.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "NL",
                    "data_mode": "TEST",
                    "last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert country is None

        assert cast(Any, response.is_closed) is True
