# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EmireportGetResponse,
    EmireportListResponse,
    EmireportTupleResponse,
    EmireportQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmireport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
        )
        assert emireport is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            actions_taken="verified connections, cables and antenna pointing angles",
            aff_activity="UPLINK",
            alt=1750,
            aor="NORTHCOM",
            band="SHF",
            beam_pattern="MAIN LOBE",
            channel="10C-10CU",
            chan_pirate=False,
            description="Interference on channel",
            dne_impact="Text description of the duration, nature and extent (DNE) of the impact.",
            emi_type="BARRAGE",
            end_time=parse_datetime("2025-01-07T21:30:51.672Z"),
            frequency=1575.42,
            geo_loc_err_ellp=[1300, 700, 35],
            gps_encrypted=False,
            gps_freq="L1",
            high_affected_frequency=1725,
            intercept=False,
            intercept_lang="ENGLISH",
            intercept_type="VOICE",
            int_src_amplitude=0.275,
            int_src_bandwidth=30,
            int_src_cent_freq=485.7,
            int_src_encrypted=False,
            int_src_modulation="FSK",
            isr_collection_impact=False,
            kill_box="7F9SW",
            lat=38.7375,
            link="SPOT-21",
            lon=-104.7889,
            mil_grid="4QFJ12345678",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="25724",
            persistence="CONTINUOUS",
            platform="CVN-78",
            rcvr_demod="FSK",
            rcvr_gain=23.7,
            rcvr_location="FORT CARSON GARAGE",
            rcvr_type="OMNI",
            resp_service="ARMY",
            satcom_priority="HIGH",
            sat_downlink_frequency=47432.5,
            sat_downlink_polarization="V",
            sat_name="MILSTAR DFS-3",
            sat_no=25724,
            sat_transponder_id="36097-8433-10C",
            sat_uplink_frequency=44532.1,
            sat_uplink_polarization="H",
            status="INITIAL",
            supported_isr_role="IMAGERY",
            system="RADIO",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            victim_alt_country="US",
            victim_country_code="US",
            victim_func_impacts="C2",
            victim_poc_mail="bob@jammer.com",
            victim_poc_name="Robert Smith",
            victim_poc_phone="7198675309",
            victim_poc_unit="4th Engineering Battalion",
            victim_reaction="TROUBLESHOOT",
        )
        assert emireport is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert emireport is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert emireport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EmireportListResponse], emireport, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EmireportListResponse], emireport, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert_matches_type(SyncOffsetPage[EmireportListResponse], emireport, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert_matches_type(SyncOffsetPage[EmireportListResponse], emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, emireport, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, emireport, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert_matches_type(str, emireport, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert_matches_type(str, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )
        assert emireport is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert emireport is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert emireport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.get(
            id="id",
        )
        assert_matches_type(EmireportGetResponse, emireport, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmireportGetResponse, emireport, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert_matches_type(EmireportGetResponse, emireport, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert_matches_type(EmireportGetResponse, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emireport.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.queryhelp()
        assert_matches_type(EmireportQueryhelpResponse, emireport, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert_matches_type(EmireportQueryhelpResponse, emireport, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert_matches_type(EmireportQueryhelpResponse, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        emireport = client.emireport.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )
        assert emireport is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.emireport.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = response.parse()
        assert emireport is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.emireport.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = response.parse()
            assert emireport is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEmireport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
        )
        assert emireport is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            actions_taken="verified connections, cables and antenna pointing angles",
            aff_activity="UPLINK",
            alt=1750,
            aor="NORTHCOM",
            band="SHF",
            beam_pattern="MAIN LOBE",
            channel="10C-10CU",
            chan_pirate=False,
            description="Interference on channel",
            dne_impact="Text description of the duration, nature and extent (DNE) of the impact.",
            emi_type="BARRAGE",
            end_time=parse_datetime("2025-01-07T21:30:51.672Z"),
            frequency=1575.42,
            geo_loc_err_ellp=[1300, 700, 35],
            gps_encrypted=False,
            gps_freq="L1",
            high_affected_frequency=1725,
            intercept=False,
            intercept_lang="ENGLISH",
            intercept_type="VOICE",
            int_src_amplitude=0.275,
            int_src_bandwidth=30,
            int_src_cent_freq=485.7,
            int_src_encrypted=False,
            int_src_modulation="FSK",
            isr_collection_impact=False,
            kill_box="7F9SW",
            lat=38.7375,
            link="SPOT-21",
            lon=-104.7889,
            mil_grid="4QFJ12345678",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="25724",
            persistence="CONTINUOUS",
            platform="CVN-78",
            rcvr_demod="FSK",
            rcvr_gain=23.7,
            rcvr_location="FORT CARSON GARAGE",
            rcvr_type="OMNI",
            resp_service="ARMY",
            satcom_priority="HIGH",
            sat_downlink_frequency=47432.5,
            sat_downlink_polarization="V",
            sat_name="MILSTAR DFS-3",
            sat_no=25724,
            sat_transponder_id="36097-8433-10C",
            sat_uplink_frequency=44532.1,
            sat_uplink_polarization="H",
            status="INITIAL",
            supported_isr_role="IMAGERY",
            system="RADIO",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            victim_alt_country="US",
            victim_country_code="US",
            victim_func_impacts="C2",
            victim_poc_mail="bob@jammer.com",
            victim_poc_name="Robert Smith",
            victim_poc_phone="7198675309",
            victim_poc_unit="4th Engineering Battalion",
            victim_reaction="TROUBLESHOOT",
        )
        assert emireport is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert emireport is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            isr=True,
            report_id="REPORT-ID",
            report_time=parse_datetime("2025-01-07T21:47:40.438Z"),
            report_type="SATCOM",
            request_assist=True,
            source="Bluestaq",
            start_time=parse_datetime("2025-01-07T20:16:03.989Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert emireport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EmireportListResponse], emireport, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EmireportListResponse], emireport, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert_matches_type(AsyncOffsetPage[EmireportListResponse], emireport, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.list(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert_matches_type(AsyncOffsetPage[EmireportListResponse], emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, emireport, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, emireport, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert_matches_type(str, emireport, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.count(
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert_matches_type(str, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )
        assert emireport is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert emireport is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert emireport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.get(
            id="id",
        )
        assert_matches_type(EmireportGetResponse, emireport, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmireportGetResponse, emireport, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert_matches_type(EmireportGetResponse, emireport, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert_matches_type(EmireportGetResponse, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emireport.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.queryhelp()
        assert_matches_type(EmireportQueryhelpResponse, emireport, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert_matches_type(EmireportQueryhelpResponse, emireport, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert_matches_type(EmireportQueryhelpResponse, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.tuple(
            columns="columns",
            report_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert_matches_type(EmireportTupleResponse, emireport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        emireport = await async_client.emireport.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )
        assert emireport is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.emireport.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        emireport = await response.parse()
        assert emireport is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.emireport.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "isr": True,
                    "report_id": "REPORT-ID",
                    "report_time": parse_datetime("2025-01-07T21:47:40.438Z"),
                    "report_type": "SATCOM",
                    "request_assist": True,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2025-01-07T20:16:03.989Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            emireport = await response.parse()
            assert emireport is None

        assert cast(Any, response.is_closed) is True
