# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EphemerisSet,
    EphemerisSetListResponse,
    EphemerisSetTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEphemerisSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert ephemeris_set is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.create(
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
        assert ephemeris_set is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.create(
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
        ephemeris_set = response.parse()
        assert ephemeris_set is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.create(
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

            ephemeris_set = response.parse()
            assert ephemeris_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.retrieve(
            "id",
        )
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ephemeris_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.list()
        assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.list(
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.count()
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.count(
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert_matches_type(str, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_retrieve(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ephemeris_set = client.ephemeris_sets.file_retrieve(
            "id",
        )
        assert ephemeris_set.is_closed
        assert ephemeris_set.json() == {"foo": "bar"}
        assert cast(Any, ephemeris_set.is_closed) is True
        assert isinstance(ephemeris_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_retrieve(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        ephemeris_set = client.ephemeris_sets.with_raw_response.file_retrieve(
            "id",
        )

        assert ephemeris_set.is_closed is True
        assert ephemeris_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert ephemeris_set.json() == {"foo": "bar"}
        assert isinstance(ephemeris_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_retrieve(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.ephemeris_sets.with_streaming_response.file_retrieve(
            "id",
        ) as ephemeris_set:
            assert not ephemeris_set.is_closed
            assert ephemeris_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert ephemeris_set.json() == {"foo": "bar"}
            assert cast(Any, ephemeris_set.is_closed) is True
            assert isinstance(ephemeris_set, StreamedBinaryAPIResponse)

        assert cast(Any, ephemeris_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ephemeris_sets.with_raw_response.file_retrieve(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.queryhelp()
        assert ephemeris_set is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert ephemeris_set is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert ephemeris_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.tuple(
            columns="columns",
        )
        assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.tuple(
            columns="columns",
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEphemerisSets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.create(
            category="category",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_points=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            type="type",
        )
        assert ephemeris_set is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.create(
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
        assert ephemeris_set is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.create(
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
        ephemeris_set = await response.parse()
        assert ephemeris_set is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.create(
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

            ephemeris_set = await response.parse()
            assert ephemeris_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.retrieve(
            "id",
        )
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ephemeris_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.list()
        assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.list(
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert_matches_type(EphemerisSetListResponse, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.count()
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.count(
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert_matches_type(str, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_retrieve(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ephemeris_set = await async_client.ephemeris_sets.file_retrieve(
            "id",
        )
        assert ephemeris_set.is_closed
        assert await ephemeris_set.json() == {"foo": "bar"}
        assert cast(Any, ephemeris_set.is_closed) is True
        assert isinstance(ephemeris_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_retrieve(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        ephemeris_set = await async_client.ephemeris_sets.with_raw_response.file_retrieve(
            "id",
        )

        assert ephemeris_set.is_closed is True
        assert ephemeris_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await ephemeris_set.json() == {"foo": "bar"}
        assert isinstance(ephemeris_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_retrieve(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.ephemeris_sets.with_streaming_response.file_retrieve(
            "id",
        ) as ephemeris_set:
            assert not ephemeris_set.is_closed
            assert ephemeris_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await ephemeris_set.json() == {"foo": "bar"}
            assert cast(Any, ephemeris_set.is_closed) is True
            assert isinstance(ephemeris_set, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, ephemeris_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ephemeris_sets.with_raw_response.file_retrieve(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.queryhelp()
        assert ephemeris_set is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert ephemeris_set is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert ephemeris_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.tuple(
            columns="columns",
        )
        assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.tuple(
            columns="columns",
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert_matches_type(EphemerisSetTupleResponse, ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True
