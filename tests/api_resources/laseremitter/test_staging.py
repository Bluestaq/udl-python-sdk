# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.laseremitter import (
    StagingListResponse,
    StagingRetrieveResponse,
    StagingQueryhelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStaging:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )
        assert staging is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
            id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            altitude=1.57543,
            laser_type="PULSED",
            lat=48.6732,
            location_country="US",
            lon=22.8455,
            owner_country="US",
        )
        assert staging is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert staging is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.retrieve(
            id="id",
        )
        assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.laseremitter.staging.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )
        assert staging is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
            body_id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            altitude=1.57543,
            laser_type="PULSED",
            lat=48.6732,
            location_country="US",
            lon=22.8455,
            owner_country="US",
        )
        assert staging is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert staging is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.laseremitter.staging.with_raw_response.update(
                path_id="",
                classification_marking="U",
                laser_name="LASER_NAME",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.list()
        assert_matches_type(SyncOffsetPage[StagingListResponse], staging, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[StagingListResponse], staging, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert_matches_type(SyncOffsetPage[StagingListResponse], staging, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert_matches_type(SyncOffsetPage[StagingListResponse], staging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.delete(
            "id",
        )
        assert staging is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert staging is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.laseremitter.staging.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "laser_name": "LASER_NAME",
                    "source": "Bluestaq",
                }
            ],
        )
        assert staging is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "laser_name": "LASER_NAME",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert staging is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "laser_name": "LASER_NAME",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        staging = client.laseremitter.staging.queryhelp()
        assert_matches_type(StagingQueryhelpResponse, staging, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.laseremitter.staging.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = response.parse()
        assert_matches_type(StagingQueryhelpResponse, staging, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.laseremitter.staging.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = response.parse()
            assert_matches_type(StagingQueryhelpResponse, staging, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStaging:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )
        assert staging is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
            id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            altitude=1.57543,
            laser_type="PULSED",
            lat=48.6732,
            location_country="US",
            lon=22.8455,
            owner_country="US",
        )
        assert staging is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert staging is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.create(
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.retrieve(
            id="id",
        )
        assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert_matches_type(StagingRetrieveResponse, staging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.laseremitter.staging.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )
        assert staging is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
            body_id="ad88770b-d824-443f-bdce-5f9e3fa500a9",
            altitude=1.57543,
            laser_type="PULSED",
            lat=48.6732,
            location_country="US",
            lon=22.8455,
            owner_country="US",
        )
        assert staging is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert staging is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            laser_name="LASER_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.laseremitter.staging.with_raw_response.update(
                path_id="",
                classification_marking="U",
                laser_name="LASER_NAME",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.list()
        assert_matches_type(AsyncOffsetPage[StagingListResponse], staging, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[StagingListResponse], staging, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert_matches_type(AsyncOffsetPage[StagingListResponse], staging, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert_matches_type(AsyncOffsetPage[StagingListResponse], staging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.delete(
            "id",
        )
        assert staging is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert staging is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.laseremitter.staging.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "laser_name": "LASER_NAME",
                    "source": "Bluestaq",
                }
            ],
        )
        assert staging is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "laser_name": "LASER_NAME",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert staging is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "laser_name": "LASER_NAME",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert staging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        staging = await async_client.laseremitter.staging.queryhelp()
        assert_matches_type(StagingQueryhelpResponse, staging, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laseremitter.staging.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staging = await response.parse()
        assert_matches_type(StagingQueryhelpResponse, staging, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laseremitter.staging.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staging = await response.parse()
            assert_matches_type(StagingQueryhelpResponse, staging, path=["response"])

        assert cast(Any, response.is_closed) is True
