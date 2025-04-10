# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeradatanavigationGetResponse,
    SeradatanavigationListResponse,
    SeradatanavigationTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeradatanavigation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatanavigation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATANAVIGATION-ID",
            area_coverage="Worldwide",
            clock_type="Rubidium",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_navigation="idNavigation",
            location_accuracy=1.23,
            manufacturer_org_id="manufacturerOrgId",
            mode_frequency="1234",
            modes="Military",
            name="WAAS GEO-5",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_type="WAAS",
        )
        assert seradatanavigation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert seradatanavigation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatanavigation is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATANAVIGATION-ID",
            area_coverage="Worldwide",
            clock_type="Rubidium",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_navigation="idNavigation",
            location_accuracy=1.23,
            manufacturer_org_id="manufacturerOrgId",
            mode_frequency="1234",
            modes="Military",
            name="WAAS GEO-5",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_type="WAAS",
        )
        assert seradatanavigation is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert seradatanavigation is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.seradatanavigation.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.list()
        assert_matches_type(SeradatanavigationListResponse, seradatanavigation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert_matches_type(SeradatanavigationListResponse, seradatanavigation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert_matches_type(SeradatanavigationListResponse, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.delete(
            "id",
        )
        assert seradatanavigation is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert seradatanavigation is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradatanavigation.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.count()
        assert_matches_type(str, seradatanavigation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert_matches_type(str, seradatanavigation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert_matches_type(str, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.get(
            "id",
        )
        assert_matches_type(SeradatanavigationGetResponse, seradatanavigation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert_matches_type(SeradatanavigationGetResponse, seradatanavigation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert_matches_type(SeradatanavigationGetResponse, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradatanavigation.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.queryhelp()
        assert seradatanavigation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert seradatanavigation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        seradatanavigation = client.seradatanavigation.tuple(
            columns="columns",
        )
        assert_matches_type(SeradatanavigationTupleResponse, seradatanavigation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.seradatanavigation.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = response.parse()
        assert_matches_type(SeradatanavigationTupleResponse, seradatanavigation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.seradatanavigation.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = response.parse()
            assert_matches_type(SeradatanavigationTupleResponse, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeradatanavigation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatanavigation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATANAVIGATION-ID",
            area_coverage="Worldwide",
            clock_type="Rubidium",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_navigation="idNavigation",
            location_accuracy=1.23,
            manufacturer_org_id="manufacturerOrgId",
            mode_frequency="1234",
            modes="Military",
            name="WAAS GEO-5",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_type="WAAS",
        )
        assert seradatanavigation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert seradatanavigation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatanavigation is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATANAVIGATION-ID",
            area_coverage="Worldwide",
            clock_type="Rubidium",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_navigation="idNavigation",
            location_accuracy=1.23,
            manufacturer_org_id="manufacturerOrgId",
            mode_frequency="1234",
            modes="Military",
            name="WAAS GEO-5",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_type="WAAS",
        )
        assert seradatanavigation is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert seradatanavigation is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.seradatanavigation.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.list()
        assert_matches_type(SeradatanavigationListResponse, seradatanavigation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert_matches_type(SeradatanavigationListResponse, seradatanavigation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert_matches_type(SeradatanavigationListResponse, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.delete(
            "id",
        )
        assert seradatanavigation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert seradatanavigation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradatanavigation.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.count()
        assert_matches_type(str, seradatanavigation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert_matches_type(str, seradatanavigation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert_matches_type(str, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.get(
            "id",
        )
        assert_matches_type(SeradatanavigationGetResponse, seradatanavigation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert_matches_type(SeradatanavigationGetResponse, seradatanavigation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert_matches_type(SeradatanavigationGetResponse, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradatanavigation.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.queryhelp()
        assert seradatanavigation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert seradatanavigation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert seradatanavigation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatanavigation = await async_client.seradatanavigation.tuple(
            columns="columns",
        )
        assert_matches_type(SeradatanavigationTupleResponse, seradatanavigation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatanavigation.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatanavigation = await response.parse()
        assert_matches_type(SeradatanavigationTupleResponse, seradatanavigation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatanavigation.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatanavigation = await response.parse()
            assert_matches_type(SeradatanavigationTupleResponse, seradatanavigation, path=["response"])

        assert cast(Any, response.is_closed) is True
