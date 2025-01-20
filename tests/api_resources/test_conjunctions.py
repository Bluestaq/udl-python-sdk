# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ConjunctionFull,
    ConjunctionListResponse,
    ConjunctionTupleResponse,
    ConjunctionGetHistoryResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConjunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.retrieve(
            "id",
        )
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionFull, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conjunctions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionListResponse, conjunction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionListResponse, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionListResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(str, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_filedrop(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_filedrop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_create_filedrop(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.create_filedrop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_create_filedrop(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.create_filedrop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_udl(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert conjunction is None

    @parametrize
    def test_method_create_udl_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            convert_pos_vel=True,
            id="id",
            ccir="ccir",
            cd_ao_m1=0,
            cd_ao_m2=0,
            collision_prob=0,
            collision_prob_method="collisionProbMethod",
            comments="comments",
            concern_notes="concernNotes",
            cr_ao_m1=0,
            cr_ao_m2=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            descriptor="descriptor",
            ephem_name1="ephemName1",
            ephem_name2="ephemName2",
            es_id1="esId1",
            es_id2="esId2",
            event_id="eventId",
            id_on_orbit1="idOnOrbit1",
            id_on_orbit2="idOnOrbit2",
            id_state_vector1="idStateVector1",
            id_state_vector2="idStateVector2",
            large_cov_warning=True,
            large_rel_pos_warning=True,
            last_ob_time1=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_ob_time2=parse_datetime("2019-12-27T18:11:19.117Z"),
            message_for="messageFor",
            message_id="messageId",
            miss_distance=0,
            orig_id_on_orbit1="origIdOnOrbit1",
            orig_id_on_orbit2="origIdOnOrbit2",
            origin="origin",
            originator="originator",
            orig_network="origNetwork",
            owner_contacted=True,
            penetration_level_sigma=0,
            raw_file_uri="rawFileURI",
            rel_pos_n=0,
            rel_pos_r=0,
            rel_pos_t=0,
            rel_vel_mag=0,
            rel_vel_n=0,
            rel_vel_r=0,
            rel_vel_t=0,
            sat_no1=0,
            sat_no2=0,
            screen_entry_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            screen_exit_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            screen_volume_x=0,
            screen_volume_y=0,
            screen_volume_z=0,
            small_cov_warning=True,
            small_rel_vel_warning=True,
            state_dept_notified=True,
            state_vector1={
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
            state_vector2={
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
            tags=["string"],
            thrust_accel1=0,
            thrust_accel2=0,
            transaction_id="transactionId",
            type="type",
            uvw_warn=True,
            vol_entry_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            vol_exit_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            vol_shape="volShape",
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_create_udl(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_create_udl(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_history(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    def test_method_get_history_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    def test_raw_response_get_history(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_get_history(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.queryhelp()
        assert conjunction is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConjunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.retrieve(
            "id",
        )
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionFull, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conjunctions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionListResponse, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionListResponse, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionListResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(str, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_filedrop(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_filedrop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_create_filedrop(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.create_filedrop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_create_filedrop(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.create_filedrop(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_udl(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert conjunction is None

    @parametrize
    async def test_method_create_udl_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            convert_pos_vel=True,
            id="id",
            ccir="ccir",
            cd_ao_m1=0,
            cd_ao_m2=0,
            collision_prob=0,
            collision_prob_method="collisionProbMethod",
            comments="comments",
            concern_notes="concernNotes",
            cr_ao_m1=0,
            cr_ao_m2=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            descriptor="descriptor",
            ephem_name1="ephemName1",
            ephem_name2="ephemName2",
            es_id1="esId1",
            es_id2="esId2",
            event_id="eventId",
            id_on_orbit1="idOnOrbit1",
            id_on_orbit2="idOnOrbit2",
            id_state_vector1="idStateVector1",
            id_state_vector2="idStateVector2",
            large_cov_warning=True,
            large_rel_pos_warning=True,
            last_ob_time1=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_ob_time2=parse_datetime("2019-12-27T18:11:19.117Z"),
            message_for="messageFor",
            message_id="messageId",
            miss_distance=0,
            orig_id_on_orbit1="origIdOnOrbit1",
            orig_id_on_orbit2="origIdOnOrbit2",
            origin="origin",
            originator="originator",
            orig_network="origNetwork",
            owner_contacted=True,
            penetration_level_sigma=0,
            raw_file_uri="rawFileURI",
            rel_pos_n=0,
            rel_pos_r=0,
            rel_pos_t=0,
            rel_vel_mag=0,
            rel_vel_n=0,
            rel_vel_r=0,
            rel_vel_t=0,
            sat_no1=0,
            sat_no2=0,
            screen_entry_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            screen_exit_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            screen_volume_x=0,
            screen_volume_y=0,
            screen_volume_z=0,
            small_cov_warning=True,
            small_rel_vel_warning=True,
            state_dept_notified=True,
            state_vector1={
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
            state_vector2={
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
            tags=["string"],
            thrust_accel1=0,
            thrust_accel2=0,
            transaction_id="transactionId",
            type="type",
            uvw_warn=True,
            vol_entry_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            vol_exit_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            vol_shape="volShape",
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_create_udl(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_create_udl(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.create_udl(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "tca": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    async def test_method_get_history_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_get_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_get_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.queryhelp()
        assert conjunction is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True
