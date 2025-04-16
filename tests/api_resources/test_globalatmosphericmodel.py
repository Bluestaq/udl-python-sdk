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
    GlobalatmosphericmodelQueryResponse,
    GlobalatmosphericmodelTupleResponse,
    GlobalatmosphericmodelRetrieveResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobalatmosphericmodel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.retrieve(
            "id",
        )
        assert_matches_type(GlobalatmosphericmodelRetrieveResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.globalatmosphericmodel.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = response.parse()
        assert_matches_type(GlobalatmosphericmodelRetrieveResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.globalatmosphericmodel.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = response.parse()
            assert_matches_type(GlobalatmosphericmodelRetrieveResponse, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.globalatmosphericmodel.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.globalatmosphericmodel.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = response.parse()
        assert_matches_type(str, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.globalatmosphericmodel.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = response.parse()
            assert_matches_type(str, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/globalatmosphericmodel/getFile/id").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        globalatmosphericmodel = client.globalatmosphericmodel.get_file(
            "id",
        )
        assert globalatmosphericmodel.is_closed
        assert globalatmosphericmodel.json() == {"foo": "bar"}
        assert cast(Any, globalatmosphericmodel.is_closed) is True
        assert isinstance(globalatmosphericmodel, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/globalatmosphericmodel/getFile/id").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        globalatmosphericmodel = client.globalatmosphericmodel.with_raw_response.get_file(
            "id",
        )

        assert globalatmosphericmodel.is_closed is True
        assert globalatmosphericmodel.http_request.headers.get("X-Stainless-Lang") == "python"
        assert globalatmosphericmodel.json() == {"foo": "bar"}
        assert isinstance(globalatmosphericmodel, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/globalatmosphericmodel/getFile/id").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.globalatmosphericmodel.with_streaming_response.get_file(
            "id",
        ) as globalatmosphericmodel:
            assert not globalatmosphericmodel.is_closed
            assert globalatmosphericmodel.http_request.headers.get("X-Stainless-Lang") == "python"

            assert globalatmosphericmodel.json() == {"foo": "bar"}
            assert cast(Any, globalatmosphericmodel.is_closed) is True
            assert isinstance(globalatmosphericmodel, StreamedBinaryAPIResponse)

        assert cast(Any, globalatmosphericmodel.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_file(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.globalatmosphericmodel.with_raw_response.get_file(
                "",
            )

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.query(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GlobalatmosphericmodelQueryResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.globalatmosphericmodel.with_raw_response.query(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = response.parse()
        assert_matches_type(GlobalatmosphericmodelQueryResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.globalatmosphericmodel.with_streaming_response.query(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = response.parse()
            assert_matches_type(GlobalatmosphericmodelQueryResponse, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.query_help()
        assert globalatmosphericmodel is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.globalatmosphericmodel.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = response.parse()
        assert globalatmosphericmodel is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.globalatmosphericmodel.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = response.parse()
            assert globalatmosphericmodel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GlobalatmosphericmodelTupleResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.globalatmosphericmodel.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = response.parse()
        assert_matches_type(GlobalatmosphericmodelTupleResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.globalatmosphericmodel.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = response.parse()
            assert_matches_type(GlobalatmosphericmodelTupleResponse, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
        )
        assert globalatmosphericmodel is None

    @parametrize
    def test_method_unvalidated_publish_with_all_params(self, client: Unifieddatalibrary) -> None:
        globalatmosphericmodel = client.globalatmosphericmodel.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            cadence=10,
            end_alt=90.125,
            end_lat=-88.75,
            end_lon=-177.5,
            filename="glotec_elecden.geojson",
            filesize=2097152,
            num_alt=35,
            num_lat=72,
            num_lon=72,
            origin="THIRD_PARTY_DATASOURCE",
            report_time=parse_datetime("2024-08-21T21:54:35.123Z"),
            start_alt=8553.163773,
            start_lat=88.75,
            start_lon=177.5,
            state="PREDICTED",
            step_lat=2.5,
            step_lon=5.5,
        )
        assert globalatmosphericmodel is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.globalatmosphericmodel.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = response.parse()
        assert globalatmosphericmodel is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.globalatmosphericmodel.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = response.parse()
            assert globalatmosphericmodel is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGlobalatmosphericmodel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.retrieve(
            "id",
        )
        assert_matches_type(GlobalatmosphericmodelRetrieveResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.globalatmosphericmodel.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = await response.parse()
        assert_matches_type(GlobalatmosphericmodelRetrieveResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.globalatmosphericmodel.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = await response.parse()
            assert_matches_type(GlobalatmosphericmodelRetrieveResponse, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.globalatmosphericmodel.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.globalatmosphericmodel.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = await response.parse()
        assert_matches_type(str, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.globalatmosphericmodel.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = await response.parse()
            assert_matches_type(str, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_file(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/globalatmosphericmodel/getFile/id").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        globalatmosphericmodel = await async_client.globalatmosphericmodel.get_file(
            "id",
        )
        assert globalatmosphericmodel.is_closed
        assert await globalatmosphericmodel.json() == {"foo": "bar"}
        assert cast(Any, globalatmosphericmodel.is_closed) is True
        assert isinstance(globalatmosphericmodel, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_file(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/globalatmosphericmodel/getFile/id").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        globalatmosphericmodel = await async_client.globalatmosphericmodel.with_raw_response.get_file(
            "id",
        )

        assert globalatmosphericmodel.is_closed is True
        assert globalatmosphericmodel.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await globalatmosphericmodel.json() == {"foo": "bar"}
        assert isinstance(globalatmosphericmodel, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_file(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/globalatmosphericmodel/getFile/id").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.globalatmosphericmodel.with_streaming_response.get_file(
            "id",
        ) as globalatmosphericmodel:
            assert not globalatmosphericmodel.is_closed
            assert globalatmosphericmodel.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await globalatmosphericmodel.json() == {"foo": "bar"}
            assert cast(Any, globalatmosphericmodel.is_closed) is True
            assert isinstance(globalatmosphericmodel, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, globalatmosphericmodel.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_file(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.globalatmosphericmodel.with_raw_response.get_file(
                "",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.query(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GlobalatmosphericmodelQueryResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.globalatmosphericmodel.with_raw_response.query(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = await response.parse()
        assert_matches_type(GlobalatmosphericmodelQueryResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.globalatmosphericmodel.with_streaming_response.query(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = await response.parse()
            assert_matches_type(GlobalatmosphericmodelQueryResponse, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.query_help()
        assert globalatmosphericmodel is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.globalatmosphericmodel.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = await response.parse()
        assert globalatmosphericmodel is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.globalatmosphericmodel.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = await response.parse()
            assert globalatmosphericmodel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GlobalatmosphericmodelTupleResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.globalatmosphericmodel.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = await response.parse()
        assert_matches_type(GlobalatmosphericmodelTupleResponse, globalatmosphericmodel, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.globalatmosphericmodel.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = await response.parse()
            assert_matches_type(GlobalatmosphericmodelTupleResponse, globalatmosphericmodel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
        )
        assert globalatmosphericmodel is None

    @parametrize
    async def test_method_unvalidated_publish_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        globalatmosphericmodel = await async_client.globalatmosphericmodel.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            cadence=10,
            end_alt=90.125,
            end_lat=-88.75,
            end_lon=-177.5,
            filename="glotec_elecden.geojson",
            filesize=2097152,
            num_alt=35,
            num_lat=72,
            num_lon=72,
            origin="THIRD_PARTY_DATASOURCE",
            report_time=parse_datetime("2024-08-21T21:54:35.123Z"),
            start_alt=8553.163773,
            start_lat=88.75,
            start_lon=177.5,
            state="PREDICTED",
            step_lat=2.5,
            step_lon=5.5,
        )
        assert globalatmosphericmodel is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.globalatmosphericmodel.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        globalatmosphericmodel = await response.parse()
        assert globalatmosphericmodel is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.globalatmosphericmodel.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2024-03-01T11:45:00.123Z"),
            type="Global Total Electron Density",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            globalatmosphericmodel = await response.parse()
            assert globalatmosphericmodel is None

        assert cast(Any, response.is_closed) is True
