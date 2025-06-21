# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EquipmentFull,
    EquipmentAbridged,
    EquipmentTupleResponse,
    EquipmentQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEquipment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )
        assert equipment is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_eqp_id="ORIG-EQP-ID",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eqp_code="X12345",
            eqp_id_num="001",
            eval=7,
            fpa="NOB",
            function="OCC",
            funct_primary="JG",
            geoidal_msl_sep=12.34,
            ident="FRIEND",
            id_operating_unit="UNIT-ID",
            id_parent_equipment="PARENT-EQUIPMENT-ID",
            id_site="SITE-ID",
            loc_reason="GR",
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            nomen="AMPHIBIOUS WARFARE SHIP",
            oper_area_primary="Territorial Sea",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            qty_oh=7,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            seq_num=5,
            src_ids=["SRC_ID_1"],
            src_typs=["AIRCRAFT"],
            sym_code="SOGPU----------",
            utm="19P4390691376966",
            wac="0427",
        )
        assert equipment is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.retrieve(
            id="id",
        )
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(EquipmentFull, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.equipment.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )
        assert equipment is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_eqp_id="ORIG-EQP-ID",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eqp_code="X12345",
            eqp_id_num="001",
            eval=7,
            fpa="NOB",
            function="OCC",
            funct_primary="JG",
            geoidal_msl_sep=12.34,
            ident="FRIEND",
            id_operating_unit="UNIT-ID",
            id_parent_equipment="PARENT-EQUIPMENT-ID",
            id_site="SITE-ID",
            loc_reason="GR",
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            nomen="AMPHIBIOUS WARFARE SHIP",
            oper_area_primary="Territorial Sea",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            qty_oh=7,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            seq_num=5,
            src_ids=["SRC_ID_1"],
            src_typs=["AIRCRAFT"],
            sym_code="SOGPU----------",
            utm="19P4390691376966",
            wac="0427",
        )
        assert equipment is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.equipment.with_raw_response.update(
                path_id="",
                classification_marking="U",
                country_code="IQ",
                data_mode="TEST",
                lat=39.019242,
                lon=-104.251659,
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.list()
        assert_matches_type(SyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(SyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(SyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.delete(
            "id",
        )
        assert equipment is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.equipment.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.count()
        assert_matches_type(str, equipment, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, equipment, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(str, equipment, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(str, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "IQ",
                    "data_mode": "TEST",
                    "lat": 39.019242,
                    "lon": -104.251659,
                    "source": "Bluestaq",
                }
            ],
        )
        assert equipment is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "IQ",
                    "data_mode": "TEST",
                    "lat": 39.019242,
                    "lon": -104.251659,
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "IQ",
                    "data_mode": "TEST",
                    "lat": 39.019242,
                    "lon": -104.251659,
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.query_help()
        assert_matches_type(EquipmentQueryHelpResponse, equipment, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(EquipmentQueryHelpResponse, equipment, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(EquipmentQueryHelpResponse, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.tuple(
            columns="columns",
        )
        assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEquipment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )
        assert equipment is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_eqp_id="ORIG-EQP-ID",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eqp_code="X12345",
            eqp_id_num="001",
            eval=7,
            fpa="NOB",
            function="OCC",
            funct_primary="JG",
            geoidal_msl_sep=12.34,
            ident="FRIEND",
            id_operating_unit="UNIT-ID",
            id_parent_equipment="PARENT-EQUIPMENT-ID",
            id_site="SITE-ID",
            loc_reason="GR",
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            nomen="AMPHIBIOUS WARFARE SHIP",
            oper_area_primary="Territorial Sea",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            qty_oh=7,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            seq_num=5,
            src_ids=["SRC_ID_1"],
            src_typs=["AIRCRAFT"],
            sym_code="SOGPU----------",
            utm="19P4390691376966",
            wac="0427",
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.create(
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.retrieve(
            id="id",
        )
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(EquipmentFull, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.equipment.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )
        assert equipment is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_eqp_id="ORIG-EQP-ID",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eqp_code="X12345",
            eqp_id_num="001",
            eval=7,
            fpa="NOB",
            function="OCC",
            funct_primary="JG",
            geoidal_msl_sep=12.34,
            ident="FRIEND",
            id_operating_unit="UNIT-ID",
            id_parent_equipment="PARENT-EQUIPMENT-ID",
            id_site="SITE-ID",
            loc_reason="GR",
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            nomen="AMPHIBIOUS WARFARE SHIP",
            oper_area_primary="Territorial Sea",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            qty_oh=7,
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            seq_num=5,
            src_ids=["SRC_ID_1"],
            src_typs=["AIRCRAFT"],
            sym_code="SOGPU----------",
            utm="19P4390691376966",
            wac="0427",
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            country_code="IQ",
            data_mode="TEST",
            lat=39.019242,
            lon=-104.251659,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.equipment.with_raw_response.update(
                path_id="",
                classification_marking="U",
                country_code="IQ",
                data_mode="TEST",
                lat=39.019242,
                lon=-104.251659,
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.list()
        assert_matches_type(AsyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(AsyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(AsyncOffsetPage[EquipmentAbridged], equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.delete(
            "id",
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.equipment.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.count()
        assert_matches_type(str, equipment, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, equipment, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(str, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(str, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "IQ",
                    "data_mode": "TEST",
                    "lat": 39.019242,
                    "lon": -104.251659,
                    "source": "Bluestaq",
                }
            ],
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "IQ",
                    "data_mode": "TEST",
                    "lat": 39.019242,
                    "lon": -104.251659,
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "country_code": "IQ",
                    "data_mode": "TEST",
                    "lat": 39.019242,
                    "lon": -104.251659,
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.query_help()
        assert_matches_type(EquipmentQueryHelpResponse, equipment, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(EquipmentQueryHelpResponse, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(EquipmentQueryHelpResponse, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.tuple(
            columns="columns",
        )
        assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(EquipmentTupleResponse, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True
