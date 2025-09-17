# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestView:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        view = client.scs.view.get(
            id="/Documentation/project.pdf",
        )
        assert view.is_closed
        assert view.json() == {"foo": "bar"}
        assert cast(Any, view.is_closed) is True
        assert isinstance(view, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        view = client.scs.view.get(
            id="/Documentation/project.pdf",
            first_result=0,
            max_results=0,
        )
        assert view.is_closed
        assert view.json() == {"foo": "bar"}
        assert cast(Any, view.is_closed) is True
        assert isinstance(view, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        view = client.scs.view.with_raw_response.get(
            id="/Documentation/project.pdf",
        )

        assert view.is_closed is True
        assert view.http_request.headers.get("X-Stainless-Lang") == "python"
        assert view.json() == {"foo": "bar"}
        assert isinstance(view, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.scs.view.with_streaming_response.get(
            id="/Documentation/project.pdf",
        ) as view:
            assert not view.is_closed
            assert view.http_request.headers.get("X-Stainless-Lang") == "python"

            assert view.json() == {"foo": "bar"}
            assert cast(Any, view.is_closed) is True
            assert isinstance(view, StreamedBinaryAPIResponse)

        assert cast(Any, view.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.scs.view.with_raw_response.get(
                id="",
            )


class TestAsyncView:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        view = await async_client.scs.view.get(
            id="/Documentation/project.pdf",
        )
        assert view.is_closed
        assert await view.json() == {"foo": "bar"}
        assert cast(Any, view.is_closed) is True
        assert isinstance(view, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        view = await async_client.scs.view.get(
            id="/Documentation/project.pdf",
            first_result=0,
            max_results=0,
        )
        assert view.is_closed
        assert await view.json() == {"foo": "bar"}
        assert cast(Any, view.is_closed) is True
        assert isinstance(view, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        view = await async_client.scs.view.with_raw_response.get(
            id="/Documentation/project.pdf",
        )

        assert view.is_closed is True
        assert view.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await view.json() == {"foo": "bar"}
        assert isinstance(view, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.scs.view.with_streaming_response.get(
            id="/Documentation/project.pdf",
        ) as view:
            assert not view.is_closed
            assert view.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await view.json() == {"foo": "bar"}
            assert cast(Any, view.is_closed) is True
            assert isinstance(view, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, view.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.scs.view.with_raw_response.get(
                id="",
            )
