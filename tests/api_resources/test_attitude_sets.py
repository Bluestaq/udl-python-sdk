# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AttitudesetAbridged,
    AttitudeSetTupleResponse,
    AttitudeSetQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AttitudesetFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttitudeSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )
        assert attitude_set is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
            id="ATTITUDESET-ID",
            as_ref=["2ea97de6-4680-4767-a07e-35d16398ef60"],
            attitude_list=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-03-07T14:51:39.653043Z"),
                    "id": "ATTITUDEDATA-ID",
                    "as_id": "773c9887-e931-42eb-8155-f0fbd227b235",
                    "coning_angle": 0.1,
                    "declination": 0.799,
                    "motion_type": "PROSOL_MOTION",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "D6593",
                    "prec_period": 36.1,
                    "q1": 0.0312,
                    "q1_dot": 0.0043,
                    "q2": 0.7854,
                    "q2_dot": 0.06,
                    "q3": 0.3916,
                    "q3_dot": 0.499,
                    "qc": 0.4783,
                    "qc_dot": 0.011,
                    "ra": -173.75,
                    "sat_no": 41947,
                    "spin_period": 0.1,
                    "x_angle": [139.753],
                    "x_rate": [0.105],
                    "y_angle": [25.066],
                    "y_rate": [0.032],
                    "z_angle": [-53.368],
                    "z_rate": [0.022],
                }
            ],
            es_id="60f7a241-b7be-48d8-acf3-786670af53f9",
            euler_rot_seq="123",
            id_sensor="a7e99418-b6d6-29ab-e767-440a989cce26",
            interpolator="LINEAR",
            interpolator_degree=2,
            notes="Notes for this attitude set",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="D6593",
            orig_sensor_id="ORIGSENSOR-ID",
            prec_angle_init=30.5,
            sat_no=41947,
            spin_angle_init=25.5,
            step_size=60,
        )
        assert attitude_set is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert attitude_set is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.retrieve(
            id="id",
        )
        assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.attitude_sets.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert_matches_type(SyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert_matches_type(SyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, attitude_set, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.query_help()
        assert_matches_type(AttitudeSetQueryHelpResponse, attitude_set, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert_matches_type(AttitudeSetQueryHelpResponse, attitude_set, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert_matches_type(AttitudeSetQueryHelpResponse, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )
        assert attitude_set is None

    @parametrize
    def test_method_unvalidated_publish_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_set = client.attitude_sets.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
            id="ATTITUDESET-ID",
            as_ref=["2ea97de6-4680-4767-a07e-35d16398ef60"],
            attitude_list=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-03-07T14:51:39.653043Z"),
                    "id": "ATTITUDEDATA-ID",
                    "as_id": "773c9887-e931-42eb-8155-f0fbd227b235",
                    "coning_angle": 0.1,
                    "declination": 0.799,
                    "motion_type": "PROSOL_MOTION",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "D6593",
                    "prec_period": 36.1,
                    "q1": 0.0312,
                    "q1_dot": 0.0043,
                    "q2": 0.7854,
                    "q2_dot": 0.06,
                    "q3": 0.3916,
                    "q3_dot": 0.499,
                    "qc": 0.4783,
                    "qc_dot": 0.011,
                    "ra": -173.75,
                    "sat_no": 41947,
                    "spin_period": 0.1,
                    "x_angle": [139.753],
                    "x_rate": [0.105],
                    "y_angle": [25.066],
                    "y_rate": [0.032],
                    "z_angle": [-53.368],
                    "z_rate": [0.022],
                }
            ],
            es_id="60f7a241-b7be-48d8-acf3-786670af53f9",
            euler_rot_seq="123",
            id_sensor="a7e99418-b6d6-29ab-e767-440a989cce26",
            interpolator="LINEAR",
            interpolator_degree=2,
            notes="Notes for this attitude set",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="D6593",
            orig_sensor_id="ORIGSENSOR-ID",
            prec_angle_init=30.5,
            sat_no=41947,
            spin_angle_init=25.5,
            step_size=60,
        )
        assert attitude_set is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_sets.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = response.parse()
        assert attitude_set is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.attitude_sets.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAttitudeSets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )
        assert attitude_set is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
            id="ATTITUDESET-ID",
            as_ref=["2ea97de6-4680-4767-a07e-35d16398ef60"],
            attitude_list=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-03-07T14:51:39.653043Z"),
                    "id": "ATTITUDEDATA-ID",
                    "as_id": "773c9887-e931-42eb-8155-f0fbd227b235",
                    "coning_angle": 0.1,
                    "declination": 0.799,
                    "motion_type": "PROSOL_MOTION",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "D6593",
                    "prec_period": 36.1,
                    "q1": 0.0312,
                    "q1_dot": 0.0043,
                    "q2": 0.7854,
                    "q2_dot": 0.06,
                    "q3": 0.3916,
                    "q3_dot": 0.499,
                    "qc": 0.4783,
                    "qc_dot": 0.011,
                    "ra": -173.75,
                    "sat_no": 41947,
                    "spin_period": 0.1,
                    "x_angle": [139.753],
                    "x_rate": [0.105],
                    "y_angle": [25.066],
                    "y_rate": [0.032],
                    "z_angle": [-53.368],
                    "z_rate": [0.022],
                }
            ],
            es_id="60f7a241-b7be-48d8-acf3-786670af53f9",
            euler_rot_seq="123",
            id_sensor="a7e99418-b6d6-29ab-e767-440a989cce26",
            interpolator="LINEAR",
            interpolator_degree=2,
            notes="Notes for this attitude set",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="D6593",
            orig_sensor_id="ORIGSENSOR-ID",
            prec_angle_init=30.5,
            sat_no=41947,
            spin_angle_init=25.5,
            step_size=60,
        )
        assert attitude_set is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert attitude_set is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.retrieve(
            id="id",
        )
        assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert_matches_type(AttitudesetFull, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.attitude_sets.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert_matches_type(AsyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert_matches_type(AsyncOffsetPage[AttitudesetAbridged], attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, attitude_set, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.query_help()
        assert_matches_type(AttitudeSetQueryHelpResponse, attitude_set, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert_matches_type(AttitudeSetQueryHelpResponse, attitude_set, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert_matches_type(AttitudeSetQueryHelpResponse, attitude_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AttitudeSetTupleResponse, attitude_set, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
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

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )
        assert attitude_set is None

    @parametrize
    async def test_method_unvalidated_publish_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_set = await async_client.attitude_sets.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
            id="ATTITUDESET-ID",
            as_ref=["2ea97de6-4680-4767-a07e-35d16398ef60"],
            attitude_list=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-03-07T14:51:39.653043Z"),
                    "id": "ATTITUDEDATA-ID",
                    "as_id": "773c9887-e931-42eb-8155-f0fbd227b235",
                    "coning_angle": 0.1,
                    "declination": 0.799,
                    "motion_type": "PROSOL_MOTION",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "D6593",
                    "prec_period": 36.1,
                    "q1": 0.0312,
                    "q1_dot": 0.0043,
                    "q2": 0.7854,
                    "q2_dot": 0.06,
                    "q3": 0.3916,
                    "q3_dot": 0.499,
                    "qc": 0.4783,
                    "qc_dot": 0.011,
                    "ra": -173.75,
                    "sat_no": 41947,
                    "spin_period": 0.1,
                    "x_angle": [139.753],
                    "x_rate": [0.105],
                    "y_angle": [25.066],
                    "y_rate": [0.032],
                    "z_angle": [-53.368],
                    "z_rate": [0.022],
                }
            ],
            es_id="60f7a241-b7be-48d8-acf3-786670af53f9",
            euler_rot_seq="123",
            id_sensor="a7e99418-b6d6-29ab-e767-440a989cce26",
            interpolator="LINEAR",
            interpolator_degree=2,
            notes="Notes for this attitude set",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="D6593",
            orig_sensor_id="ORIGSENSOR-ID",
            prec_angle_init=30.5,
            sat_no=41947,
            spin_angle_init=25.5,
            step_size=60,
        )
        assert attitude_set is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_sets.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_set = await response.parse()
        assert attitude_set is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_sets.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2022-07-07T18:00:00.654321Z"),
            frame1="SCBODY",
            frame2="J2000",
            num_points=120,
            source="Bluestaq",
            start_time=parse_datetime("2022-07-07T16:00:00.123456Z"),
            type="AEM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_set = await response.parse()
            assert attitude_set is None

        assert cast(Any, response.is_closed) is True
