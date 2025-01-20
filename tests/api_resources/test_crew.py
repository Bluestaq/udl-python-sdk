# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    CrewFull,
    CrewListResponse,
    CrewTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrew:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )
        assert crew is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
            id="id",
            adj_return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            adj_return_time_approver="adjReturnTimeApprover",
            aircraft_mds="aircraftMDS",
            alerted_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            arms_crew_unit="armsCrewUnit",
            arr_icao="arrICAO",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            crew_home=True,
            crew_members=[
                {
                    "branch": "branch",
                    "civilian": True,
                    "commander": True,
                    "crew_position": "crewPosition",
                    "dod_id": "dodID",
                    "duty_position": "dutyPosition",
                    "first_name": "firstName",
                    "last4_ssn": "last4SSN",
                    "last_name": "lastName",
                    "member_id": "memberId",
                    "member_remarks": "memberRemarks",
                    "member_type": "memberType",
                    "middle_initial": "middleInitial",
                    "rank": "rank",
                    "squadron": "squadron",
                    "username": "username",
                    "wing": "wing",
                }
            ],
            crew_name="crewName",
            crew_squadron="crewSquadron",
            crew_type="crewType",
            crew_wing="crewWing",
            current_icao="currentICAO",
            dep_icao="depICAO",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            fdp_elig_type="fdpEligType",
            fdp_type="fdpType",
            female_enlisted_qty=0,
            female_officer_qty=0,
            id_sortie="idSortie",
            init_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_alert_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_bravo_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            linked_task=True,
            male_enlisted_qty=0,
            male_officer_qty=0,
            mission_id="missionId",
            origin="origin",
            orig_network="origNetwork",
            post_rest_applied=True,
            pre_rest_applied=True,
            return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stage_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert crew is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert crew is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.retrieve(
            "id",
        )
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )
        assert crew is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
            id_2="id",
            adj_return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            adj_return_time_approver="adjReturnTimeApprover",
            aircraft_mds="aircraftMDS",
            alerted_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            arms_crew_unit="armsCrewUnit",
            arr_icao="arrICAO",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            crew_home=True,
            crew_members=[
                {
                    "branch": "branch",
                    "civilian": True,
                    "commander": True,
                    "crew_position": "crewPosition",
                    "dod_id": "dodID",
                    "duty_position": "dutyPosition",
                    "first_name": "firstName",
                    "last4_ssn": "last4SSN",
                    "last_name": "lastName",
                    "member_id": "memberId",
                    "member_remarks": "memberRemarks",
                    "member_type": "memberType",
                    "middle_initial": "middleInitial",
                    "rank": "rank",
                    "squadron": "squadron",
                    "username": "username",
                    "wing": "wing",
                }
            ],
            crew_name="crewName",
            crew_squadron="crewSquadron",
            crew_type="crewType",
            crew_wing="crewWing",
            current_icao="currentICAO",
            dep_icao="depICAO",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            fdp_elig_type="fdpEligType",
            fdp_type="fdpType",
            female_enlisted_qty=0,
            female_officer_qty=0,
            id_sortie="idSortie",
            init_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_alert_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_bravo_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            linked_task=True,
            male_enlisted_qty=0,
            male_officer_qty=0,
            mission_id="missionId",
            origin="origin",
            orig_network="origNetwork",
            post_rest_applied=True,
            pre_rest_applied=True,
            return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stage_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert crew is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert crew is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.crew.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                orig_crew_id="origCrewId",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.list()
        assert_matches_type(CrewListResponse, crew, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert_matches_type(CrewListResponse, crew, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert_matches_type(CrewListResponse, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.count()
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
        assert crew is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = response.parse()
        assert crew is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.crew.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.tuple(
            columns="columns",
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


class TestAsyncCrew:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )
        assert crew is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
            id="id",
            adj_return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            adj_return_time_approver="adjReturnTimeApprover",
            aircraft_mds="aircraftMDS",
            alerted_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            arms_crew_unit="armsCrewUnit",
            arr_icao="arrICAO",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            crew_home=True,
            crew_members=[
                {
                    "branch": "branch",
                    "civilian": True,
                    "commander": True,
                    "crew_position": "crewPosition",
                    "dod_id": "dodID",
                    "duty_position": "dutyPosition",
                    "first_name": "firstName",
                    "last4_ssn": "last4SSN",
                    "last_name": "lastName",
                    "member_id": "memberId",
                    "member_remarks": "memberRemarks",
                    "member_type": "memberType",
                    "middle_initial": "middleInitial",
                    "rank": "rank",
                    "squadron": "squadron",
                    "username": "username",
                    "wing": "wing",
                }
            ],
            crew_name="crewName",
            crew_squadron="crewSquadron",
            crew_type="crewType",
            crew_wing="crewWing",
            current_icao="currentICAO",
            dep_icao="depICAO",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            fdp_elig_type="fdpEligType",
            fdp_type="fdpType",
            female_enlisted_qty=0,
            female_officer_qty=0,
            id_sortie="idSortie",
            init_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_alert_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_bravo_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            linked_task=True,
            male_enlisted_qty=0,
            male_officer_qty=0,
            mission_id="missionId",
            origin="origin",
            orig_network="origNetwork",
            post_rest_applied=True,
            pre_rest_applied=True,
            return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stage_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert crew is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert crew is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.retrieve(
            "id",
        )
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(CrewFull, crew, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )
        assert crew is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
            id_2="id",
            adj_return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            adj_return_time_approver="adjReturnTimeApprover",
            aircraft_mds="aircraftMDS",
            alerted_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            arms_crew_unit="armsCrewUnit",
            arr_icao="arrICAO",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            crew_home=True,
            crew_members=[
                {
                    "branch": "branch",
                    "civilian": True,
                    "commander": True,
                    "crew_position": "crewPosition",
                    "dod_id": "dodID",
                    "duty_position": "dutyPosition",
                    "first_name": "firstName",
                    "last4_ssn": "last4SSN",
                    "last_name": "lastName",
                    "member_id": "memberId",
                    "member_remarks": "memberRemarks",
                    "member_type": "memberType",
                    "middle_initial": "middleInitial",
                    "rank": "rank",
                    "squadron": "squadron",
                    "username": "username",
                    "wing": "wing",
                }
            ],
            crew_name="crewName",
            crew_squadron="crewSquadron",
            crew_type="crewType",
            crew_wing="crewWing",
            current_icao="currentICAO",
            dep_icao="depICAO",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            fdp_elig_type="fdpEligType",
            fdp_type="fdpType",
            female_enlisted_qty=0,
            female_officer_qty=0,
            id_sortie="idSortie",
            init_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_alert_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            legal_bravo_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            linked_task=True,
            male_enlisted_qty=0,
            male_officer_qty=0,
            mission_id="missionId",
            origin="origin",
            orig_network="origNetwork",
            post_rest_applied=True,
            pre_rest_applied=True,
            return_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stage_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert crew is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert crew is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            orig_crew_id="origCrewId",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.crew.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                orig_crew_id="origCrewId",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.list()
        assert_matches_type(CrewListResponse, crew, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert_matches_type(CrewListResponse, crew, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert_matches_type(CrewListResponse, crew, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.count()
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
        assert crew is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crew = await response.parse()
        assert crew is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.crew.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crew = await response.parse()
            assert crew is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.tuple(
            columns="columns",
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
