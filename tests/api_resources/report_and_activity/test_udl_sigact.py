# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlSigact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        udl_sigact = client.report_and_activity.udl_sigact.file_get(
            id="id",
        )
        assert udl_sigact.is_closed
        assert udl_sigact.json() == {"foo": "bar"}
        assert cast(Any, udl_sigact.is_closed) is True
        assert isinstance(udl_sigact, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        udl_sigact = client.report_and_activity.udl_sigact.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert udl_sigact.is_closed
        assert udl_sigact.json() == {"foo": "bar"}
        assert cast(Any, udl_sigact.is_closed) is True
        assert isinstance(udl_sigact, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        udl_sigact = client.report_and_activity.udl_sigact.with_raw_response.file_get(
            id="id",
        )

        assert udl_sigact.is_closed is True
        assert udl_sigact.http_request.headers.get("X-Stainless-Lang") == "python"
        assert udl_sigact.json() == {"foo": "bar"}
        assert isinstance(udl_sigact, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.report_and_activity.udl_sigact.with_streaming_response.file_get(
            id="id",
        ) as udl_sigact:
            assert not udl_sigact.is_closed
            assert udl_sigact.http_request.headers.get("X-Stainless-Lang") == "python"

            assert udl_sigact.json() == {"foo": "bar"}
            assert cast(Any, udl_sigact.is_closed) is True
            assert isinstance(udl_sigact, StreamedBinaryAPIResponse)

        assert cast(Any, udl_sigact.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.report_and_activity.udl_sigact.with_raw_response.file_get(
                id="",
            )

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        udl_sigact = client.report_and_activity.udl_sigact.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "report_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sigact is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.report_and_activity.udl_sigact.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "report_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sigact = response.parse()
        assert udl_sigact is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.report_and_activity.udl_sigact.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "report_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sigact = response.parse()
            assert udl_sigact is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlSigact:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        udl_sigact = await async_client.report_and_activity.udl_sigact.file_get(
            id="id",
        )
        assert udl_sigact.is_closed
        assert await udl_sigact.json() == {"foo": "bar"}
        assert cast(Any, udl_sigact.is_closed) is True
        assert isinstance(udl_sigact, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        udl_sigact = await async_client.report_and_activity.udl_sigact.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert udl_sigact.is_closed
        assert await udl_sigact.json() == {"foo": "bar"}
        assert cast(Any, udl_sigact.is_closed) is True
        assert isinstance(udl_sigact, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        udl_sigact = await async_client.report_and_activity.udl_sigact.with_raw_response.file_get(
            id="id",
        )

        assert udl_sigact.is_closed is True
        assert udl_sigact.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await udl_sigact.json() == {"foo": "bar"}
        assert isinstance(udl_sigact, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_get(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/sigact/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.report_and_activity.udl_sigact.with_streaming_response.file_get(
            id="id",
        ) as udl_sigact:
            assert not udl_sigact.is_closed
            assert udl_sigact.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await udl_sigact.json() == {"foo": "bar"}
            assert cast(Any, udl_sigact.is_closed) is True
            assert isinstance(udl_sigact, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, udl_sigact.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.report_and_activity.udl_sigact.with_raw_response.file_get(
                id="",
            )

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sigact = await async_client.report_and_activity.udl_sigact.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "report_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sigact is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.report_and_activity.udl_sigact.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "report_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sigact = await response.parse()
        assert udl_sigact is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.report_and_activity.udl_sigact.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "report_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sigact = await response.parse()
            assert udl_sigact is None

        assert cast(Any, response.is_closed) is True
