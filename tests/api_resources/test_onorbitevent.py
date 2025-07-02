# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbiteventGetResponse,
    OnorbiteventListResponse,
    OnorbiteventTupleResponse,
    OnorbiteventQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbitevent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert onorbitevent is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="ONORBITEVENT-ID",
            achieved_flight_phase="Phase 2",
            age_at_event=5.23,
            capability_loss=0.5,
            capability_loss_notes="Example notes",
            capacity_loss=0.5,
            consequential_equipment_failure="Example Equipment",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="DECLASS_STRING",
            derived_from="DERIVED_SOURCE",
            description="Example notes",
            equipment_at_fault="Example Equipment",
            equipment_causing_loss_notes="Example notes",
            equipment_part_at_fault="Example Equipment",
            equipment_type_at_fault="Example Equipment",
            event_result="Example results",
            event_time_notes="Notes on validity",
            event_type="Type1",
            geo_position=45.23,
            id_on_orbit="ONORBIT-ID",
            inclined=False,
            injured=1,
            insurance_carried_notes="Insurance notes",
            insurance_loss=0.5,
            insurance_loss_notes="Insurance notes",
            killed=23,
            lessee_org_id="LESSEEORG-ID",
            life_lost=0.5,
            net_amount=10000.23,
            object_status="Status1",
            occurrence_flight_phase="Phase 2",
            official_loss_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            operated_on_behalf_of_org_id="OPERATEDONBEHALFOFORG-ID",
            operator_org_id="OPERATORORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            owner_org_id="OWNERORG-ID",
            plane_number="PL_1",
            plane_slot="example_slot",
            position_status="Stable",
            remarks="Example remarks",
            satellite_position="Example description",
            sat_no=1,
            stage_at_fault="Phase 2",
            third_party_insurance_loss=10000.23,
            underlying_cause="CAUSE_EXAMPLE",
            until_time=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert onorbitevent is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert onorbitevent is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert onorbitevent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert onorbitevent is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="ONORBITEVENT-ID",
            achieved_flight_phase="Phase 2",
            age_at_event=5.23,
            capability_loss=0.5,
            capability_loss_notes="Example notes",
            capacity_loss=0.5,
            consequential_equipment_failure="Example Equipment",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="DECLASS_STRING",
            derived_from="DERIVED_SOURCE",
            description="Example notes",
            equipment_at_fault="Example Equipment",
            equipment_causing_loss_notes="Example notes",
            equipment_part_at_fault="Example Equipment",
            equipment_type_at_fault="Example Equipment",
            event_result="Example results",
            event_time_notes="Notes on validity",
            event_type="Type1",
            geo_position=45.23,
            id_on_orbit="ONORBIT-ID",
            inclined=False,
            injured=1,
            insurance_carried_notes="Insurance notes",
            insurance_loss=0.5,
            insurance_loss_notes="Insurance notes",
            killed=23,
            lessee_org_id="LESSEEORG-ID",
            life_lost=0.5,
            net_amount=10000.23,
            object_status="Status1",
            occurrence_flight_phase="Phase 2",
            official_loss_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            operated_on_behalf_of_org_id="OPERATEDONBEHALFOFORG-ID",
            operator_org_id="OPERATORORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            owner_org_id="OWNERORG-ID",
            plane_number="PL_1",
            plane_slot="example_slot",
            position_status="Stable",
            remarks="Example remarks",
            satellite_position="Example description",
            sat_no=1,
            stage_at_fault="Phase 2",
            third_party_insurance_loss=10000.23,
            underlying_cause="CAUSE_EXAMPLE",
            until_time=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert onorbitevent is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert onorbitevent is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert onorbitevent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.onorbitevent.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.list()
        assert_matches_type(SyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert_matches_type(SyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.delete(
            "id",
        )
        assert onorbitevent is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert onorbitevent is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert onorbitevent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitevent.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.count()
        assert_matches_type(str, onorbitevent, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbitevent, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert_matches_type(str, onorbitevent, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert_matches_type(str, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.get(
            id="id",
        )
        assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitevent.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.queryhelp()
        assert_matches_type(OnorbiteventQueryhelpResponse, onorbitevent, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert_matches_type(OnorbiteventQueryhelpResponse, onorbitevent, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert_matches_type(OnorbiteventQueryhelpResponse, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitevent = client.onorbitevent.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitevent.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = response.parse()
        assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.onorbitevent.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = response.parse()
            assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnorbitevent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert onorbitevent is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="ONORBITEVENT-ID",
            achieved_flight_phase="Phase 2",
            age_at_event=5.23,
            capability_loss=0.5,
            capability_loss_notes="Example notes",
            capacity_loss=0.5,
            consequential_equipment_failure="Example Equipment",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="DECLASS_STRING",
            derived_from="DERIVED_SOURCE",
            description="Example notes",
            equipment_at_fault="Example Equipment",
            equipment_causing_loss_notes="Example notes",
            equipment_part_at_fault="Example Equipment",
            equipment_type_at_fault="Example Equipment",
            event_result="Example results",
            event_time_notes="Notes on validity",
            event_type="Type1",
            geo_position=45.23,
            id_on_orbit="ONORBIT-ID",
            inclined=False,
            injured=1,
            insurance_carried_notes="Insurance notes",
            insurance_loss=0.5,
            insurance_loss_notes="Insurance notes",
            killed=23,
            lessee_org_id="LESSEEORG-ID",
            life_lost=0.5,
            net_amount=10000.23,
            object_status="Status1",
            occurrence_flight_phase="Phase 2",
            official_loss_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            operated_on_behalf_of_org_id="OPERATEDONBEHALFOFORG-ID",
            operator_org_id="OPERATORORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            owner_org_id="OWNERORG-ID",
            plane_number="PL_1",
            plane_slot="example_slot",
            position_status="Stable",
            remarks="Example remarks",
            satellite_position="Example description",
            sat_no=1,
            stage_at_fault="Phase 2",
            third_party_insurance_loss=10000.23,
            underlying_cause="CAUSE_EXAMPLE",
            until_time=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert onorbitevent is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert onorbitevent is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert onorbitevent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert onorbitevent is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="ONORBITEVENT-ID",
            achieved_flight_phase="Phase 2",
            age_at_event=5.23,
            capability_loss=0.5,
            capability_loss_notes="Example notes",
            capacity_loss=0.5,
            consequential_equipment_failure="Example Equipment",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="DECLASS_STRING",
            derived_from="DERIVED_SOURCE",
            description="Example notes",
            equipment_at_fault="Example Equipment",
            equipment_causing_loss_notes="Example notes",
            equipment_part_at_fault="Example Equipment",
            equipment_type_at_fault="Example Equipment",
            event_result="Example results",
            event_time_notes="Notes on validity",
            event_type="Type1",
            geo_position=45.23,
            id_on_orbit="ONORBIT-ID",
            inclined=False,
            injured=1,
            insurance_carried_notes="Insurance notes",
            insurance_loss=0.5,
            insurance_loss_notes="Insurance notes",
            killed=23,
            lessee_org_id="LESSEEORG-ID",
            life_lost=0.5,
            net_amount=10000.23,
            object_status="Status1",
            occurrence_flight_phase="Phase 2",
            official_loss_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            operated_on_behalf_of_org_id="OPERATEDONBEHALFOFORG-ID",
            operator_org_id="OPERATORORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            owner_org_id="OWNERORG-ID",
            plane_number="PL_1",
            plane_slot="example_slot",
            position_status="Stable",
            remarks="Example remarks",
            satellite_position="Example description",
            sat_no=1,
            stage_at_fault="Phase 2",
            third_party_insurance_loss=10000.23,
            underlying_cause="CAUSE_EXAMPLE",
            until_time=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert onorbitevent is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert onorbitevent is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert onorbitevent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.onorbitevent.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                event_time=parse_datetime("2018-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.list()
        assert_matches_type(AsyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert_matches_type(AsyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert_matches_type(AsyncOffsetPage[OnorbiteventListResponse], onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.delete(
            "id",
        )
        assert onorbitevent is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert onorbitevent is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert onorbitevent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitevent.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.count()
        assert_matches_type(str, onorbitevent, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbitevent, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert_matches_type(str, onorbitevent, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert_matches_type(str, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.get(
            id="id",
        )
        assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert_matches_type(OnorbiteventGetResponse, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitevent.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.queryhelp()
        assert_matches_type(OnorbiteventQueryhelpResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert_matches_type(OnorbiteventQueryhelpResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert_matches_type(OnorbiteventQueryhelpResponse, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitevent = await async_client.onorbitevent.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitevent.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitevent = await response.parse()
        assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitevent.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitevent = await response.parse()
            assert_matches_type(OnorbiteventTupleResponse, onorbitevent, path=["response"])

        assert cast(Any, response.is_closed) is True
