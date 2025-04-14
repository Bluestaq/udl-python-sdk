# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SensormaintenanceListResponse,
    SensormaintenanceTupleResponse,
    SensormaintenanceCurrentResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.udl.sensormaintenance import SensormaintenanceFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensormaintenance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensormaintenance is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.create(
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
        assert sensormaintenance is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert sensormaintenance is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensormaintenance is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.update(
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
        assert sensormaintenance is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.update(
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
        sensormaintenance = response.parse()
        assert sensormaintenance is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.update(
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

            sensormaintenance = response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sensormaintenance.with_raw_response.update(
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
        sensormaintenance = client.sensormaintenance.list()
        assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.delete(
            "id",
        )
        assert sensormaintenance is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert sensormaintenance is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensormaintenance.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.count()
        assert_matches_type(str, sensormaintenance, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.count(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sensormaintenance, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert_matches_type(str, sensormaintenance, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert_matches_type(str, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.create_bulk(
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
        assert sensormaintenance is None

    @parametrize
    def test_method_create_bulk_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.create_bulk(
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
        assert sensormaintenance is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.create_bulk(
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
        sensormaintenance = response.parse()
        assert sensormaintenance is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.create_bulk(
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

            sensormaintenance = response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_current(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.current()
        assert_matches_type(SensormaintenanceCurrentResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_raw_response_current(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.current()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert_matches_type(SensormaintenanceCurrentResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_streaming_response_current(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.current() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert_matches_type(SensormaintenanceCurrentResponse, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.get(
            "id",
        )
        assert_matches_type(SensormaintenanceFull, sensormaintenance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert_matches_type(SensormaintenanceFull, sensormaintenance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert_matches_type(SensormaintenanceFull, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensormaintenance.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.queryhelp()
        assert sensormaintenance is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert sensormaintenance is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.tuple(
            columns="columns",
        )
        assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensormaintenance = client.sensormaintenance.tuple(
            columns="columns",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sensormaintenance.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = response.parse()
        assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sensormaintenance.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = response.parse()
            assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSensormaintenance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensormaintenance is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.create(
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
        assert sensormaintenance is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert sensormaintenance is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            site_code="site01",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
        )
        assert sensormaintenance is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.update(
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
        assert sensormaintenance is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.update(
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
        sensormaintenance = await response.parse()
        assert sensormaintenance is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.update(
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

            sensormaintenance = await response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sensormaintenance.with_raw_response.update(
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
        sensormaintenance = await async_client.sensormaintenance.list()
        assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert_matches_type(SensormaintenanceListResponse, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.delete(
            "id",
        )
        assert sensormaintenance is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert sensormaintenance is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensormaintenance.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.count()
        assert_matches_type(str, sensormaintenance, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.count(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sensormaintenance, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert_matches_type(str, sensormaintenance, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert_matches_type(str, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.create_bulk(
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
        assert sensormaintenance is None

    @parametrize
    async def test_method_create_bulk_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.create_bulk(
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
        assert sensormaintenance is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.create_bulk(
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
        sensormaintenance = await response.parse()
        assert sensormaintenance is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.create_bulk(
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

            sensormaintenance = await response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_current(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.current()
        assert_matches_type(SensormaintenanceCurrentResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_raw_response_current(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.current()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert_matches_type(SensormaintenanceCurrentResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_streaming_response_current(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.current() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert_matches_type(SensormaintenanceCurrentResponse, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.get(
            "id",
        )
        assert_matches_type(SensormaintenanceFull, sensormaintenance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert_matches_type(SensormaintenanceFull, sensormaintenance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert_matches_type(SensormaintenanceFull, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensormaintenance.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.queryhelp()
        assert sensormaintenance is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert sensormaintenance is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert sensormaintenance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.tuple(
            columns="columns",
        )
        assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensormaintenance = await async_client.sensormaintenance.tuple(
            columns="columns",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensormaintenance.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensormaintenance = await response.parse()
        assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensormaintenance.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensormaintenance = await response.parse()
            assert_matches_type(SensormaintenanceTupleResponse, sensormaintenance, path=["response"])

        assert cast(Any, response.is_closed) is True
