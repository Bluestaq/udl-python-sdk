# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinkstatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        linkstatus = client.linkstatus.update(
            path_id="id",
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
        assert linkstatus is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        linkstatus = client.linkstatus.update(
            path_id="id",
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
            body_id="LINKSTATUS-ID",
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
            snr=10.1,
            sys_cap="Example status",
        )
        assert linkstatus is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.linkstatus.with_raw_response.update(
            path_id="id",
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
        linkstatus = response.parse()
        assert linkstatus is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.linkstatus.with_streaming_response.update(
            path_id="id",
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

            linkstatus = response.parse()
            assert linkstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.linkstatus.with_raw_response.update(
                path_id="",
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

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        linkstatus = client.linkstatus.delete(
            "id",
        )
        assert linkstatus is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.linkstatus.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linkstatus = response.parse()
        assert linkstatus is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.linkstatus.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linkstatus = response.parse()
            assert linkstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linkstatus.with_raw_response.delete(
                "",
            )


class TestAsyncLinkstatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        linkstatus = await async_client.linkstatus.update(
            path_id="id",
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
        assert linkstatus is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        linkstatus = await async_client.linkstatus.update(
            path_id="id",
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
            body_id="LINKSTATUS-ID",
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
            snr=10.1,
            sys_cap="Example status",
        )
        assert linkstatus is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.linkstatus.with_raw_response.update(
            path_id="id",
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
        linkstatus = await response.parse()
        assert linkstatus is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.linkstatus.with_streaming_response.update(
            path_id="id",
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

            linkstatus = await response.parse()
            assert linkstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.linkstatus.with_raw_response.update(
                path_id="",
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

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        linkstatus = await async_client.linkstatus.delete(
            "id",
        )
        assert linkstatus is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.linkstatus.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linkstatus = await response.parse()
        assert linkstatus is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.linkstatus.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linkstatus = await response.parse()
            assert linkstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linkstatus.with_raw_response.delete(
                "",
            )
