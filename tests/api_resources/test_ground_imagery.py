# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroundImagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_history_aodr(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ground_imagery is None

    @parametrize
    def test_method_history_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert ground_imagery is None

    @parametrize
    def test_raw_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert ground_imagery is None

    @parametrize
    def test_streaming_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.upload_zip(
            file=b"raw file contents",
        )
        assert ground_imagery is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert ground_imagery is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGroundImagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ground_imagery is None

    @parametrize
    async def test_method_history_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert ground_imagery is None

    @parametrize
    async def test_raw_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert ground_imagery is None

    @parametrize
    async def test_streaming_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.upload_zip(
            file=b"raw file contents",
        )
        assert ground_imagery is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert ground_imagery is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True
