# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ManifoldelsetGetResponse,
    ManifoldelsetListResponse,
    ManifoldelsetTupleResponse,
    ManifoldelsetQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManifoldelset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )
        assert manifoldelset is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
            id="MANIFOLDELSET-ID",
            apogee=10.23,
            arg_of_perigee=10.23,
            b_star=10.23,
            eccentricity=0.5,
            inclination=90.23,
            mean_anomaly=10.23,
            mean_motion=10.23,
            mean_motion_d_dot=10.23,
            mean_motion_dot=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            perigee=10.23,
            period=10.23,
            raan=10.23,
            rev_no=123,
            semi_major_axis=10.23,
        )
        assert manifoldelset is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert manifoldelset is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )
        assert manifoldelset is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
            body_id="MANIFOLDELSET-ID",
            apogee=10.23,
            arg_of_perigee=10.23,
            b_star=10.23,
            eccentricity=0.5,
            inclination=90.23,
            mean_anomaly=10.23,
            mean_motion=10.23,
            mean_motion_d_dot=10.23,
            mean_motion_dot=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            perigee=10.23,
            period=10.23,
            raan=10.23,
            rev_no=123,
            semi_major_axis=10.23,
        )
        assert manifoldelset is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert manifoldelset is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.manifoldelset.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
                id_manifold="REF-MANIFOLD-ID",
                source="Bluestaq",
                tmp_sat_no=10,
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert_matches_type(SyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert_matches_type(SyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.delete(
            "id",
        )
        assert manifoldelset is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert manifoldelset is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.manifoldelset.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, manifoldelset, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, manifoldelset, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert_matches_type(str, manifoldelset, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert_matches_type(str, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "id_manifold": "REF-MANIFOLD-ID",
                    "source": "Bluestaq",
                    "tmp_sat_no": 10,
                }
            ],
        )
        assert manifoldelset is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "id_manifold": "REF-MANIFOLD-ID",
                    "source": "Bluestaq",
                    "tmp_sat_no": 10,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert manifoldelset is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "id_manifold": "REF-MANIFOLD-ID",
                    "source": "Bluestaq",
                    "tmp_sat_no": 10,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.get(
            id="id",
        )
        assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.manifoldelset.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.queryhelp()
        assert_matches_type(ManifoldelsetQueryhelpResponse, manifoldelset, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert_matches_type(ManifoldelsetQueryhelpResponse, manifoldelset, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert_matches_type(ManifoldelsetQueryhelpResponse, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifoldelset = client.manifoldelset.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.manifoldelset.with_raw_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = response.parse()
        assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.manifoldelset.with_streaming_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = response.parse()
            assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncManifoldelset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )
        assert manifoldelset is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
            id="MANIFOLDELSET-ID",
            apogee=10.23,
            arg_of_perigee=10.23,
            b_star=10.23,
            eccentricity=0.5,
            inclination=90.23,
            mean_anomaly=10.23,
            mean_motion=10.23,
            mean_motion_d_dot=10.23,
            mean_motion_dot=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            perigee=10.23,
            period=10.23,
            raan=10.23,
            rev_no=123,
            semi_major_axis=10.23,
        )
        assert manifoldelset is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert manifoldelset is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )
        assert manifoldelset is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
            body_id="MANIFOLDELSET-ID",
            apogee=10.23,
            arg_of_perigee=10.23,
            b_star=10.23,
            eccentricity=0.5,
            inclination=90.23,
            mean_anomaly=10.23,
            mean_motion=10.23,
            mean_motion_d_dot=10.23,
            mean_motion_dot=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            perigee=10.23,
            period=10.23,
            raan=10.23,
            rev_no=123,
            semi_major_axis=10.23,
        )
        assert manifoldelset is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert manifoldelset is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id_manifold="REF-MANIFOLD-ID",
            source="Bluestaq",
            tmp_sat_no=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.manifoldelset.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
                id_manifold="REF-MANIFOLD-ID",
                source="Bluestaq",
                tmp_sat_no=10,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert_matches_type(AsyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert_matches_type(AsyncOffsetPage[ManifoldelsetListResponse], manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.delete(
            "id",
        )
        assert manifoldelset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert manifoldelset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.manifoldelset.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, manifoldelset, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, manifoldelset, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert_matches_type(str, manifoldelset, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert_matches_type(str, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "id_manifold": "REF-MANIFOLD-ID",
                    "source": "Bluestaq",
                    "tmp_sat_no": 10,
                }
            ],
        )
        assert manifoldelset is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "id_manifold": "REF-MANIFOLD-ID",
                    "source": "Bluestaq",
                    "tmp_sat_no": 10,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert manifoldelset is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "id_manifold": "REF-MANIFOLD-ID",
                    "source": "Bluestaq",
                    "tmp_sat_no": 10,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert manifoldelset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.get(
            id="id",
        )
        assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert_matches_type(ManifoldelsetGetResponse, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.manifoldelset.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.queryhelp()
        assert_matches_type(ManifoldelsetQueryhelpResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert_matches_type(ManifoldelsetQueryhelpResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert_matches_type(ManifoldelsetQueryhelpResponse, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifoldelset = await async_client.manifoldelset.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifoldelset.with_raw_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifoldelset = await response.parse()
        assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifoldelset.with_streaming_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifoldelset = await response.parse()
            assert_matches_type(ManifoldelsetTupleResponse, manifoldelset, path=["response"])

        assert cast(Any, response.is_closed) is True
