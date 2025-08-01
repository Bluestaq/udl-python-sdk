# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EntityAbridged,
    EntityTupleResponse,
    EntityQueryHelpResponse,
    EntityGetAllTypesResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import EntityFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )
        assert entity is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
            country_code="US",
            id_entity="ENTITY-ID",
            id_location="LOCATION-ID",
            id_on_orbit="ONORBIT-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            location={
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
            on_orbit={
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
            origin="THIRD_PARTY_DATASOURCE",
            owner_type="Commercial",
            taskable=False,
            urls=["URL1", "URL2"],
        )
        assert entity is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.retrieve(
            id="id",
        )
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityFull, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )
        assert entity is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
            country_code="US",
            id_entity="ENTITY-ID",
            id_location="LOCATION-ID",
            id_on_orbit="ONORBIT-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            location={
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
            on_orbit={
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
            origin="THIRD_PARTY_DATASOURCE",
            owner_type="Commercial",
            taskable=False,
            urls=["URL1", "URL2"],
        )
        assert entity is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example name",
                source="Bluestaq",
                type="ONORBIT",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.list()
        assert_matches_type(SyncOffsetPage[EntityAbridged], entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EntityAbridged], entity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(SyncOffsetPage[EntityAbridged], entity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(SyncOffsetPage[EntityAbridged], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.delete(
            "id",
        )
        assert entity is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.count()
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(str, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_all_types(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.get_all_types()
        assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

    @parametrize
    def test_method_get_all_types_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.get_all_types(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_get_all_types(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.get_all_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_get_all_types(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.get_all_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.query_help()
        assert_matches_type(EntityQueryHelpResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityQueryHelpResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityQueryHelpResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.tuple(
            columns="columns",
        )
        assert_matches_type(EntityTupleResponse, entity, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EntityTupleResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityTupleResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityTupleResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )
        assert entity is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
            country_code="US",
            id_entity="ENTITY-ID",
            id_location="LOCATION-ID",
            id_on_orbit="ONORBIT-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            location={
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
            on_orbit={
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
            origin="THIRD_PARTY_DATASOURCE",
            owner_type="Commercial",
            taskable=False,
            urls=["URL1", "URL2"],
        )
        assert entity is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.retrieve(
            id="id",
        )
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityFull, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )
        assert entity is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
            country_code="US",
            id_entity="ENTITY-ID",
            id_location="LOCATION-ID",
            id_on_orbit="ONORBIT-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            location={
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
            on_orbit={
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
            origin="THIRD_PARTY_DATASOURCE",
            owner_type="Commercial",
            taskable=False,
            urls=["URL1", "URL2"],
        )
        assert entity is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            type="ONORBIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example name",
                source="Bluestaq",
                type="ONORBIT",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.list()
        assert_matches_type(AsyncOffsetPage[EntityAbridged], entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EntityAbridged], entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(AsyncOffsetPage[EntityAbridged], entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(AsyncOffsetPage[EntityAbridged], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.delete(
            "id",
        )
        assert entity is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.count()
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(str, entity, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(str, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_all_types(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.get_all_types()
        assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

    @parametrize
    async def test_method_get_all_types_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.get_all_types(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_get_all_types(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.get_all_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_get_all_types(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.get_all_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetAllTypesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.query_help()
        assert_matches_type(EntityQueryHelpResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityQueryHelpResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityQueryHelpResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.tuple(
            columns="columns",
        )
        assert_matches_type(EntityTupleResponse, entity, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EntityTupleResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityTupleResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityTupleResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
