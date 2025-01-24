# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    RfgeolocationGetResponse,
    RfgeolocationListResponse,
    RfgeolocationTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRfgeolocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )
        assert rfgeolocation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            agjson='{"type":"Polygon","coordinates":[[[67.3291113966927,26.156175339112],[67.2580009640721,26.091022064271],[67.1795862381682,26.6637992964562],[67.2501237475598,26.730115808233],[67.3291113966927,26.156175339112]]]}',
            alg_version="v1.0-3-gps_nb_3ball",
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="MultiPolygon",
            center_freq=1575.42,
            conf_area=81577480.056,
            conf_orientation=89.852,
            conf_semi_major=9435.896,
            conf_semi_minor=2751.929,
            constellation="HawkEye360",
            created_ts=parse_datetime("2024-05-31T23:06:18.123456Z"),
            detect_alt=123.456,
            detect_lat=41.172,
            detect_lon=37.019,
            end_time=parse_datetime("2024-05-31T21:16:15.123456Z"),
            external_id="780180925",
            id_rf_emitter="RFEMITTER-ID",
            max_freq=1575.42,
            min_freq=1575.42,
            num_bursts=17,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_rf_emitter_id="ORIGRFEMITTER-ID",
            pass_group_id="80fd25a8-8b41-448d-888a-91c9dfcd940b",
            sat_no=101,
            signal_of_interest="GPS",
            tags=["TAG1", "TAG2"],
        )
        assert rfgeolocation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert rfgeolocation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RfgeolocationListResponse, rfgeolocation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert_matches_type(RfgeolocationListResponse, rfgeolocation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert_matches_type(RfgeolocationListResponse, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.delete(
            "id",
        )
        assert rfgeolocation is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert rfgeolocation is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rfgeolocation.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, rfgeolocation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert_matches_type(str, rfgeolocation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert_matches_type(str, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )
        assert rfgeolocation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert rfgeolocation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.get(
            "id",
        )
        assert_matches_type(RfgeolocationGetResponse, rfgeolocation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert_matches_type(RfgeolocationGetResponse, rfgeolocation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert_matches_type(RfgeolocationGetResponse, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rfgeolocation.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.queryhelp()
        assert rfgeolocation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert rfgeolocation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        rfgeolocation = client.rfgeolocation.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RfgeolocationTupleResponse, rfgeolocation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.rfgeolocation.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = response.parse()
        assert_matches_type(RfgeolocationTupleResponse, rfgeolocation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.rfgeolocation.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = response.parse()
            assert_matches_type(RfgeolocationTupleResponse, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRfgeolocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )
        assert rfgeolocation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            agjson='{"type":"Polygon","coordinates":[[[67.3291113966927,26.156175339112],[67.2580009640721,26.091022064271],[67.1795862381682,26.6637992964562],[67.2501237475598,26.730115808233],[67.3291113966927,26.156175339112]]]}',
            alg_version="v1.0-3-gps_nb_3ball",
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="MultiPolygon",
            center_freq=1575.42,
            conf_area=81577480.056,
            conf_orientation=89.852,
            conf_semi_major=9435.896,
            conf_semi_minor=2751.929,
            constellation="HawkEye360",
            created_ts=parse_datetime("2024-05-31T23:06:18.123456Z"),
            detect_alt=123.456,
            detect_lat=41.172,
            detect_lon=37.019,
            end_time=parse_datetime("2024-05-31T21:16:15.123456Z"),
            external_id="780180925",
            id_rf_emitter="RFEMITTER-ID",
            max_freq=1575.42,
            min_freq=1575.42,
            num_bursts=17,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_rf_emitter_id="ORIGRFEMITTER-ID",
            pass_group_id="80fd25a8-8b41-448d-888a-91c9dfcd940b",
            sat_no=101,
            signal_of_interest="GPS",
            tags=["TAG1", "TAG2"],
        )
        assert rfgeolocation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert rfgeolocation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.create(
            classification_marking="U",
            data_mode="REAL",
            order_id="155240",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RfgeolocationListResponse, rfgeolocation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert_matches_type(RfgeolocationListResponse, rfgeolocation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert_matches_type(RfgeolocationListResponse, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.delete(
            "id",
        )
        assert rfgeolocation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert rfgeolocation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rfgeolocation.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, rfgeolocation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert_matches_type(str, rfgeolocation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert_matches_type(str, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )
        assert rfgeolocation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert rfgeolocation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.get(
            "id",
        )
        assert_matches_type(RfgeolocationGetResponse, rfgeolocation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert_matches_type(RfgeolocationGetResponse, rfgeolocation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert_matches_type(RfgeolocationGetResponse, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rfgeolocation.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.queryhelp()
        assert rfgeolocation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert rfgeolocation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert rfgeolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfgeolocation = await async_client.rfgeolocation.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RfgeolocationTupleResponse, rfgeolocation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfgeolocation.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfgeolocation = await response.parse()
        assert_matches_type(RfgeolocationTupleResponse, rfgeolocation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfgeolocation.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfgeolocation = await response.parse()
            assert_matches_type(RfgeolocationTupleResponse, rfgeolocation, path=["response"])

        assert cast(Any, response.is_closed) is True
