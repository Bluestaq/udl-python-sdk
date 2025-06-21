# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    FeatureAssessmentQueryResponse,
    FeatureAssessmentTupleResponse,
    FeatureAssessmentRetrieveResponse,
    FeatureAssessmentQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeatureAssessment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
        )
        assert feature_assessment is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            agjson='{"type":"Point","coordinates":[52.23486096929749 16.191937138595005]}',
            andims=1,
            ann_lims=[[1, 1], [1, 2], [1, 3], [1, 4]],
            ann_text=["rec1", "rec2"],
            area="POINT(52.23486096929749 16.191937138595005)",
            asrid=4326,
            assessment="Vessel bigger than other small fishing boats commonly found along the coastline",
            atext="POINT(52.23486096929749 16.191937138595005)",
            atype="POINT",
            confidence=0.85,
            external_id="2024-06-22-17-53-05_UMBRA-05_GEC",
            feature_array=[1227.6, 1575.42],
            feature_bool=True,
            feature_string="TRANSMITTING FREQUENCIES",
            feature_string_array=["String1", "String2"],
            feature_value=1227.6,
            heading=97.1,
            height=7.25,
            length=10.54,
            name="HEADING",
            origin="THIRD_PARTY_DATASOURCE",
            speed=0.1,
            src_ids=["b008c63b-ad89-4493-80e0-77bc982bef77", "3565a6dd-654e-4969-89e0-ee7c51ab1e1b"],
            src_ts=[parse_datetime("2025-02-24T16:27:18.471Z"), parse_datetime("2025-02-24T16:29:31.000000Z")],
            src_typs=["SAR", "AIS"],
            tags=["TAG1", "TAG2"],
            transaction_id="c3bdef1f-5a4f-4716-bee4-7a1e0ec7d37d",
            type="VESSEL",
            width=3.74,
        )
        assert feature_assessment is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert feature_assessment is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert feature_assessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.retrieve(
            id="id",
        )
        assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.feature_assessment.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.count(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(str, feature_assessment, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.count(
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, feature_assessment, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.count(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert_matches_type(str, feature_assessment, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.count(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert_matches_type(str, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )
        assert feature_assessment is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert feature_assessment is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert feature_assessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.query(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.query(
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.query(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.query(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.query_help()
        assert_matches_type(FeatureAssessmentQueryHelpResponse, feature_assessment, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert_matches_type(FeatureAssessmentQueryHelpResponse, feature_assessment, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert_matches_type(FeatureAssessmentQueryHelpResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        feature_assessment = client.feature_assessment.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )
        assert feature_assessment is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.feature_assessment.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = response.parse()
        assert feature_assessment is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.feature_assessment.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = response.parse()
            assert feature_assessment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFeatureAssessment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
        )
        assert feature_assessment is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            agjson='{"type":"Point","coordinates":[52.23486096929749 16.191937138595005]}',
            andims=1,
            ann_lims=[[1, 1], [1, 2], [1, 3], [1, 4]],
            ann_text=["rec1", "rec2"],
            area="POINT(52.23486096929749 16.191937138595005)",
            asrid=4326,
            assessment="Vessel bigger than other small fishing boats commonly found along the coastline",
            atext="POINT(52.23486096929749 16.191937138595005)",
            atype="POINT",
            confidence=0.85,
            external_id="2024-06-22-17-53-05_UMBRA-05_GEC",
            feature_array=[1227.6, 1575.42],
            feature_bool=True,
            feature_string="TRANSMITTING FREQUENCIES",
            feature_string_array=["String1", "String2"],
            feature_value=1227.6,
            heading=97.1,
            height=7.25,
            length=10.54,
            name="HEADING",
            origin="THIRD_PARTY_DATASOURCE",
            speed=0.1,
            src_ids=["b008c63b-ad89-4493-80e0-77bc982bef77", "3565a6dd-654e-4969-89e0-ee7c51ab1e1b"],
            src_ts=[parse_datetime("2025-02-24T16:27:18.471Z"), parse_datetime("2025-02-24T16:29:31.000000Z")],
            src_typs=["SAR", "AIS"],
            tags=["TAG1", "TAG2"],
            transaction_id="c3bdef1f-5a4f-4716-bee4-7a1e0ec7d37d",
            type="VESSEL",
            width=3.74,
        )
        assert feature_assessment is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert feature_assessment is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            feature_ts=parse_datetime("2024-06-22T17:53:06.123Z"),
            feature_uo_m="MHz",
            id_analytic_imagery="fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert feature_assessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.retrieve(
            id="id",
        )
        assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert_matches_type(FeatureAssessmentRetrieveResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.feature_assessment.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.count(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(str, feature_assessment, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.count(
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, feature_assessment, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.count(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert_matches_type(str, feature_assessment, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.count(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert_matches_type(str, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )
        assert feature_assessment is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert feature_assessment is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert feature_assessment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.query(
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.query(
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.query(
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.query(
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert_matches_type(FeatureAssessmentQueryResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.query_help()
        assert_matches_type(FeatureAssessmentQueryHelpResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert_matches_type(FeatureAssessmentQueryHelpResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert_matches_type(FeatureAssessmentQueryHelpResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
        )
        assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.tuple(
            columns="columns",
            id_analytic_imagery="idAnalyticImagery",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert_matches_type(FeatureAssessmentTupleResponse, feature_assessment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        feature_assessment = await async_client.feature_assessment.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )
        assert feature_assessment is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.feature_assessment.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_assessment = await response.parse()
        assert feature_assessment is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.feature_assessment.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "feature_ts": parse_datetime("2024-06-22T17:53:06.123Z"),
                    "feature_uo_m": "MHz",
                    "id_analytic_imagery": "fa1509ae-c19d-432e-9542-e5d1e0f47bc3",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_assessment = await response.parse()
            assert feature_assessment is None

        assert cast(Any, response.is_closed) is True
