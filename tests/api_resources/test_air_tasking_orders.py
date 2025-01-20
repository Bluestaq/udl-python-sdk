# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirTaskingOrderFull,
    AirTaskingOrderTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirTaskingOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_tasking_orders.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
        )
        assert air_tasking_order is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_tasking_orders.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
            id="id",
            ack_req_ind="ackReqInd",
            ack_unit_instructions="ackUnitInstructions",
            ac_msn_tasking=[
                {
                    "country_code": "countryCode",
                    "tasked_service": "taskedService",
                    "unit_designator": "unitDesignator",
                    "ac_msn_loc_seg": [
                        {
                            "start_time": "2019-12-27T18:11:19.117Z",
                            "air_msn_pri": "airMsnPri",
                            "alt": 0,
                            "area_geo_rad": 0,
                            "end_time": "2019-12-27T18:11:19.117Z",
                            "msn_loc_name": "msnLocName",
                            "msn_loc_pt_bar_t": "msnLocPtBarT",
                            "msn_loc_pt_lat": 0,
                            "msn_loc_pt_lon": 0,
                            "msn_loc_pt_name": "msnLocPtName",
                        }
                    ],
                    "alert_status": 0,
                    "amc_msn_num": "amcMsnNum",
                    "dep_loc_lat": 0,
                    "dep_loc_lon": 0,
                    "dep_loc_name": "depLocName",
                    "dep_loc_utm": "depLocUTM",
                    "dep_time": "2019-12-27T18:11:19.117Z",
                    "ind_ac_tasking": [
                        {
                            "acft_type": "acftType",
                            "call_sign": "callSign",
                            "iff_sif_mode1_code": "iffSifMode1Code",
                            "iff_sif_mode2_code": "iffSifMode2Code",
                            "iff_sif_mode3_code": "iffSifMode3Code",
                            "ju_address": [0],
                            "link16_call_sign": "link16CallSign",
                            "num_acft": 0,
                            "pri_config_code": "priConfigCode",
                            "sec_config_code": "secConfigCode",
                            "tacan_chan": 0,
                        }
                    ],
                    "msn_commander": "msnCommander",
                    "msn_num": "msnNum",
                    "pkg_id": "pkgId",
                    "pri_msn_type": "priMsnType",
                    "rcvy_loc_lat": [0],
                    "rcvy_loc_lon": [0],
                    "rcvy_loc_name": ["string"],
                    "rcvy_loc_utm": ["string"],
                    "rcvy_time": ["2019-12-27T18:11:19.117Z"],
                    "res_msn_ind": "resMsnInd",
                    "sec_msn_type": "secMsnType",
                    "unit_loc_name": "unitLocName",
                }
            ],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            end_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            gen_text=[
                {
                    "text": "text",
                    "text_ind": "textInd",
                }
            ],
            msg_month="msgMonth",
            msg_originator="msgOriginator",
            msg_qualifier="msgQualifier",
            msg_sn="msgSN",
            naval_flt_ops=[
                {
                    "ship_name": "shipName",
                    "flt_op_start": "2019-12-27T18:11:19.117Z",
                    "flt_op_stop": "2019-12-27T18:11:19.117Z",
                    "schd_launch_rcvy_time": ["2019-12-27T18:11:19.117Z"],
                }
            ],
            origin="origin",
            orig_network="origNetwork",
            raw_file_uri="rawFileURI",
            source_dl="sourceDL",
        )
        assert air_tasking_order is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_tasking_orders.with_raw_response.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert air_tasking_order is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_tasking_orders.with_streaming_response.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_tasking_orders.retrieve(
            "id",
        )
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.air_tasking_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.air_tasking_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.air_tasking_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_tasking_orders.count()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.air_tasking_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.air_tasking_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(str, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_tasking_orders.query_help()
        assert air_tasking_order is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.air_tasking_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert air_tasking_order is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.air_tasking_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_tasking_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.air_tasking_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.air_tasking_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirTaskingOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_tasking_orders.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
        )
        assert air_tasking_order is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_tasking_orders.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
            id="id",
            ack_req_ind="ackReqInd",
            ack_unit_instructions="ackUnitInstructions",
            ac_msn_tasking=[
                {
                    "country_code": "countryCode",
                    "tasked_service": "taskedService",
                    "unit_designator": "unitDesignator",
                    "ac_msn_loc_seg": [
                        {
                            "start_time": "2019-12-27T18:11:19.117Z",
                            "air_msn_pri": "airMsnPri",
                            "alt": 0,
                            "area_geo_rad": 0,
                            "end_time": "2019-12-27T18:11:19.117Z",
                            "msn_loc_name": "msnLocName",
                            "msn_loc_pt_bar_t": "msnLocPtBarT",
                            "msn_loc_pt_lat": 0,
                            "msn_loc_pt_lon": 0,
                            "msn_loc_pt_name": "msnLocPtName",
                        }
                    ],
                    "alert_status": 0,
                    "amc_msn_num": "amcMsnNum",
                    "dep_loc_lat": 0,
                    "dep_loc_lon": 0,
                    "dep_loc_name": "depLocName",
                    "dep_loc_utm": "depLocUTM",
                    "dep_time": "2019-12-27T18:11:19.117Z",
                    "ind_ac_tasking": [
                        {
                            "acft_type": "acftType",
                            "call_sign": "callSign",
                            "iff_sif_mode1_code": "iffSifMode1Code",
                            "iff_sif_mode2_code": "iffSifMode2Code",
                            "iff_sif_mode3_code": "iffSifMode3Code",
                            "ju_address": [0],
                            "link16_call_sign": "link16CallSign",
                            "num_acft": 0,
                            "pri_config_code": "priConfigCode",
                            "sec_config_code": "secConfigCode",
                            "tacan_chan": 0,
                        }
                    ],
                    "msn_commander": "msnCommander",
                    "msn_num": "msnNum",
                    "pkg_id": "pkgId",
                    "pri_msn_type": "priMsnType",
                    "rcvy_loc_lat": [0],
                    "rcvy_loc_lon": [0],
                    "rcvy_loc_name": ["string"],
                    "rcvy_loc_utm": ["string"],
                    "rcvy_time": ["2019-12-27T18:11:19.117Z"],
                    "res_msn_ind": "resMsnInd",
                    "sec_msn_type": "secMsnType",
                    "unit_loc_name": "unitLocName",
                }
            ],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            end_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            gen_text=[
                {
                    "text": "text",
                    "text_ind": "textInd",
                }
            ],
            msg_month="msgMonth",
            msg_originator="msgOriginator",
            msg_qualifier="msgQualifier",
            msg_sn="msgSN",
            naval_flt_ops=[
                {
                    "ship_name": "shipName",
                    "flt_op_start": "2019-12-27T18:11:19.117Z",
                    "flt_op_stop": "2019-12-27T18:11:19.117Z",
                    "schd_launch_rcvy_time": ["2019-12-27T18:11:19.117Z"],
                }
            ],
            origin="origin",
            orig_network="origNetwork",
            raw_file_uri="rawFileURI",
            source_dl="sourceDL",
        )
        assert air_tasking_order is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_tasking_orders.with_raw_response.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert air_tasking_order is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_tasking_orders.with_streaming_response.create(
            begin_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_exer_name="opExerName",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_tasking_orders.retrieve(
            "id",
        )
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_tasking_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_tasking_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.air_tasking_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_tasking_orders.count()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_tasking_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_tasking_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(str, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_tasking_orders.query_help()
        assert air_tasking_order is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_tasking_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert air_tasking_order is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_tasking_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_tasking_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_tasking_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_tasking_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True
