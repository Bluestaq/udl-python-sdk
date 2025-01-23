# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGnssrawif:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.filedrop.gnssrawif.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
        )
        assert gnssrawif is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.filedrop.gnssrawif.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
            id="GNSSRawIF-ID",
            bit_depth=8,
            boresight=[0, 1, 0],
            data_rate=0.205,
            diff_code_bias=[0.0271, 0.0016],
            end_alt=525.626,
            end_lat=38.922,
            end_lon=-104.67,
            es_id="60f7a241-b7be-48d8-acf3-786670af53f9",
            event_id="2f2205c9-7bc2-4e1a-8416-2f80cc71f64b",
            if_freq=[4.09, 5.87],
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="L2045",
            post_fourier=["NONE", "NONE"],
            quat=[0, -0.2734104, 0.1562345, 0.9491246],
            receiver="GPS1",
            sample_rate=[8000, 9000],
            sample_type="COMPLEX",
            sat_no=32375,
            sequence_id=1,
            set_id="2b0b1b1a-a3c0-4267-894a-0c40cb84a5af",
            set_length=7,
            src_ids=["GNSSSET_ID"],
            src_typs=["GNSSSET"],
            start_alt=525.664,
            start_index=2,
            start_lat=38.834,
            start_lon=-104.821,
            tags=["TAG1", "TAG2"],
        )
        assert gnssrawif is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.gnssrawif.with_raw_response.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert gnssrawif is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.gnssrawif.with_streaming_response.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGnssrawif:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.filedrop.gnssrawif.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
        )
        assert gnssrawif is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.filedrop.gnssrawif.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
            id="GNSSRawIF-ID",
            bit_depth=8,
            boresight=[0, 1, 0],
            data_rate=0.205,
            diff_code_bias=[0.0271, 0.0016],
            end_alt=525.626,
            end_lat=38.922,
            end_lon=-104.67,
            es_id="60f7a241-b7be-48d8-acf3-786670af53f9",
            event_id="2f2205c9-7bc2-4e1a-8416-2f80cc71f64b",
            if_freq=[4.09, 5.87],
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="L2045",
            post_fourier=["NONE", "NONE"],
            quat=[0, -0.2734104, 0.1562345, 0.9491246],
            receiver="GPS1",
            sample_rate=[8000, 9000],
            sample_type="COMPLEX",
            sat_no=32375,
            sequence_id=1,
            set_id="2b0b1b1a-a3c0-4267-894a-0c40cb84a5af",
            set_length=7,
            src_ids=["GNSSSET_ID"],
            src_typs=["GNSSSET"],
            start_alt=525.664,
            start_index=2,
            start_lat=38.834,
            start_lon=-104.821,
            tags=["TAG1", "TAG2"],
        )
        assert gnssrawif is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.gnssrawif.with_raw_response.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert gnssrawif is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.gnssrawif.with_streaming_response.create(
            center_freq=[1227.6, 1575.4],
            classification_marking="U",
            data_mode="REAL",
            end_time=parse_datetime("2022-04-09T18:12:28.919768Z"),
            file_name="somefile.hdf5",
            source="Bluestaq",
            start_time=parse_datetime("2022-04-09T18:11:28.919768Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True
