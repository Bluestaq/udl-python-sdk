# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AnalyticImageryFull,
    AnalyticImageryAbridged,
    AnalyticImageryTupleResponse,
    AnalyticImageryHistoryResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalyticImagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.retrieve(
            id="id",
        )
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.analytic_imagery.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(SyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(SyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        analytic_imagery = client.analytic_imagery.file_get(
            id="id",
        )
        assert analytic_imagery.is_closed
        assert analytic_imagery.json() == {"foo": "bar"}
        assert cast(Any, analytic_imagery.is_closed) is True
        assert isinstance(analytic_imagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        analytic_imagery = client.analytic_imagery.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert analytic_imagery.is_closed
        assert analytic_imagery.json() == {"foo": "bar"}
        assert cast(Any, analytic_imagery.is_closed) is True
        assert isinstance(analytic_imagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        analytic_imagery = client.analytic_imagery.with_raw_response.file_get(
            id="id",
        )

        assert analytic_imagery.is_closed is True
        assert analytic_imagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert analytic_imagery.json() == {"foo": "bar"}
        assert isinstance(analytic_imagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.analytic_imagery.with_streaming_response.file_get(
            id="id",
        ) as analytic_imagery:
            assert not analytic_imagery.is_closed
            assert analytic_imagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert analytic_imagery.json() == {"foo": "bar"}
            assert cast(Any, analytic_imagery.is_closed) is True
            assert isinstance(analytic_imagery, StreamedBinaryAPIResponse)

        assert cast(Any, analytic_imagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.analytic_imagery.with_raw_response.file_get(
                id="",
            )

    @parametrize
    def test_method_history(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history_aodr(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert analytic_imagery is None

    @parametrize
    def test_method_history_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert analytic_imagery is None

    @parametrize
    def test_raw_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert analytic_imagery is None

    @parametrize
    def test_streaming_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history_count(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_method_history_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_history_count(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_history_count(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.queryhelp()
        assert analytic_imagery is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert analytic_imagery is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.unvalidated_publish(
            file=b"raw file contents",
        )
        assert analytic_imagery is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.unvalidated_publish(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert analytic_imagery is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.unvalidated_publish(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalyticImagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.retrieve(
            id="id",
        )
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.analytic_imagery.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AsyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AsyncOffsetPage[AnalyticImageryAbridged], analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        analytic_imagery = await async_client.analytic_imagery.file_get(
            id="id",
        )
        assert analytic_imagery.is_closed
        assert await analytic_imagery.json() == {"foo": "bar"}
        assert cast(Any, analytic_imagery.is_closed) is True
        assert isinstance(analytic_imagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        analytic_imagery = await async_client.analytic_imagery.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert analytic_imagery.is_closed
        assert await analytic_imagery.json() == {"foo": "bar"}
        assert cast(Any, analytic_imagery.is_closed) is True
        assert isinstance(analytic_imagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        analytic_imagery = await async_client.analytic_imagery.with_raw_response.file_get(
            id="id",
        )

        assert analytic_imagery.is_closed is True
        assert analytic_imagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await analytic_imagery.json() == {"foo": "bar"}
        assert isinstance(analytic_imagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_get(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/analyticimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.analytic_imagery.with_streaming_response.file_get(
            id="id",
        ) as analytic_imagery:
            assert not analytic_imagery.is_closed
            assert analytic_imagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await analytic_imagery.json() == {"foo": "bar"}
            assert cast(Any, analytic_imagery.is_closed) is True
            assert isinstance(analytic_imagery, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, analytic_imagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.analytic_imagery.with_raw_response.file_get(
                id="",
            )

    @parametrize
    async def test_method_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert analytic_imagery is None

    @parametrize
    async def test_method_history_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert analytic_imagery is None

    @parametrize
    async def test_raw_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert analytic_imagery is None

    @parametrize
    async def test_streaming_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_method_history_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.queryhelp()
        assert analytic_imagery is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert analytic_imagery is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.unvalidated_publish(
            file=b"raw file contents",
        )
        assert analytic_imagery is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.unvalidated_publish(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert analytic_imagery is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.unvalidated_publish(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True
