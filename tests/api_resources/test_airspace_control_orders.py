# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirspacecontrolorderFull,
    AirspaceControlOrderListResponse,
    AirspaceControlOrderTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirspaceControlOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert airspace_control_order is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            aco_comments="acoComments",
            aco_serial_num="acoSerialNum",
            airspace_control_means_status=[
                {
                    "airspace_control_means": [
                        {
                            "airspace_control_point": [
                                {
                                    "ctrl_pt_altitude": "ctrlPtAltitude",
                                    "ctrl_pt_location": "ctrlPtLocation",
                                    "ctrl_pt_name": "ctrlPtName",
                                    "ctrl_pt_type": "ctrlPtType",
                                }
                            ],
                            "airspace_time_period": [
                                {
                                    "int_dur": ["string"],
                                    "int_freq": ["string"],
                                    "time_end": "timeEnd",
                                    "time_mode": "timeMode",
                                    "time_start": "timeStart",
                                }
                            ],
                            "bearing0": 0,
                            "bearing1": 0,
                            "cm_id": "cmId",
                            "cm_shape": "cmShape",
                            "cm_type": "cmType",
                            "cntrl_auth": "cntrlAuth",
                            "cntrl_auth_freqs": ["string"],
                            "coord0": "coord0",
                            "coord1": "coord1",
                            "corr_way_points": ["string"],
                            "eff_v_dim": "effVDim",
                            "free_text": "freeText",
                            "gen_text_ind": "genTextInd",
                            "geo_datum_alt": "geoDatumAlt",
                            "link16_id": "link16Id",
                            "orbit_alignment": "orbitAlignment",
                            "poly_coord": ["string"],
                            "rad_mag0": 0,
                            "rad_mag1": 0,
                            "rad_mag_unit": "radMagUnit",
                            "track_leg": 0,
                            "trans_altitude": "transAltitude",
                            "usage": "usage",
                            "width": 0,
                            "width_left": 0,
                            "width_right": 0,
                            "width_unit": "widthUnit",
                        }
                    ],
                    "cm_stat": "cmStat",
                    "cm_stat_id": ["string"],
                }
            ],
            airspace_control_order_references=[
                {
                    "ref_originator": "refOriginator",
                    "ref_serial_num": "refSerialNum",
                    "ref_si_cs": ["string"],
                    "ref_s_id": "refSId",
                    "ref_special_notation": "refSpecialNotation",
                    "ref_ts": "2019-12-27T18:11:19.117Z",
                    "ref_type": "refType",
                }
            ],
            area_of_validity="areaOfValidity",
            class_reasons=["string"],
            class_source="classSource",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            declass_exemption_codes=["string"],
            downgrade_ins_dates=["string"],
            geo_datum="geoDatum",
            month="month",
            op_ex_info="opExInfo",
            op_ex_info_alt="opExInfoAlt",
            origin="origin",
            orig_network="origNetwork",
            plan_orig_num="planOrigNum",
            qualifier="qualifier",
            qual_sn=0,
            raw_file_uri="rawFileURI",
            serial_num="serialNum",
            source_dl="sourceDL",
            stop_qualifier="stopQualifier",
            stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            und_lnk_trks=["string"],
        )
        assert airspace_control_order is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert airspace_control_order is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.retrieve(
            "id",
        )
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airspace_control_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.list()
        assert_matches_type(AirspaceControlOrderListResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(AirspaceControlOrderListResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(AirspaceControlOrderListResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.count()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(str, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.create_bulk(
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
        assert airspace_control_order is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.create_bulk(
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
        airspace_control_order = response.parse()
        assert airspace_control_order is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.create_bulk(
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

            airspace_control_order = response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.query_help()
        assert airspace_control_order is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert airspace_control_order is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirspaceControlOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert airspace_control_order is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            aco_comments="acoComments",
            aco_serial_num="acoSerialNum",
            airspace_control_means_status=[
                {
                    "airspace_control_means": [
                        {
                            "airspace_control_point": [
                                {
                                    "ctrl_pt_altitude": "ctrlPtAltitude",
                                    "ctrl_pt_location": "ctrlPtLocation",
                                    "ctrl_pt_name": "ctrlPtName",
                                    "ctrl_pt_type": "ctrlPtType",
                                }
                            ],
                            "airspace_time_period": [
                                {
                                    "int_dur": ["string"],
                                    "int_freq": ["string"],
                                    "time_end": "timeEnd",
                                    "time_mode": "timeMode",
                                    "time_start": "timeStart",
                                }
                            ],
                            "bearing0": 0,
                            "bearing1": 0,
                            "cm_id": "cmId",
                            "cm_shape": "cmShape",
                            "cm_type": "cmType",
                            "cntrl_auth": "cntrlAuth",
                            "cntrl_auth_freqs": ["string"],
                            "coord0": "coord0",
                            "coord1": "coord1",
                            "corr_way_points": ["string"],
                            "eff_v_dim": "effVDim",
                            "free_text": "freeText",
                            "gen_text_ind": "genTextInd",
                            "geo_datum_alt": "geoDatumAlt",
                            "link16_id": "link16Id",
                            "orbit_alignment": "orbitAlignment",
                            "poly_coord": ["string"],
                            "rad_mag0": 0,
                            "rad_mag1": 0,
                            "rad_mag_unit": "radMagUnit",
                            "track_leg": 0,
                            "trans_altitude": "transAltitude",
                            "usage": "usage",
                            "width": 0,
                            "width_left": 0,
                            "width_right": 0,
                            "width_unit": "widthUnit",
                        }
                    ],
                    "cm_stat": "cmStat",
                    "cm_stat_id": ["string"],
                }
            ],
            airspace_control_order_references=[
                {
                    "ref_originator": "refOriginator",
                    "ref_serial_num": "refSerialNum",
                    "ref_si_cs": ["string"],
                    "ref_s_id": "refSId",
                    "ref_special_notation": "refSpecialNotation",
                    "ref_ts": "2019-12-27T18:11:19.117Z",
                    "ref_type": "refType",
                }
            ],
            area_of_validity="areaOfValidity",
            class_reasons=["string"],
            class_source="classSource",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            declass_exemption_codes=["string"],
            downgrade_ins_dates=["string"],
            geo_datum="geoDatum",
            month="month",
            op_ex_info="opExInfo",
            op_ex_info_alt="opExInfoAlt",
            origin="origin",
            orig_network="origNetwork",
            plan_orig_num="planOrigNum",
            qualifier="qualifier",
            qual_sn=0,
            raw_file_uri="rawFileURI",
            serial_num="serialNum",
            source_dl="sourceDL",
            stop_qualifier="stopQualifier",
            stop_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            und_lnk_trks=["string"],
        )
        assert airspace_control_order is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert airspace_control_order is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            op_ex_name="opExName",
            originator="originator",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.retrieve(
            "id",
        )
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airspace_control_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.list()
        assert_matches_type(AirspaceControlOrderListResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AirspaceControlOrderListResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(AirspaceControlOrderListResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.count()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(str, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.create_bulk(
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
        assert airspace_control_order is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.create_bulk(
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
        airspace_control_order = await response.parse()
        assert airspace_control_order is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.create_bulk(
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

            airspace_control_order = await response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.query_help()
        assert airspace_control_order is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert airspace_control_order is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True
