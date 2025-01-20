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
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert ephemeris is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris = client.filedrop.ephemeris.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
            id="id",
            b_dot=0,
            cent_body="centBody",
            comments="comments",
            cov_reference_frame="covReferenceFrame",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            descriptor="descriptor",
            drag_model="dragModel",
            edr=0,
            ephemeris_list=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "ts": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "xpos": 0,
                    "xvel": 0,
                    "ypos": 0,
                    "yvel": 0,
                    "zpos": 0,
                    "zvel": 0,
                    "id": "id",
                    "cov": [0],
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "es_id": "esId",
                    "id_on_orbit": "idOnOrbit",
                    "origin": "origin",
                    "orig_object_id": "origObjectId",
                    "xaccel": 0,
                    "yaccel": 0,
                    "zaccel": 0,
                }
            ],
            filename="filename",
            geopotential_model="geopotentialModel",
            has_accel=True,
            has_cov=True,
            has_mnvr=True,
            id_maneuvers=["string"],
            id_on_orbit="idOnOrbit",
            id_state_vector="idStateVector",
            integrator="integrator",
            interpolation="interpolation",
            interpolation_degree=0,
            lunar_solar=True,
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            pedigree="pedigree",
            reference_frame="referenceFrame",
            sat_no=0,
            solid_earth_tides=True,
            step_size=0,
            tags=["string"],
            transaction_id="transactionId",
            usable_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            usable_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ephemeris is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.ephemeris.with_raw_response.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris = response.parse()
        assert ephemeris is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.ephemeris.with_streaming_response.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
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
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert ephemeris is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris = await async_client.filedrop.ephemeris.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
            id="id",
            b_dot=0,
            cent_body="centBody",
            comments="comments",
            cov_reference_frame="covReferenceFrame",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            descriptor="descriptor",
            drag_model="dragModel",
            edr=0,
            ephemeris_list=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "ts": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "xpos": 0,
                    "xvel": 0,
                    "ypos": 0,
                    "yvel": 0,
                    "zpos": 0,
                    "zvel": 0,
                    "id": "id",
                    "cov": [0],
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "es_id": "esId",
                    "id_on_orbit": "idOnOrbit",
                    "origin": "origin",
                    "orig_object_id": "origObjectId",
                    "xaccel": 0,
                    "yaccel": 0,
                    "zaccel": 0,
                }
            ],
            filename="filename",
            geopotential_model="geopotentialModel",
            has_accel=True,
            has_cov=True,
            has_mnvr=True,
            id_maneuvers=["string"],
            id_on_orbit="idOnOrbit",
            id_state_vector="idStateVector",
            integrator="integrator",
            interpolation="interpolation",
            interpolation_degree=0,
            lunar_solar=True,
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            pedigree="pedigree",
            reference_frame="referenceFrame",
            sat_no=0,
            solid_earth_tides=True,
            step_size=0,
            tags=["string"],
            transaction_id="transactionId",
            usable_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            usable_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ephemeris is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.ephemeris.with_raw_response.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris = await response.parse()
        assert ephemeris is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.ephemeris.with_streaming_response.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris = await response.parse()
            assert ephemeris is None

        assert cast(Any, response.is_closed) is True
