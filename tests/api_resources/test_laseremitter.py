# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaseremitterGetResponse,
    LaseremitterListResponse,
    LaseremitterTupleResponse,
    LaseremitterQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaseremitter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )
        assert laseremitter is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            atmospheric_transmission=1,
            beam_output_power=100.5,
            beam_waist=14.4,
            divergence=2.5,
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
            id_entity="ENTITY-ID",
            is_operational=True,
            max_duration=1.5,
            max_focus_range=30000.5,
            min_focus_range=2500.5,
            origin="THIRD_PARTY_DATASOURCE",
            pulse_fluence=1000005.5,
            pulse_peak_power=640.25,
            pulse_rep_freq=2225.5,
            pulse_shape="RECTANGULAR",
            pulse_width=0.25,
            wavelength=0.11,
        )
        assert laseremitter is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert laseremitter is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert laseremitter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )
        assert laseremitter is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            atmospheric_transmission=1,
            beam_output_power=100.5,
            beam_waist=14.4,
            divergence=2.5,
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
            id_entity="ENTITY-ID",
            is_operational=True,
            max_duration=1.5,
            max_focus_range=30000.5,
            min_focus_range=2500.5,
            origin="THIRD_PARTY_DATASOURCE",
            pulse_fluence=1000005.5,
            pulse_peak_power=640.25,
            pulse_rep_freq=2225.5,
            pulse_shape="RECTANGULAR",
            pulse_width=0.25,
            wavelength=0.11,
        )
        assert laseremitter is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert laseremitter is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert laseremitter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.laseremitter.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                laser_name="HEL",
                laser_type="PULSED",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.list()
        assert_matches_type(SyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert_matches_type(SyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert_matches_type(SyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.delete(
            "id",
        )
        assert laseremitter is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert laseremitter is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert laseremitter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.laseremitter.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.count()
        assert_matches_type(str, laseremitter, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, laseremitter, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert_matches_type(str, laseremitter, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert_matches_type(str, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.get(
            id="id",
        )
        assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.laseremitter.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.queryhelp()
        assert_matches_type(LaseremitterQueryhelpResponse, laseremitter, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert_matches_type(LaseremitterQueryhelpResponse, laseremitter, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert_matches_type(LaseremitterQueryhelpResponse, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.tuple(
            columns="columns",
        )
        assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        laseremitter = client.laseremitter.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = response.parse()
        assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = response.parse()
            assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLaseremitter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )
        assert laseremitter is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            atmospheric_transmission=1,
            beam_output_power=100.5,
            beam_waist=14.4,
            divergence=2.5,
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
            id_entity="ENTITY-ID",
            is_operational=True,
            max_duration=1.5,
            max_focus_range=30000.5,
            min_focus_range=2500.5,
            origin="THIRD_PARTY_DATASOURCE",
            pulse_fluence=1000005.5,
            pulse_peak_power=640.25,
            pulse_rep_freq=2225.5,
            pulse_shape="RECTANGULAR",
            pulse_width=0.25,
            wavelength=0.11,
        )
        assert laseremitter is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert laseremitter is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert laseremitter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )
        assert laseremitter is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            atmospheric_transmission=1,
            beam_output_power=100.5,
            beam_waist=14.4,
            divergence=2.5,
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
            id_entity="ENTITY-ID",
            is_operational=True,
            max_duration=1.5,
            max_focus_range=30000.5,
            min_focus_range=2500.5,
            origin="THIRD_PARTY_DATASOURCE",
            pulse_fluence=1000005.5,
            pulse_peak_power=640.25,
            pulse_rep_freq=2225.5,
            pulse_shape="RECTANGULAR",
            pulse_width=0.25,
            wavelength=0.11,
        )
        assert laseremitter is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert laseremitter is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            laser_name="HEL",
            laser_type="PULSED",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert laseremitter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.laseremitter.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                laser_name="HEL",
                laser_type="PULSED",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.list()
        assert_matches_type(AsyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert_matches_type(AsyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert_matches_type(AsyncOffsetPage[LaseremitterListResponse], laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.delete(
            "id",
        )
        assert laseremitter is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert laseremitter is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert laseremitter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.laseremitter.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.count()
        assert_matches_type(str, laseremitter, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, laseremitter, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert_matches_type(str, laseremitter, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert_matches_type(str, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.get(
            id="id",
        )
        assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert_matches_type(LaseremitterGetResponse, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.laseremitter.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.queryhelp()
        assert_matches_type(LaseremitterQueryhelpResponse, laseremitter, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert_matches_type(LaseremitterQueryhelpResponse, laseremitter, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert_matches_type(LaseremitterQueryhelpResponse, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.tuple(
            columns="columns",
        )
        assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laseremitter = await async_client.laseremitter.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laseremitter = await response.parse()
        assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laseremitter = await response.parse()
            assert_matches_type(LaseremitterTupleResponse, laseremitter, path=["response"])

        assert cast(Any, response.is_closed) is True
