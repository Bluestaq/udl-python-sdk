# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrewpapers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_unpublish(self, client: Unifieddatalibrary) -> None:
        crewpaper = client.air_operations.crewpapers.unpublish(
            ids="ids",
        )
        assert crewpaper is None

    @parametrize
    def test_raw_response_unpublish(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.crewpapers.with_raw_response.unpublish(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crewpaper = response.parse()
        assert crewpaper is None

    @parametrize
    def test_streaming_response_unpublish(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.crewpapers.with_streaming_response.unpublish(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crewpaper = response.parse()
            assert crewpaper is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_pdf(self, client: Unifieddatalibrary) -> None:
        crewpaper = client.air_operations.crewpapers.upload_pdf(
            aircraft_sortie_ids="aircraftSortieIds",
            classification_marking="x",
            paper_status="PUBLISHED",
            papers_version="x",
            body=b"raw file contents",
        )
        assert crewpaper is None

    @parametrize
    def test_raw_response_upload_pdf(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.crewpapers.with_raw_response.upload_pdf(
            aircraft_sortie_ids="aircraftSortieIds",
            classification_marking="x",
            paper_status="PUBLISHED",
            papers_version="x",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crewpaper = response.parse()
        assert crewpaper is None

    @parametrize
    def test_streaming_response_upload_pdf(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.crewpapers.with_streaming_response.upload_pdf(
            aircraft_sortie_ids="aircraftSortieIds",
            classification_marking="x",
            paper_status="PUBLISHED",
            papers_version="x",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crewpaper = response.parse()
            assert crewpaper is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCrewpapers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_unpublish(self, async_client: AsyncUnifieddatalibrary) -> None:
        crewpaper = await async_client.air_operations.crewpapers.unpublish(
            ids="ids",
        )
        assert crewpaper is None

    @parametrize
    async def test_raw_response_unpublish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.crewpapers.with_raw_response.unpublish(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crewpaper = await response.parse()
        assert crewpaper is None

    @parametrize
    async def test_streaming_response_unpublish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.crewpapers.with_streaming_response.unpublish(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crewpaper = await response.parse()
            assert crewpaper is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_pdf(self, async_client: AsyncUnifieddatalibrary) -> None:
        crewpaper = await async_client.air_operations.crewpapers.upload_pdf(
            aircraft_sortie_ids="aircraftSortieIds",
            classification_marking="x",
            paper_status="PUBLISHED",
            papers_version="x",
            body=b"raw file contents",
        )
        assert crewpaper is None

    @parametrize
    async def test_raw_response_upload_pdf(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.crewpapers.with_raw_response.upload_pdf(
            aircraft_sortie_ids="aircraftSortieIds",
            classification_marking="x",
            paper_status="PUBLISHED",
            papers_version="x",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crewpaper = await response.parse()
        assert crewpaper is None

    @parametrize
    async def test_streaming_response_upload_pdf(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.crewpapers.with_streaming_response.upload_pdf(
            aircraft_sortie_ids="aircraftSortieIds",
            classification_marking="x",
            paper_status="PUBLISHED",
            papers_version="x",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crewpaper = await response.parse()
            assert crewpaper is None

        assert cast(Any, response.is_closed) is True
