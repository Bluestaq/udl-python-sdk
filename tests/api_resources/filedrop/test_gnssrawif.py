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
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert gnssrawif is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.filedrop.gnssrawif.create(
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            bit_depth=0,
            boresight=[0],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            data_rate=0,
            diff_code_bias=[0],
            end_alt=0,
            end_lat=0,
            end_lon=0,
            es_id="esId",
            event_id="eventId",
            file_size=0,
            id_on_orbit="idOnOrbit",
            if_freq=[0],
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            post_fourier=["string"],
            quat=[0],
            receiver="receiver",
            sample_rate=[0],
            sample_type="sampleType",
            sat_no=0,
            sequence_id=0,
            set_id="setId",
            set_length=0,
            src_ids=["string"],
            src_typs=["string"],
            start_alt=0,
            start_index=0,
            start_lat=0,
            start_lon=0,
            tags=["string"],
        )
        assert gnssrawif is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.gnssrawif.with_raw_response.create(
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert gnssrawif is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.gnssrawif.with_streaming_response.create(
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
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
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert gnssrawif is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.filedrop.gnssrawif.create(
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            bit_depth=0,
            boresight=[0],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            data_rate=0,
            diff_code_bias=[0],
            end_alt=0,
            end_lat=0,
            end_lon=0,
            es_id="esId",
            event_id="eventId",
            file_size=0,
            id_on_orbit="idOnOrbit",
            if_freq=[0],
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            post_fourier=["string"],
            quat=[0],
            receiver="receiver",
            sample_rate=[0],
            sample_type="sampleType",
            sat_no=0,
            sequence_id=0,
            set_id="setId",
            set_length=0,
            src_ids=["string"],
            src_typs=["string"],
            start_alt=0,
            start_index=0,
            start_lat=0,
            start_lon=0,
            tags=["string"],
        )
        assert gnssrawif is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.gnssrawif.with_raw_response.create(
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert gnssrawif is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.gnssrawif.with_streaming_response.create(
            center_freq=[0],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_name="fileName",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True
