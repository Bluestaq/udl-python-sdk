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
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        trackroute = client.filedrop.trackroutes.create(
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.trackroutes.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.trackroutes.with_streaming_response.create(
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
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
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.filedrop.trackroutes.create(
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.trackroutes.with_raw_response.create(
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.trackroutes.with_streaming_response.create(
            classification_marking="U",
            data_mode="REAL",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True
