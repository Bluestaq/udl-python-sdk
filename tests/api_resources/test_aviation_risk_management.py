# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AviationRiskManagementQueryResponse,
    AviationRiskManagementTupleResponse,
    AviationRiskManagementRetrieveResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAviationRiskManagement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )
        assert aviation_risk_management is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            aviation_risk_management_worksheet_record=[
                {
                    "mission_date": parse_date("2024-11-25"),
                    "aircraft_mds": "E-2C HAWKEYE",
                    "approval_pending": True,
                    "approved": False,
                    "aviation_risk_management_worksheet_score": [
                        {
                            "approval_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                            "approved_by": "John Smith",
                            "approved_code": 0,
                            "aviation_risk_management_sortie": [
                                {
                                    "ext_sortie_id": "MB014313032022407540",
                                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                                    "leg_num": 100,
                                    "sortie_score": 3,
                                }
                            ],
                            "ext_score_id": "BM022301191649232740",
                            "risk_category": "Crew/Aircraft",
                            "risk_description": "Upgrade training",
                            "risk_key": "26",
                            "risk_name": "Crew Qualification",
                            "score": 1,
                            "score_remark": "Worksheet score remark.",
                        }
                    ],
                    "disposition_comments": "Disposition comment.",
                    "ext_record_id": "B022401191649232716",
                    "itinerary": "RJTY-PGUA-RJTY",
                    "last_updated_at": parse_datetime("2024-11-02T16:00:00.123Z"),
                    "remarks": "Worksheet record remark.",
                    "severity_level": 0,
                    "submission_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                    "tier_number": 2,
                    "total_score": 11,
                    "user_id": "TIER0SCORING",
                }
            ],
            ext_mission_id="MCD04250106123509230",
            mission_number="LVM134412001",
            org_id="50000002",
            origin="THIRD_PARTY_DATASOURCE",
            unit_id="63",
        )
        assert aviation_risk_management is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert aviation_risk_management is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.retrieve(
            id="id",
        )
        assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aviation_risk_management.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )
        assert aviation_risk_management is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            aviation_risk_management_worksheet_record=[
                {
                    "mission_date": parse_date("2024-11-25"),
                    "aircraft_mds": "E-2C HAWKEYE",
                    "approval_pending": True,
                    "approved": False,
                    "aviation_risk_management_worksheet_score": [
                        {
                            "approval_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                            "approved_by": "John Smith",
                            "approved_code": 0,
                            "aviation_risk_management_sortie": [
                                {
                                    "ext_sortie_id": "MB014313032022407540",
                                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                                    "leg_num": 100,
                                    "sortie_score": 3,
                                }
                            ],
                            "ext_score_id": "BM022301191649232740",
                            "risk_category": "Crew/Aircraft",
                            "risk_description": "Upgrade training",
                            "risk_key": "26",
                            "risk_name": "Crew Qualification",
                            "score": 1,
                            "score_remark": "Worksheet score remark.",
                        }
                    ],
                    "disposition_comments": "Disposition comment.",
                    "ext_record_id": "B022401191649232716",
                    "itinerary": "RJTY-PGUA-RJTY",
                    "last_updated_at": parse_datetime("2024-11-02T16:00:00.123Z"),
                    "remarks": "Worksheet record remark.",
                    "severity_level": 0,
                    "submission_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                    "tier_number": 2,
                    "total_score": 11,
                    "user_id": "TIER0SCORING",
                }
            ],
            ext_mission_id="MCD04250106123509230",
            mission_number="LVM134412001",
            org_id="50000002",
            origin="THIRD_PARTY_DATASOURCE",
            unit_id="63",
        )
        assert aviation_risk_management is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert aviation_risk_management is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.aviation_risk_management.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
                source="Bluestaq",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.delete(
            "id",
        )
        assert aviation_risk_management is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert aviation_risk_management is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aviation_risk_management.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.count(
            id_mission="idMission",
        )
        assert_matches_type(str, aviation_risk_management, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.count(
            id_mission="idMission",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aviation_risk_management, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.count(
            id_mission="idMission",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert_matches_type(str, aviation_risk_management, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.count(
            id_mission="idMission",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert_matches_type(str, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )
        assert aviation_risk_management is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert aviation_risk_management is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.query(
            id_mission="idMission",
        )
        assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.query(
            id_mission="idMission",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.query(
            id_mission="idMission",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.query(
            id_mission="idMission",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.query_help()
        assert aviation_risk_management is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert aviation_risk_management is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.tuple(
            columns="columns",
            id_mission="idMission",
        )
        assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.tuple(
            columns="columns",
            id_mission="idMission",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.tuple(
            columns="columns",
            id_mission="idMission",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.tuple(
            columns="columns",
            id_mission="idMission",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        aviation_risk_management = client.aviation_risk_management.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )
        assert aviation_risk_management is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.aviation_risk_management.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = response.parse()
        assert aviation_risk_management is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.aviation_risk_management.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAviationRiskManagement:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            aviation_risk_management_worksheet_record=[
                {
                    "mission_date": parse_date("2024-11-25"),
                    "aircraft_mds": "E-2C HAWKEYE",
                    "approval_pending": True,
                    "approved": False,
                    "aviation_risk_management_worksheet_score": [
                        {
                            "approval_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                            "approved_by": "John Smith",
                            "approved_code": 0,
                            "aviation_risk_management_sortie": [
                                {
                                    "ext_sortie_id": "MB014313032022407540",
                                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                                    "leg_num": 100,
                                    "sortie_score": 3,
                                }
                            ],
                            "ext_score_id": "BM022301191649232740",
                            "risk_category": "Crew/Aircraft",
                            "risk_description": "Upgrade training",
                            "risk_key": "26",
                            "risk_name": "Crew Qualification",
                            "score": 1,
                            "score_remark": "Worksheet score remark.",
                        }
                    ],
                    "disposition_comments": "Disposition comment.",
                    "ext_record_id": "B022401191649232716",
                    "itinerary": "RJTY-PGUA-RJTY",
                    "last_updated_at": parse_datetime("2024-11-02T16:00:00.123Z"),
                    "remarks": "Worksheet record remark.",
                    "severity_level": 0,
                    "submission_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                    "tier_number": 2,
                    "total_score": 11,
                    "user_id": "TIER0SCORING",
                }
            ],
            ext_mission_id="MCD04250106123509230",
            mission_number="LVM134412001",
            org_id="50000002",
            origin="THIRD_PARTY_DATASOURCE",
            unit_id="63",
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert aviation_risk_management is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.retrieve(
            id="id",
        )
        assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert_matches_type(AviationRiskManagementRetrieveResponse, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aviation_risk_management.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            aviation_risk_management_worksheet_record=[
                {
                    "mission_date": parse_date("2024-11-25"),
                    "aircraft_mds": "E-2C HAWKEYE",
                    "approval_pending": True,
                    "approved": False,
                    "aviation_risk_management_worksheet_score": [
                        {
                            "approval_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                            "approved_by": "John Smith",
                            "approved_code": 0,
                            "aviation_risk_management_sortie": [
                                {
                                    "ext_sortie_id": "MB014313032022407540",
                                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                                    "leg_num": 100,
                                    "sortie_score": 3,
                                }
                            ],
                            "ext_score_id": "BM022301191649232740",
                            "risk_category": "Crew/Aircraft",
                            "risk_description": "Upgrade training",
                            "risk_key": "26",
                            "risk_name": "Crew Qualification",
                            "score": 1,
                            "score_remark": "Worksheet score remark.",
                        }
                    ],
                    "disposition_comments": "Disposition comment.",
                    "ext_record_id": "B022401191649232716",
                    "itinerary": "RJTY-PGUA-RJTY",
                    "last_updated_at": parse_datetime("2024-11-02T16:00:00.123Z"),
                    "remarks": "Worksheet record remark.",
                    "severity_level": 0,
                    "submission_date": parse_datetime("2024-11-01T16:00:00.123Z"),
                    "tier_number": 2,
                    "total_score": 11,
                    "user_id": "TIER0SCORING",
                }
            ],
            ext_mission_id="MCD04250106123509230",
            mission_number="LVM134412001",
            org_id="50000002",
            origin="THIRD_PARTY_DATASOURCE",
            unit_id="63",
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert aviation_risk_management is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.aviation_risk_management.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_mission="fa18d96e-91ea-60da-a7a8-1af6500066c8",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.delete(
            "id",
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert aviation_risk_management is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aviation_risk_management.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.count(
            id_mission="idMission",
        )
        assert_matches_type(str, aviation_risk_management, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.count(
            id_mission="idMission",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aviation_risk_management, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.count(
            id_mission="idMission",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert_matches_type(str, aviation_risk_management, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.count(
            id_mission="idMission",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert_matches_type(str, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert aviation_risk_management is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.query(
            id_mission="idMission",
        )
        assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.query(
            id_mission="idMission",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.query(
            id_mission="idMission",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.query(
            id_mission="idMission",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert_matches_type(AviationRiskManagementQueryResponse, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.query_help()
        assert aviation_risk_management is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert aviation_risk_management is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.tuple(
            columns="columns",
            id_mission="idMission",
        )
        assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.tuple(
            columns="columns",
            id_mission="idMission",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.tuple(
            columns="columns",
            id_mission="idMission",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.tuple(
            columns="columns",
            id_mission="idMission",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert_matches_type(AviationRiskManagementTupleResponse, aviation_risk_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        aviation_risk_management = await async_client.aviation_risk_management.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )
        assert aviation_risk_management is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aviation_risk_management.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aviation_risk_management = await response.parse()
        assert aviation_risk_management is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aviation_risk_management.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_mission": "fa18d96e-91ea-60da-a7a8-1af6500066c8",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aviation_risk_management = await response.parse()
            assert aviation_risk_management is None

        assert cast(Any, response.is_closed) is True
