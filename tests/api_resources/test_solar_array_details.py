# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SolarArrayDetailsFull,
    SolarArrayDetailListResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSolarArrayDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solar_array_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solar_array_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = response.parse()
        assert solar_array_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.solar_array_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = response.parse()
            assert solar_array_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solar_array_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            body_id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solar_array_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = response.parse()
        assert solar_array_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.solar_array_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = response.parse()
            assert solar_array_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.solar_array_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_solar_array="SOLARARRAY-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.list()
        assert_matches_type(SyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.list(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_result=0,
            max_results=0,
            source="source",
        )
        assert_matches_type(SyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = response.parse()
        assert_matches_type(SyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.solar_array_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = response.parse()
            assert_matches_type(SyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.delete(
            "id",
        )
        assert solar_array_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = response.parse()
        assert solar_array_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.solar_array_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = response.parse()
            assert solar_array_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.solar_array_details.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.get(
            id="id",
        )
        assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array_detail = client.solar_array_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = response.parse()
        assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.solar_array_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = response.parse()
            assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.solar_array_details.with_raw_response.get(
                id="",
            )


class TestAsyncSolarArrayDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solar_array_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solar_array_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = await response.parse()
        assert solar_array_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = await response.parse()
            assert solar_array_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solar_array_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            body_id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solar_array_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = await response.parse()
        assert solar_array_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = await response.parse()
            assert solar_array_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.solar_array_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_solar_array="SOLARARRAY-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.list()
        assert_matches_type(AsyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.list(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_result=0,
            max_results=0,
            source="source",
        )
        assert_matches_type(AsyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = await response.parse()
            assert_matches_type(AsyncOffsetPage[SolarArrayDetailListResponse], solar_array_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.delete(
            "id",
        )
        assert solar_array_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = await response.parse()
        assert solar_array_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = await response.parse()
            assert solar_array_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.solar_array_details.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.get(
            id="id",
        )
        assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array_detail = await async_client.solar_array_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array_detail = await response.parse()
        assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array_detail = await response.parse()
            assert_matches_type(SolarArrayDetailsFull, solar_array_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.solar_array_details.with_raw_response.get(
                id="",
            )
