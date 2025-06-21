# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.link_status import (
    DatalinkListResponse,
    DatalinkTupleResponse,
    DatalinkQueryhelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatalink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )
        assert datalink is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            ack_inst_units=["AOC EXT 2345", "317 AW"],
            ack_req=True,
            alt_diff=20,
            canx_id="ABSTAT",
            canx_originator="505 AOC",
            canx_serial_num="ABC1234567",
            canx_si_cs=["RDU", "X234BS"],
            canx_special_notation="PASEP",
            canx_ts=parse_datetime("2024-01-07T13:55:43.123Z"),
            class_reasons=["15C", "15D"],
            class_source="USJFCOM EXORD SOLID WASTE 98",
            consec_decorr=3,
            course_diff=60,
            dec_exempt_codes=["X1", "X2"],
            dec_inst_dates=["AT EXERCISE ENDEX", "DATE:25NOV1997"],
            decorr_win_mult=1.7,
            geo_datum="EUR-T",
            jre_call_sign="CHARLIE ONE",
            jre_details="JRE details",
            jre_pri_add=71777,
            jre_sec_add=77771,
            jre_unit_des="CVN-72",
            max_geo_pos_qual=12,
            max_track_qual=12,
            mgmt_code="VICTOR",
            mgmt_code_meaning="ORBIT AT POINT BRAVO",
            min_geo_pos_qual=3,
            min_track_qual=6,
            month="OCT",
            multi_duty=[
                {
                    "duty": "SICO",
                    "duty_tele_freq_nums": ["TEL:804-555-4142", "TEL:804-867-5309"],
                    "multi_duty_voice_coord": [
                        {
                            "multi_comm_pri": "P",
                            "multi_freq_des": "ST300A",
                            "multi_tele_freq_nums": ["TEL:804-555-4142", "TEL:804-867-5309"],
                            "multi_voice_net_des": "VPN",
                        }
                    ],
                    "name": "POPOVICH",
                    "rank": "LCDR",
                    "unit_des": "SHIP:STENNIS",
                }
            ],
            non_link_unit_des=["CS:GRAY GHOST", "CS:WHITE WHALE"],
            op_ex_info="CONTROL",
            op_ex_info_alt="ORANGE",
            ops=[
                {
                    "link_details": "Link details",
                    "link_name": "Link-16",
                    "link_start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                    "link_stop_time": parse_datetime("2024-01-08T13:55:43.123Z"),
                    "link_stop_time_mod": "AFTER",
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            plan_orig_num="SACEUR 106",
            poc_call_sign="4077 MASH",
            poc_lat=45.23,
            poc_loc_name="CAMP SWAMPY",
            poc_lon=179.1,
            poc_name="F. BURNS",
            poc_nums=["TEL:804-555-4142", "TEL:804-867-5309"],
            poc_rank="MAJ",
            qualifier="CHG",
            qual_sn=1,
            references=[
                {
                    "ref_originator": "CENTCOM",
                    "ref_serial_id": "A",
                    "ref_serial_num": "1402001",
                    "ref_si_cs": ["RDU", "C-123-92"],
                    "ref_special_notation": "NOTAL",
                    "ref_ts": parse_datetime("2024-01-07T13:55:43.123Z"),
                    "ref_type": "ABSTAT",
                }
            ],
            ref_points=[
                {
                    "eff_event_time": parse_datetime("2024-01-08T13:55:43.123Z"),
                    "ref_des": "L5",
                    "ref_lat": 45.23,
                    "ref_loc_name": "FORT BRAGG",
                    "ref_lon": 179.1,
                    "ref_point_type": "DLRP",
                }
            ],
            remarks=[
                {
                    "text": "Example data link remarks",
                    "type": "CONTINGENCY PROCEDURES",
                }
            ],
            res_track_qual=3,
            serial_num="1201003",
            spec_tracks=[
                {
                    "spec_track_num": "12345",
                    "spec_track_num_desc": "SAM SITE CHARLIE",
                }
            ],
            speed_diff=50,
            stop_time=parse_datetime("2024-01-08T13:55:43.123Z"),
            stop_time_mod="AFTER",
            sys_default_code="MAN",
            track_num_block_l_ls=[1234, 2345],
            track_num_blocks=["0200-0300", "0400-4412"],
            voice_coord=[
                {
                    "comm_pri": "P",
                    "freq_des": "ST300A",
                    "tele_freq_nums": ["TEL:804-555-4142", "TEL:804-867-5309"],
                    "voice_net_des": "VPN",
                }
            ],
            win_size_min=1.25,
            win_size_mult=2.1,
        )
        assert datalink is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert datalink is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
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
        assert_matches_type(SyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert_matches_type(SyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert_matches_type(SyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, datalink, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.queryhelp()
        assert_matches_type(DatalinkQueryhelpResponse, datalink, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert_matches_type(DatalinkQueryhelpResponse, datalink, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert_matches_type(DatalinkQueryhelpResponse, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        datalink = client.link_status.datalink.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )
        assert datalink is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.link_status.datalink.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = response.parse()
        assert datalink is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.link_status.datalink.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDatalink:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )
        assert datalink is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            ack_inst_units=["AOC EXT 2345", "317 AW"],
            ack_req=True,
            alt_diff=20,
            canx_id="ABSTAT",
            canx_originator="505 AOC",
            canx_serial_num="ABC1234567",
            canx_si_cs=["RDU", "X234BS"],
            canx_special_notation="PASEP",
            canx_ts=parse_datetime("2024-01-07T13:55:43.123Z"),
            class_reasons=["15C", "15D"],
            class_source="USJFCOM EXORD SOLID WASTE 98",
            consec_decorr=3,
            course_diff=60,
            dec_exempt_codes=["X1", "X2"],
            dec_inst_dates=["AT EXERCISE ENDEX", "DATE:25NOV1997"],
            decorr_win_mult=1.7,
            geo_datum="EUR-T",
            jre_call_sign="CHARLIE ONE",
            jre_details="JRE details",
            jre_pri_add=71777,
            jre_sec_add=77771,
            jre_unit_des="CVN-72",
            max_geo_pos_qual=12,
            max_track_qual=12,
            mgmt_code="VICTOR",
            mgmt_code_meaning="ORBIT AT POINT BRAVO",
            min_geo_pos_qual=3,
            min_track_qual=6,
            month="OCT",
            multi_duty=[
                {
                    "duty": "SICO",
                    "duty_tele_freq_nums": ["TEL:804-555-4142", "TEL:804-867-5309"],
                    "multi_duty_voice_coord": [
                        {
                            "multi_comm_pri": "P",
                            "multi_freq_des": "ST300A",
                            "multi_tele_freq_nums": ["TEL:804-555-4142", "TEL:804-867-5309"],
                            "multi_voice_net_des": "VPN",
                        }
                    ],
                    "name": "POPOVICH",
                    "rank": "LCDR",
                    "unit_des": "SHIP:STENNIS",
                }
            ],
            non_link_unit_des=["CS:GRAY GHOST", "CS:WHITE WHALE"],
            op_ex_info="CONTROL",
            op_ex_info_alt="ORANGE",
            ops=[
                {
                    "link_details": "Link details",
                    "link_name": "Link-16",
                    "link_start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                    "link_stop_time": parse_datetime("2024-01-08T13:55:43.123Z"),
                    "link_stop_time_mod": "AFTER",
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            plan_orig_num="SACEUR 106",
            poc_call_sign="4077 MASH",
            poc_lat=45.23,
            poc_loc_name="CAMP SWAMPY",
            poc_lon=179.1,
            poc_name="F. BURNS",
            poc_nums=["TEL:804-555-4142", "TEL:804-867-5309"],
            poc_rank="MAJ",
            qualifier="CHG",
            qual_sn=1,
            references=[
                {
                    "ref_originator": "CENTCOM",
                    "ref_serial_id": "A",
                    "ref_serial_num": "1402001",
                    "ref_si_cs": ["RDU", "C-123-92"],
                    "ref_special_notation": "NOTAL",
                    "ref_ts": parse_datetime("2024-01-07T13:55:43.123Z"),
                    "ref_type": "ABSTAT",
                }
            ],
            ref_points=[
                {
                    "eff_event_time": parse_datetime("2024-01-08T13:55:43.123Z"),
                    "ref_des": "L5",
                    "ref_lat": 45.23,
                    "ref_loc_name": "FORT BRAGG",
                    "ref_lon": 179.1,
                    "ref_point_type": "DLRP",
                }
            ],
            remarks=[
                {
                    "text": "Example data link remarks",
                    "type": "CONTINGENCY PROCEDURES",
                }
            ],
            res_track_qual=3,
            serial_num="1201003",
            spec_tracks=[
                {
                    "spec_track_num": "12345",
                    "spec_track_num_desc": "SAM SITE CHARLIE",
                }
            ],
            speed_diff=50,
            stop_time=parse_datetime("2024-01-08T13:55:43.123Z"),
            stop_time_mod="AFTER",
            sys_default_code="MAN",
            track_num_block_l_ls=[1234, 2345],
            track_num_blocks=["0200-0300", "0400-4412"],
            voice_coord=[
                {
                    "comm_pri": "P",
                    "freq_des": "ST300A",
                    "tele_freq_nums": ["TEL:804-555-4142", "TEL:804-867-5309"],
                    "voice_net_des": "VPN",
                }
            ],
            win_size_min=1.25,
            win_size_mult=2.1,
        )
        assert datalink is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert datalink is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
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
        assert_matches_type(AsyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert_matches_type(AsyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert_matches_type(AsyncOffsetPage[DatalinkListResponse], datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, datalink, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.queryhelp()
        assert_matches_type(DatalinkQueryhelpResponse, datalink, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert_matches_type(DatalinkQueryhelpResponse, datalink, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert_matches_type(DatalinkQueryhelpResponse, datalink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DatalinkTupleResponse, datalink, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        datalink = await async_client.link_status.datalink.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )
        assert datalink is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.link_status.datalink.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datalink = await response.parse()
        assert datalink is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.link_status.datalink.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datalink = await response.parse()
            assert datalink is None

        assert cast(Any, response.is_closed) is True
