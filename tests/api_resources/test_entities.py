# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EntityFull,
    EntityTupleResponse,
    EntityGetAllTypesResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert entity is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            id_entity="idEntity",
            id_location="idLocation",
            id_on_orbit="idOnOrbit",
            id_operating_unit="idOperatingUnit",
            location={
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
            on_orbit={
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
            origin="origin",
            orig_network="origNetwork",
            owner_type="ownerType",
            taskable=True,
            urls=["string"],
        )
        assert entity is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.retrieve(
            "id",
        )
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert entity is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            id_entity="idEntity",
            id_location="idLocation",
            id_on_orbit="idOnOrbit",
            id_operating_unit="idOperatingUnit",
            location={
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
            on_orbit={
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
            origin="origin",
            orig_network="origNetwork",
            owner_type="ownerType",
            taskable=True,
            urls=["string"],
        )
        assert entity is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
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
                classification_marking="classificationMarking",
                data_mode="dataMode",
                name="name",
                source="source",
                type="type",
            )

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
        assert entity is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.entities.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.entities.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        entity = client.entities.tuple(
            columns="columns",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert entity is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            id_entity="idEntity",
            id_location="idLocation",
            id_on_orbit="idOnOrbit",
            id_operating_unit="idOperatingUnit",
            location={
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
            on_orbit={
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
            origin="origin",
            orig_network="origNetwork",
            owner_type="ownerType",
            taskable=True,
            urls=["string"],
        )
        assert entity is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.retrieve(
            "id",
        )
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityFull, entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )
        assert entity is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            id_entity="idEntity",
            id_location="idLocation",
            id_on_orbit="idOnOrbit",
            id_operating_unit="idOperatingUnit",
            location={
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
            on_orbit={
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
            origin="origin",
            orig_network="origNetwork",
            owner_type="ownerType",
            taskable=True,
            urls=["string"],
        )
        assert entity is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            name="name",
            source="source",
            type="type",
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
                classification_marking="classificationMarking",
                data_mode="dataMode",
                name="name",
                source="source",
                type="type",
            )

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
        assert entity is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.entities.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.entities.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        entity = await async_client.entities.tuple(
            columns="columns",
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
