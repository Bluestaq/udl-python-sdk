# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    CollectRequestListResponse,
    CollectRequestTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.shared import CollectRequestFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollectRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )
        assert collect_request is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            id="id",
            alt=0,
            arg_of_perigee=0,
            az=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            customer="customer",
            dec=0,
            duration=0,
            dwell_id="dwellId",
            eccentricity=0,
            el=0,
            elset={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "epoch": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": "source",
                "agom": 0,
                "algorithm": "algorithm",
                "apogee": 0,
                "arg_of_perigee": 0,
                "ballistic_coeff": 0,
                "b_star": 0,
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "descriptor": "descriptor",
                "eccentricity": 0,
                "ephem_type": 0,
                "id_elset": "idElset",
                "id_on_orbit": "idOnOrbit",
                "id_orbit_determination": "idOrbitDetermination",
                "inclination": 0,
                "line1": "line1",
                "line2": "line2",
                "mean_anomaly": 0,
                "mean_motion": 0,
                "mean_motion_d_dot": 0,
                "mean_motion_dot": 0,
                "origin": "origin",
                "orig_network": "origNetwork",
                "orig_object_id": "origObjectId",
                "perigee": 0,
                "period": 0,
                "raan": 0,
                "raw_file_uri": "rawFileURI",
                "rev_no": 0,
                "sat_no": 0,
                "semi_major_axis": 0,
                "sourced_data": ["string"],
                "sourced_data_types": ["string"],
                "source_dl": "sourceDL",
                "tags": ["string"],
                "transaction_id": "transactionId",
                "uct": True,
            },
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            es_id="esId",
            extent_az=0,
            extent_el=0,
            extent_range=0,
            external_id="externalId",
            frame_rate=0,
            freq=0,
            freq_max=0,
            freq_min=0,
            id_elset="idElset",
            id_manifold="idManifold",
            id_on_orbit="idOnOrbit",
            id_parent_req="idParentReq",
            id_plan="idPlan",
            id_sensor="idSensor",
            id_state_vector="idStateVector",
            inclination=0,
            integration_time=0,
            iron=0,
            irradiance=0,
            lat=0,
            lon=0,
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            msg_type="msgType",
            notes="notes",
            num_frames=0,
            num_obs=0,
            num_tracks=0,
            ob_type="obType",
            orbit_regime="orbitRegime",
            orient_angle=0,
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            plan_index=0,
            polarization="polarization",
            priority="priority",
            ra=0,
            raan=0,
            range=0,
            rcs=0,
            rcs_max=0,
            rcs_min=0,
            reflectance=0,
            sat_no=0,
            scenario="scenario",
            semi_major_axis=0,
            spectral_model="spectralModel",
            srch_inc=0,
            srch_pattern="srchPattern",
            state_vector={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "epoch": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": "source",
                "actual_od_span": 0,
                "algorithm": "algorithm",
                "alt1_reference_frame": "alt1ReferenceFrame",
                "alt2_reference_frame": "alt2ReferenceFrame",
                "area": 0,
                "b_dot": 0,
                "cm_offset": 0,
                "cov": [0],
                "cov_method": "covMethod",
                "cov_reference_frame": "covReferenceFrame",
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "descriptor": "descriptor",
                "drag_area": 0,
                "drag_coeff": 0,
                "drag_model": "dragModel",
                "edr": 0,
                "eq_cov": [0],
                "error_control": 0,
                "fixed_step": True,
                "geopotential_model": "geopotentialModel",
                "iau1980_terms": 0,
                "id_on_orbit": "idOnOrbit",
                "id_orbit_determination": "idOrbitDetermination",
                "id_state_vector": "idStateVector",
                "integrator_mode": "integratorMode",
                "in_track_thrust": True,
                "last_ob_end": "2019-12-27T18:11:19.117Z",
                "last_ob_start": "2019-12-27T18:11:19.117Z",
                "leap_second_time": "2019-12-27T18:11:19.117Z",
                "lunar_solar": True,
                "mass": 0,
                "obs_available": 0,
                "obs_used": 0,
                "origin": "origin",
                "orig_network": "origNetwork",
                "orig_object_id": "origObjectId",
                "partials": "partials",
                "pedigree": "pedigree",
                "polar_motion_x": 0,
                "polar_motion_y": 0,
                "pos_unc": 0,
                "raw_file_uri": "rawFileURI",
                "rec_od_span": 0,
                "reference_frame": "referenceFrame",
                "residuals_acc": 0,
                "rev_no": 0,
                "rms": 0,
                "sat_no": 0,
                "sigma_pos_uvw": [0],
                "sigma_vel_uvw": [0],
                "solar_flux_ap_avg": 0,
                "solar_flux_f10": 0,
                "solar_flux_f10_avg": 0,
                "solar_rad_press": True,
                "solar_rad_press_coeff": 0,
                "solid_earth_tides": True,
                "sourced_data": ["string"],
                "sourced_data_types": ["string"],
                "source_dl": "sourceDL",
                "srp_area": 0,
                "step_mode": "stepMode",
                "step_size": 0,
                "step_size_selection": "stepSizeSelection",
                "tags": ["string"],
                "tai_utc": 0,
                "thrust_accel": 0,
                "tracks_avail": 0,
                "tracks_used": 0,
                "transaction_id": "transactionId",
                "uct": True,
                "ut1_rate": 0,
                "ut1_utc": 0,
                "vel_unc": 0,
                "xaccel": 0,
                "xpos": 0,
                "xpos_alt1": 0,
                "xpos_alt2": 0,
                "xvel": 0,
                "xvel_alt1": 0,
                "xvel_alt2": 0,
                "yaccel": 0,
                "ypos": 0,
                "ypos_alt1": 0,
                "ypos_alt2": 0,
                "yvel": 0,
                "yvel_alt1": 0,
                "yvel_alt2": 0,
                "zaccel": 0,
                "zpos": 0,
                "zpos_alt1": 0,
                "zpos_alt2": 0,
                "zvel": 0,
                "zvel_alt1": 0,
                "zvel_alt2": 0,
            },
            stop_alt=0,
            stop_lat=0,
            stop_lon=0,
            suffix="suffix",
            tags=["string"],
            target_size=0,
            task_category=0,
            task_group="taskGroup",
            task_id="taskId",
            true_anomoly=0,
            uct_follow_up=True,
            vis_mag=0,
            vis_mag_max=0,
            vis_mag_min=0,
            x_angle=0,
            y_angle=0,
        )
        assert collect_request is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.retrieve(
            "id",
        )
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(CollectRequestFull, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collect_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectRequestListResponse, collect_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(CollectRequestListResponse, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(CollectRequestListResponse, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(str, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "type": "type",
                }
            ],
        )
        assert collect_request is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.query_help()
        assert collect_request is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollectRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )
        assert collect_request is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            id="id",
            alt=0,
            arg_of_perigee=0,
            az=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            customer="customer",
            dec=0,
            duration=0,
            dwell_id="dwellId",
            eccentricity=0,
            el=0,
            elset={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "epoch": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": "source",
                "agom": 0,
                "algorithm": "algorithm",
                "apogee": 0,
                "arg_of_perigee": 0,
                "ballistic_coeff": 0,
                "b_star": 0,
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "descriptor": "descriptor",
                "eccentricity": 0,
                "ephem_type": 0,
                "id_elset": "idElset",
                "id_on_orbit": "idOnOrbit",
                "id_orbit_determination": "idOrbitDetermination",
                "inclination": 0,
                "line1": "line1",
                "line2": "line2",
                "mean_anomaly": 0,
                "mean_motion": 0,
                "mean_motion_d_dot": 0,
                "mean_motion_dot": 0,
                "origin": "origin",
                "orig_network": "origNetwork",
                "orig_object_id": "origObjectId",
                "perigee": 0,
                "period": 0,
                "raan": 0,
                "raw_file_uri": "rawFileURI",
                "rev_no": 0,
                "sat_no": 0,
                "semi_major_axis": 0,
                "sourced_data": ["string"],
                "sourced_data_types": ["string"],
                "source_dl": "sourceDL",
                "tags": ["string"],
                "transaction_id": "transactionId",
                "uct": True,
            },
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            es_id="esId",
            extent_az=0,
            extent_el=0,
            extent_range=0,
            external_id="externalId",
            frame_rate=0,
            freq=0,
            freq_max=0,
            freq_min=0,
            id_elset="idElset",
            id_manifold="idManifold",
            id_on_orbit="idOnOrbit",
            id_parent_req="idParentReq",
            id_plan="idPlan",
            id_sensor="idSensor",
            id_state_vector="idStateVector",
            inclination=0,
            integration_time=0,
            iron=0,
            irradiance=0,
            lat=0,
            lon=0,
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            msg_type="msgType",
            notes="notes",
            num_frames=0,
            num_obs=0,
            num_tracks=0,
            ob_type="obType",
            orbit_regime="orbitRegime",
            orient_angle=0,
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            plan_index=0,
            polarization="polarization",
            priority="priority",
            ra=0,
            raan=0,
            range=0,
            rcs=0,
            rcs_max=0,
            rcs_min=0,
            reflectance=0,
            sat_no=0,
            scenario="scenario",
            semi_major_axis=0,
            spectral_model="spectralModel",
            srch_inc=0,
            srch_pattern="srchPattern",
            state_vector={
                "classification_marking": "classificationMarking",
                "data_mode": "dataMode",
                "epoch": parse_datetime("2019-12-27T18:11:19.117Z"),
                "source": "source",
                "actual_od_span": 0,
                "algorithm": "algorithm",
                "alt1_reference_frame": "alt1ReferenceFrame",
                "alt2_reference_frame": "alt2ReferenceFrame",
                "area": 0,
                "b_dot": 0,
                "cm_offset": 0,
                "cov": [0],
                "cov_method": "covMethod",
                "cov_reference_frame": "covReferenceFrame",
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "descriptor": "descriptor",
                "drag_area": 0,
                "drag_coeff": 0,
                "drag_model": "dragModel",
                "edr": 0,
                "eq_cov": [0],
                "error_control": 0,
                "fixed_step": True,
                "geopotential_model": "geopotentialModel",
                "iau1980_terms": 0,
                "id_on_orbit": "idOnOrbit",
                "id_orbit_determination": "idOrbitDetermination",
                "id_state_vector": "idStateVector",
                "integrator_mode": "integratorMode",
                "in_track_thrust": True,
                "last_ob_end": "2019-12-27T18:11:19.117Z",
                "last_ob_start": "2019-12-27T18:11:19.117Z",
                "leap_second_time": "2019-12-27T18:11:19.117Z",
                "lunar_solar": True,
                "mass": 0,
                "obs_available": 0,
                "obs_used": 0,
                "origin": "origin",
                "orig_network": "origNetwork",
                "orig_object_id": "origObjectId",
                "partials": "partials",
                "pedigree": "pedigree",
                "polar_motion_x": 0,
                "polar_motion_y": 0,
                "pos_unc": 0,
                "raw_file_uri": "rawFileURI",
                "rec_od_span": 0,
                "reference_frame": "referenceFrame",
                "residuals_acc": 0,
                "rev_no": 0,
                "rms": 0,
                "sat_no": 0,
                "sigma_pos_uvw": [0],
                "sigma_vel_uvw": [0],
                "solar_flux_ap_avg": 0,
                "solar_flux_f10": 0,
                "solar_flux_f10_avg": 0,
                "solar_rad_press": True,
                "solar_rad_press_coeff": 0,
                "solid_earth_tides": True,
                "sourced_data": ["string"],
                "sourced_data_types": ["string"],
                "source_dl": "sourceDL",
                "srp_area": 0,
                "step_mode": "stepMode",
                "step_size": 0,
                "step_size_selection": "stepSizeSelection",
                "tags": ["string"],
                "tai_utc": 0,
                "thrust_accel": 0,
                "tracks_avail": 0,
                "tracks_used": 0,
                "transaction_id": "transactionId",
                "uct": True,
                "ut1_rate": 0,
                "ut1_utc": 0,
                "vel_unc": 0,
                "xaccel": 0,
                "xpos": 0,
                "xpos_alt1": 0,
                "xpos_alt2": 0,
                "xvel": 0,
                "xvel_alt1": 0,
                "xvel_alt2": 0,
                "yaccel": 0,
                "ypos": 0,
                "ypos_alt1": 0,
                "ypos_alt2": 0,
                "yvel": 0,
                "yvel_alt1": 0,
                "yvel_alt2": 0,
                "zaccel": 0,
                "zpos": 0,
                "zpos_alt1": 0,
                "zpos_alt2": 0,
                "zvel": 0,
                "zvel_alt1": 0,
                "zvel_alt2": 0,
            },
            stop_alt=0,
            stop_lat=0,
            stop_lon=0,
            suffix="suffix",
            tags=["string"],
            target_size=0,
            task_category=0,
            task_group="taskGroup",
            task_id="taskId",
            true_anomoly=0,
            uct_follow_up=True,
            vis_mag=0,
            vis_mag_max=0,
            vis_mag_min=0,
            x_angle=0,
            y_angle=0,
        )
        assert collect_request is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.retrieve(
            "id",
        )
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(CollectRequestFull, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collect_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectRequestListResponse, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(CollectRequestListResponse, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(CollectRequestListResponse, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(str, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "type": "type",
                }
            ],
        )
        assert collect_request is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.query_help()
        assert collect_request is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True
