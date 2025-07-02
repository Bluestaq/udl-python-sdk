# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeraDataCommDetailGetResponse,
    SeraDataCommDetailListResponse,
    SeraDataCommDetailTupleResponse,
    SeraDataCommDetailQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeraDataCommDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert sera_data_comm_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="SERADATACOMMDETAILS-ID",
            band="X",
            bandwidth=1.23,
            eirp=1.23,
            est_hts_total_capacity=1.23,
            est_hts_total_user_downlink_bandwidth_per_beam=1.23,
            est_hts_total_user_uplink_bandwidth_per_beam=1.23,
            gateway_downlink_from=1.23,
            gateway_downlink_to=1.23,
            gateway_uplink_from=1.23,
            gateway_uplink_to=1.23,
            hosted_for_company_org_id="hostedForCompanyOrgId",
            hts_num_user_spot_beams=1,
            hts_user_downlink_bandwidth_per_beam=1.23,
            hts_user_uplink_bandwidth_per_beam=1.23,
            id_comm="idComm",
            manufacturer_org_id="manufacturerOrgId",
            num36_mhz_equivalent_transponders=1,
            num_operational_transponders=1,
            num_spare_transponders=1,
            origin="THIRD_PARTY_DATASOURCE",
            payload_notes="Sample Notes",
            polarization="polarization",
            solid_state_power_amp=1.23,
            spacecraft_id="spacecraftId",
            trade_lease_org_id="tradeLeaseOrgId",
            traveling_wave_tube_amplifier=1.23,
            user_downlink_from=1.23,
            user_downlink_to=1.23,
            user_uplink_from=1.23,
            user_uplink_to=1.23,
        )
        assert sera_data_comm_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert sera_data_comm_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert sera_data_comm_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert sera_data_comm_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="SERADATACOMMDETAILS-ID",
            band="X",
            bandwidth=1.23,
            eirp=1.23,
            est_hts_total_capacity=1.23,
            est_hts_total_user_downlink_bandwidth_per_beam=1.23,
            est_hts_total_user_uplink_bandwidth_per_beam=1.23,
            gateway_downlink_from=1.23,
            gateway_downlink_to=1.23,
            gateway_uplink_from=1.23,
            gateway_uplink_to=1.23,
            hosted_for_company_org_id="hostedForCompanyOrgId",
            hts_num_user_spot_beams=1,
            hts_user_downlink_bandwidth_per_beam=1.23,
            hts_user_uplink_bandwidth_per_beam=1.23,
            id_comm="idComm",
            manufacturer_org_id="manufacturerOrgId",
            num36_mhz_equivalent_transponders=1,
            num_operational_transponders=1,
            num_spare_transponders=1,
            origin="THIRD_PARTY_DATASOURCE",
            payload_notes="Sample Notes",
            polarization="polarization",
            solid_state_power_amp=1.23,
            spacecraft_id="spacecraftId",
            trade_lease_org_id="tradeLeaseOrgId",
            traveling_wave_tube_amplifier=1.23,
            user_downlink_from=1.23,
            user_downlink_to=1.23,
            user_uplink_from=1.23,
            user_uplink_to=1.23,
        )
        assert sera_data_comm_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert sera_data_comm_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert sera_data_comm_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sera_data_comm_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.list()
        assert_matches_type(SyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert_matches_type(SyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert_matches_type(
                SyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.delete(
            "id",
        )
        assert sera_data_comm_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert sera_data_comm_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert sera_data_comm_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sera_data_comm_details.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.count()
        assert_matches_type(str, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert_matches_type(str, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert_matches_type(str, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.get(
            id="id",
        )
        assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sera_data_comm_details.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.queryhelp()
        assert_matches_type(SeraDataCommDetailQueryhelpResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert_matches_type(SeraDataCommDetailQueryhelpResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert_matches_type(SeraDataCommDetailQueryhelpResponse, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.tuple(
            columns="columns",
        )
        assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_comm_detail = client.sera_data_comm_details.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_comm_details.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = response.parse()
        assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_comm_details.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = response.parse()
            assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeraDataCommDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert sera_data_comm_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="SERADATACOMMDETAILS-ID",
            band="X",
            bandwidth=1.23,
            eirp=1.23,
            est_hts_total_capacity=1.23,
            est_hts_total_user_downlink_bandwidth_per_beam=1.23,
            est_hts_total_user_uplink_bandwidth_per_beam=1.23,
            gateway_downlink_from=1.23,
            gateway_downlink_to=1.23,
            gateway_uplink_from=1.23,
            gateway_uplink_to=1.23,
            hosted_for_company_org_id="hostedForCompanyOrgId",
            hts_num_user_spot_beams=1,
            hts_user_downlink_bandwidth_per_beam=1.23,
            hts_user_uplink_bandwidth_per_beam=1.23,
            id_comm="idComm",
            manufacturer_org_id="manufacturerOrgId",
            num36_mhz_equivalent_transponders=1,
            num_operational_transponders=1,
            num_spare_transponders=1,
            origin="THIRD_PARTY_DATASOURCE",
            payload_notes="Sample Notes",
            polarization="polarization",
            solid_state_power_amp=1.23,
            spacecraft_id="spacecraftId",
            trade_lease_org_id="tradeLeaseOrgId",
            traveling_wave_tube_amplifier=1.23,
            user_downlink_from=1.23,
            user_downlink_to=1.23,
            user_uplink_from=1.23,
            user_uplink_to=1.23,
        )
        assert sera_data_comm_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert sera_data_comm_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert sera_data_comm_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert sera_data_comm_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="SERADATACOMMDETAILS-ID",
            band="X",
            bandwidth=1.23,
            eirp=1.23,
            est_hts_total_capacity=1.23,
            est_hts_total_user_downlink_bandwidth_per_beam=1.23,
            est_hts_total_user_uplink_bandwidth_per_beam=1.23,
            gateway_downlink_from=1.23,
            gateway_downlink_to=1.23,
            gateway_uplink_from=1.23,
            gateway_uplink_to=1.23,
            hosted_for_company_org_id="hostedForCompanyOrgId",
            hts_num_user_spot_beams=1,
            hts_user_downlink_bandwidth_per_beam=1.23,
            hts_user_uplink_bandwidth_per_beam=1.23,
            id_comm="idComm",
            manufacturer_org_id="manufacturerOrgId",
            num36_mhz_equivalent_transponders=1,
            num_operational_transponders=1,
            num_spare_transponders=1,
            origin="THIRD_PARTY_DATASOURCE",
            payload_notes="Sample Notes",
            polarization="polarization",
            solid_state_power_amp=1.23,
            spacecraft_id="spacecraftId",
            trade_lease_org_id="tradeLeaseOrgId",
            traveling_wave_tube_amplifier=1.23,
            user_downlink_from=1.23,
            user_downlink_to=1.23,
            user_uplink_from=1.23,
            user_uplink_to=1.23,
        )
        assert sera_data_comm_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert sera_data_comm_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert sera_data_comm_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sera_data_comm_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.list()
        assert_matches_type(AsyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[SeraDataCommDetailListResponse], sera_data_comm_detail, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.delete(
            "id",
        )
        assert sera_data_comm_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert sera_data_comm_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert sera_data_comm_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sera_data_comm_details.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.count()
        assert_matches_type(str, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert_matches_type(str, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert_matches_type(str, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.get(
            id="id",
        )
        assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert_matches_type(SeraDataCommDetailGetResponse, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sera_data_comm_details.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.queryhelp()
        assert_matches_type(SeraDataCommDetailQueryhelpResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert_matches_type(SeraDataCommDetailQueryhelpResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert_matches_type(SeraDataCommDetailQueryhelpResponse, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.tuple(
            columns="columns",
        )
        assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_comm_detail = await async_client.sera_data_comm_details.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_comm_details.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_comm_detail = await response.parse()
        assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_comm_details.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_comm_detail = await response.parse()
            assert_matches_type(SeraDataCommDetailTupleResponse, sera_data_comm_detail, path=["response"])

        assert cast(Any, response.is_closed) is True
