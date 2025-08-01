# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OrganizationdetailListResponse,
    OrganizationdetailFindBySourceResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import OrganizationDetailsFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizationdetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )
        assert organizationdetail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
            id="ORGANIZATIONDETAILS-ID",
            address1="123 Main Street",
            address2="Apt 4B",
            address3="Colorado Springs CO, 80903",
            broker="some.user",
            ceo="some.user",
            cfo="some.user",
            cto="some.user",
            description="Example description",
            ebitda=123.4,
            email="some_organization@organization.com",
            financial_notes="Example notes",
            financial_year_end_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            fleet_plan_notes="Example notes",
            former_org_id="FORMERORG-ID",
            ftes=123,
            geo_admin_level1="Colorado",
            geo_admin_level2="El Paso County",
            geo_admin_level3="Colorado Springs",
            mass_ranking=123,
            origin="some.user",
            parent_org_id="PARENTORG-ID",
            postal_code="80903",
            profit=123.4,
            revenue=123.4,
            revenue_ranking=123,
            risk_manager="some.user",
            services_notes="Example notes",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert organizationdetail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.organizationdetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = response.parse()
        assert organizationdetail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.organizationdetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = response.parse()
            assert organizationdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )
        assert organizationdetail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
            body_id="ORGANIZATIONDETAILS-ID",
            address1="123 Main Street",
            address2="Apt 4B",
            address3="Colorado Springs CO, 80903",
            broker="some.user",
            ceo="some.user",
            cfo="some.user",
            cto="some.user",
            description="Example description",
            ebitda=123.4,
            email="some_organization@organization.com",
            financial_notes="Example notes",
            financial_year_end_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            fleet_plan_notes="Example notes",
            former_org_id="FORMERORG-ID",
            ftes=123,
            geo_admin_level1="Colorado",
            geo_admin_level2="El Paso County",
            geo_admin_level3="Colorado Springs",
            mass_ranking=123,
            origin="some.user",
            parent_org_id="PARENTORG-ID",
            postal_code="80903",
            profit=123.4,
            revenue=123.4,
            revenue_ranking=123,
            risk_manager="some.user",
            services_notes="Example notes",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert organizationdetail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.organizationdetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = response.parse()
        assert organizationdetail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.organizationdetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = response.parse()
            assert organizationdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.organizationdetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_organization="ORGANIZATION-ID",
                name="some.user",
                source="some.user",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.list(
            name="name",
        )
        assert_matches_type(SyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.list(
            name="name",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.organizationdetails.with_raw_response.list(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = response.parse()
        assert_matches_type(SyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.organizationdetails.with_streaming_response.list(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = response.parse()
            assert_matches_type(SyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.delete(
            "id",
        )
        assert organizationdetail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.organizationdetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = response.parse()
        assert organizationdetail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.organizationdetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = response.parse()
            assert organizationdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organizationdetails.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_find_by_source(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.find_by_source(
            name="name",
            source="source",
        )
        assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

    @parametrize
    def test_method_find_by_source_with_all_params(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.find_by_source(
            name="name",
            source="source",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

    @parametrize
    def test_raw_response_find_by_source(self, client: Unifieddatalibrary) -> None:
        response = client.organizationdetails.with_raw_response.find_by_source(
            name="name",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = response.parse()
        assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

    @parametrize
    def test_streaming_response_find_by_source(self, client: Unifieddatalibrary) -> None:
        with client.organizationdetails.with_streaming_response.find_by_source(
            name="name",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = response.parse()
            assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.get(
            id="id",
        )
        assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        organizationdetail = client.organizationdetails.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.organizationdetails.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = response.parse()
        assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.organizationdetails.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = response.parse()
            assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organizationdetails.with_raw_response.get(
                id="",
            )


class TestAsyncOrganizationdetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )
        assert organizationdetail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
            id="ORGANIZATIONDETAILS-ID",
            address1="123 Main Street",
            address2="Apt 4B",
            address3="Colorado Springs CO, 80903",
            broker="some.user",
            ceo="some.user",
            cfo="some.user",
            cto="some.user",
            description="Example description",
            ebitda=123.4,
            email="some_organization@organization.com",
            financial_notes="Example notes",
            financial_year_end_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            fleet_plan_notes="Example notes",
            former_org_id="FORMERORG-ID",
            ftes=123,
            geo_admin_level1="Colorado",
            geo_admin_level2="El Paso County",
            geo_admin_level3="Colorado Springs",
            mass_ranking=123,
            origin="some.user",
            parent_org_id="PARENTORG-ID",
            postal_code="80903",
            profit=123.4,
            revenue=123.4,
            revenue_ranking=123,
            risk_manager="some.user",
            services_notes="Example notes",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert organizationdetail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organizationdetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = await response.parse()
        assert organizationdetail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organizationdetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = await response.parse()
            assert organizationdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )
        assert organizationdetail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
            body_id="ORGANIZATIONDETAILS-ID",
            address1="123 Main Street",
            address2="Apt 4B",
            address3="Colorado Springs CO, 80903",
            broker="some.user",
            ceo="some.user",
            cfo="some.user",
            cto="some.user",
            description="Example description",
            ebitda=123.4,
            email="some_organization@organization.com",
            financial_notes="Example notes",
            financial_year_end_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            fleet_plan_notes="Example notes",
            former_org_id="FORMERORG-ID",
            ftes=123,
            geo_admin_level1="Colorado",
            geo_admin_level2="El Paso County",
            geo_admin_level3="Colorado Springs",
            mass_ranking=123,
            origin="some.user",
            parent_org_id="PARENTORG-ID",
            postal_code="80903",
            profit=123.4,
            revenue=123.4,
            revenue_ranking=123,
            risk_manager="some.user",
            services_notes="Example notes",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert organizationdetail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organizationdetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = await response.parse()
        assert organizationdetail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organizationdetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_organization="ORGANIZATION-ID",
            name="some.user",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = await response.parse()
            assert organizationdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.organizationdetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_organization="ORGANIZATION-ID",
                name="some.user",
                source="some.user",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.list(
            name="name",
        )
        assert_matches_type(AsyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.list(
            name="name",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organizationdetails.with_raw_response.list(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = await response.parse()
        assert_matches_type(AsyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organizationdetails.with_streaming_response.list(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = await response.parse()
            assert_matches_type(AsyncOffsetPage[OrganizationdetailListResponse], organizationdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.delete(
            "id",
        )
        assert organizationdetail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organizationdetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = await response.parse()
        assert organizationdetail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organizationdetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = await response.parse()
            assert organizationdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organizationdetails.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_find_by_source(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.find_by_source(
            name="name",
            source="source",
        )
        assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

    @parametrize
    async def test_method_find_by_source_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.find_by_source(
            name="name",
            source="source",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

    @parametrize
    async def test_raw_response_find_by_source(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organizationdetails.with_raw_response.find_by_source(
            name="name",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = await response.parse()
        assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

    @parametrize
    async def test_streaming_response_find_by_source(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organizationdetails.with_streaming_response.find_by_source(
            name="name",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = await response.parse()
            assert_matches_type(OrganizationdetailFindBySourceResponse, organizationdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.get(
            id="id",
        )
        assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        organizationdetail = await async_client.organizationdetails.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.organizationdetails.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organizationdetail = await response.parse()
        assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.organizationdetails.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organizationdetail = await response.parse()
            assert_matches_type(OrganizationDetailsFull, organizationdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organizationdetails.with_raw_response.get(
                id="",
            )
