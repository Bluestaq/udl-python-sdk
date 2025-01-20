# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    DiplomaticClearanceListResponse,
    DiplomaticClearanceTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.air_operations import DiplomaticclearanceFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiplomaticClearance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
            id="id",
            apacs_id="apacsId",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            diplomatic_clearance_details=[
                {
                    "action": "action",
                    "alt_country_code": "altCountryCode",
                    "clearance_id": "clearanceId",
                    "clearance_remark": "clearanceRemark",
                    "cleared_call_sign": "clearedCallSign",
                    "country_code": "countryCode",
                    "country_name": "countryName",
                    "entry_net": "2019-12-27T18:11:19.117Z",
                    "entry_point": "entryPoint",
                    "exit_nlt": "2019-12-27T18:11:19.117Z",
                    "exit_point": "exitPoint",
                    "external_clearance_id": "externalClearanceId",
                    "id_sortie": "idSortie",
                    "leg_num": 0,
                    "profile": "profile",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "routeString",
                    "sequence_num": 0,
                    "status": "status",
                    "valid_desc": "validDesc",
                    "valid_end_time": "2019-12-27T18:11:19.117Z",
                    "valid_start_time": "2019-12-27T18:11:19.117Z",
                    "window_remark": "windowRemark",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "text": "text",
                    "user": "user",
                }
            ],
            dip_worksheet_name="dipWorksheetName",
            doc_deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_worksheet_id="externalWorksheetId",
            origin="origin",
            orig_network="origNetwork",
            source_dl="sourceDL",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.retrieve(
            "id",
        )
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
            id_2="id",
            apacs_id="apacsId",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            diplomatic_clearance_details=[
                {
                    "action": "action",
                    "alt_country_code": "altCountryCode",
                    "clearance_id": "clearanceId",
                    "clearance_remark": "clearanceRemark",
                    "cleared_call_sign": "clearedCallSign",
                    "country_code": "countryCode",
                    "country_name": "countryName",
                    "entry_net": "2019-12-27T18:11:19.117Z",
                    "entry_point": "entryPoint",
                    "exit_nlt": "2019-12-27T18:11:19.117Z",
                    "exit_point": "exitPoint",
                    "external_clearance_id": "externalClearanceId",
                    "id_sortie": "idSortie",
                    "leg_num": 0,
                    "profile": "profile",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "routeString",
                    "sequence_num": 0,
                    "status": "status",
                    "valid_desc": "validDesc",
                    "valid_end_time": "2019-12-27T18:11:19.117Z",
                    "valid_start_time": "2019-12-27T18:11:19.117Z",
                    "window_remark": "windowRemark",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "text": "text",
                    "user": "user",
                }
            ],
            dip_worksheet_name="dipWorksheetName",
            doc_deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_worksheet_id="externalWorksheetId",
            origin="origin",
            orig_network="origNetwork",
            source_dl="sourceDL",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.diplomatic_clearance.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                id_mission="idMission",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.diplomatic_clearance.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DiplomaticClearanceListResponse, diplomatic_clearance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert_matches_type(DiplomaticClearanceListResponse, diplomatic_clearance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.diplomatic_clearance.with_streaming_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert_matches_type(DiplomaticClearanceListResponse, diplomatic_clearance, path=["response"])

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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "first_dep_date": "2019-12-27T18:11:19.117Z",
                    "id_mission": "idMission",
                    "source": "source",
                }
            ],
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.diplomatic_clearance.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "first_dep_date": "2019-12-27T18:11:19.117Z",
                    "id_mission": "idMission",
                    "source": "source",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "first_dep_date": "2019-12-27T18:11:19.117Z",
                    "id_mission": "idMission",
                    "source": "source",
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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
            id="id",
            apacs_id="apacsId",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            diplomatic_clearance_details=[
                {
                    "action": "action",
                    "alt_country_code": "altCountryCode",
                    "clearance_id": "clearanceId",
                    "clearance_remark": "clearanceRemark",
                    "cleared_call_sign": "clearedCallSign",
                    "country_code": "countryCode",
                    "country_name": "countryName",
                    "entry_net": "2019-12-27T18:11:19.117Z",
                    "entry_point": "entryPoint",
                    "exit_nlt": "2019-12-27T18:11:19.117Z",
                    "exit_point": "exitPoint",
                    "external_clearance_id": "externalClearanceId",
                    "id_sortie": "idSortie",
                    "leg_num": 0,
                    "profile": "profile",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "routeString",
                    "sequence_num": 0,
                    "status": "status",
                    "valid_desc": "validDesc",
                    "valid_end_time": "2019-12-27T18:11:19.117Z",
                    "valid_start_time": "2019-12-27T18:11:19.117Z",
                    "window_remark": "windowRemark",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "text": "text",
                    "user": "user",
                }
            ],
            dip_worksheet_name="dipWorksheetName",
            doc_deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_worksheet_id="externalWorksheetId",
            origin="origin",
            orig_network="origNetwork",
            source_dl="sourceDL",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.retrieve(
            "id",
        )
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert_matches_type(DiplomaticclearanceFull, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
            id_2="id",
            apacs_id="apacsId",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            diplomatic_clearance_details=[
                {
                    "action": "action",
                    "alt_country_code": "altCountryCode",
                    "clearance_id": "clearanceId",
                    "clearance_remark": "clearanceRemark",
                    "cleared_call_sign": "clearedCallSign",
                    "country_code": "countryCode",
                    "country_name": "countryName",
                    "entry_net": "2019-12-27T18:11:19.117Z",
                    "entry_point": "entryPoint",
                    "exit_nlt": "2019-12-27T18:11:19.117Z",
                    "exit_point": "exitPoint",
                    "external_clearance_id": "externalClearanceId",
                    "id_sortie": "idSortie",
                    "leg_num": 0,
                    "profile": "profile",
                    "req_icao": True,
                    "req_point": True,
                    "route_string": "routeString",
                    "sequence_num": 0,
                    "status": "status",
                    "valid_desc": "validDesc",
                    "valid_end_time": "2019-12-27T18:11:19.117Z",
                    "valid_start_time": "2019-12-27T18:11:19.117Z",
                    "window_remark": "windowRemark",
                }
            ],
            diplomatic_clearance_remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "text": "text",
                    "user": "user",
                }
            ],
            dip_worksheet_name="dipWorksheetName",
            doc_deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_worksheet_id="externalWorksheetId",
            origin="origin",
            orig_network="origNetwork",
            source_dl="sourceDL",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            id_mission="idMission",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.diplomatic_clearance.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                id_mission="idMission",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.diplomatic_clearance.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DiplomaticClearanceListResponse, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert_matches_type(DiplomaticClearanceListResponse, diplomatic_clearance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diplomatic_clearance.with_streaming_response.list(
            first_dep_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert_matches_type(DiplomaticClearanceListResponse, diplomatic_clearance, path=["response"])

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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "first_dep_date": "2019-12-27T18:11:19.117Z",
                    "id_mission": "idMission",
                    "source": "source",
                }
            ],
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diplomatic_clearance.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "first_dep_date": "2019-12-27T18:11:19.117Z",
                    "id_mission": "idMission",
                    "source": "source",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "first_dep_date": "2019-12-27T18:11:19.117Z",
                    "id_mission": "idMission",
                    "source": "source",
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
