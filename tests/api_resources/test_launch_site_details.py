# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaunchSiteDetailGetResponse,
    LaunchSiteDetailListResponse,
    LaunchSiteDetailFindBySourceResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchSiteDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )
        assert launch_site_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
            id="LAUNCHSITEDETAILS-ID",
            available_inclinations=[10.23, 10.23, 12.23, 14.23],
            description="Example notes",
            id_location="LOCATION-ID",
            launch_group="Example-group-name",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert launch_site_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.launch_site_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = response.parse()
        assert launch_site_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.launch_site_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = response.parse()
            assert launch_site_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )
        assert launch_site_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
            body_id="LAUNCHSITEDETAILS-ID",
            available_inclinations=[10.23, 10.23, 12.23, 14.23],
            description="Example notes",
            id_location="LOCATION-ID",
            launch_group="Example-group-name",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert launch_site_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.launch_site_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = response.parse()
        assert launch_site_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.launch_site_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = response.parse()
            assert launch_site_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.launch_site_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_launch_site="LAUNCHSITE-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.list()
        assert_matches_type(SyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.launch_site_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = response.parse()
        assert_matches_type(SyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.launch_site_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = response.parse()
            assert_matches_type(SyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.delete(
            "id",
        )
        assert launch_site_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.launch_site_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = response.parse()
        assert launch_site_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.launch_site_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = response.parse()
            assert launch_site_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_site_details.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_find_by_source(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.find_by_source(
            source="source",
        )
        assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

    @parametrize
    def test_method_find_by_source_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.find_by_source(
            source="source",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

    @parametrize
    def test_raw_response_find_by_source(self, client: Unifieddatalibrary) -> None:
        response = client.launch_site_details.with_raw_response.find_by_source(
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = response.parse()
        assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

    @parametrize
    def test_streaming_response_find_by_source(self, client: Unifieddatalibrary) -> None:
        with client.launch_site_details.with_streaming_response.find_by_source(
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = response.parse()
            assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.get(
            id="id",
        )
        assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_site_detail = client.launch_site_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.launch_site_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = response.parse()
        assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.launch_site_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = response.parse()
            assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_site_details.with_raw_response.get(
                id="",
            )


class TestAsyncLaunchSiteDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )
        assert launch_site_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
            id="LAUNCHSITEDETAILS-ID",
            available_inclinations=[10.23, 10.23, 12.23, 14.23],
            description="Example notes",
            id_location="LOCATION-ID",
            launch_group="Example-group-name",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert launch_site_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_site_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = await response.parse()
        assert launch_site_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_site_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = await response.parse()
            assert launch_site_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )
        assert launch_site_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
            body_id="LAUNCHSITEDETAILS-ID",
            available_inclinations=[10.23, 10.23, 12.23, 14.23],
            description="Example notes",
            id_location="LOCATION-ID",
            launch_group="Example-group-name",
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
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert launch_site_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_site_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = await response.parse()
        assert launch_site_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_site_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_site="LAUNCHSITE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = await response.parse()
            assert launch_site_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.launch_site_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_launch_site="LAUNCHSITE-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.list()
        assert_matches_type(AsyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_site_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_site_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = await response.parse()
            assert_matches_type(AsyncOffsetPage[LaunchSiteDetailListResponse], launch_site_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.delete(
            "id",
        )
        assert launch_site_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_site_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = await response.parse()
        assert launch_site_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_site_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = await response.parse()
            assert launch_site_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_site_details.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_find_by_source(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.find_by_source(
            source="source",
        )
        assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

    @parametrize
    async def test_method_find_by_source_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.find_by_source(
            source="source",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

    @parametrize
    async def test_raw_response_find_by_source(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_site_details.with_raw_response.find_by_source(
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = await response.parse()
        assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

    @parametrize
    async def test_streaming_response_find_by_source(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_site_details.with_streaming_response.find_by_source(
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = await response.parse()
            assert_matches_type(LaunchSiteDetailFindBySourceResponse, launch_site_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.get(
            id="id",
        )
        assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_site_detail = await async_client.launch_site_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_site_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_site_detail = await response.parse()
        assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_site_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_site_detail = await response.parse()
            assert_matches_type(LaunchSiteDetailGetResponse, launch_site_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_site_details.with_raw_response.get(
                id="",
            )
