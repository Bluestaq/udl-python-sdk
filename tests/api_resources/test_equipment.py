# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EquipmentFull,
    EquipmentListResponse,
    EquipmentTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEquipment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )
        assert equipment is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
            id="id",
            air_def_area="airDefArea",
            allegiance="allegiance",
            alt_allegiance="altAllegiance",
            alt_country_code="altCountryCode",
            alt_eqp_id="altEqpId",
            class_rating="classRating",
            condition="condition",
            condition_avail="conditionAvail",
            coord="coord",
            coord_datum="coordDatum",
            coord_deriv_acc=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_msl=0,
            elev_msl_conf_lvl=0,
            elev_msl_deriv_acc=0,
            eqp_code="eqpCode",
            eqp_id_num="eqpIdNum",
            eval=0,
            fpa="fpa",
            function="function",
            funct_primary="functPrimary",
            geoidal_msl_sep=0,
            ident="ident",
            id_operating_unit="idOperatingUnit",
            id_parent_equipment="idParentEquipment",
            id_site="idSite",
            loc_reason="locReason",
            mil_grid="milGrid",
            mil_grid_sys="milGridSys",
            nomen="nomen",
            oper_area_primary="operAreaPrimary",
            oper_status="operStatus",
            origin="origin",
            pol_subdiv="polSubdiv",
            qty_oh=0,
            rec_status="recStatus",
            reference_doc="referenceDoc",
            res_prod="resProd",
            review_date=parse_date("2019-12-27"),
            seq_num=0,
            src_ids=["string"],
            src_typs=["string"],
            sym_code="symCode",
            utm="utm",
            wac="wac",
        )
        assert equipment is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.retrieve(
            "id",
        )
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )
        assert equipment is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
            id_2="id",
            air_def_area="airDefArea",
            allegiance="allegiance",
            alt_allegiance="altAllegiance",
            alt_country_code="altCountryCode",
            alt_eqp_id="altEqpId",
            class_rating="classRating",
            condition="condition",
            condition_avail="conditionAvail",
            coord="coord",
            coord_datum="coordDatum",
            coord_deriv_acc=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_msl=0,
            elev_msl_conf_lvl=0,
            elev_msl_deriv_acc=0,
            eqp_code="eqpCode",
            eqp_id_num="eqpIdNum",
            eval=0,
            fpa="fpa",
            function="function",
            funct_primary="functPrimary",
            geoidal_msl_sep=0,
            ident="ident",
            id_operating_unit="idOperatingUnit",
            id_parent_equipment="idParentEquipment",
            id_site="idSite",
            loc_reason="locReason",
            mil_grid="milGrid",
            mil_grid_sys="milGridSys",
            nomen="nomen",
            oper_area_primary="operAreaPrimary",
            oper_status="operStatus",
            origin="origin",
            pol_subdiv="polSubdiv",
            qty_oh=0,
            rec_status="recStatus",
            reference_doc="referenceDoc",
            res_prod="resProd",
            review_date=parse_date("2019-12-27"),
            seq_num=0,
            src_ids=["string"],
            src_typs=["string"],
            sym_code="symCode",
            utm="utm",
            wac="wac",
        )
        assert equipment is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.equipment.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                country_code="countryCode",
                data_mode="dataMode",
                lat=0,
                lon=0,
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.list()
        assert_matches_type(EquipmentListResponse, equipment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(EquipmentListResponse, equipment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(EquipmentListResponse, equipment, path=["response"])

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
                    "classification_marking": "classificationMarking",
                    "country_code": "countryCode",
                    "data_mode": "dataMode",
                    "lat": 0,
                    "lon": 0,
                    "source": "source",
                }
            ],
        )
        assert equipment is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "country_code": "countryCode",
                    "data_mode": "dataMode",
                    "lat": 0,
                    "lon": 0,
                    "source": "source",
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
                    "classification_marking": "classificationMarking",
                    "country_code": "countryCode",
                    "data_mode": "dataMode",
                    "lat": 0,
                    "lon": 0,
                    "source": "source",
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
        assert equipment is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.equipment.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert equipment is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.equipment.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        equipment = client.equipment.tuple(
            columns="columns",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )
        assert equipment is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
            id="id",
            air_def_area="airDefArea",
            allegiance="allegiance",
            alt_allegiance="altAllegiance",
            alt_country_code="altCountryCode",
            alt_eqp_id="altEqpId",
            class_rating="classRating",
            condition="condition",
            condition_avail="conditionAvail",
            coord="coord",
            coord_datum="coordDatum",
            coord_deriv_acc=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_msl=0,
            elev_msl_conf_lvl=0,
            elev_msl_deriv_acc=0,
            eqp_code="eqpCode",
            eqp_id_num="eqpIdNum",
            eval=0,
            fpa="fpa",
            function="function",
            funct_primary="functPrimary",
            geoidal_msl_sep=0,
            ident="ident",
            id_operating_unit="idOperatingUnit",
            id_parent_equipment="idParentEquipment",
            id_site="idSite",
            loc_reason="locReason",
            mil_grid="milGrid",
            mil_grid_sys="milGridSys",
            nomen="nomen",
            oper_area_primary="operAreaPrimary",
            oper_status="operStatus",
            origin="origin",
            pol_subdiv="polSubdiv",
            qty_oh=0,
            rec_status="recStatus",
            reference_doc="referenceDoc",
            res_prod="resProd",
            review_date=parse_date("2019-12-27"),
            seq_num=0,
            src_ids=["string"],
            src_typs=["string"],
            sym_code="symCode",
            utm="utm",
            wac="wac",
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.create(
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.retrieve(
            "id",
        )
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(EquipmentFull, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )
        assert equipment is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
            id_2="id",
            air_def_area="airDefArea",
            allegiance="allegiance",
            alt_allegiance="altAllegiance",
            alt_country_code="altCountryCode",
            alt_eqp_id="altEqpId",
            class_rating="classRating",
            condition="condition",
            condition_avail="conditionAvail",
            coord="coord",
            coord_datum="coordDatum",
            coord_deriv_acc=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            elev_msl=0,
            elev_msl_conf_lvl=0,
            elev_msl_deriv_acc=0,
            eqp_code="eqpCode",
            eqp_id_num="eqpIdNum",
            eval=0,
            fpa="fpa",
            function="function",
            funct_primary="functPrimary",
            geoidal_msl_sep=0,
            ident="ident",
            id_operating_unit="idOperatingUnit",
            id_parent_equipment="idParentEquipment",
            id_site="idSite",
            loc_reason="locReason",
            mil_grid="milGrid",
            mil_grid_sys="milGridSys",
            nomen="nomen",
            oper_area_primary="operAreaPrimary",
            oper_status="operStatus",
            origin="origin",
            pol_subdiv="polSubdiv",
            qty_oh=0,
            rec_status="recStatus",
            reference_doc="referenceDoc",
            res_prod="resProd",
            review_date=parse_date("2019-12-27"),
            seq_num=0,
            src_ids=["string"],
            src_typs=["string"],
            sym_code="symCode",
            utm="utm",
            wac="wac",
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            country_code="countryCode",
            data_mode="dataMode",
            lat=0,
            lon=0,
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.equipment.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                country_code="countryCode",
                data_mode="dataMode",
                lat=0,
                lon=0,
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.list()
        assert_matches_type(EquipmentListResponse, equipment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(EquipmentListResponse, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(EquipmentListResponse, equipment, path=["response"])

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
                    "classification_marking": "classificationMarking",
                    "country_code": "countryCode",
                    "data_mode": "dataMode",
                    "lat": 0,
                    "lon": 0,
                    "source": "source",
                }
            ],
        )
        assert equipment is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "country_code": "countryCode",
                    "data_mode": "dataMode",
                    "lat": 0,
                    "lon": 0,
                    "source": "source",
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
                    "classification_marking": "classificationMarking",
                    "country_code": "countryCode",
                    "data_mode": "dataMode",
                    "lat": 0,
                    "lon": 0,
                    "source": "source",
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
        assert equipment is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert equipment is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert equipment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment = await async_client.equipment.tuple(
            columns="columns",
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
