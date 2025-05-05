# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.feature_assessment import (
    HistoryQueryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        history = client.feature_assessment.history.count(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.feature_assessment.history.count(
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.history.with_raw_response.count(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.history.with_streaming_response.count(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        history = client.feature_assessment.history.query(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.feature_assessment.history.query(
            id_analytic_imagery="idAnalyticImagery",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.history.with_raw_response.query(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.history.with_streaming_response.query(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryQueryResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_write_aodr(self, client: Unifieddatalibrary) -> None:
        history = client.feature_assessment.history.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert history is None

    @parametrize
    def test_method_write_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.feature_assessment.history.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert history is None

    @parametrize
    def test_raw_response_write_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.history.with_raw_response.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert history is None

    @parametrize
    def test_streaming_response_write_aodr(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.history.with_streaming_response.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.feature_assessment.history.count(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.feature_assessment.history.count(
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.history.with_raw_response.count(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.history.with_streaming_response.count(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.feature_assessment.history.query(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.feature_assessment.history.query(
            id_analytic_imagery="idAnalyticImagery",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.history.with_raw_response.query(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.history.with_streaming_response.query(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryQueryResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_write_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.feature_assessment.history.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert history is None

    @parametrize
    async def test_method_write_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.feature_assessment.history.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert history is None

    @parametrize
    async def test_raw_response_write_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.history.with_raw_response.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert history is None

    @parametrize
    async def test_streaming_response_write_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.history.with_streaming_response.write_aodr(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True
