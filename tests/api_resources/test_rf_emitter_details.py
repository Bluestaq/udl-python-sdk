# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    RfEmitterDetailGetResponse,
    RfEmitterDetailListResponse,
    RfEmitterDetailTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRfEmitterDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert rf_emitter_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            id="RFEMITTERDETAILS-ID",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            antenna_diameter=20.23,
            antenna_size=[1.1, 2.2],
            barrage_noise_bandwidth=5.23,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            manufacturer_org_id="MANUFACTURERORG-ID",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            production_facility_location_id="PRODUCTIONFACILITYLOCATION-ID",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_bandwidth=15.23,
            receiver_sensitivity=10.23,
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.23,
            transmit_power=100.23,
            transmitter_bandwidth=0.125,
            transmitter_frequency=105.9,
            urls=["TAG1", "TAG2"],
        )
        assert rf_emitter_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert rf_emitter_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert rf_emitter_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            body_id="RFEMITTERDETAILS-ID",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            antenna_diameter=20.23,
            antenna_size=[1.1, 2.2],
            barrage_noise_bandwidth=5.23,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            manufacturer_org_id="MANUFACTURERORG-ID",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            production_facility_location_id="PRODUCTIONFACILITYLOCATION-ID",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_bandwidth=15.23,
            receiver_sensitivity=10.23,
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.23,
            transmit_power=100.23,
            transmitter_bandwidth=0.125,
            transmitter_frequency=105.9,
            urls=["TAG1", "TAG2"],
        )
        assert rf_emitter_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert rf_emitter_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.rf_emitter_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_rf_emitter="RFEMITTER-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.list()
        assert_matches_type(SyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert_matches_type(SyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert_matches_type(SyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.delete(
            "id",
        )
        assert rf_emitter_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert rf_emitter_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rf_emitter_details.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.count()
        assert_matches_type(str, rf_emitter_detail, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, rf_emitter_detail, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert_matches_type(str, rf_emitter_detail, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert_matches_type(str, rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.get(
            id="id",
        )
        assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rf_emitter_details.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.queryhelp()
        assert rf_emitter_detail is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert rf_emitter_detail is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.tuple(
            columns="columns",
        )
        assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        rf_emitter_detail = client.rf_emitter_details.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.rf_emitter_details.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = response.parse()
        assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.rf_emitter_details.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = response.parse()
            assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRfEmitterDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert rf_emitter_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            id="RFEMITTERDETAILS-ID",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            antenna_diameter=20.23,
            antenna_size=[1.1, 2.2],
            barrage_noise_bandwidth=5.23,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            manufacturer_org_id="MANUFACTURERORG-ID",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            production_facility_location_id="PRODUCTIONFACILITYLOCATION-ID",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_bandwidth=15.23,
            receiver_sensitivity=10.23,
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.23,
            transmit_power=100.23,
            transmitter_bandwidth=0.125,
            transmitter_frequency=105.9,
            urls=["TAG1", "TAG2"],
        )
        assert rf_emitter_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert rf_emitter_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )
        assert rf_emitter_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
            body_id="RFEMITTERDETAILS-ID",
            alternate_facility_name="ALTERNATE_FACILITY_NAME",
            alt_name="ALTERNATE_NAME",
            antenna_diameter=20.23,
            antenna_size=[1.1, 2.2],
            barrage_noise_bandwidth=5.23,
            description="DESCRIPTION",
            designator="DESIGNATOR",
            doppler_noise=10.23,
            drfm_instantaneous_bandwidth=20.23,
            family="FAMILY",
            manufacturer_org_id="MANUFACTURERORG-ID",
            notes="NOTES",
            num_bits=256,
            num_channels=10,
            origin="THIRD_PARTY_DATASOURCE",
            production_facility_location_id="PRODUCTIONFACILITYLOCATION-ID",
            production_facility_name="PRODUCTION_FACILITY",
            receiver_bandwidth=15.23,
            receiver_sensitivity=10.23,
            receiver_type="RECEIVER_TYPE",
            secondary_notes="MORE_NOTES",
            system_sensitivity_end=150.23,
            system_sensitivity_start=50.23,
            transmit_power=100.23,
            transmitter_bandwidth=0.125,
            transmitter_frequency=105.9,
            urls=["TAG1", "TAG2"],
        )
        assert rf_emitter_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert rf_emitter_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_rf_emitter="RFEMITTER-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.rf_emitter_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_rf_emitter="RFEMITTER-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.list()
        assert_matches_type(AsyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert_matches_type(AsyncOffsetPage[RfEmitterDetailListResponse], rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.delete(
            "id",
        )
        assert rf_emitter_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert rf_emitter_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rf_emitter_details.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.count()
        assert_matches_type(str, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert_matches_type(str, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert_matches_type(str, rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.get(
            id="id",
        )
        assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert_matches_type(RfEmitterDetailGetResponse, rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rf_emitter_details.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.queryhelp()
        assert rf_emitter_detail is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert rf_emitter_detail is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert rf_emitter_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.tuple(
            columns="columns",
        )
        assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_emitter_detail = await async_client.rf_emitter_details.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rf_emitter_details.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_emitter_detail = await response.parse()
        assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rf_emitter_details.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_emitter_detail = await response.parse()
            assert_matches_type(RfEmitterDetailTupleResponse, rf_emitter_detail, path=["response"])

        assert cast(Any, response.is_closed) is True
