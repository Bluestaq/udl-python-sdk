# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.site import (
    OperationListResponse,
    OperationTupleResponse,
    OperationRetrieveResponse,
    OperationQueryHelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )
        assert operation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
            id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            daily_operations=[
                {
                    "day_of_week": "MONDAY",
                    "operating_hours": [
                        {
                            "op_start_time": "12:00",
                            "op_stop_time": "22:00",
                        }
                    ],
                    "operation_name": "Arrivals",
                    "ophrs_last_changed_by": "John Smith",
                    "ophrs_last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
            dops_last_changed_by="John Smith",
            dops_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            dops_last_changed_reason="Example reason for change.",
            id_launch_site="b150b3ee-884b-b9ac-60a0-6408b4b16088",
            maximum_on_grounds=[
                {
                    "aircraft_mds": "C017A",
                    "contingency_mog": 3,
                    "mog_last_changed_by": "John Smith",
                    "mog_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "wide_parking_mog": 1,
                    "wide_working_mog": 1,
                }
            ],
            mogs_last_changed_by="Jane Doe",
            mogs_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            mogs_last_changed_reason="Example reason for change.",
            operational_deviations=[
                {
                    "affected_aircraft_mds": "C017A",
                    "affected_mog": 1,
                    "aircraft_on_ground_time": "14:00",
                    "crew_rest_time": "14:00",
                    "od_last_changed_by": "John Smith",
                    "od_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "od_remark": "Example remark about this operational deviation.",
                }
            ],
            operational_plannings=[
                {
                    "op_end_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_last_changed_by": "John Smith",
                    "op_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_remark": "Example planning remark",
                    "op_source": "a3",
                    "op_start_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_status": "Verified",
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            pathways=[
                {
                    "pw_definition": "AGP: 14L, K6, K, G (ANG APRN TO TWY K), GUARD (MAIN)",
                    "pw_last_changed_by": "John Smith",
                    "pw_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "pw_type": "Taxiway",
                    "pw_usage": "Arrival",
                }
            ],
            waivers=[
                {
                    "expiration_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "has_expired": False,
                    "issue_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "issuer_name": "John Smith",
                    "requester_name": "Jane Doe",
                    "requester_phone_number": "808-123-4567",
                    "requesting_unit": "2A1",
                    "waiver_applies_to": "C017A",
                    "waiver_description": "Example waiver description",
                    "waiver_last_changed_by": "J. Appleseed",
                    "waiver_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                }
            ],
        )
        assert operation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert operation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.retrieve(
            id="id",
        )
        assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.site.operations.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )
        assert operation is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
            body_id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            daily_operations=[
                {
                    "day_of_week": "MONDAY",
                    "operating_hours": [
                        {
                            "op_start_time": "12:00",
                            "op_stop_time": "22:00",
                        }
                    ],
                    "operation_name": "Arrivals",
                    "ophrs_last_changed_by": "John Smith",
                    "ophrs_last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
            dops_last_changed_by="John Smith",
            dops_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            dops_last_changed_reason="Example reason for change.",
            id_launch_site="b150b3ee-884b-b9ac-60a0-6408b4b16088",
            maximum_on_grounds=[
                {
                    "aircraft_mds": "C017A",
                    "contingency_mog": 3,
                    "mog_last_changed_by": "John Smith",
                    "mog_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "wide_parking_mog": 1,
                    "wide_working_mog": 1,
                }
            ],
            mogs_last_changed_by="Jane Doe",
            mogs_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            mogs_last_changed_reason="Example reason for change.",
            operational_deviations=[
                {
                    "affected_aircraft_mds": "C017A",
                    "affected_mog": 1,
                    "aircraft_on_ground_time": "14:00",
                    "crew_rest_time": "14:00",
                    "od_last_changed_by": "John Smith",
                    "od_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "od_remark": "Example remark about this operational deviation.",
                }
            ],
            operational_plannings=[
                {
                    "op_end_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_last_changed_by": "John Smith",
                    "op_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_remark": "Example planning remark",
                    "op_source": "a3",
                    "op_start_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_status": "Verified",
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            pathways=[
                {
                    "pw_definition": "AGP: 14L, K6, K, G (ANG APRN TO TWY K), GUARD (MAIN)",
                    "pw_last_changed_by": "John Smith",
                    "pw_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "pw_type": "Taxiway",
                    "pw_usage": "Arrival",
                }
            ],
            waivers=[
                {
                    "expiration_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "has_expired": False,
                    "issue_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "issuer_name": "John Smith",
                    "requester_name": "Jane Doe",
                    "requester_phone_number": "808-123-4567",
                    "requesting_unit": "2A1",
                    "waiver_applies_to": "C017A",
                    "waiver_description": "Example waiver description",
                    "waiver_last_changed_by": "J. Appleseed",
                    "waiver_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                }
            ],
        )
        assert operation is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert operation is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.site.operations.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.list(
            id_site="idSite",
        )
        assert_matches_type(SyncOffsetPage[OperationListResponse], operation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.list(
            id_site="idSite",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OperationListResponse], operation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.list(
            id_site="idSite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(SyncOffsetPage[OperationListResponse], operation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.list(
            id_site="idSite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(SyncOffsetPage[OperationListResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.delete(
            "id",
        )
        assert operation is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert operation is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.site.operations.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.count(
            id_site="idSite",
        )
        assert_matches_type(str, operation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.count(
            id_site="idSite",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, operation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.count(
            id_site="idSite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(str, operation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.count(
            id_site="idSite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(str, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )
        assert operation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert operation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.query_help()
        assert_matches_type(OperationQueryHelpResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationQueryHelpResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationQueryHelpResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.tuple(
            columns="columns",
            id_site="idSite",
        )
        assert_matches_type(OperationTupleResponse, operation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.tuple(
            columns="columns",
            id_site="idSite",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperationTupleResponse, operation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.tuple(
            columns="columns",
            id_site="idSite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationTupleResponse, operation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.tuple(
            columns="columns",
            id_site="idSite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationTupleResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        operation = client.site.operations.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )
        assert operation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.site.operations.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert operation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.site.operations.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOperations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )
        assert operation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
            id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            daily_operations=[
                {
                    "day_of_week": "MONDAY",
                    "operating_hours": [
                        {
                            "op_start_time": "12:00",
                            "op_stop_time": "22:00",
                        }
                    ],
                    "operation_name": "Arrivals",
                    "ophrs_last_changed_by": "John Smith",
                    "ophrs_last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
            dops_last_changed_by="John Smith",
            dops_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            dops_last_changed_reason="Example reason for change.",
            id_launch_site="b150b3ee-884b-b9ac-60a0-6408b4b16088",
            maximum_on_grounds=[
                {
                    "aircraft_mds": "C017A",
                    "contingency_mog": 3,
                    "mog_last_changed_by": "John Smith",
                    "mog_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "wide_parking_mog": 1,
                    "wide_working_mog": 1,
                }
            ],
            mogs_last_changed_by="Jane Doe",
            mogs_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            mogs_last_changed_reason="Example reason for change.",
            operational_deviations=[
                {
                    "affected_aircraft_mds": "C017A",
                    "affected_mog": 1,
                    "aircraft_on_ground_time": "14:00",
                    "crew_rest_time": "14:00",
                    "od_last_changed_by": "John Smith",
                    "od_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "od_remark": "Example remark about this operational deviation.",
                }
            ],
            operational_plannings=[
                {
                    "op_end_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_last_changed_by": "John Smith",
                    "op_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_remark": "Example planning remark",
                    "op_source": "a3",
                    "op_start_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_status": "Verified",
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            pathways=[
                {
                    "pw_definition": "AGP: 14L, K6, K, G (ANG APRN TO TWY K), GUARD (MAIN)",
                    "pw_last_changed_by": "John Smith",
                    "pw_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "pw_type": "Taxiway",
                    "pw_usage": "Arrival",
                }
            ],
            waivers=[
                {
                    "expiration_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "has_expired": False,
                    "issue_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "issuer_name": "John Smith",
                    "requester_name": "Jane Doe",
                    "requester_phone_number": "808-123-4567",
                    "requesting_unit": "2A1",
                    "waiver_applies_to": "C017A",
                    "waiver_description": "Example waiver description",
                    "waiver_last_changed_by": "J. Appleseed",
                    "waiver_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                }
            ],
        )
        assert operation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert operation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.retrieve(
            id="id",
        )
        assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationRetrieveResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.site.operations.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )
        assert operation is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
            body_id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            daily_operations=[
                {
                    "day_of_week": "MONDAY",
                    "operating_hours": [
                        {
                            "op_start_time": "12:00",
                            "op_stop_time": "22:00",
                        }
                    ],
                    "operation_name": "Arrivals",
                    "ophrs_last_changed_by": "John Smith",
                    "ophrs_last_changed_date": parse_datetime("2024-01-01T16:00:00.123Z"),
                }
            ],
            dops_last_changed_by="John Smith",
            dops_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            dops_last_changed_reason="Example reason for change.",
            id_launch_site="b150b3ee-884b-b9ac-60a0-6408b4b16088",
            maximum_on_grounds=[
                {
                    "aircraft_mds": "C017A",
                    "contingency_mog": 3,
                    "mog_last_changed_by": "John Smith",
                    "mog_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "wide_parking_mog": 1,
                    "wide_working_mog": 1,
                }
            ],
            mogs_last_changed_by="Jane Doe",
            mogs_last_changed_date=parse_datetime("2024-01-01T16:00:00.000Z"),
            mogs_last_changed_reason="Example reason for change.",
            operational_deviations=[
                {
                    "affected_aircraft_mds": "C017A",
                    "affected_mog": 1,
                    "aircraft_on_ground_time": "14:00",
                    "crew_rest_time": "14:00",
                    "od_last_changed_by": "John Smith",
                    "od_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "od_remark": "Example remark about this operational deviation.",
                }
            ],
            operational_plannings=[
                {
                    "op_end_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_last_changed_by": "John Smith",
                    "op_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_remark": "Example planning remark",
                    "op_source": "a3",
                    "op_start_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "op_status": "Verified",
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            pathways=[
                {
                    "pw_definition": "AGP: 14L, K6, K, G (ANG APRN TO TWY K), GUARD (MAIN)",
                    "pw_last_changed_by": "John Smith",
                    "pw_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "pw_type": "Taxiway",
                    "pw_usage": "Arrival",
                }
            ],
            waivers=[
                {
                    "expiration_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "has_expired": False,
                    "issue_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                    "issuer_name": "John Smith",
                    "requester_name": "Jane Doe",
                    "requester_phone_number": "808-123-4567",
                    "requesting_unit": "2A1",
                    "waiver_applies_to": "C017A",
                    "waiver_description": "Example waiver description",
                    "waiver_last_changed_by": "J. Appleseed",
                    "waiver_last_changed_date": parse_datetime("2024-01-01T16:00:00.000Z"),
                }
            ],
        )
        assert operation is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert operation is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.site.operations.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.list(
            id_site="idSite",
        )
        assert_matches_type(AsyncOffsetPage[OperationListResponse], operation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.list(
            id_site="idSite",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OperationListResponse], operation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.list(
            id_site="idSite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(AsyncOffsetPage[OperationListResponse], operation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.list(
            id_site="idSite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(AsyncOffsetPage[OperationListResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.delete(
            "id",
        )
        assert operation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert operation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.site.operations.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.count(
            id_site="idSite",
        )
        assert_matches_type(str, operation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.count(
            id_site="idSite",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, operation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.count(
            id_site="idSite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(str, operation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.count(
            id_site="idSite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(str, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )
        assert operation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert operation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.query_help()
        assert_matches_type(OperationQueryHelpResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationQueryHelpResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationQueryHelpResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.tuple(
            columns="columns",
            id_site="idSite",
        )
        assert_matches_type(OperationTupleResponse, operation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.tuple(
            columns="columns",
            id_site="idSite",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OperationTupleResponse, operation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.tuple(
            columns="columns",
            id_site="idSite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationTupleResponse, operation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.tuple(
            columns="columns",
            id_site="idSite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationTupleResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        operation = await async_client.site.operations.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )
        assert operation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.site.operations.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert operation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.site.operations.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_site": "a150b3ee-884b-b9ac-60a0-6408b4b16088",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert operation is None

        assert cast(Any, response.is_closed) is True
