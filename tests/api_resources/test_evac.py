# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EvacListResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.shared import EvacFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvac:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert evac is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
            id="id",
            casualty_info=[
                {
                    "age": 0,
                    "allergy": [
                        {
                            "comments": "comments",
                            "type": "type",
                        }
                    ],
                    "blood_type": "bloodType",
                    "body_part": "bodyPart",
                    "burial_location": [0],
                    "call_sign": "callSign",
                    "care_provider_urn": "careProviderUrn",
                    "casualty_key": "casualtyKey",
                    "casualty_type": "casualtyType",
                    "collection_point": [0],
                    "comments": "comments",
                    "condition": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "contam_type": "contamType",
                    "disposition": "disposition",
                    "disposition_type": "dispositionType",
                    "etiology": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "evac_type": "evacType",
                    "gender": "gender",
                    "health_state": [
                        {
                            "health_state_code": "healthStateCode",
                            "med_conf_factor": 0,
                            "time": "2019-12-27T18:11:19.117Z",
                            "type": "type",
                        }
                    ],
                    "injury": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "last4_ssn": "last4SSN",
                    "medication": [
                        {
                            "admin_route": "adminRoute",
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "dose": "dose",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "name": "name",
                    "nationality": "nationality",
                    "occ_speciality": "occSpeciality",
                    "patient_identity": "patientIdentity",
                    "patient_status": "patientStatus",
                    "pay_grade": "payGrade",
                    "priority": "priority",
                    "report_gen": "reportGen",
                    "report_time": "2019-12-27T18:11:19.117Z",
                    "service": "service",
                    "spec_med_equip": ["string"],
                    "treatment": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "vital_sign_data": [
                        {
                            "med_conf_factor": 0,
                            "time": "2019-12-27T18:11:19.117Z",
                            "vital_sign": "vitalSign",
                            "vital_sign1": 0,
                            "vital_sign2": 0,
                        }
                    ],
                }
            ],
            ce=0,
            cntct_freq=0,
            comments="comments",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            enemy_data=[
                {
                    "dir_to_enemy": "dirToEnemy",
                    "friendlies_remarks": "friendliesRemarks",
                    "hlz_remarks": "hlzRemarks",
                    "hostile_fire_type": "hostileFireType",
                }
            ],
            id_weather_report="idWeatherReport",
            le=0,
            medevac_id="medevacId",
            medic_req=True,
            mission_type="missionType",
            num_ambulatory=0,
            num_casualties=0,
            num_kia=0,
            num_litter=0,
            num_wia=0,
            obstacles_remarks="obstaclesRemarks",
            origin="origin",
            orig_network="origNetwork",
            pickup_alt=0,
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            req_call_sign="reqCallSign",
            req_num="reqNum",
            terrain="terrain",
            terrain_remarks="terrainRemarks",
            zone_contr_call_sign="zoneContrCallSign",
            zone_hot=True,
            zone_marking="zoneMarking",
            zone_marking_color="zoneMarkingColor",
            zone_name="zoneName",
            zone_security="zoneSecurity",
        )
        assert evac is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.retrieve(
            "id",
        )
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert_matches_type(EvacFull, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evac.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EvacListResponse, evac, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert_matches_type(EvacListResponse, evac, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert_matches_type(EvacListResponse, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert_matches_type(str, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "pickup_lat": 0,
                    "pickup_lon": 0,
                    "req_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )
        assert evac is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "pickup_lat": 0,
                    "pickup_lon": 0,
                    "req_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "pickup_lat": 0,
                    "pickup_lon": 0,
                    "req_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.query_help()
        assert evac is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvac:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert evac is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
            id="id",
            casualty_info=[
                {
                    "age": 0,
                    "allergy": [
                        {
                            "comments": "comments",
                            "type": "type",
                        }
                    ],
                    "blood_type": "bloodType",
                    "body_part": "bodyPart",
                    "burial_location": [0],
                    "call_sign": "callSign",
                    "care_provider_urn": "careProviderUrn",
                    "casualty_key": "casualtyKey",
                    "casualty_type": "casualtyType",
                    "collection_point": [0],
                    "comments": "comments",
                    "condition": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "contam_type": "contamType",
                    "disposition": "disposition",
                    "disposition_type": "dispositionType",
                    "etiology": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "evac_type": "evacType",
                    "gender": "gender",
                    "health_state": [
                        {
                            "health_state_code": "healthStateCode",
                            "med_conf_factor": 0,
                            "time": "2019-12-27T18:11:19.117Z",
                            "type": "type",
                        }
                    ],
                    "injury": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "last4_ssn": "last4SSN",
                    "medication": [
                        {
                            "admin_route": "adminRoute",
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "dose": "dose",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "name": "name",
                    "nationality": "nationality",
                    "occ_speciality": "occSpeciality",
                    "patient_identity": "patientIdentity",
                    "patient_status": "patientStatus",
                    "pay_grade": "payGrade",
                    "priority": "priority",
                    "report_gen": "reportGen",
                    "report_time": "2019-12-27T18:11:19.117Z",
                    "service": "service",
                    "spec_med_equip": ["string"],
                    "treatment": [
                        {
                            "body_part": "bodyPart",
                            "comments": "comments",
                            "time": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "vital_sign_data": [
                        {
                            "med_conf_factor": 0,
                            "time": "2019-12-27T18:11:19.117Z",
                            "vital_sign": "vitalSign",
                            "vital_sign1": 0,
                            "vital_sign2": 0,
                        }
                    ],
                }
            ],
            ce=0,
            cntct_freq=0,
            comments="comments",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            enemy_data=[
                {
                    "dir_to_enemy": "dirToEnemy",
                    "friendlies_remarks": "friendliesRemarks",
                    "hlz_remarks": "hlzRemarks",
                    "hostile_fire_type": "hostileFireType",
                }
            ],
            id_weather_report="idWeatherReport",
            le=0,
            medevac_id="medevacId",
            medic_req=True,
            mission_type="missionType",
            num_ambulatory=0,
            num_casualties=0,
            num_kia=0,
            num_litter=0,
            num_wia=0,
            obstacles_remarks="obstaclesRemarks",
            origin="origin",
            orig_network="origNetwork",
            pickup_alt=0,
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            req_call_sign="reqCallSign",
            req_num="reqNum",
            terrain="terrain",
            terrain_remarks="terrainRemarks",
            zone_contr_call_sign="zoneContrCallSign",
            zone_hot=True,
            zone_marking="zoneMarking",
            zone_marking_color="zoneMarkingColor",
            zone_name="zoneName",
            zone_security="zoneSecurity",
        )
        assert evac is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            pickup_lat=0,
            pickup_lon=0,
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.retrieve(
            "id",
        )
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert_matches_type(EvacFull, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evac.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EvacListResponse, evac, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert_matches_type(EvacListResponse, evac, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert_matches_type(EvacListResponse, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert_matches_type(str, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "pickup_lat": 0,
                    "pickup_lon": 0,
                    "req_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )
        assert evac is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "pickup_lat": 0,
                    "pickup_lon": 0,
                    "req_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "pickup_lat": 0,
                    "pickup_lon": 0,
                    "req_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.query_help()
        assert evac is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True
