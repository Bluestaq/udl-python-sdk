# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OrganizationFull,
    OrganizationListResponse,
    OrganizationTupleResponse,
    OrganizationGetOrganizationTypesResponse,
    OrganizationGetOrganizationCategoriesResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )
        assert organization is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
            id="ORGANIZATION-ID",
            active=False,
            category="Private company",
            country_code="US",
            description="Example description",
            external_id="EXTERNAL-ID",
            nationality="US",
            origin="some.user",
        )
        assert organization is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )
        assert organization is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
            body_id="ORGANIZATION-ID",
            active=False,
            category="Private company",
            country_code="US",
            description="Example description",
            external_id="EXTERNAL-ID",
            nationality="US",
            origin="some.user",
        )
        assert organization is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.organization.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="some.user",
                source="some.user",
                type="GOVERNMENT",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.list()
        assert_matches_type(SyncOffsetPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncOffsetPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncOffsetPage[OrganizationListResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.delete(
            "id",
        )
        assert organization is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organization.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.count()
        assert_matches_type(str, organization, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, organization, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(str, organization, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(str, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.get(
            id="id",
        )
        assert_matches_type(OrganizationFull, organization, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationFull, organization, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationFull, organization, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationFull, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organization.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_get_organization_categories(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.get_organization_categories()
        assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

    @parametrize
    def test_method_get_organization_categories_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.get_organization_categories(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_get_organization_categories(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.get_organization_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_get_organization_categories(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.get_organization_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_organization_types(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.get_organization_types()
        assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

    @parametrize
    def test_method_get_organization_types_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.get_organization_types(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_get_organization_types(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.get_organization_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_get_organization_types(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.get_organization_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.queryhelp()
        assert organization is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert organization is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.tuple(
            columns="columns",
        )
        assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        organization = client.organization.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.organization.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.organization.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )
        assert organization is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
            id="ORGANIZATION-ID",
            active=False,
            category="Private company",
            country_code="US",
            description="Example description",
            external_id="EXTERNAL-ID",
            nationality="US",
            origin="some.user",
        )
        assert organization is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )
        assert organization is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
            body_id="ORGANIZATION-ID",
            active=False,
            category="Private company",
            country_code="US",
            description="Example description",
            external_id="EXTERNAL-ID",
            nationality="US",
            origin="some.user",
        )
        assert organization is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="some.user",
            source="some.user",
            type="GOVERNMENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.organization.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="some.user",
                source="some.user",
                type="GOVERNMENT",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.list()
        assert_matches_type(AsyncOffsetPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncOffsetPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(AsyncOffsetPage[OrganizationListResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.delete(
            "id",
        )
        assert organization is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organization.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.count()
        assert_matches_type(str, organization, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, organization, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(str, organization, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(str, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.get(
            id="id",
        )
        assert_matches_type(OrganizationFull, organization, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationFull, organization, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationFull, organization, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationFull, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organization.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_get_organization_categories(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.get_organization_categories()
        assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

    @parametrize
    async def test_method_get_organization_categories_with_all_params(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        organization = await async_client.organization.get_organization_categories(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_get_organization_categories(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.get_organization_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_get_organization_categories(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.get_organization_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationGetOrganizationCategoriesResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_organization_types(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.get_organization_types()
        assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

    @parametrize
    async def test_method_get_organization_types_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.get_organization_types(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_get_organization_types(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.get_organization_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_get_organization_types(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.get_organization_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationGetOrganizationTypesResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.queryhelp()
        assert organization is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert organization is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert organization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.tuple(
            columns="columns",
        )
        assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organization = await async_client.organization.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organization.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organization.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationTupleResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
