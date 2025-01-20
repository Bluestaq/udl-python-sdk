# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.link_status import (
    DatalinkListResponse,
    DatalinkTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatalink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert datalink is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            ack_inst_units=["string"],
            ack_req=True,
            alt_diff=0,
            canx_id="canxId",
            canx_originator="canxOriginator",
            canx_serial_num="canxSerialNum",
            canx_si_cs=["string"],
            canx_special_notation="canxSpecialNotation",
            canx_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            class_reasons=["string"],
            class_source="classSource",
            consec_decorr=0,
            course_diff=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            dec_exempt_codes=["string"],
            dec_inst_dates=["string"],
            decorr_win_mult=0,
            geo_datum="geoDatum",
            jre_call_sign="jreCallSign",
            jre_details="jreDetails",
            jre_pri_add=0,
            jre_sec_add=0,
            jre_unit_des="jreUnitDes",
            max_geo_pos_qual=0,
            max_track_qual=0,
            mgmt_code="mgmtCode",
            mgmt_code_meaning="mgmtCodeMeaning",
            min_geo_pos_qual=0,
            min_track_qual=0,
            month="month",
            multi_duty=[
                {
                    "duty": "duty",
                    "duty_tele_freq_nums": ["string"],
                    "multi_duty_voice_coord": [
                        {
                            "multi_comm_pri": "multiCommPri",
                            "multi_freq_des": "multiFreqDes",
                            "multi_tele_freq_nums": ["string"],
                            "multi_voice_net_des": "multiVoiceNetDes",
                        }
                    ],
                    "name": "name",
                    "rank": "rank",
                    "unit_des": "unitDes",
                }
            ],
            non_link_unit_des=["string"],
            op_ex_info="opExInfo",
            op_ex_info_alt="opExInfoAlt",
            ops=[
                {
                    "link_details": "linkDetails",
                    "link_name": "linkName",
                    "link_start_time": "2019-12-27T18:11:19.117Z",
                    "link_stop_time": "2019-12-27T18:11:19.117Z",
                    "link_stop_time_mod": "linkStopTimeMod",
                }
            ],
            origin="origin",
            orig_network="origNetwork",
            plan_orig_num="planOrigNum",
            poc_call_sign="pocCallSign",
            poc_lat=0,
            poc_loc_name="pocLocName",
            poc_lon=0,
            poc_name="pocName",
            poc_nums=["string"],
            poc_rank="pocRank",
            qualifier="qualifier",
            qual_sn=0,
            raw_file_uri="rawFileURI",
            references=[
                {
                    "ref_originator": "refOriginator",
                    "ref_serial_id": "refSerialId",
                    "ref_serial_num": "refSerialNum",
                    "ref_si_cs": ["string"],
                    "ref_special_notation": "refSpecialNotation",
                    "ref_ts": "2019-12-27T18:11:19.117Z",
                    "ref_type": "refType",
                }
            ],
            ref_points=[
                {
                    "eff_event_time": "2019-12-27T18:11:19.117Z",
                    "ref_des": "refDes",
                    "ref_lat": 0,
                    "ref_loc_name": "refLocName",
                    "ref_lon": 0,
                    "ref_point_type": "refPointType",
                }
            ],
            remarks=[
                {
                    "text": "text",
                    "type": "type",
                }
            ],
            res_track_qual=0,
            serial_num="serialNum",
            source_dl="sourceDL",
            spec_tracks=[
                {
                    "spec_track_num": "specTrackNum",
                    "spec_track_num_desc": "specTrackNumDesc",
                }
            ],
            speed_diff=0,
            stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stop_time_mod="stopTimeMod",
            sys_default_code="sysDefaultCode",
            track_num_block_l_ls=[0],
            track_num_blocks=["string"],
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
            voice_coord=[
                {
                    "comm_pri": "commPri",
                    "freq_des": "freqDes",
                    "tele_freq_nums": ["string"],
                    "voice_net_des": "voiceNetDes",
                }
            ],
            win_size_min=0,
            win_size_mult=0,
        )
        assert datalink is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert datalink is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DatalinkListResponse, datalink, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert_matches_type(DatalinkListResponse, datalink, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert_matches_type(DatalinkListResponse, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, datalink, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert_matches_type(str, datalink, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert_matches_type(str, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_file_drop(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.create_file_drop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "op_ex_name": "opExName",
                    "originator": "originator",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                }
            ],
        )
        assert datalink is None

    @parametrize
    def test_raw_response_create_file_drop(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.create_file_drop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "op_ex_name": "opExName",
                    "originator": "originator",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert datalink is None

    @parametrize
    def test_streaming_response_create_file_drop(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.create_file_drop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "op_ex_name": "opExName",
                    "originator": "originator",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.queryhelp()
        assert datalink is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert datalink is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatalink:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert datalink is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            ack_inst_units=["string"],
            ack_req=True,
            alt_diff=0,
            canx_id="canxId",
            canx_originator="canxOriginator",
            canx_serial_num="canxSerialNum",
            canx_si_cs=["string"],
            canx_special_notation="canxSpecialNotation",
            canx_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            class_reasons=["string"],
            class_source="classSource",
            consec_decorr=0,
            course_diff=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            dec_exempt_codes=["string"],
            dec_inst_dates=["string"],
            decorr_win_mult=0,
            geo_datum="geoDatum",
            jre_call_sign="jreCallSign",
            jre_details="jreDetails",
            jre_pri_add=0,
            jre_sec_add=0,
            jre_unit_des="jreUnitDes",
            max_geo_pos_qual=0,
            max_track_qual=0,
            mgmt_code="mgmtCode",
            mgmt_code_meaning="mgmtCodeMeaning",
            min_geo_pos_qual=0,
            min_track_qual=0,
            month="month",
            multi_duty=[
                {
                    "duty": "duty",
                    "duty_tele_freq_nums": ["string"],
                    "multi_duty_voice_coord": [
                        {
                            "multi_comm_pri": "multiCommPri",
                            "multi_freq_des": "multiFreqDes",
                            "multi_tele_freq_nums": ["string"],
                            "multi_voice_net_des": "multiVoiceNetDes",
                        }
                    ],
                    "name": "name",
                    "rank": "rank",
                    "unit_des": "unitDes",
                }
            ],
            non_link_unit_des=["string"],
            op_ex_info="opExInfo",
            op_ex_info_alt="opExInfoAlt",
            ops=[
                {
                    "link_details": "linkDetails",
                    "link_name": "linkName",
                    "link_start_time": "2019-12-27T18:11:19.117Z",
                    "link_stop_time": "2019-12-27T18:11:19.117Z",
                    "link_stop_time_mod": "linkStopTimeMod",
                }
            ],
            origin="origin",
            orig_network="origNetwork",
            plan_orig_num="planOrigNum",
            poc_call_sign="pocCallSign",
            poc_lat=0,
            poc_loc_name="pocLocName",
            poc_lon=0,
            poc_name="pocName",
            poc_nums=["string"],
            poc_rank="pocRank",
            qualifier="qualifier",
            qual_sn=0,
            raw_file_uri="rawFileURI",
            references=[
                {
                    "ref_originator": "refOriginator",
                    "ref_serial_id": "refSerialId",
                    "ref_serial_num": "refSerialNum",
                    "ref_si_cs": ["string"],
                    "ref_special_notation": "refSpecialNotation",
                    "ref_ts": "2019-12-27T18:11:19.117Z",
                    "ref_type": "refType",
                }
            ],
            ref_points=[
                {
                    "eff_event_time": "2019-12-27T18:11:19.117Z",
                    "ref_des": "refDes",
                    "ref_lat": 0,
                    "ref_loc_name": "refLocName",
                    "ref_lon": 0,
                    "ref_point_type": "refPointType",
                }
            ],
            remarks=[
                {
                    "text": "text",
                    "type": "type",
                }
            ],
            res_track_qual=0,
            serial_num="serialNum",
            source_dl="sourceDL",
            spec_tracks=[
                {
                    "spec_track_num": "specTrackNum",
                    "spec_track_num_desc": "specTrackNumDesc",
                }
            ],
            speed_diff=0,
            stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stop_time_mod="stopTimeMod",
            sys_default_code="sysDefaultCode",
            track_num_block_l_ls=[0],
            track_num_blocks=["string"],
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
            voice_coord=[
                {
                    "comm_pri": "commPri",
                    "freq_des": "freqDes",
                    "tele_freq_nums": ["string"],
                    "voice_net_des": "voiceNetDes",
                }
            ],
            win_size_min=0,
            win_size_mult=0,
        )
        assert datalink is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert datalink is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DatalinkListResponse, datalink, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert_matches_type(DatalinkListResponse, datalink, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert_matches_type(DatalinkListResponse, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, datalink, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert_matches_type(str, datalink, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert_matches_type(str, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_file_drop(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.create_file_drop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "op_ex_name": "opExName",
                    "originator": "originator",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                }
            ],
        )
        assert datalink is None

    @parametrize
    async def test_raw_response_create_file_drop(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.create_file_drop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "op_ex_name": "opExName",
                    "originator": "originator",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert datalink is None

    @parametrize
    async def test_streaming_response_create_file_drop(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.create_file_drop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "op_ex_name": "opExName",
                    "originator": "originator",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.queryhelp()
        assert datalink is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert datalink is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True
