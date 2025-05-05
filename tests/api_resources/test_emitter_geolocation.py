# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EmitterGeolocationQueryResponse,
    EmitterGeolocationTupleResponse,
    EmitterGeolocationRetrieveResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmitterGeolocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )
        assert emitter_geolocation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            alg_version="v1.0-3-gps_nb_3ball",
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="MultiPolygon",
            center_freq=1575.42,
            cluster="CONSTELLATION1-F",
            conf_area=81577480.056,
            constellation="HawkEye360",
            created_ts=parse_datetime("2024-05-31T23:06:18.123456Z"),
            detect_alt=123.456,
            detect_lat=41.172,
            detect_lon=37.019,
            end_time=parse_datetime("2024-05-31T21:16:15.123456Z"),
            err_ellp=[1.23, 2.34, 3.45],
            external_id="780180925",
            id_rf_emitter="026dd511-8ba5-47d3-9909-836149f87686",
            id_sensor="OCULUSA",
            max_freq=1575.42,
            min_freq=1575.42,
            num_bursts=17,
            order_id="155240",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_rf_emitter_id="12345678",
            orig_sensor_id="ORIGSENSOR-ID",
            pass_group_id="80fd25a8-8b41-448d-888a-91c9dfcd940b",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            sat_no=101,
            signal_of_interest="GPS",
            tags=["TAG1", "TAG2"],
        )
        assert emitter_geolocation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert emitter_geolocation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.retrieve(
            id="id",
        )
        assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emitter_geolocation.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.delete(
            "id",
        )
        assert emitter_geolocation is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert emitter_geolocation is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emitter_geolocation.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, emitter_geolocation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, emitter_geolocation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert_matches_type(str, emitter_geolocation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert_matches_type(str, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )
        assert emitter_geolocation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert emitter_geolocation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.query_help()
        assert emitter_geolocation is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert emitter_geolocation is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        emitter_geolocation = client.emitter_geolocation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )
        assert emitter_geolocation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.emitter_geolocation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = response.parse()
        assert emitter_geolocation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.emitter_geolocation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEmitterGeolocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )
        assert emitter_geolocation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            alg_version="v1.0-3-gps_nb_3ball",
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="MultiPolygon",
            center_freq=1575.42,
            cluster="CONSTELLATION1-F",
            conf_area=81577480.056,
            constellation="HawkEye360",
            created_ts=parse_datetime("2024-05-31T23:06:18.123456Z"),
            detect_alt=123.456,
            detect_lat=41.172,
            detect_lon=37.019,
            end_time=parse_datetime("2024-05-31T21:16:15.123456Z"),
            err_ellp=[1.23, 2.34, 3.45],
            external_id="780180925",
            id_rf_emitter="026dd511-8ba5-47d3-9909-836149f87686",
            id_sensor="OCULUSA",
            max_freq=1575.42,
            min_freq=1575.42,
            num_bursts=17,
            order_id="155240",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_rf_emitter_id="12345678",
            orig_sensor_id="ORIGSENSOR-ID",
            pass_group_id="80fd25a8-8b41-448d-888a-91c9dfcd940b",
            received_ts=parse_datetime("2024-05-31T21:16:58.123456Z"),
            sat_no=101,
            signal_of_interest="GPS",
            tags=["TAG1", "TAG2"],
        )
        assert emitter_geolocation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert emitter_geolocation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            signal_of_interest_type="RF",
            source="Bluestaq",
            start_time=parse_datetime("2024-05-31T21:12:12.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.retrieve(
            id="id",
        )
        assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert_matches_type(EmitterGeolocationRetrieveResponse, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emitter_geolocation.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.delete(
            "id",
        )
        assert emitter_geolocation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert emitter_geolocation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emitter_geolocation.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, emitter_geolocation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, emitter_geolocation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert_matches_type(str, emitter_geolocation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert_matches_type(str, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )
        assert emitter_geolocation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert emitter_geolocation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert_matches_type(EmitterGeolocationQueryResponse, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.query_help()
        assert emitter_geolocation is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert emitter_geolocation is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert_matches_type(EmitterGeolocationTupleResponse, emitter_geolocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        emitter_geolocation = await async_client.emitter_geolocation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )
        assert emitter_geolocation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emitter_geolocation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emitter_geolocation = await response.parse()
        assert emitter_geolocation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emitter_geolocation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "signal_of_interest_type": "RF",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-05-31T21:12:12.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emitter_geolocation = await response.parse()
            assert emitter_geolocation is None

        assert cast(Any, response.is_closed) is True
