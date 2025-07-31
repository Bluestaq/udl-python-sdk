# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    CrewAbridged,
    CrewTupleResponse,
    CrewQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import CrewFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrew:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            id="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            alert_type="ALPHA",
            arms_crew_unit="00016ALSQ",
            assigned_qual_code=["AL", "CS"],
            commander_id="763a1c1e8d2f3c16af825a11e3f1f579",
            commander_last4_ssn="1234",
            commander_name="John Doe",
            crew_home=False,
            crew_members=[
                {
                    "alerted": True,
                    "all_sortie": True,
                    "approved": True,
                    "attached": True,
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "duty_status": "AGR",
                    "emailed": True,
                    "extra_time": True,
                    "first_name": "Freddie",
                    "flt_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_currency_exp_id": "SS05AM",
                    "flt_rec_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_rec_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "fly_squadron": "141ARS",
                    "funded": True,
                    "gender": "F",
                    "gnd_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gnd_currency_exp_id": "AH03YM",
                    "grounded": True,
                    "guest_start": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "guest_stop": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last4_ssn": "1234",
                    "last_flt_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last_name": "Smith",
                    "loaned_to": "Thunderbirds",
                    "lodging": "Peterson SFB",
                    "member_actual_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_adj_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_adj_return_time_approver": "Smith",
                    "member_id": "12345678abc",
                    "member_init_start_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_last_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_legal_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_pickup_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "member_post_rest_offset": "+05:00",
                    "member_post_rest_time": parse_datetime("2024-01-02T16:00:00.123Z"),
                    "member_pre_rest_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_remarks": "Crew member remark",
                    "member_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_sched_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_source": "ACTIVE",
                    "member_stage_name": "Falcon Squadron",
                    "member_transport_req": True,
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "notified": True,
                    "phone_number": "+14155552671",
                    "phys_av_code": "D",
                    "phys_av_status": "OVERDUE",
                    "phys_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "rank": "Capt",
                    "remark_code": "ABE33",
                    "rms_mds": "C017A",
                    "show_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "squadron": "21AS",
                    "training_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_rms="ARMS",
            crew_role="DEADHEAD",
            crew_source="ACTIVE",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_unit="00016ALSQ",
            crew_wing="60AMW",
            current_icao="KCOS",
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            flt_auth_num="KT001",
            id_site_current="b677cf3b-d44d-450e-8b8f-d23f997f8778",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_alert_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            personnel_type="AIRCREW",
            pickup_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            post_rest_applied=False,
            post_rest_end=parse_datetime("2024-01-02T16:00:00.123Z"),
            post_rest_offset="+05:00",
            pre_rest_applied=False,
            pre_rest_start=parse_datetime("2024-01-01T16:00:00.123Z"),
            req_qual_code=["AL", "CS"],
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage1_qual="1AXXX",
            stage2_qual="2AXXX",
            stage3_qual="3AXXX",
            stage_name="Falcon Squadron",
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
            transport_req=True,
            trip_kit="TK-1234",
        )
        assert crew is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert crew is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.retrieve(
            id="id",
        )
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert_matches_type(CrewFull, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crew.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            body_id="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            alert_type="ALPHA",
            arms_crew_unit="00016ALSQ",
            assigned_qual_code=["AL", "CS"],
            commander_id="763a1c1e8d2f3c16af825a11e3f1f579",
            commander_last4_ssn="1234",
            commander_name="John Doe",
            crew_home=False,
            crew_members=[
                {
                    "alerted": True,
                    "all_sortie": True,
                    "approved": True,
                    "attached": True,
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "duty_status": "AGR",
                    "emailed": True,
                    "extra_time": True,
                    "first_name": "Freddie",
                    "flt_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_currency_exp_id": "SS05AM",
                    "flt_rec_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_rec_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "fly_squadron": "141ARS",
                    "funded": True,
                    "gender": "F",
                    "gnd_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gnd_currency_exp_id": "AH03YM",
                    "grounded": True,
                    "guest_start": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "guest_stop": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last4_ssn": "1234",
                    "last_flt_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last_name": "Smith",
                    "loaned_to": "Thunderbirds",
                    "lodging": "Peterson SFB",
                    "member_actual_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_adj_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_adj_return_time_approver": "Smith",
                    "member_id": "12345678abc",
                    "member_init_start_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_last_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_legal_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_pickup_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "member_post_rest_offset": "+05:00",
                    "member_post_rest_time": parse_datetime("2024-01-02T16:00:00.123Z"),
                    "member_pre_rest_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_remarks": "Crew member remark",
                    "member_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_sched_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_source": "ACTIVE",
                    "member_stage_name": "Falcon Squadron",
                    "member_transport_req": True,
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "notified": True,
                    "phone_number": "+14155552671",
                    "phys_av_code": "D",
                    "phys_av_status": "OVERDUE",
                    "phys_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "rank": "Capt",
                    "remark_code": "ABE33",
                    "rms_mds": "C017A",
                    "show_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "squadron": "21AS",
                    "training_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_rms="ARMS",
            crew_role="DEADHEAD",
            crew_source="ACTIVE",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_unit="00016ALSQ",
            crew_wing="60AMW",
            current_icao="KCOS",
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            flt_auth_num="KT001",
            id_site_current="b677cf3b-d44d-450e-8b8f-d23f997f8778",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_alert_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            personnel_type="AIRCREW",
            pickup_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            post_rest_applied=False,
            post_rest_end=parse_datetime("2024-01-02T16:00:00.123Z"),
            post_rest_offset="+05:00",
            pre_rest_applied=False,
            pre_rest_start=parse_datetime("2024-01-01T16:00:00.123Z"),
            req_qual_code=["AL", "CS"],
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage1_qual="1AXXX",
            stage2_qual="2AXXX",
            stage3_qual="3AXXX",
            stage_name="Falcon Squadron",
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
            transport_req=True,
            trip_kit="TK-1234",
        )
        assert crew is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert crew is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.crew.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                orig_crew_id="JHJDHjhuu929o92",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.list()
        assert_matches_type(SyncOffsetPage[CrewAbridged], crew, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[CrewAbridged], crew, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(SyncOffsetPage[CrewAbridged], crew, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert_matches_type(SyncOffsetPage[CrewAbridged], crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.count()
        assert_matches_type(str, crew, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, crew, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(str, crew, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert_matches_type(str, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.queryhelp()
        assert_matches_type(CrewQueryhelpResponse, crew, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(CrewQueryhelpResponse, crew, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert_matches_type(CrewQueryhelpResponse, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.tuple(
            columns="columns",
        )
        assert_matches_type(CrewTupleResponse, crew, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CrewTupleResponse, crew, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(CrewTupleResponse, crew, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert_matches_type(CrewTupleResponse, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "orig_crew_id": "JHJDHjhuu929o92",
                    "source": "Bluestaq",
                }
            ],
        )
        assert crew is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "orig_crew_id": "JHJDHjhuu929o92",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert crew is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "orig_crew_id": "JHJDHjhuu929o92",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCrew:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            id="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            alert_type="ALPHA",
            arms_crew_unit="00016ALSQ",
            assigned_qual_code=["AL", "CS"],
            commander_id="763a1c1e8d2f3c16af825a11e3f1f579",
            commander_last4_ssn="1234",
            commander_name="John Doe",
            crew_home=False,
            crew_members=[
                {
                    "alerted": True,
                    "all_sortie": True,
                    "approved": True,
                    "attached": True,
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "duty_status": "AGR",
                    "emailed": True,
                    "extra_time": True,
                    "first_name": "Freddie",
                    "flt_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_currency_exp_id": "SS05AM",
                    "flt_rec_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_rec_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "fly_squadron": "141ARS",
                    "funded": True,
                    "gender": "F",
                    "gnd_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gnd_currency_exp_id": "AH03YM",
                    "grounded": True,
                    "guest_start": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "guest_stop": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last4_ssn": "1234",
                    "last_flt_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last_name": "Smith",
                    "loaned_to": "Thunderbirds",
                    "lodging": "Peterson SFB",
                    "member_actual_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_adj_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_adj_return_time_approver": "Smith",
                    "member_id": "12345678abc",
                    "member_init_start_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_last_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_legal_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_pickup_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "member_post_rest_offset": "+05:00",
                    "member_post_rest_time": parse_datetime("2024-01-02T16:00:00.123Z"),
                    "member_pre_rest_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_remarks": "Crew member remark",
                    "member_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_sched_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_source": "ACTIVE",
                    "member_stage_name": "Falcon Squadron",
                    "member_transport_req": True,
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "notified": True,
                    "phone_number": "+14155552671",
                    "phys_av_code": "D",
                    "phys_av_status": "OVERDUE",
                    "phys_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "rank": "Capt",
                    "remark_code": "ABE33",
                    "rms_mds": "C017A",
                    "show_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "squadron": "21AS",
                    "training_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_rms="ARMS",
            crew_role="DEADHEAD",
            crew_source="ACTIVE",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_unit="00016ALSQ",
            crew_wing="60AMW",
            current_icao="KCOS",
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            flt_auth_num="KT001",
            id_site_current="b677cf3b-d44d-450e-8b8f-d23f997f8778",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_alert_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            personnel_type="AIRCREW",
            pickup_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            post_rest_applied=False,
            post_rest_end=parse_datetime("2024-01-02T16:00:00.123Z"),
            post_rest_offset="+05:00",
            pre_rest_applied=False,
            pre_rest_start=parse_datetime("2024-01-01T16:00:00.123Z"),
            req_qual_code=["AL", "CS"],
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage1_qual="1AXXX",
            stage2_qual="2AXXX",
            stage3_qual="3AXXX",
            stage_name="Falcon Squadron",
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
            transport_req=True,
            trip_kit="TK-1234",
        )
        assert crew is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert crew is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.retrieve(
            id="id",
        )
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert_matches_type(CrewFull, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crew.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            body_id="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            alert_type="ALPHA",
            arms_crew_unit="00016ALSQ",
            assigned_qual_code=["AL", "CS"],
            commander_id="763a1c1e8d2f3c16af825a11e3f1f579",
            commander_last4_ssn="1234",
            commander_name="John Doe",
            crew_home=False,
            crew_members=[
                {
                    "alerted": True,
                    "all_sortie": True,
                    "approved": True,
                    "attached": True,
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "duty_status": "AGR",
                    "emailed": True,
                    "extra_time": True,
                    "first_name": "Freddie",
                    "flt_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_currency_exp_id": "SS05AM",
                    "flt_rec_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "flt_rec_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "fly_squadron": "141ARS",
                    "funded": True,
                    "gender": "F",
                    "gnd_currency_exp": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gnd_currency_exp_id": "AH03YM",
                    "grounded": True,
                    "guest_start": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "guest_stop": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last4_ssn": "1234",
                    "last_flt_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "last_name": "Smith",
                    "loaned_to": "Thunderbirds",
                    "lodging": "Peterson SFB",
                    "member_actual_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_adj_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_adj_return_time_approver": "Smith",
                    "member_id": "12345678abc",
                    "member_init_start_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_last_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_legal_alert_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_pickup_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "member_post_rest_offset": "+05:00",
                    "member_post_rest_time": parse_datetime("2024-01-02T16:00:00.123Z"),
                    "member_pre_rest_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_remarks": "Crew member remark",
                    "member_return_time": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "member_sched_alert_time": parse_datetime("2024-02-26T09:15:00.123Z"),
                    "member_source": "ACTIVE",
                    "member_stage_name": "Falcon Squadron",
                    "member_transport_req": True,
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "notified": True,
                    "phone_number": "+14155552671",
                    "phys_av_code": "D",
                    "phys_av_status": "OVERDUE",
                    "phys_due": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "rank": "Capt",
                    "remark_code": "ABE33",
                    "rms_mds": "C017A",
                    "show_time": parse_datetime("2024-02-26T10:15:00.123Z"),
                    "squadron": "21AS",
                    "training_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_rms="ARMS",
            crew_role="DEADHEAD",
            crew_source="ACTIVE",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_unit="00016ALSQ",
            crew_wing="60AMW",
            current_icao="KCOS",
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            flt_auth_num="KT001",
            id_site_current="b677cf3b-d44d-450e-8b8f-d23f997f8778",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_alert_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            personnel_type="AIRCREW",
            pickup_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            post_rest_applied=False,
            post_rest_end=parse_datetime("2024-01-02T16:00:00.123Z"),
            post_rest_offset="+05:00",
            pre_rest_applied=False,
            pre_rest_start=parse_datetime("2024-01-01T16:00:00.123Z"),
            req_qual_code=["AL", "CS"],
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage1_qual="1AXXX",
            stage2_qual="2AXXX",
            stage3_qual="3AXXX",
            stage_name="Falcon Squadron",
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
            transport_req=True,
            trip_kit="TK-1234",
        )
        assert crew is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert crew is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.crew.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                orig_crew_id="JHJDHjhuu929o92",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.list()
        assert_matches_type(AsyncOffsetPage[CrewAbridged], crew, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[CrewAbridged], crew, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(AsyncOffsetPage[CrewAbridged], crew, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert_matches_type(AsyncOffsetPage[CrewAbridged], crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.count()
        assert_matches_type(str, crew, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, crew, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(str, crew, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert_matches_type(str, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.queryhelp()
        assert_matches_type(CrewQueryhelpResponse, crew, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(CrewQueryhelpResponse, crew, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert_matches_type(CrewQueryhelpResponse, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.tuple(
            columns="columns",
        )
        assert_matches_type(CrewTupleResponse, crew, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CrewTupleResponse, crew, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(CrewTupleResponse, crew, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert_matches_type(CrewTupleResponse, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "orig_crew_id": "JHJDHjhuu929o92",
                    "source": "Bluestaq",
                }
            ],
        )
        assert crew is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "orig_crew_id": "JHJDHjhuu929o92",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert crew is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "orig_crew_id": "JHJDHjhuu929o92",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True
