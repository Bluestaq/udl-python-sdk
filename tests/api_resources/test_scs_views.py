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


class TestScsViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scs_view = client.scs_views.retrieve(
            id="/Documentation/project.pdf",
        )
        assert scs_view.is_closed
        assert scs_view.json() == {"foo": "bar"}
        assert cast(Any, scs_view.is_closed) is True
        assert isinstance(scs_view, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scs_view = client.scs_views.retrieve(
            id="/Documentation/project.pdf",
            first_result=0,
            max_results=0,
        )
        assert scs_view.is_closed
        assert scs_view.json() == {"foo": "bar"}
        assert cast(Any, scs_view.is_closed) is True
        assert isinstance(scs_view, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scs_view = client.scs_views.with_raw_response.retrieve(
            id="/Documentation/project.pdf",
        )

        assert scs_view.is_closed is True
        assert scs_view.http_request.headers.get("X-Stainless-Lang") == "python"
        assert scs_view.json() == {"foo": "bar"}
        assert isinstance(scs_view, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.scs_views.with_streaming_response.retrieve(
            id="/Documentation/project.pdf",
        ) as scs_view:
            assert not scs_view.is_closed
            assert scs_view.http_request.headers.get("X-Stainless-Lang") == "python"

            assert scs_view.json() == {"foo": "bar"}
            assert cast(Any, scs_view.is_closed) is True
            assert isinstance(scs_view, StreamedBinaryAPIResponse)

        assert cast(Any, scs_view.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.scs_views.with_raw_response.retrieve(
                id="",
            )


class TestAsyncScsViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scs_view = await async_client.scs_views.retrieve(
            id="/Documentation/project.pdf",
        )
        assert scs_view.is_closed
        assert await scs_view.json() == {"foo": "bar"}
        assert cast(Any, scs_view.is_closed) is True
        assert isinstance(scs_view, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scs_view = await async_client.scs_views.retrieve(
            id="/Documentation/project.pdf",
            first_result=0,
            max_results=0,
        )
        assert scs_view.is_closed
        assert await scs_view.json() == {"foo": "bar"}
        assert cast(Any, scs_view.is_closed) is True
        assert isinstance(scs_view, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scs_view = await async_client.scs_views.with_raw_response.retrieve(
            id="/Documentation/project.pdf",
        )

        assert scs_view.is_closed is True
        assert scs_view.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await scs_view.json() == {"foo": "bar"}
        assert isinstance(scs_view, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/scs/view//Documentation/project.pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.scs_views.with_streaming_response.retrieve(
            id="/Documentation/project.pdf",
        ) as scs_view:
            assert not scs_view.is_closed
            assert scs_view.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await scs_view.json() == {"foo": "bar"}
            assert cast(Any, scs_view.is_closed) is True
            assert isinstance(scs_view, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, scs_view.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.scs_views.with_raw_response.retrieve(
                id="",
            )
