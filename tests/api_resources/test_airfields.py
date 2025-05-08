# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirfieldFull,
    AirfieldAbridged,
    AirfieldTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )
        assert airfield is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
            id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_airfield_id="45301",
            alternative_names=["BELLEVILLE", "JONESTOWN"],
            city="Honolulu",
            country_code="US",
            country_name="United States",
            dst_info="SEE THE ENROUTE SUPP FOR INFORMATION",
            elev_ft=33.562,
            elev_m=10.29,
            faa="FAA1",
            geoloc="XLSX",
            gmt_offset="-4:30",
            host_nat_code="ZPU",
            iata="AAA",
            icao="KCOS",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            info_url="URL Link to the Airfield",
            lat=45.23,
            lon=179.1,
            mag_dec=7.35,
            max_runway_length=1000,
            misc_codes="AMZ",
            origin="THIRD_PARTY_DATASOURCE",
            regional_authority="18TH AF",
            region_name="Hawaii",
            runways=5,
            secondary_icao="PHNL",
            state="Hawaii",
            state_province_code="US15",
            suitability_code_descs=["Suitable C-32", "Suitable C-5", "Suitable C-130"],
            suitability_codes="ABC",
            wac_innr="0409-00039",
            zar_id="231",
        )
        assert airfield is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert airfield is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.retrieve(
            id="id",
        )
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert_matches_type(AirfieldFull, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfields.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )
        assert airfield is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
            body_id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_airfield_id="45301",
            alternative_names=["BELLEVILLE", "JONESTOWN"],
            city="Honolulu",
            country_code="US",
            country_name="United States",
            dst_info="SEE THE ENROUTE SUPP FOR INFORMATION",
            elev_ft=33.562,
            elev_m=10.29,
            faa="FAA1",
            geoloc="XLSX",
            gmt_offset="-4:30",
            host_nat_code="ZPU",
            iata="AAA",
            icao="KCOS",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            info_url="URL Link to the Airfield",
            lat=45.23,
            lon=179.1,
            mag_dec=7.35,
            max_runway_length=1000,
            misc_codes="AMZ",
            origin="THIRD_PARTY_DATASOURCE",
            regional_authority="18TH AF",
            region_name="Hawaii",
            runways=5,
            secondary_icao="PHNL",
            state="Hawaii",
            state_province_code="US15",
            suitability_code_descs=["Suitable C-32", "Suitable C-5", "Suitable C-130"],
            suitability_codes="ABC",
            wac_innr="0409-00039",
            zar_id="231",
        )
        assert airfield is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert airfield is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.airfields.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Hickam Air Force Base",
                source="Bluestaq",
                type="Commercial",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.list()
        assert_matches_type(SyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert_matches_type(SyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert_matches_type(SyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.count()
        assert_matches_type(str, airfield, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, airfield, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert_matches_type(str, airfield, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert_matches_type(str, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.queryhelp()
        assert airfield is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert airfield is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.tuple(
            columns="columns",
        )
        assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirfields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )
        assert airfield is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
            id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_airfield_id="45301",
            alternative_names=["BELLEVILLE", "JONESTOWN"],
            city="Honolulu",
            country_code="US",
            country_name="United States",
            dst_info="SEE THE ENROUTE SUPP FOR INFORMATION",
            elev_ft=33.562,
            elev_m=10.29,
            faa="FAA1",
            geoloc="XLSX",
            gmt_offset="-4:30",
            host_nat_code="ZPU",
            iata="AAA",
            icao="KCOS",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            info_url="URL Link to the Airfield",
            lat=45.23,
            lon=179.1,
            mag_dec=7.35,
            max_runway_length=1000,
            misc_codes="AMZ",
            origin="THIRD_PARTY_DATASOURCE",
            regional_authority="18TH AF",
            region_name="Hawaii",
            runways=5,
            secondary_icao="PHNL",
            state="Hawaii",
            state_province_code="US15",
            suitability_code_descs=["Suitable C-32", "Suitable C-5", "Suitable C-130"],
            suitability_codes="ABC",
            wac_innr="0409-00039",
            zar_id="231",
        )
        assert airfield is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert airfield is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.retrieve(
            id="id",
        )
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert_matches_type(AirfieldFull, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfields.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )
        assert airfield is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
            body_id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_airfield_id="45301",
            alternative_names=["BELLEVILLE", "JONESTOWN"],
            city="Honolulu",
            country_code="US",
            country_name="United States",
            dst_info="SEE THE ENROUTE SUPP FOR INFORMATION",
            elev_ft=33.562,
            elev_m=10.29,
            faa="FAA1",
            geoloc="XLSX",
            gmt_offset="-4:30",
            host_nat_code="ZPU",
            iata="AAA",
            icao="KCOS",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            info_url="URL Link to the Airfield",
            lat=45.23,
            lon=179.1,
            mag_dec=7.35,
            max_runway_length=1000,
            misc_codes="AMZ",
            origin="THIRD_PARTY_DATASOURCE",
            regional_authority="18TH AF",
            region_name="Hawaii",
            runways=5,
            secondary_icao="PHNL",
            state="Hawaii",
            state_province_code="US15",
            suitability_code_descs=["Suitable C-32", "Suitable C-5", "Suitable C-130"],
            suitability_codes="ABC",
            wac_innr="0409-00039",
            zar_id="231",
        )
        assert airfield is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert airfield is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Hickam Air Force Base",
            source="Bluestaq",
            type="Commercial",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.airfields.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Hickam Air Force Base",
                source="Bluestaq",
                type="Commercial",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.list()
        assert_matches_type(AsyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert_matches_type(AsyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert_matches_type(AsyncOffsetPage[AirfieldAbridged], airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.count()
        assert_matches_type(str, airfield, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, airfield, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert_matches_type(str, airfield, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert_matches_type(str, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.queryhelp()
        assert airfield is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert airfield is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.tuple(
            columns="columns",
        )
        assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert_matches_type(AirfieldTupleResponse, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True
