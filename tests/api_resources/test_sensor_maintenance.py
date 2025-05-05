# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SensorMaintenanceGetResponse,
    SensorMaintenanceListResponse,
    SensorMaintenanceTupleResponse,
    SensorMaintenanceCurrentResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensorMaintenance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensor_maintenance is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            id="SENSORMAINTENANCE-ID",
            activity="Activity Description",
            approver="approver",
            changer="changer",
            duration="128:16:52",
            eow_id="eowId",
            equip_status="FMC",
            id_sensor="idSensor",
            impacted_faces="impactedFaces",
            line_number="lineNumber",
            md_ops_cap="R",
            mw_ops_cap="G",
            origin="THIRD_PARTY_DATASOURCE",
            priority="low",
            recall="128:16:52",
            rel="rel",
            remark="Remarks",
            requestor="requestor",
            resource="resource",
            rev="rev",
            ss_ops_cap="Y",
        )
        assert sensor_maintenance is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert sensor_maintenance is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensor_maintenance is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            body_id="SENSORMAINTENANCE-ID",
            activity="Activity Description",
            approver="approver",
            changer="changer",
            duration="128:16:52",
            eow_id="eowId",
            equip_status="FMC",
            id_sensor="idSensor",
            impacted_faces="impactedFaces",
            line_number="lineNumber",
            md_ops_cap="R",
            mw_ops_cap="G",
            origin="THIRD_PARTY_DATASOURCE",
            priority="low",
            recall="128:16:52",
            rel="rel",
            remark="Remarks",
            requestor="requestor",
            resource="resource",
            rev="rev",
            ss_ops_cap="Y",
        )
        assert sensor_maintenance is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert sensor_maintenance is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sensor_maintenance.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
                site_code="site01",
                source="Bluestaq",
                start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.list()
        assert_matches_type(SyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert_matches_type(SyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert_matches_type(SyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.delete(
            "id",
        )
        assert sensor_maintenance is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert sensor_maintenance is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor_maintenance.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.count()
        assert_matches_type(str, sensor_maintenance, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.count(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sensor_maintenance, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert_matches_type(str, sensor_maintenance, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert_matches_type(str, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert sensor_maintenance is None

    @parametrize
    def test_method_create_bulk_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "id": "SENSORMAINTENANCE-ID",
                    "activity": "Activity Description",
                    "approver": "approver",
                    "changer": "changer",
                    "duration": "128:16:52",
                    "eow_id": "eowId",
                    "equip_status": "FMC",
                    "id_sensor": "idSensor",
                    "impacted_faces": "impactedFaces",
                    "line_number": "lineNumber",
                    "md_ops_cap": "R",
                    "mw_ops_cap": "G",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "priority": "low",
                    "recall": "128:16:52",
                    "rel": "rel",
                    "remark": "Remarks",
                    "requestor": "requestor",
                    "resource": "resource",
                    "rev": "rev",
                    "ss_ops_cap": "Y",
                }
            ],
            origin="origin",
            source="source",
        )
        assert sensor_maintenance is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert sensor_maintenance is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_current(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.current()
        assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_method_current_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.current(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_raw_response_current(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.current()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_streaming_response_current(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.current() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.get(
            id="id",
        )
        assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor_maintenance.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.queryhelp()
        assert sensor_maintenance is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert sensor_maintenance is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.tuple(
            columns="columns",
        )
        assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_maintenance = client.sensor_maintenance.tuple(
            columns="columns",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_maintenance.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = response.parse()
        assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sensor_maintenance.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = response.parse()
            assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSensorMaintenance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            id="SENSORMAINTENANCE-ID",
            activity="Activity Description",
            approver="approver",
            changer="changer",
            duration="128:16:52",
            eow_id="eowId",
            equip_status="FMC",
            id_sensor="idSensor",
            impacted_faces="impactedFaces",
            line_number="lineNumber",
            md_ops_cap="R",
            mw_ops_cap="G",
            origin="THIRD_PARTY_DATASOURCE",
            priority="low",
            recall="128:16:52",
            rel="rel",
            remark="Remarks",
            requestor="requestor",
            resource="resource",
            rev="rev",
            ss_ops_cap="Y",
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert sensor_maintenance is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            body_id="SENSORMAINTENANCE-ID",
            activity="Activity Description",
            approver="approver",
            changer="changer",
            duration="128:16:52",
            eow_id="eowId",
            equip_status="FMC",
            id_sensor="idSensor",
            impacted_faces="impactedFaces",
            line_number="lineNumber",
            md_ops_cap="R",
            mw_ops_cap="G",
            origin="THIRD_PARTY_DATASOURCE",
            priority="low",
            recall="128:16:52",
            rel="rel",
            remark="Remarks",
            requestor="requestor",
            resource="resource",
            rev="rev",
            ss_ops_cap="Y",
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert sensor_maintenance is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sensor_maintenance.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
                site_code="site01",
                source="Bluestaq",
                start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.list()
        assert_matches_type(AsyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert_matches_type(AsyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert_matches_type(AsyncOffsetPage[SensorMaintenanceListResponse], sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.delete(
            "id",
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert sensor_maintenance is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor_maintenance.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.count()
        assert_matches_type(str, sensor_maintenance, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.count(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sensor_maintenance, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert_matches_type(str, sensor_maintenance, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert_matches_type(str, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_method_create_bulk_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "id": "SENSORMAINTENANCE-ID",
                    "activity": "Activity Description",
                    "approver": "approver",
                    "changer": "changer",
                    "duration": "128:16:52",
                    "eow_id": "eowId",
                    "equip_status": "FMC",
                    "id_sensor": "idSensor",
                    "impacted_faces": "impactedFaces",
                    "line_number": "lineNumber",
                    "md_ops_cap": "R",
                    "mw_ops_cap": "G",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "priority": "low",
                    "recall": "128:16:52",
                    "rel": "rel",
                    "remark": "Remarks",
                    "requestor": "requestor",
                    "resource": "resource",
                    "rev": "rev",
                    "ss_ops_cap": "Y",
                }
            ],
            origin="origin",
            source="source",
        )
        assert sensor_maintenance is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert sensor_maintenance is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "site_code": "site01",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_current(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.current()
        assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_method_current_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.current(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_raw_response_current(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.current()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_streaming_response_current(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.current() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert_matches_type(SensorMaintenanceCurrentResponse, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.get(
            id="id",
        )
        assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert_matches_type(SensorMaintenanceGetResponse, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor_maintenance.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.queryhelp()
        assert sensor_maintenance is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert sensor_maintenance is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert sensor_maintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.tuple(
            columns="columns",
        )
        assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_maintenance = await async_client.sensor_maintenance.tuple(
            columns="columns",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_maintenance.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_maintenance = await response.parse()
        assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_maintenance.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_maintenance = await response.parse()
            assert_matches_type(SensorMaintenanceTupleResponse, sensor_maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True
