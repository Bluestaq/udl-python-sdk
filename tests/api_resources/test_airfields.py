# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirfieldFull,
    AirfieldListResponse,
    AirfieldTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert airfield is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            id="id",
            alt_airfield_id="altAirfieldId",
            city="city",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_ft=0,
            elev_m=0,
            faa="faa",
            geoloc="geoloc",
            gmt_offset="gmtOffset",
            host_nat_code="hostNatCode",
            iata="iata",
            icao="icao",
            id_site="idSite",
            info_url="infoURL",
            lat=0,
            lon=0,
            mag_dec=0,
            max_runway_length=0,
            misc_codes="miscCodes",
            origin="origin",
            orig_network="origNetwork",
            region_name="regionName",
            runways=0,
            source_dl="sourceDL",
            state="state",
            suitability_codes="suitabilityCodes",
            wac_innr="wacINNR",
            zar_id="zarId",
        )
        assert airfield is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert airfield is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.retrieve(
            "id",
        )
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert airfield is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            id_2="id",
            alt_airfield_id="altAirfieldId",
            city="city",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_ft=0,
            elev_m=0,
            faa="faa",
            geoloc="geoloc",
            gmt_offset="gmtOffset",
            host_nat_code="hostNatCode",
            iata="iata",
            icao="icao",
            id_site="idSite",
            info_url="infoURL",
            lat=0,
            lon=0,
            mag_dec=0,
            max_runway_length=0,
            misc_codes="miscCodes",
            origin="origin",
            orig_network="origNetwork",
            region_name="regionName",
            runways=0,
            source_dl="sourceDL",
            state="state",
            suitability_codes="suitabilityCodes",
            wac_innr="wacINNR",
            zar_id="zarId",
        )
        assert airfield is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert airfield is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.airfields.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                name="name",
                source="source",
                type="type",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.list()
        assert_matches_type(AirfieldListResponse, airfield, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airfields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = response.parse()
        assert_matches_type(AirfieldListResponse, airfield, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airfields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = response.parse()
            assert_matches_type(AirfieldListResponse, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airfield = client.airfields.count()
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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert airfield is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            id="id",
            alt_airfield_id="altAirfieldId",
            city="city",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_ft=0,
            elev_m=0,
            faa="faa",
            geoloc="geoloc",
            gmt_offset="gmtOffset",
            host_nat_code="hostNatCode",
            iata="iata",
            icao="icao",
            id_site="idSite",
            info_url="infoURL",
            lat=0,
            lon=0,
            mag_dec=0,
            max_runway_length=0,
            misc_codes="miscCodes",
            origin="origin",
            orig_network="origNetwork",
            region_name="regionName",
            runways=0,
            source_dl="sourceDL",
            state="state",
            suitability_codes="suitabilityCodes",
            wac_innr="wacINNR",
            zar_id="zarId",
        )
        assert airfield is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert airfield is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.retrieve(
            "id",
        )
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert_matches_type(AirfieldFull, airfield, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert airfield is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            id_2="id",
            alt_airfield_id="altAirfieldId",
            city="city",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_ft=0,
            elev_m=0,
            faa="faa",
            geoloc="geoloc",
            gmt_offset="gmtOffset",
            host_nat_code="hostNatCode",
            iata="iata",
            icao="icao",
            id_site="idSite",
            info_url="infoURL",
            lat=0,
            lon=0,
            mag_dec=0,
            max_runway_length=0,
            misc_codes="miscCodes",
            origin="origin",
            orig_network="origNetwork",
            region_name="regionName",
            runways=0,
            source_dl="sourceDL",
            state="state",
            suitability_codes="suitabilityCodes",
            wac_innr="wacINNR",
            zar_id="zarId",
        )
        assert airfield is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert airfield is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert airfield is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.airfields.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                name="name",
                source="source",
                type="type",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.list()
        assert_matches_type(AirfieldListResponse, airfield, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield = await response.parse()
        assert_matches_type(AirfieldListResponse, airfield, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield = await response.parse()
            assert_matches_type(AirfieldListResponse, airfield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield = await async_client.airfields.count()
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
