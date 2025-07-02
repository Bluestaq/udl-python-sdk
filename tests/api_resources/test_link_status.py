# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LinkStatusGetResponse,
    LinkStatusListResponse,
    LinkStatusTupleResponse,
    LinkStatusQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinkStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert link_status is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
            id="LINKSTATUS-ID",
            band="MIL-KA",
            constellation="Fornax",
            data_rate1_to2=10.23,
            data_rate2_to1=10.23,
            id_beam1="REF-BEAM1-ID",
            id_beam2="REF-BEAM2-ID",
            link_state="DEGRADED-WEATHER",
            link_type="Example link",
            ops_cap="Example status",
            origin="THIRD_PARTY_DATASOURCE",
            sat_no1=1,
            sat_no2=2,
            sys_cap="Example status",
        )
        assert link_status is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = response.parse()
        assert link_status is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.link_status.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = response.parse()
            assert link_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.list()
        assert_matches_type(SyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            link_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            link_stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = response.parse()
        assert_matches_type(SyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.link_status.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = response.parse()
            assert_matches_type(SyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.count()
        assert_matches_type(str, link_status, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            link_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            link_stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_results=0,
        )
        assert_matches_type(str, link_status, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = response.parse()
        assert_matches_type(str, link_status, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.link_status.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = response.parse()
            assert_matches_type(str, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.get(
            id="id",
        )
        assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = response.parse()
        assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.link_status.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = response.parse()
            assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.link_status.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.queryhelp()
        assert_matches_type(LinkStatusQueryhelpResponse, link_status, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = response.parse()
        assert_matches_type(LinkStatusQueryhelpResponse, link_status, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.link_status.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = response.parse()
            assert_matches_type(LinkStatusQueryhelpResponse, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.tuple(
            columns="columns",
        )
        assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        link_status = client.link_status.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            link_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            link_stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_results=0,
        )
        assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = response.parse()
        assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.link_status.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = response.parse()
            assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLinkStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert link_status is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
            id="LINKSTATUS-ID",
            band="MIL-KA",
            constellation="Fornax",
            data_rate1_to2=10.23,
            data_rate2_to1=10.23,
            id_beam1="REF-BEAM1-ID",
            id_beam2="REF-BEAM2-ID",
            link_state="DEGRADED-WEATHER",
            link_type="Example link",
            ops_cap="Example status",
            origin="THIRD_PARTY_DATASOURCE",
            sat_no1=1,
            sat_no2=2,
            sys_cap="Example status",
        )
        assert link_status is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = await response.parse()
        assert link_status is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_point1_lat=45.23,
            end_point1_lon=80.23,
            end_point1_name="Example endpoint",
            end_point2_lat=45.23,
            end_point2_lon=80.23,
            end_point2_name="Example description",
            link_name="Example description",
            link_start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            link_stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = await response.parse()
            assert link_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.list()
        assert_matches_type(AsyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            link_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            link_stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = await response.parse()
        assert_matches_type(AsyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = await response.parse()
            assert_matches_type(AsyncOffsetPage[LinkStatusListResponse], link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.count()
        assert_matches_type(str, link_status, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            link_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            link_stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_results=0,
        )
        assert_matches_type(str, link_status, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = await response.parse()
        assert_matches_type(str, link_status, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = await response.parse()
            assert_matches_type(str, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.get(
            id="id",
        )
        assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = await response.parse()
        assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = await response.parse()
            assert_matches_type(LinkStatusGetResponse, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.link_status.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.queryhelp()
        assert_matches_type(LinkStatusQueryhelpResponse, link_status, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = await response.parse()
        assert_matches_type(LinkStatusQueryhelpResponse, link_status, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = await response.parse()
            assert_matches_type(LinkStatusQueryhelpResponse, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.tuple(
            columns="columns",
        )
        assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        link_status = await async_client.link_status.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            link_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            link_stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_results=0,
        )
        assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link_status = await response.parse()
        assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link_status = await response.parse()
            assert_matches_type(LinkStatusTupleResponse, link_status, path=["response"])

        assert cast(Any, response.is_closed) is True
