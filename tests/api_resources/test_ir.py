# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    IrGetResponse,
    IrListResponse,
    IrTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert ir is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            id="IR-ID",
            description="Example description",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert ir is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert ir is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert ir is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            body_id="IR-ID",
            description="Example description",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert ir is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert ir is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.ir.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example name",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.list()
        assert_matches_type(SyncOffsetPage[IrListResponse], ir, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[IrListResponse], ir, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert_matches_type(SyncOffsetPage[IrListResponse], ir, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert_matches_type(SyncOffsetPage[IrListResponse], ir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.delete(
            "id",
        )
        assert ir is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert ir is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ir.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.count()
        assert_matches_type(str, ir, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ir, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert_matches_type(str, ir, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert_matches_type(str, ir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.get(
            id="id",
        )
        assert_matches_type(IrGetResponse, ir, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(IrGetResponse, ir, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert_matches_type(IrGetResponse, ir, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert_matches_type(IrGetResponse, ir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ir.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.queryhelp()
        assert ir is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert ir is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.tuple(
            columns="columns",
        )
        assert_matches_type(IrTupleResponse, ir, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        ir = client.ir.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(IrTupleResponse, ir, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.ir.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = response.parse()
        assert_matches_type(IrTupleResponse, ir, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.ir.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = response.parse()
            assert_matches_type(IrTupleResponse, ir, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert ir is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            id="IR-ID",
            description="Example description",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert ir is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert ir is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert ir is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            body_id="IR-ID",
            description="Example description",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert ir is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert ir is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.ir.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example name",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.list()
        assert_matches_type(AsyncOffsetPage[IrListResponse], ir, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[IrListResponse], ir, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert_matches_type(AsyncOffsetPage[IrListResponse], ir, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert_matches_type(AsyncOffsetPage[IrListResponse], ir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.delete(
            "id",
        )
        assert ir is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert ir is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ir.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.count()
        assert_matches_type(str, ir, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ir, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert_matches_type(str, ir, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert_matches_type(str, ir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.get(
            id="id",
        )
        assert_matches_type(IrGetResponse, ir, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(IrGetResponse, ir, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert_matches_type(IrGetResponse, ir, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert_matches_type(IrGetResponse, ir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ir.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.queryhelp()
        assert ir is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert ir is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert ir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.tuple(
            columns="columns",
        )
        assert_matches_type(IrTupleResponse, ir, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ir = await async_client.ir.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(IrTupleResponse, ir, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ir.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ir = await response.parse()
        assert_matches_type(IrTupleResponse, ir, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ir.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ir = await response.parse()
            assert_matches_type(IrTupleResponse, ir, path=["response"])

        assert cast(Any, response.is_closed) is True
