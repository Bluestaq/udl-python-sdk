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
    EphemerisSetAbridged,
    EphemerisSetTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEphemerisSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )
        assert ephemeris_set is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
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
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "xpos": 1.1,
                    "xvel": 1.1,
                    "ypos": 1.1,
                    "yvel": 1.1,
                    "zpos": 1.1,
                    "zvel": 1.1,
                    "id": "EPHEMERIS-ID",
                    "cov": [1.1, 2.4, 3.8, 4.2, 5.5, 6],
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
        assert ephemeris_set is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert ephemeris_set is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert ephemeris_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.retrieve(
            id="id",
        )
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.retrieve(
            id="id",
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
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.list()
        assert_matches_type(SyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.list(
            first_result=0,
            max_results=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = response.parse()
        assert_matches_type(SyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = response.parse()
            assert_matches_type(SyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.count()
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        ephemeris_set = client.ephemeris_sets.count(
            first_result=0,
            max_results=0,
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
            id="id",
        )
        assert ephemeris_set.is_closed
        assert ephemeris_set.json() == {"foo": "bar"}
        assert cast(Any, ephemeris_set.is_closed) is True
        assert isinstance(ephemeris_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_retrieve_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ephemeris_set = client.ephemeris_sets.file_retrieve(
            id="id",
            first_result=0,
            max_results=0,
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
            id="id",
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
            id="id",
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
                id="",
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
            first_result=0,
            max_results=0,
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
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )
        assert ephemeris_set is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
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
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "xpos": 1.1,
                    "xvel": 1.1,
                    "ypos": 1.1,
                    "yvel": 1.1,
                    "zpos": 1.1,
                    "zvel": 1.1,
                    "id": "EPHEMERIS-ID",
                    "cov": [1.1, 2.4, 3.8, 4.2, 5.5, 6],
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
        assert ephemeris_set is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert ephemeris_set is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.create(
            category="ANALYST",
            classification_marking="U",
            data_mode="TEST",
            num_points=1,
            point_end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            point_start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            type="LAUNCH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert ephemeris_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.retrieve(
            id="id",
        )
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert_matches_type(EphemerisSet, ephemeris_set, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.retrieve(
            id="id",
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
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.list()
        assert_matches_type(AsyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.list(
            first_result=0,
            max_results=0,
            point_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            point_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeris_set = await response.parse()
        assert_matches_type(AsyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeris_set = await response.parse()
            assert_matches_type(AsyncOffsetPage[EphemerisSetAbridged], ephemeris_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.count()
        assert_matches_type(str, ephemeris_set, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ephemeris_set = await async_client.ephemeris_sets.count(
            first_result=0,
            max_results=0,
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
            id="id",
        )
        assert ephemeris_set.is_closed
        assert await ephemeris_set.json() == {"foo": "bar"}
        assert cast(Any, ephemeris_set.is_closed) is True
        assert isinstance(ephemeris_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_retrieve_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/ephemerisset/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ephemeris_set = await async_client.ephemeris_sets.file_retrieve(
            id="id",
            first_result=0,
            max_results=0,
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
            id="id",
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
            id="id",
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
                id="",
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
            first_result=0,
            max_results=0,
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
