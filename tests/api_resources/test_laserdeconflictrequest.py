# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaserdeconflictrequestGetResponse,
    LaserdeconflictrequestListResponse,
    LaserdeconflictrequestTupleResponse,
    LaserdeconflictrequestQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaserdeconflictrequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )
        assert laserdeconflictrequest is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            centerline_azimuth=20.3,
            centerline_elevation=19.434,
            default_cha=2.5,
            enable_dss=True,
            fixed_points=[
                {
                    "latitude": -10.18,
                    "longitude": -179.98,
                    "height": -18.13,
                }
            ],
            geopotential_model="WGS84",
            laser_deconflict_targets=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "026dd511-8ba5-47d3-9909-836149f87686",
                    "azimuth": 27.91,
                    "azimuth_end": 90.5,
                    "azimuth_increment": 1.5,
                    "azimuth_start": 60.5,
                    "centerline_azimuth": 11.02,
                    "centerline_elevation": 1.68,
                    "declination": 10.23,
                    "elevation": 17.09,
                    "elevation_end": 88.05,
                    "elevation_increment": 0.5,
                    "elevation_start": 67.05,
                    "fixed_points": [
                        {
                            "latitude": -10.18,
                            "longitude": -179.98,
                            "height": -18.13,
                        }
                    ],
                    "id_laser_deconflict_request": "026dd511-8ba5-47d3-9909-836149f87686",
                    "length_centerline": 369.79,
                    "length_left_right": 20.23,
                    "length_up_down": 28.67,
                    "maximum_height": 0.5,
                    "minimum_height": 0.25,
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "ra": 11.93,
                    "solar_system_body": "MARS",
                    "star_number": 3791,
                    "target_number": 100,
                    "target_object_no": 46852,
                }
            ],
            laser_system_name="HEL-1",
            length_centerline=79.35,
            length_left_right=56.23,
            length_up_down=22.6,
            maximum_height=440.3,
            minimum_height=0.5,
            mission_name="USSF LP 18-1 Test Laser",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            platform_location_name="Vandenberg",
            platform_location_type="FIXED_POINT",
            program_id="performance_test_llh-sat",
            propagator="GP",
            protect_list=[1234, 5678],
            sat_no=46852,
            source_enabled=False,
            status="REQUESTED",
            tags=["TAG1", "TAG2"],
            target_enabled=True,
            target_type="BOX_CENTERPOINT_LINE",
            transaction_id="TRANSACTION-ID",
            treat_earth_as="VICTIM",
            use_field_of_regard=True,
            victim_enabled=True,
        )
        assert laserdeconflictrequest is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert laserdeconflictrequest is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert laserdeconflictrequest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            SyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            SyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert_matches_type(
            SyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert_matches_type(
                SyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert_matches_type(str, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert_matches_type(str, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.get(
            id="id",
        )
        assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.laserdeconflictrequest.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.queryhelp()
        assert_matches_type(LaserdeconflictrequestQueryhelpResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert_matches_type(LaserdeconflictrequestQueryhelpResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert_matches_type(LaserdeconflictrequestQueryhelpResponse, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )
        assert laserdeconflictrequest is None

    @parametrize
    def test_method_unvalidated_publish_with_all_params(self, client: Unifieddatalibrary) -> None:
        laserdeconflictrequest = client.laserdeconflictrequest.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            centerline_azimuth=20.3,
            centerline_elevation=19.434,
            default_cha=2.5,
            enable_dss=True,
            fixed_points=[
                {
                    "latitude": -10.18,
                    "longitude": -179.98,
                    "height": -18.13,
                }
            ],
            geopotential_model="WGS84",
            laser_deconflict_targets=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "026dd511-8ba5-47d3-9909-836149f87686",
                    "azimuth": 27.91,
                    "azimuth_end": 90.5,
                    "azimuth_increment": 1.5,
                    "azimuth_start": 60.5,
                    "centerline_azimuth": 11.02,
                    "centerline_elevation": 1.68,
                    "declination": 10.23,
                    "elevation": 17.09,
                    "elevation_end": 88.05,
                    "elevation_increment": 0.5,
                    "elevation_start": 67.05,
                    "fixed_points": [
                        {
                            "latitude": -10.18,
                            "longitude": -179.98,
                            "height": -18.13,
                        }
                    ],
                    "id_laser_deconflict_request": "026dd511-8ba5-47d3-9909-836149f87686",
                    "length_centerline": 369.79,
                    "length_left_right": 20.23,
                    "length_up_down": 28.67,
                    "maximum_height": 0.5,
                    "minimum_height": 0.25,
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "ra": 11.93,
                    "solar_system_body": "MARS",
                    "star_number": 3791,
                    "target_number": 100,
                    "target_object_no": 46852,
                }
            ],
            laser_system_name="HEL-1",
            length_centerline=79.35,
            length_left_right=56.23,
            length_up_down=22.6,
            maximum_height=440.3,
            minimum_height=0.5,
            mission_name="USSF LP 18-1 Test Laser",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            platform_location_name="Vandenberg",
            platform_location_type="FIXED_POINT",
            program_id="performance_test_llh-sat",
            propagator="GP",
            protect_list=[1234, 5678],
            sat_no=46852,
            source_enabled=False,
            status="REQUESTED",
            tags=["TAG1", "TAG2"],
            target_enabled=True,
            target_type="BOX_CENTERPOINT_LINE",
            transaction_id="TRANSACTION-ID",
            treat_earth_as="VICTIM",
            use_field_of_regard=True,
            victim_enabled=True,
        )
        assert laserdeconflictrequest is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.laserdeconflictrequest.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = response.parse()
        assert laserdeconflictrequest is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.laserdeconflictrequest.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = response.parse()
            assert laserdeconflictrequest is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLaserdeconflictrequest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )
        assert laserdeconflictrequest is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            centerline_azimuth=20.3,
            centerline_elevation=19.434,
            default_cha=2.5,
            enable_dss=True,
            fixed_points=[
                {
                    "latitude": -10.18,
                    "longitude": -179.98,
                    "height": -18.13,
                }
            ],
            geopotential_model="WGS84",
            laser_deconflict_targets=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "026dd511-8ba5-47d3-9909-836149f87686",
                    "azimuth": 27.91,
                    "azimuth_end": 90.5,
                    "azimuth_increment": 1.5,
                    "azimuth_start": 60.5,
                    "centerline_azimuth": 11.02,
                    "centerline_elevation": 1.68,
                    "declination": 10.23,
                    "elevation": 17.09,
                    "elevation_end": 88.05,
                    "elevation_increment": 0.5,
                    "elevation_start": 67.05,
                    "fixed_points": [
                        {
                            "latitude": -10.18,
                            "longitude": -179.98,
                            "height": -18.13,
                        }
                    ],
                    "id_laser_deconflict_request": "026dd511-8ba5-47d3-9909-836149f87686",
                    "length_centerline": 369.79,
                    "length_left_right": 20.23,
                    "length_up_down": 28.67,
                    "maximum_height": 0.5,
                    "minimum_height": 0.25,
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "ra": 11.93,
                    "solar_system_body": "MARS",
                    "star_number": 3791,
                    "target_number": 100,
                    "target_object_no": 46852,
                }
            ],
            laser_system_name="HEL-1",
            length_centerline=79.35,
            length_left_right=56.23,
            length_up_down=22.6,
            maximum_height=440.3,
            minimum_height=0.5,
            mission_name="USSF LP 18-1 Test Laser",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            platform_location_name="Vandenberg",
            platform_location_type="FIXED_POINT",
            program_id="performance_test_llh-sat",
            propagator="GP",
            protect_list=[1234, 5678],
            sat_no=46852,
            source_enabled=False,
            status="REQUESTED",
            tags=["TAG1", "TAG2"],
            target_enabled=True,
            target_type="BOX_CENTERPOINT_LINE",
            transaction_id="TRANSACTION-ID",
            treat_earth_as="VICTIM",
            use_field_of_regard=True,
            victim_enabled=True,
        )
        assert laserdeconflictrequest is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert laserdeconflictrequest is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert laserdeconflictrequest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            AsyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            AsyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.list(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[LaserdeconflictrequestListResponse], laserdeconflictrequest, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert_matches_type(str, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.count(
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert_matches_type(str, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.get(
            id="id",
        )
        assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert_matches_type(LaserdeconflictrequestGetResponse, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.laserdeconflictrequest.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.queryhelp()
        assert_matches_type(LaserdeconflictrequestQueryhelpResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert_matches_type(LaserdeconflictrequestQueryhelpResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert_matches_type(LaserdeconflictrequestQueryhelpResponse, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.tuple(
            columns="columns",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert_matches_type(LaserdeconflictrequestTupleResponse, laserdeconflictrequest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )
        assert laserdeconflictrequest is None

    @parametrize
    async def test_method_unvalidated_publish_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        laserdeconflictrequest = await async_client.laserdeconflictrequest.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            centerline_azimuth=20.3,
            centerline_elevation=19.434,
            default_cha=2.5,
            enable_dss=True,
            fixed_points=[
                {
                    "latitude": -10.18,
                    "longitude": -179.98,
                    "height": -18.13,
                }
            ],
            geopotential_model="WGS84",
            laser_deconflict_targets=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "026dd511-8ba5-47d3-9909-836149f87686",
                    "azimuth": 27.91,
                    "azimuth_end": 90.5,
                    "azimuth_increment": 1.5,
                    "azimuth_start": 60.5,
                    "centerline_azimuth": 11.02,
                    "centerline_elevation": 1.68,
                    "declination": 10.23,
                    "elevation": 17.09,
                    "elevation_end": 88.05,
                    "elevation_increment": 0.5,
                    "elevation_start": 67.05,
                    "fixed_points": [
                        {
                            "latitude": -10.18,
                            "longitude": -179.98,
                            "height": -18.13,
                        }
                    ],
                    "id_laser_deconflict_request": "026dd511-8ba5-47d3-9909-836149f87686",
                    "length_centerline": 369.79,
                    "length_left_right": 20.23,
                    "length_up_down": 28.67,
                    "maximum_height": 0.5,
                    "minimum_height": 0.25,
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "ra": 11.93,
                    "solar_system_body": "MARS",
                    "star_number": 3791,
                    "target_number": 100,
                    "target_object_no": 46852,
                }
            ],
            laser_system_name="HEL-1",
            length_centerline=79.35,
            length_left_right=56.23,
            length_up_down=22.6,
            maximum_height=440.3,
            minimum_height=0.5,
            mission_name="USSF LP 18-1 Test Laser",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            platform_location_name="Vandenberg",
            platform_location_type="FIXED_POINT",
            program_id="performance_test_llh-sat",
            propagator="GP",
            protect_list=[1234, 5678],
            sat_no=46852,
            source_enabled=False,
            status="REQUESTED",
            tags=["TAG1", "TAG2"],
            target_enabled=True,
            target_type="BOX_CENTERPOINT_LINE",
            transaction_id="TRANSACTION-ID",
            treat_earth_as="VICTIM",
            use_field_of_regard=True,
            victim_enabled=True,
        )
        assert laserdeconflictrequest is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.laserdeconflictrequest.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        laserdeconflictrequest = await response.parse()
        assert laserdeconflictrequest is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.laserdeconflictrequest.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_date=parse_datetime("2023-07-20T00:00:00.123Z"),
            id_laser_emitters=["2346c0a0-585f-4232-af5d-93bad320fdc0", "4446c0a0-585f-4232-af5d-93bad320fbb1"],
            num_targets=25,
            request_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            request_ts=parse_datetime("2023-07-15T12:30:30.123Z"),
            source="Bluestaq",
            start_date=parse_datetime("2023-07-19T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            laserdeconflictrequest = await response.parse()
            assert laserdeconflictrequest is None

        assert cast(Any, response.is_closed) is True
