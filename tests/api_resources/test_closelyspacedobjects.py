# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    CloselyspacedobjectsAbridged,
    CloselyspacedobjectTupleResponse,
    CloselyspacedobjectRetrieveResponse,
    CloselyspacedobjectQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCloselyspacedobjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
        )
        assert closelyspacedobject is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            actor_sv_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            analysis_duration=60.1,
            analysis_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            comp_type="LONGITUDE",
            context_keys=["MsnID_DescLabel", "msnVer", "serVer"],
            context_values=["MissionID Descriptive Label text", "1", "001.9b"],
            cso_details=[
                {
                    "object_event": "MEAN",
                    "object_type": "DELTA",
                    "id": "026dd511-8ba5-47d3-9909-836149f87686",
                    "apogee": 1.1,
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_cso": "CSO-ID",
                    "inclination": 45.1,
                    "longitude": 45.1,
                    "perigee": 1.1,
                }
            ],
            delta_v_tol=0.123,
            duration_threshold=60.1,
            event_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_interval_coverage=22.3,
            ext_id="EXTERNAL-ID",
            hohmann_delta_v=0.012,
            id_actor_sv="ACTOR-SV-ID",
            id_on_orbit1="ONORBIT1-ID",
            id_on_orbit2="ONORBIT2-ID",
            id_target_sv="TARGET-SV-ID",
            inclination_delta_v=0.012,
            indication_source="Manually input",
            lon_tol=30.1,
            max_range=233.266,
            min_plane_sep_angle=30.1,
            min_plane_sep_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_range=0.5,
            min_range_analysis_duration=60.1,
            min_range_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            notes="FREE-TEXT",
            num_sub_intervals=0,
            orbit_align_del=12.3,
            orbit_plane_tol=1.23,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id1="ORIGONORBIT1-ID",
            orig_object_id2="ORIGONORBIT2-ID",
            range_threshold=0.1,
            range_tol=0.123,
            rel_pos=[0.12, 0.23, -0.12],
            rel_pos_mag=0.12,
            rel_speed_mag=1.23,
            rel_vel=[0.12, 0.23, -0.12],
            sat_no1=1,
            sat_no2=2,
            station_lim_lon_tol=12.5,
            target_sv_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            total_delta_v=2.46,
        )
        assert closelyspacedobject is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert closelyspacedobject is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert closelyspacedobject is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.retrieve(
            id="id",
        )
        assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.closelyspacedobjects.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert_matches_type(SyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert_matches_type(SyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, closelyspacedobject, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, closelyspacedobject, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert_matches_type(str, closelyspacedobject, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert_matches_type(str, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )
        assert closelyspacedobject is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert closelyspacedobject is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert closelyspacedobject is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.query_help()
        assert_matches_type(CloselyspacedobjectQueryHelpResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert_matches_type(CloselyspacedobjectQueryHelpResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert_matches_type(CloselyspacedobjectQueryHelpResponse, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        closelyspacedobject = client.closelyspacedobjects.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )
        assert closelyspacedobject is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.closelyspacedobjects.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = response.parse()
        assert closelyspacedobject is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.closelyspacedobjects.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = response.parse()
            assert closelyspacedobject is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCloselyspacedobjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
        )
        assert closelyspacedobject is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            actor_sv_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            analysis_duration=60.1,
            analysis_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            comp_type="LONGITUDE",
            context_keys=["MsnID_DescLabel", "msnVer", "serVer"],
            context_values=["MissionID Descriptive Label text", "1", "001.9b"],
            cso_details=[
                {
                    "object_event": "MEAN",
                    "object_type": "DELTA",
                    "id": "026dd511-8ba5-47d3-9909-836149f87686",
                    "apogee": 1.1,
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_cso": "CSO-ID",
                    "inclination": 45.1,
                    "longitude": 45.1,
                    "perigee": 1.1,
                }
            ],
            delta_v_tol=0.123,
            duration_threshold=60.1,
            event_end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_interval_coverage=22.3,
            ext_id="EXTERNAL-ID",
            hohmann_delta_v=0.012,
            id_actor_sv="ACTOR-SV-ID",
            id_on_orbit1="ONORBIT1-ID",
            id_on_orbit2="ONORBIT2-ID",
            id_target_sv="TARGET-SV-ID",
            inclination_delta_v=0.012,
            indication_source="Manually input",
            lon_tol=30.1,
            max_range=233.266,
            min_plane_sep_angle=30.1,
            min_plane_sep_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_range=0.5,
            min_range_analysis_duration=60.1,
            min_range_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            notes="FREE-TEXT",
            num_sub_intervals=0,
            orbit_align_del=12.3,
            orbit_plane_tol=1.23,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id1="ORIGONORBIT1-ID",
            orig_object_id2="ORIGONORBIT2-ID",
            range_threshold=0.1,
            range_tol=0.123,
            rel_pos=[0.12, 0.23, -0.12],
            rel_pos_mag=0.12,
            rel_speed_mag=1.23,
            rel_vel=[0.12, 0.23, -0.12],
            sat_no1=1,
            sat_no2=2,
            station_lim_lon_tol=12.5,
            target_sv_epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            total_delta_v=2.46,
        )
        assert closelyspacedobject is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert closelyspacedobject is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.create(
            classification_marking="U",
            cso_state="POSSIBLE",
            data_mode="TEST",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="RENDEZVOUS",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert closelyspacedobject is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.retrieve(
            id="id",
        )
        assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert_matches_type(CloselyspacedobjectRetrieveResponse, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.closelyspacedobjects.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert_matches_type(AsyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert_matches_type(AsyncOffsetPage[CloselyspacedobjectsAbridged], closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, closelyspacedobject, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, closelyspacedobject, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert_matches_type(str, closelyspacedobject, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert_matches_type(str, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )
        assert closelyspacedobject is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert closelyspacedobject is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert closelyspacedobject is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.query_help()
        assert_matches_type(CloselyspacedobjectQueryHelpResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert_matches_type(CloselyspacedobjectQueryHelpResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert_matches_type(CloselyspacedobjectQueryHelpResponse, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert_matches_type(CloselyspacedobjectTupleResponse, closelyspacedobject, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        closelyspacedobject = await async_client.closelyspacedobjects.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )
        assert closelyspacedobject is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.closelyspacedobjects.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closelyspacedobject = await response.parse()
        assert closelyspacedobject is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.closelyspacedobjects.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "cso_state": "POSSIBLE",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "event_type": "RENDEZVOUS",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closelyspacedobject = await response.parse()
            assert closelyspacedobject is None

        assert cast(Any, response.is_closed) is True
