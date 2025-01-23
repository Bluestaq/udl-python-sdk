# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEphemeris:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ephemeris = client.filedrop.ephemeris.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )
        assert ephemeris is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris = client.filedrop.ephemeris.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
            id="EPHEMERISSET-ID",
            b_dot=1.1,
            cent_body="Earth",
            comments="Example notes",
            cov_reference_frame="J2000",
            description="Example notes",
            descriptor="Example descriptor",
            drag_model="JAC70",
            edr=1.1,
            ephemeris_list=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "xpos": 1.1,
                    "xvel": 1.1,
                    "ypos": 1.1,
                    "yvel": 1.1,
                    "zpos": 1.1,
                    "zvel": 1.1,
                    "id": "EPHEMERIS-ID",
                    "cov": [0],
                    "created_at": "2018-01-01T16:00:00.123Z",
                    "created_by": "some.user",
                    "es_id": "ES-ID",
                    "id_on_orbit": "ONORBIT-ID",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "xaccel": 1.1,
                    "yaccel": 1.1,
                    "zaccel": 1.1,
                }
            ],
            filename="Example file name",
            geopotential_model="GEM-T3",
            has_accel=False,
            has_cov=False,
            has_mnvr=False,
            id_maneuvers=["EXAMPLE_ID1", "EXAMPLE_ID2"],
            id_on_orbit="ONORBIT-ID",
            id_state_vector="STATEVECTOR-ID",
            integrator="COWELL",
            interpolation="LINEAR",
            interpolation_degree=5,
            lunar_solar=False,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            pedigree="PROPAGATED",
            reference_frame="J2000",
            sat_no=2,
            solid_earth_tides=False,
            step_size=1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            usable_end_time=parse_datetime("2018-01-01T20:50:00.123456Z"),
            usable_start_time=parse_datetime("2018-01-01T16:10:00.123456Z"),
        )
        assert ephemeris is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.ephemeris.with_raw_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris = response.parse()
        assert ephemeris is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.ephemeris.with_streaming_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris = response.parse()
            assert ephemeris is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEphemeris:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris = await async_client.filedrop.ephemeris.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )
        assert ephemeris is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris = await async_client.filedrop.ephemeris.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
            id="EPHEMERISSET-ID",
            b_dot=1.1,
            cent_body="Earth",
            comments="Example notes",
            cov_reference_frame="J2000",
            description="Example notes",
            descriptor="Example descriptor",
            drag_model="JAC70",
            edr=1.1,
            ephemeris_list=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "xpos": 1.1,
                    "xvel": 1.1,
                    "ypos": 1.1,
                    "yvel": 1.1,
                    "zpos": 1.1,
                    "zvel": 1.1,
                    "id": "EPHEMERIS-ID",
                    "cov": [0],
                    "created_at": "2018-01-01T16:00:00.123Z",
                    "created_by": "some.user",
                    "es_id": "ES-ID",
                    "id_on_orbit": "ONORBIT-ID",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "xaccel": 1.1,
                    "yaccel": 1.1,
                    "zaccel": 1.1,
                }
            ],
            filename="Example file name",
            geopotential_model="GEM-T3",
            has_accel=False,
            has_cov=False,
            has_mnvr=False,
            id_maneuvers=["EXAMPLE_ID1", "EXAMPLE_ID2"],
            id_on_orbit="ONORBIT-ID",
            id_state_vector="STATEVECTOR-ID",
            integrator="COWELL",
            interpolation="LINEAR",
            interpolation_degree=5,
            lunar_solar=False,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            pedigree="PROPAGATED",
            reference_frame="J2000",
            sat_no=2,
            solid_earth_tides=False,
            step_size=1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            usable_end_time=parse_datetime("2018-01-01T20:50:00.123456Z"),
            usable_start_time=parse_datetime("2018-01-01T16:10:00.123456Z"),
        )
        assert ephemeris is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.ephemeris.with_raw_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris = await response.parse()
        assert ephemeris is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.ephemeris.with_streaming_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="REAL",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris = await response.parse()
            assert ephemeris is None

        assert cast(Any, response.is_closed) is True
