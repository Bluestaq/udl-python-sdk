# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.observations import (
    PassiveRadarObservationGetResponse,
    PassiveRadarObservationListResponse,
    PassiveRadarObservationTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPassiveRadarObservation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
        )
        assert passive_radar_observation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
            id="bdcacfb0-3c47-4bd0-9d6c-9fa7d2c4fbb0",
            accel=1.23,
            accel_unc=0.1,
            alt=478.056378,
            azimuth=134.5,
            azimuth_bias=0.123,
            azimuth_rate=0.5,
            azimuth_unc=0.5,
            bistatic_range=754.8212,
            bistatic_range_accel=1.23,
            bistatic_range_accel_unc=0.1,
            bistatic_range_bias=2.34,
            bistatic_range_rate=-0.30222,
            bistatic_range_rate_unc=0.123,
            bistatic_range_unc=5.1,
            coning=60.1,
            coning_unc=0.5,
            declination=10.23,
            delay=0.00505820232809312,
            delay_bias=0.00000123,
            delay_unc=0.0000031,
            descriptor="Descriptor",
            doppler=-101.781641000597,
            doppler_unc=0.2,
            elevation=76.1,
            elevation_bias=0.123,
            elevation_rate=0.5,
            elevation_unc=0.5,
            ext_observation_id="26892",
            id_rf_emitter="RED_CLIFFS_3ABCRN",
            id_sensor="OCULUSA",
            id_sensor_ref_receiver="OculusRef1",
            lat=-35.1181763996856,
            lon=139.613567052763,
            ob_position="FIRST",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            orthogonal_rcs=10.23,
            orthogonal_rcs_unc=1.23,
            ra=1.23,
            rcs=100.23,
            rcs_unc=1.23,
            sat_no=40699,
            snr=17.292053,
            tags=["TAG1", "TAG2"],
            task_id="TASK-ID",
            timing_bias=1.23,
            tof=0.00592856674135648,
            tof_bias=0.00000123,
            tof_unc=0.0000031,
            track_id="12212",
            transaction_id="TRANSACTION-ID",
            uct=False,
            xvel=1.23,
            yvel=3.21,
            zvel=3.12,
        )
        assert passive_radar_observation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert passive_radar_observation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            SyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            SyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert_matches_type(
            SyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert_matches_type(
                SyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, passive_radar_observation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, passive_radar_observation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert_matches_type(str, passive_radar_observation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert_matches_type(str, passive_radar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert passive_radar_observation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert passive_radar_observation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_file_create(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert passive_radar_observation is None

    @parametrize
    def test_raw_response_file_create(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert passive_radar_observation is None

    @parametrize
    def test_streaming_response_file_create(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.get(
            id="id",
        )
        assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.observations.passive_radar_observation.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.queryhelp()
        assert passive_radar_observation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert passive_radar_observation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        passive_radar_observation = client.observations.passive_radar_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.observations.passive_radar_observation.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = response.parse()
        assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.observations.passive_radar_observation.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = response.parse()
            assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPassiveRadarObservation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
        )
        assert passive_radar_observation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
            id="bdcacfb0-3c47-4bd0-9d6c-9fa7d2c4fbb0",
            accel=1.23,
            accel_unc=0.1,
            alt=478.056378,
            azimuth=134.5,
            azimuth_bias=0.123,
            azimuth_rate=0.5,
            azimuth_unc=0.5,
            bistatic_range=754.8212,
            bistatic_range_accel=1.23,
            bistatic_range_accel_unc=0.1,
            bistatic_range_bias=2.34,
            bistatic_range_rate=-0.30222,
            bistatic_range_rate_unc=0.123,
            bistatic_range_unc=5.1,
            coning=60.1,
            coning_unc=0.5,
            declination=10.23,
            delay=0.00505820232809312,
            delay_bias=0.00000123,
            delay_unc=0.0000031,
            descriptor="Descriptor",
            doppler=-101.781641000597,
            doppler_unc=0.2,
            elevation=76.1,
            elevation_bias=0.123,
            elevation_rate=0.5,
            elevation_unc=0.5,
            ext_observation_id="26892",
            id_rf_emitter="RED_CLIFFS_3ABCRN",
            id_sensor="OCULUSA",
            id_sensor_ref_receiver="OculusRef1",
            lat=-35.1181763996856,
            lon=139.613567052763,
            ob_position="FIRST",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            orthogonal_rcs=10.23,
            orthogonal_rcs_unc=1.23,
            ra=1.23,
            rcs=100.23,
            rcs_unc=1.23,
            sat_no=40699,
            snr=17.292053,
            tags=["TAG1", "TAG2"],
            task_id="TASK-ID",
            timing_bias=1.23,
            tof=0.00592856674135648,
            tof_bias=0.00000123,
            tof_unc=0.0000031,
            track_id="12212",
            transaction_id="TRANSACTION-ID",
            uct=False,
            xvel=1.23,
            yvel=3.21,
            zvel=3.12,
        )
        assert passive_radar_observation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert passive_radar_observation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2023-01-24T23:35:26.518152Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            AsyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            AsyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[PassiveRadarObservationListResponse], passive_radar_observation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, passive_radar_observation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, passive_radar_observation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert_matches_type(str, passive_radar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert_matches_type(str, passive_radar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert passive_radar_observation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert passive_radar_observation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert passive_radar_observation is None

    @parametrize
    async def test_raw_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert passive_radar_observation is None

    @parametrize
    async def test_streaming_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2023-01-24T23:35:26.518152Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.get(
            id="id",
        )
        assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert_matches_type(PassiveRadarObservationGetResponse, passive_radar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.observations.passive_radar_observation.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.queryhelp()
        assert passive_radar_observation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert passive_radar_observation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert passive_radar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        passive_radar_observation = await async_client.observations.passive_radar_observation.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.passive_radar_observation.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        passive_radar_observation = await response.parse()
        assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.passive_radar_observation.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            passive_radar_observation = await response.parse()
            assert_matches_type(PassiveRadarObservationTupleResponse, passive_radar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True
