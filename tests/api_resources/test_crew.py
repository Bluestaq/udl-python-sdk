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
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.create(
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            id="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            arms_crew_unit="00016ALSQ",
            arr_icao="KDEN",
            crew_home=False,
            crew_members=[
                {
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "first_name": "Freddie",
                    "last4_ssn": "1234",
                    "last_name": "Smith",
                    "member_id": "12345678abc",
                    "member_remarks": "Crew member remark",
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "rank": "Capt",
                    "squadron": "21AS",
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_wing="60AMW",
            current_icao="KCOS",
            dep_icao="KCOS",
            est_arr_time=parse_datetime("2024-01-01T18:00:00.123Z"),
            est_dep_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            post_rest_applied=False,
            pre_rest_applied=False,
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
        )
        assert crew is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
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
            data_mode="REAL",
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
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        crew = client.crew.update(
            id_1="id",
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            id_2="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            arms_crew_unit="00016ALSQ",
            arr_icao="KDEN",
            crew_home=False,
            crew_members=[
                {
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "first_name": "Freddie",
                    "last4_ssn": "1234",
                    "last_name": "Smith",
                    "member_id": "12345678abc",
                    "member_remarks": "Crew member remark",
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "rank": "Capt",
                    "squadron": "21AS",
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_wing="60AMW",
            current_icao="KCOS",
            dep_icao="KCOS",
            est_arr_time=parse_datetime("2024-01-01T18:00:00.123Z"),
            est_dep_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            post_rest_applied=False,
            pre_rest_applied=False,
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
        )
        assert crew is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.crew.with_raw_response.update(
            id_1="id",
            classification_marking="U",
            data_mode="REAL",
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
            id_1="id",
            classification_marking="U",
            data_mode="REAL",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.crew.with_raw_response.update(
                id_1="",
                classification_marking="U",
                data_mode="REAL",
                orig_crew_id="JHJDHjhuu929o92",
                source="Bluestaq",
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
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.create(
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            id="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            arms_crew_unit="00016ALSQ",
            arr_icao="KDEN",
            crew_home=False,
            crew_members=[
                {
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "first_name": "Freddie",
                    "last4_ssn": "1234",
                    "last_name": "Smith",
                    "member_id": "12345678abc",
                    "member_remarks": "Crew member remark",
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "rank": "Capt",
                    "squadron": "21AS",
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_wing="60AMW",
            current_icao="KCOS",
            dep_icao="KCOS",
            est_arr_time=parse_datetime("2024-01-01T18:00:00.123Z"),
            est_dep_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            post_rest_applied=False,
            pre_rest_applied=False,
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
        )
        assert crew is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
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
            data_mode="REAL",
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
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
        )
        assert crew is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        crew = await async_client.crew.update(
            id_1="id",
            classification_marking="U",
            data_mode="REAL",
            orig_crew_id="JHJDHjhuu929o92",
            source="Bluestaq",
            id_2="bdad6945-c9e4-b829-f7be-1ad075541921",
            adj_return_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            adj_return_time_approver="Smith",
            aircraft_mds="C017A",
            alerted_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            arms_crew_unit="00016ALSQ",
            arr_icao="KDEN",
            crew_home=False,
            crew_members=[
                {
                    "branch": "Air Force",
                    "civilian": False,
                    "commander": False,
                    "crew_position": "EP A",
                    "dod_id": "0123456789",
                    "duty_position": "IP",
                    "first_name": "Freddie",
                    "last4_ssn": "1234",
                    "last_name": "Smith",
                    "member_id": "12345678abc",
                    "member_remarks": "Crew member remark",
                    "member_type": "AIRCREW",
                    "middle_initial": "G",
                    "rank": "Capt",
                    "squadron": "21AS",
                    "username": "fgsmith",
                    "wing": "60AMW",
                }
            ],
            crew_name="falcon",
            crew_squadron="21AS",
            crew_type="AIRLAND",
            crew_wing="60AMW",
            current_icao="KCOS",
            dep_icao="KCOS",
            est_arr_time=parse_datetime("2024-01-01T18:00:00.123Z"),
            est_dep_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            fdp_elig_type="A",
            fdp_type="A",
            female_enlisted_qty=2,
            female_officer_qty=1,
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            init_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            legal_alert_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            legal_bravo_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            linked_task=False,
            male_enlisted_qty=3,
            male_officer_qty=1,
            mission_id="AJM123456123",
            origin="THIRD_PARTY_DATASOURCE",
            post_rest_applied=False,
            pre_rest_applied=False,
            return_time=parse_datetime("2022-01-01T16:00:00.123Z"),
            stage_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            status="APPROVED",
        )
        assert crew is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.crew.with_raw_response.update(
            id_1="id",
            classification_marking="U",
            data_mode="REAL",
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
            id_1="id",
            classification_marking="U",
            data_mode="REAL",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.crew.with_raw_response.update(
                id_1="",
                classification_marking="U",
                data_mode="REAL",
                orig_crew_id="JHJDHjhuu929o92",
                source="Bluestaq",
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
