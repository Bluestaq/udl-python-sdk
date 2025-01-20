# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrackroutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        trackroute = client.filedrop.trackroutes.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert trackroute is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        trackroute = client.filedrop.trackroutes.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
            id="id",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "altitudeSequenceId",
                    "lower_altitude": 0,
                    "upper_altitude": 0,
                }
            ],
            apn_setting="apnSetting",
            apx_beacon_code="apxBeaconCode",
            artcc_message="artccMessage",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            creating_org="creatingOrg",
            direction="direction",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_id="externalId",
            last_used_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location_track_id="locationTrackId",
            origin="origin",
            orig_network="origNetwork",
            poc=[
                {
                    "office": "office",
                    "phone": "phone",
                    "poc_name": "pocName",
                    "poc_org": "pocOrg",
                    "poc_sequence_id": 0,
                    "poc_type_name": "pocTypeName",
                    "rank": "rank",
                    "remark": "remark",
                    "username": "username",
                }
            ],
            pri_freq=0,
            receiver_tanker_ch_code="receiverTankerCHCode",
            region_code="regionCode",
            region_name="regionName",
            review_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            route_points=[
                {
                    "alt_country_code": "altCountryCode",
                    "country_code": "countryCode",
                    "dafif_pt": True,
                    "mag_dec": 0,
                    "navaid": "navaid",
                    "navaid_length": 0,
                    "navaid_type": "navaidType",
                    "pt_lat": 0,
                    "pt_lon": 0,
                    "pt_sequence_id": 0,
                    "pt_type_code": "ptTypeCode",
                    "pt_type_name": "ptTypeName",
                    "waypoint_name": "waypointName",
                }
            ],
            scheduler_org_name="schedulerOrgName",
            scheduler_org_unit="schedulerOrgUnit",
            sec_freq=0,
            short_name="shortName",
            sic="sic",
            source_dl="sourceDL",
            track_id="trackId",
            track_name="trackName",
            type_code="typeCode",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.trackroutes.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.trackroutes.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTrackroutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.filedrop.trackroutes.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert trackroute is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.filedrop.trackroutes.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
            id="id",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "altitudeSequenceId",
                    "lower_altitude": 0,
                    "upper_altitude": 0,
                }
            ],
            apn_setting="apnSetting",
            apx_beacon_code="apxBeaconCode",
            artcc_message="artccMessage",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            creating_org="creatingOrg",
            direction="direction",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_id="externalId",
            last_used_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location_track_id="locationTrackId",
            origin="origin",
            orig_network="origNetwork",
            poc=[
                {
                    "office": "office",
                    "phone": "phone",
                    "poc_name": "pocName",
                    "poc_org": "pocOrg",
                    "poc_sequence_id": 0,
                    "poc_type_name": "pocTypeName",
                    "rank": "rank",
                    "remark": "remark",
                    "username": "username",
                }
            ],
            pri_freq=0,
            receiver_tanker_ch_code="receiverTankerCHCode",
            region_code="regionCode",
            region_name="regionName",
            review_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            route_points=[
                {
                    "alt_country_code": "altCountryCode",
                    "country_code": "countryCode",
                    "dafif_pt": True,
                    "mag_dec": 0,
                    "navaid": "navaid",
                    "navaid_length": 0,
                    "navaid_type": "navaidType",
                    "pt_lat": 0,
                    "pt_lon": 0,
                    "pt_sequence_id": 0,
                    "pt_type_code": "ptTypeCode",
                    "pt_type_name": "ptTypeName",
                    "waypoint_name": "waypointName",
                }
            ],
            scheduler_org_name="schedulerOrgName",
            scheduler_org_unit="schedulerOrgUnit",
            sec_freq=0,
            short_name="shortName",
            sic="sic",
            source_dl="sourceDL",
            track_id="trackId",
            track_name="trackName",
            type_code="typeCode",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.trackroutes.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.trackroutes.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True
