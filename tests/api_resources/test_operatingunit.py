# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OperatingunitGetResponse,
    OperatingunitListResponse,
    OperatingunitTupleResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperatingunit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )
        assert operatingunit is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_operating_unit_id="32100000000021",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            country_code="IQ",
            deploy_status="ND",
            description="Description of unit",
            div_cat="5",
            echelon="SHIP",
            echelon_tier="68",
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eval=7,
            flag_flown="IZ",
            fleet_id="A",
            force="NV",
            force_name="FORCE-NAME",
            fpa="EOB",
            funct_role="MIL",
            geoidal_msl_sep=12.34,
            id_contact="CONTACT-ID",
            ident="FRIEND",
            id_location="LOCATION-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            id_organization="ORGANIZATION-ID",
            lat=45.23,
            loc_name="LOCATION_NAME",
            loc_reason="GR",
            lon=179.1,
            master_unit=True,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="W6",
            msn_primary_specialty="QK",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            stylized_unit=True,
            sym_code="SOGPU----------",
            unit_identifier="AZXAZ12345",
            utm="19P4390691376966",
            wac="0427",
        )
        assert operatingunit is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert operatingunit is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )
        assert operatingunit is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_operating_unit_id="32100000000021",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            country_code="IQ",
            deploy_status="ND",
            description="Description of unit",
            div_cat="5",
            echelon="SHIP",
            echelon_tier="68",
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eval=7,
            flag_flown="IZ",
            fleet_id="A",
            force="NV",
            force_name="FORCE-NAME",
            fpa="EOB",
            funct_role="MIL",
            geoidal_msl_sep=12.34,
            id_contact="CONTACT-ID",
            ident="FRIEND",
            id_location="LOCATION-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            id_organization="ORGANIZATION-ID",
            lat=45.23,
            loc_name="LOCATION_NAME",
            loc_reason="GR",
            lon=179.1,
            master_unit=True,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="W6",
            msn_primary_specialty="QK",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            stylized_unit=True,
            sym_code="SOGPU----------",
            unit_identifier="AZXAZ12345",
            utm="19P4390691376966",
            wac="0427",
        )
        assert operatingunit is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert operatingunit is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.operatingunit.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                name="SOME_NAME",
                source="some.user",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.list()
        assert_matches_type(SyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert_matches_type(SyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert_matches_type(SyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.delete(
            "id",
        )
        assert operatingunit is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert operatingunit is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.operatingunit.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.count()
        assert_matches_type(str, operatingunit, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, operatingunit, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert_matches_type(str, operatingunit, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert_matches_type(str, operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.get(
            id="id",
        )
        assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.operatingunit.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.queryhelp()
        assert operatingunit is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert operatingunit is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.tuple(
            columns="columns",
        )
        assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        operatingunit = client.operatingunit.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.operatingunit.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = response.parse()
        assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.operatingunit.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = response.parse()
            assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOperatingunit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )
        assert operatingunit is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_operating_unit_id="32100000000021",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            country_code="IQ",
            deploy_status="ND",
            description="Description of unit",
            div_cat="5",
            echelon="SHIP",
            echelon_tier="68",
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eval=7,
            flag_flown="IZ",
            fleet_id="A",
            force="NV",
            force_name="FORCE-NAME",
            fpa="EOB",
            funct_role="MIL",
            geoidal_msl_sep=12.34,
            id_contact="CONTACT-ID",
            ident="FRIEND",
            id_location="LOCATION-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            id_organization="ORGANIZATION-ID",
            lat=45.23,
            loc_name="LOCATION_NAME",
            loc_reason="GR",
            lon=179.1,
            master_unit=True,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="W6",
            msn_primary_specialty="QK",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            stylized_unit=True,
            sym_code="SOGPU----------",
            unit_identifier="AZXAZ12345",
            utm="19P4390691376966",
            wac="0427",
        )
        assert operatingunit is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert operatingunit is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )
        assert operatingunit is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
            air_def_area="AL006",
            allegiance="OTHR",
            alt_allegiance="HL",
            alt_country_code="IZ",
            alt_operating_unit_id="32100000000021",
            class_rating="1",
            condition="RDY",
            condition_avail="A",
            coord="340000000N0430000000E",
            coord_datum="WGS",
            coord_deriv_acc=12.345,
            country_code="IQ",
            deploy_status="ND",
            description="Description of unit",
            div_cat="5",
            echelon="SHIP",
            echelon_tier="68",
            elev_msl=123.45,
            elev_msl_conf_lvl=50,
            elev_msl_deriv_acc=12.34,
            eval=7,
            flag_flown="IZ",
            fleet_id="A",
            force="NV",
            force_name="FORCE-NAME",
            fpa="EOB",
            funct_role="MIL",
            geoidal_msl_sep=12.34,
            id_contact="CONTACT-ID",
            ident="FRIEND",
            id_location="LOCATION-ID",
            id_operating_unit="OPERATINGUNIT-ID",
            id_organization="ORGANIZATION-ID",
            lat=45.23,
            loc_name="LOCATION_NAME",
            loc_reason="GR",
            lon=179.1,
            master_unit=True,
            mil_grid="4QFJ12345678",
            mil_grid_sys="UTM",
            msn_primary="W6",
            msn_primary_specialty="QK",
            oper_status="OPR",
            origin="THIRD_PARTY_DATASOURCE",
            pol_subdiv="IZ07",
            rec_status="A",
            reference_doc="Provider Reference Documentation",
            res_prod="RT",
            review_date=parse_date("2008-06-10"),
            stylized_unit=True,
            sym_code="SOGPU----------",
            unit_identifier="AZXAZ12345",
            utm="19P4390691376966",
            wac="0427",
        )
        assert operatingunit is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert operatingunit is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            name="SOME_NAME",
            source="some.user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.operatingunit.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                name="SOME_NAME",
                source="some.user",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.list()
        assert_matches_type(AsyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert_matches_type(AsyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert_matches_type(AsyncOffsetPage[OperatingunitListResponse], operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.delete(
            "id",
        )
        assert operatingunit is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert operatingunit is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.operatingunit.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.count()
        assert_matches_type(str, operatingunit, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, operatingunit, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert_matches_type(str, operatingunit, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert_matches_type(str, operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.get(
            id="id",
        )
        assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert_matches_type(OperatingunitGetResponse, operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.operatingunit.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.queryhelp()
        assert operatingunit is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert operatingunit is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert operatingunit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.tuple(
            columns="columns",
        )
        assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operatingunit = await async_client.operatingunit.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.operatingunit.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operatingunit = await response.parse()
        assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.operatingunit.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operatingunit = await response.parse()
            assert_matches_type(OperatingunitTupleResponse, operatingunit, path=["response"])

        assert cast(Any, response.is_closed) is True
