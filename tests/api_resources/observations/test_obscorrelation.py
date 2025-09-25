# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.observations import (
    ObscorrelationListResponse,
    ObscorrelationTupleResponse,
    ObscorrelationRetrieveResponse,
    ObscorrelationQueryHelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObscorrelation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
        )
        assert obscorrelation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            algorithm_corr_type="ROTAS",
            alt_catalog="CATALOG",
            alt_namespace="18SDS",
            alt_object_id="26900",
            alt_uct=False,
            astat=2,
            corr_quality=0.96,
            id_parent_correlation="ID-PARENT-CORRELATION",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            sat_no=12100,
            tags=["TAG1", "TAG2"],
            track_id="TRACK-ID",
            transaction_id="TRANSACTION-ID",
        )
        assert obscorrelation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert obscorrelation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert obscorrelation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.retrieve(
            id="id",
        )
        assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.observations.obscorrelation.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert_matches_type(SyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert_matches_type(SyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, obscorrelation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, obscorrelation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert_matches_type(str, obscorrelation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert_matches_type(str, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )
        assert obscorrelation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert obscorrelation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert obscorrelation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.query_help()
        assert_matches_type(ObscorrelationQueryHelpResponse, obscorrelation, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert_matches_type(ObscorrelationQueryHelpResponse, obscorrelation, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert_matches_type(ObscorrelationQueryHelpResponse, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        obscorrelation = client.observations.obscorrelation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )
        assert obscorrelation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.observations.obscorrelation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = response.parse()
        assert obscorrelation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.observations.obscorrelation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = response.parse()
            assert obscorrelation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncObscorrelation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
        )
        assert obscorrelation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            algorithm_corr_type="ROTAS",
            alt_catalog="CATALOG",
            alt_namespace="18SDS",
            alt_object_id="26900",
            alt_uct=False,
            astat=2,
            corr_quality=0.96,
            id_parent_correlation="ID-PARENT-CORRELATION",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            sat_no=12100,
            tags=["TAG1", "TAG2"],
            track_id="TRACK-ID",
            transaction_id="TRANSACTION-ID",
        )
        assert obscorrelation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert obscorrelation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.create(
            classification_marking="U",
            corr_type="OBSERVATION",
            data_mode="TEST",
            msg_ts=parse_datetime("2021-01-01T01:01:01.123Z"),
            ob_id="e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
            ob_type="EO",
            reference_orbit_id="21826de2-5639-4c2a-b68f-30b67753b983",
            reference_orbit_type="ELSET",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert obscorrelation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.retrieve(
            id="id",
        )
        assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert_matches_type(ObscorrelationRetrieveResponse, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.observations.obscorrelation.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert_matches_type(AsyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.list(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert_matches_type(AsyncOffsetPage[ObscorrelationListResponse], obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, obscorrelation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, obscorrelation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert_matches_type(str, obscorrelation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.count(
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert_matches_type(str, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )
        assert obscorrelation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert obscorrelation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert obscorrelation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.query_help()
        assert_matches_type(ObscorrelationQueryHelpResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert_matches_type(ObscorrelationQueryHelpResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert_matches_type(ObscorrelationQueryHelpResponse, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.tuple(
            columns="columns",
            msg_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert_matches_type(ObscorrelationTupleResponse, obscorrelation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        obscorrelation = await async_client.observations.obscorrelation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )
        assert obscorrelation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.obscorrelation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        obscorrelation = await response.parse()
        assert obscorrelation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.obscorrelation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "corr_type": "OBSERVATION",
                    "data_mode": "TEST",
                    "msg_ts": parse_datetime("2021-01-01T01:01:01.123Z"),
                    "ob_id": "e69c6734-30a1-4c4f-8fe2-7187e7012e8c",
                    "ob_type": "EO",
                    "reference_orbit_id": "21826de2-5639-4c2a-b68f-30b67753b983",
                    "reference_orbit_type": "ELSET",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            obscorrelation = await response.parse()
            assert obscorrelation is None

        assert cast(Any, response.is_closed) is True
