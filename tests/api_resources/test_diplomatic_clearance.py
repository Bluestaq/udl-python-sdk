# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    DiplomaticClearanceTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.air_operations import DiplomaticclearanceFull, DiplomaticclearanceAbridged

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiplomaticClearance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
            id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            apacs_id="1083034",
            diplomatic_clearance_details=[
                {
                    "action": "O",
                    "alt_country_code": "IZ",
                    "clearance_id": "MFMW225662GHQ",
                    "clearance_remark": "Clearance remarks",
                    "cleared_call_sign": "FALCN09",
                    "country_code": "NL",
                    "country_name": "NETHERLANDS",
                    "entry_net": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "entry_point": "LOMOS",
                    "exit_nlt": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "exit_point": "BUDOP",
                    "external_clearance_id": "aa714f4d52a37ab1a00b21af9566e379",
                    "id_sortie": "207010e0-f97d-431c-8c00-7e46acfef0f5",
                    "leg_num": 825,
                    "profile": "T LAND/OFLY IATA COMPLIANT CARGO 23",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "DCT DOH P430 BAYAN/M062F150 P430 RAMKI",
                    "sequence_num": 3,
                    "status": "IN WORK",
                    "valid_desc": "CY2023",
                    "valid_end_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "valid_start_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "window_remark": "Period remarks",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "text": "Example mission remarks.",
                    "user": "John Doe",
                }
            ],
            dip_worksheet_name="G2-939911-AC",
            doc_deadline=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_worksheet_id="990ae849089e3d6cad69655324176bb6",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.retrieve(
            id="id",
        )
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.diplomatic_clearance.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
            body_id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            apacs_id="1083034",
            diplomatic_clearance_details=[
                {
                    "action": "O",
                    "alt_country_code": "IZ",
                    "clearance_id": "MFMW225662GHQ",
                    "clearance_remark": "Clearance remarks",
                    "cleared_call_sign": "FALCN09",
                    "country_code": "NL",
                    "country_name": "NETHERLANDS",
                    "entry_net": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "entry_point": "LOMOS",
                    "exit_nlt": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "exit_point": "BUDOP",
                    "external_clearance_id": "aa714f4d52a37ab1a00b21af9566e379",
                    "id_sortie": "207010e0-f97d-431c-8c00-7e46acfef0f5",
                    "leg_num": 825,
                    "profile": "T LAND/OFLY IATA COMPLIANT CARGO 23",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "DCT DOH P430 BAYAN/M062F150 P430 RAMKI",
                    "sequence_num": 3,
                    "status": "IN WORK",
                    "valid_desc": "CY2023",
                    "valid_end_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "valid_start_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "window_remark": "Period remarks",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "text": "Example mission remarks.",
                    "user": "John Doe",
                }
            ],
            dip_worksheet_name="G2-939911-AC",
            doc_deadline=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_worksheet_id="990ae849089e3d6cad69655324176bb6",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.diplomatic_clearance.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
                id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert_matches_type(SyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert_matches_type(SyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.delete(
            "id",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.diplomatic_clearance.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, diplomatic_clearance, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, diplomatic_clearance, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert_matches_type(str, diplomatic_clearance, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert_matches_type(str, diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.queryhelp()
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDiplomaticClearance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
            id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            apacs_id="1083034",
            diplomatic_clearance_details=[
                {
                    "action": "O",
                    "alt_country_code": "IZ",
                    "clearance_id": "MFMW225662GHQ",
                    "clearance_remark": "Clearance remarks",
                    "cleared_call_sign": "FALCN09",
                    "country_code": "NL",
                    "country_name": "NETHERLANDS",
                    "entry_net": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "entry_point": "LOMOS",
                    "exit_nlt": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "exit_point": "BUDOP",
                    "external_clearance_id": "aa714f4d52a37ab1a00b21af9566e379",
                    "id_sortie": "207010e0-f97d-431c-8c00-7e46acfef0f5",
                    "leg_num": 825,
                    "profile": "T LAND/OFLY IATA COMPLIANT CARGO 23",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "DCT DOH P430 BAYAN/M062F150 P430 RAMKI",
                    "sequence_num": 3,
                    "status": "IN WORK",
                    "valid_desc": "CY2023",
                    "valid_end_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "valid_start_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "window_remark": "Period remarks",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "text": "Example mission remarks.",
                    "user": "John Doe",
                }
            ],
            dip_worksheet_name="G2-939911-AC",
            doc_deadline=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_worksheet_id="990ae849089e3d6cad69655324176bb6",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.retrieve(
            id="id",
        )
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.diplomatic_clearance.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
            body_id="25059135-4afc-45c2-b78b-d6e843dbd96d",
            apacs_id="1083034",
            diplomatic_clearance_details=[
                {
                    "action": "O",
                    "alt_country_code": "IZ",
                    "clearance_id": "MFMW225662GHQ",
                    "clearance_remark": "Clearance remarks",
                    "cleared_call_sign": "FALCN09",
                    "country_code": "NL",
                    "country_name": "NETHERLANDS",
                    "entry_net": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "entry_point": "LOMOS",
                    "exit_nlt": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "exit_point": "BUDOP",
                    "external_clearance_id": "aa714f4d52a37ab1a00b21af9566e379",
                    "id_sortie": "207010e0-f97d-431c-8c00-7e46acfef0f5",
                    "leg_num": 825,
                    "profile": "T LAND/OFLY IATA COMPLIANT CARGO 23",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "DCT DOH P430 BAYAN/M062F150 P430 RAMKI",
                    "sequence_num": 3,
                    "status": "IN WORK",
                    "valid_desc": "CY2023",
                    "valid_end_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "valid_start_time": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "window_remark": "Period remarks",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "text": "Example mission remarks.",
                    "user": "John Doe",
                }
            ],
            dip_worksheet_name="G2-939911-AC",
            doc_deadline=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_worksheet_id="990ae849089e3d6cad69655324176bb6",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
            id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.diplomatic_clearance.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                first_dep_date=parse_datetime("2024-01-01T01:01:01.123Z"),
                id_mission="0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert_matches_type(AsyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert_matches_type(AsyncOffsetPage[DiplomaticclearanceAbridged], diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.delete(
            "id",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.diplomatic_clearance.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert_matches_type(str, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.count(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert_matches_type(str, diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.queryhelp()
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.tuple(
            columns="columns",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert_matches_type(DiplomaticClearanceTupleResponse, diplomatic_clearance, path=["response"])

        assert cast(Any, response.is_closed) is True
