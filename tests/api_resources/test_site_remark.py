# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SiteRemarkGetResponse,
    SiteRemarkListResponse,
    SiteRemarkTupleResponse,
    SiteRemarkQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSiteRemark:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
        )
        assert site_remark is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
            id="5000a3ef-8e39-2551-80f1-b3cd1895fe7b",
            code="M",
            name="Remark name",
            origin="THIRD_PARTY_DATASOURCE",
            orig_rmk_id="123456ABC",
            type="Restriction",
        )
        assert site_remark is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.site_remark.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = response.parse()
        assert site_remark is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.site_remark.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = response.parse()
            assert site_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.list()
        assert_matches_type(SyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.site_remark.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = response.parse()
        assert_matches_type(SyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.site_remark.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = response.parse()
            assert_matches_type(SyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.count()
        assert_matches_type(str, site_remark, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, site_remark, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.site_remark.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = response.parse()
        assert_matches_type(str, site_remark, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.site_remark.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = response.parse()
            assert_matches_type(str, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.get(
            id="id",
        )
        assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.site_remark.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = response.parse()
        assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.site_remark.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = response.parse()
            assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.site_remark.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.queryhelp()
        assert_matches_type(SiteRemarkQueryhelpResponse, site_remark, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.site_remark.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = response.parse()
        assert_matches_type(SiteRemarkQueryhelpResponse, site_remark, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.site_remark.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = response.parse()
            assert_matches_type(SiteRemarkQueryhelpResponse, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.tuple(
            columns="columns",
        )
        assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        site_remark = client.site_remark.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.site_remark.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = response.parse()
        assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.site_remark.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = response.parse()
            assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSiteRemark:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
        )
        assert site_remark is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
            id="5000a3ef-8e39-2551-80f1-b3cd1895fe7b",
            code="M",
            name="Remark name",
            origin="THIRD_PARTY_DATASOURCE",
            orig_rmk_id="123456ABC",
            type="Restriction",
        )
        assert site_remark is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site_remark.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = await response.parse()
        assert site_remark is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site_remark.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="SITE-ID",
            source="Bluestaq",
            text="This is a remark",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = await response.parse()
            assert site_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.list()
        assert_matches_type(AsyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site_remark.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = await response.parse()
        assert_matches_type(AsyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site_remark.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = await response.parse()
            assert_matches_type(AsyncOffsetPage[SiteRemarkListResponse], site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.count()
        assert_matches_type(str, site_remark, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, site_remark, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site_remark.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = await response.parse()
        assert_matches_type(str, site_remark, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site_remark.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = await response.parse()
            assert_matches_type(str, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.get(
            id="id",
        )
        assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site_remark.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = await response.parse()
        assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site_remark.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = await response.parse()
            assert_matches_type(SiteRemarkGetResponse, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.site_remark.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.queryhelp()
        assert_matches_type(SiteRemarkQueryhelpResponse, site_remark, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site_remark.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = await response.parse()
        assert_matches_type(SiteRemarkQueryhelpResponse, site_remark, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site_remark.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = await response.parse()
            assert_matches_type(SiteRemarkQueryhelpResponse, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.tuple(
            columns="columns",
        )
        assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        site_remark = await async_client.site_remark.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site_remark.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_remark = await response.parse()
        assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site_remark.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_remark = await response.parse()
            assert_matches_type(SiteRemarkTupleResponse, site_remark, path=["response"])

        assert cast(Any, response.is_closed) is True
