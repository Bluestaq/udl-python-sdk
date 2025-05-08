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
    Ecpsdr,
    EcpsdrAbridged,
    EcpsdrTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEcpsdr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
        )
        assert ecpsdr is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
            id="ECPSDR-ID",
            asl5_v_curr_mon=12,
            cds_plate_v_mon=12,
            cds_ref_v_mon=12,
            cds_threshold=12,
            cds_throttle=12,
            checksum=12,
            dos_bias=12,
            dsl5_v_curr_mon=12,
            esd_trig_count_h=12,
            esd_trig_count_l=12,
            hi_let_l=2,
            hi_let_m=2,
            id_sensor="SENSOR-ID",
            low_let_l=2,
            low_let_m=2,
            med_let1_l=2,
            med_let1_m=2,
            med_let2_l=2,
            med_let2_m=2,
            med_let3_l=2,
            med_let3_m=2,
            med_let4_l=2,
            med_let4_m=2,
            mp_temp=12,
            ob_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            pd1_sig_lev=12,
            pd2_sig_lev=12,
            ps_temp_mon=12,
            retransmit=True,
            sat_no=101,
            sen_mode="TEST",
            surf_dos_charge_h=12,
            surf_dos_charge_l=12,
            surf_dos_h=12,
            surf_dos_l=12,
            surf_dos_m=12,
            surf_dos_stat=2,
            transient_data=[1, 2, 3],
            v_ref=12,
        )
        assert ecpsdr is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert ecpsdr is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.retrieve(
            id="id",
        )
        assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.observations.ecpsdr.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert_matches_type(SyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert_matches_type(SyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ecpsdr, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ecpsdr, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert_matches_type(str, ecpsdr, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert_matches_type(str, ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )
        assert ecpsdr is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert ecpsdr is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.query_help()
        assert ecpsdr is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert ecpsdr is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.observations.ecpsdr.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.observations.ecpsdr.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.observations.ecpsdr.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEcpsdr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
        )
        assert ecpsdr is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
            id="ECPSDR-ID",
            asl5_v_curr_mon=12,
            cds_plate_v_mon=12,
            cds_ref_v_mon=12,
            cds_threshold=12,
            cds_throttle=12,
            checksum=12,
            dos_bias=12,
            dsl5_v_curr_mon=12,
            esd_trig_count_h=12,
            esd_trig_count_l=12,
            hi_let_l=2,
            hi_let_m=2,
            id_sensor="SENSOR-ID",
            low_let_l=2,
            low_let_m=2,
            med_let1_l=2,
            med_let1_m=2,
            med_let2_l=2,
            med_let2_m=2,
            med_let3_l=2,
            med_let3_m=2,
            med_let4_l=2,
            med_let4_m=2,
            mp_temp=12,
            ob_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            pd1_sig_lev=12,
            pd2_sig_lev=12,
            ps_temp_mon=12,
            retransmit=True,
            sat_no=101,
            sen_mode="TEST",
            surf_dos_charge_h=12,
            surf_dos_charge_l=12,
            surf_dos_h=12,
            surf_dos_l=12,
            surf_dos_m=12,
            surf_dos_stat=2,
            transient_data=[1, 2, 3],
            v_ref=12,
        )
        assert ecpsdr is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert ecpsdr is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            type="STANDARD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.retrieve(
            id="id",
        )
        assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert_matches_type(Ecpsdr, ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.observations.ecpsdr.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert_matches_type(AsyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert_matches_type(AsyncOffsetPage[EcpsdrAbridged], ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ecpsdr, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ecpsdr, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert_matches_type(str, ecpsdr, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert_matches_type(str, ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )
        assert ecpsdr is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert ecpsdr is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.query_help()
        assert ecpsdr is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert ecpsdr is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.observations.ecpsdr.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.ecpsdr.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.ecpsdr.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert_matches_type(EcpsdrTupleResponse, ecpsdr, path=["response"])

        assert cast(Any, response.is_closed) is True
