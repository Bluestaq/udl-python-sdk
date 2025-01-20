# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AttitudeSetListResponse,
    AttitudeSetTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttitudeSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )
        assert attitude_set is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            id="id",
            as_ref=["string"],
            attitude_list=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "ts": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "id": "id",
                    "as_id": "asId",
                    "coning_angle": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "declination": 0,
                    "id_on_orbit": "idOnOrbit",
                    "motion_type": "motionType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "orig_object_id": "origObjectId",
                    "prec_period": 0,
                    "q1": 0,
                    "q1_dot": 0,
                    "q2": 0,
                    "q2_dot": 0,
                    "q3": 0,
                    "q3_dot": 0,
                    "qc": 0,
                    "qc_dot": 0,
                    "ra": 0,
                    "sat_no": 0,
                    "spin_period": 0,
                    "x_angle": [0],
                    "x_rate": [0],
                    "y_angle": [0],
                    "y_rate": [0],
                    "z_angle": [0],
                    "z_rate": [0],
                }
            ],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            es_id="esId",
            euler_rot_seq="eulerRotSeq",
            id_on_orbit="idOnOrbit",
            id_sensor="idSensor",
            interpolator="interpolator",
            interpolator_degree=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            prec_angle_init=0,
            sat_no=0,
            spin_angle_init=0,
            step_size=0,
        )
        assert attitude_set is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert attitude_set is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AttitudeSetListResponse, attitude_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert_matches_type(AttitudeSetListResponse, attitude_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert_matches_type(AttitudeSetListResponse, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, attitude_set, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert_matches_type(str, attitude_set, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert_matches_type(str, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_filedrop(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )
        assert attitude_set is None

    @parametrize
    def test_method_create_filedrop_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            id="id",
            as_ref=["string"],
            attitude_list=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "ts": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "id": "id",
                    "as_id": "asId",
                    "coning_angle": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "declination": 0,
                    "id_on_orbit": "idOnOrbit",
                    "motion_type": "motionType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "orig_object_id": "origObjectId",
                    "prec_period": 0,
                    "q1": 0,
                    "q1_dot": 0,
                    "q2": 0,
                    "q2_dot": 0,
                    "q3": 0,
                    "q3_dot": 0,
                    "qc": 0,
                    "qc_dot": 0,
                    "ra": 0,
                    "sat_no": 0,
                    "spin_period": 0,
                    "x_angle": [0],
                    "x_rate": [0],
                    "y_angle": [0],
                    "y_rate": [0],
                    "z_angle": [0],
                    "z_rate": [0],
                }
            ],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            es_id="esId",
            euler_rot_seq="eulerRotSeq",
            id_on_orbit="idOnOrbit",
            id_sensor="idSensor",
            interpolator="interpolator",
            interpolator_degree=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            prec_angle_init=0,
            sat_no=0,
            spin_angle_init=0,
            step_size=0,
        )
        assert attitude_set is None

    @parametrize
    def test_raw_response_create_filedrop(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert attitude_set is None

    @parametrize
    def test_streaming_response_create_filedrop(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.query_help()
        assert attitude_set is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert attitude_set is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAttitudeSets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )
        assert attitude_set is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            id="id",
            as_ref=["string"],
            attitude_list=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "ts": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "id": "id",
                    "as_id": "asId",
                    "coning_angle": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "declination": 0,
                    "id_on_orbit": "idOnOrbit",
                    "motion_type": "motionType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "orig_object_id": "origObjectId",
                    "prec_period": 0,
                    "q1": 0,
                    "q1_dot": 0,
                    "q2": 0,
                    "q2_dot": 0,
                    "q3": 0,
                    "q3_dot": 0,
                    "qc": 0,
                    "qc_dot": 0,
                    "ra": 0,
                    "sat_no": 0,
                    "spin_period": 0,
                    "x_angle": [0],
                    "x_rate": [0],
                    "y_angle": [0],
                    "y_rate": [0],
                    "z_angle": [0],
                    "z_rate": [0],
                }
            ],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            es_id="esId",
            euler_rot_seq="eulerRotSeq",
            id_on_orbit="idOnOrbit",
            id_sensor="idSensor",
            interpolator="interpolator",
            interpolator_degree=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            prec_angle_init=0,
            sat_no=0,
            spin_angle_init=0,
            step_size=0,
        )
        assert attitude_set is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert attitude_set is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AttitudeSetListResponse, attitude_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert_matches_type(AttitudeSetListResponse, attitude_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert_matches_type(AttitudeSetListResponse, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, attitude_set, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert_matches_type(str, attitude_set, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert_matches_type(str, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_filedrop(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )
        assert attitude_set is None

    @parametrize
    async def test_method_create_filedrop_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            id="id",
            as_ref=["string"],
            attitude_list=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "ts": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "id": "id",
                    "as_id": "asId",
                    "coning_angle": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "declination": 0,
                    "id_on_orbit": "idOnOrbit",
                    "motion_type": "motionType",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "orig_object_id": "origObjectId",
                    "prec_period": 0,
                    "q1": 0,
                    "q1_dot": 0,
                    "q2": 0,
                    "q2_dot": 0,
                    "q3": 0,
                    "q3_dot": 0,
                    "qc": 0,
                    "qc_dot": 0,
                    "ra": 0,
                    "sat_no": 0,
                    "spin_period": 0,
                    "x_angle": [0],
                    "x_rate": [0],
                    "y_angle": [0],
                    "y_rate": [0],
                    "z_angle": [0],
                    "z_rate": [0],
                }
            ],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            es_id="esId",
            euler_rot_seq="eulerRotSeq",
            id_on_orbit="idOnOrbit",
            id_sensor="idSensor",
            interpolator="interpolator",
            interpolator_degree=0,
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            prec_angle_init=0,
            sat_no=0,
            spin_angle_init=0,
            step_size=0,
        )
        assert attitude_set is None

    @parametrize
    async def test_raw_response_create_filedrop(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert attitude_set is None

    @parametrize
    async def test_streaming_response_create_filedrop(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.create_filedrop(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            frame1="frame1",
            frame2="frame2",
            num_points=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.query_help()
        assert attitude_set is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert attitude_set is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True
