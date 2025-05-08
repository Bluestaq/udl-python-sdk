# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    NavigationalObstructionGetResponse,
    NavigationalObstructionListResponse,
    NavigationalObstructionTupleResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNavigationalObstruction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )
        assert navigational_obstruction is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            act_del_code="A",
            airac_cycle=2406,
            base_airac_cycle=2405,
            baseline_cutoff_date=parse_date("2024-04-23"),
            bound_ne_lat=29.1,
            bound_ne_lon=99.1,
            bound_sw_lat=-44.1,
            bound_sw_lon=-144.1,
            country_code="US",
            cutoff_date=parse_date("2024-05-21"),
            data_set_remarks="Data set remarks",
            deleting_org="ACME",
            deriving_org="ACME",
            directivity_code=2,
            elevation=840.1,
            elevation_acc=17.1,
            external_id="OU812",
            facc="AT040",
            feature_code="540",
            feature_description="Powerline Pylon, General",
            feature_name="PYLON",
            feature_type="540",
            height_agl=314.1,
            height_agl_acc=30.1,
            height_msl=1154.1,
            height_msl_acc=34.1,
            horiz_acc=8.1,
            horiz_datum_code="WGS-84",
            init_record_date=parse_date("1991-03-28"),
            keys=["key1", "key2"],
            lighting_code="U",
            line_ne_lat=49.000584,
            line_ne_lon=-122.197891,
            lines_filename="lines.txt",
            line_sw_lat=48.507027,
            line_sw_lon=-122.722946,
            min_height_agl=20.1,
            mult_obs="S",
            next_cycle_date=parse_date("2024-07-11"),
            num_lines=45993,
            num_obs=1,
            num_points=21830590,
            obstacle_remarks="Obstacle remarks",
            orig_id="L0000002289",
            origin="THIRD_PARTY_DATASOURCE",
            owner_country_code="US",
            point_lat=46.757211,
            point_lon=-67.759494,
            points_filename="points.txt",
            process_code="OT",
            producer="ACME",
            province_code="23",
            quality="0",
            rev_date=parse_date("2020-02-26"),
            seg_end_point=359655,
            seg_num=1,
            seg_start_point=359655,
            source_date=parse_date("2016-04-01"),
            surface_mat_code="U",
            transaction_code="V",
            validation_code=3,
            values=["value1", "value2"],
            vectors_filename="vectors.txt",
            wac="262",
            wac_innr="0409-00039",
        )
        assert navigational_obstruction is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert navigational_obstruction is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )
        assert navigational_obstruction is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            act_del_code="A",
            airac_cycle=2406,
            base_airac_cycle=2405,
            baseline_cutoff_date=parse_date("2024-04-23"),
            bound_ne_lat=29.1,
            bound_ne_lon=99.1,
            bound_sw_lat=-44.1,
            bound_sw_lon=-144.1,
            country_code="US",
            cutoff_date=parse_date("2024-05-21"),
            data_set_remarks="Data set remarks",
            deleting_org="ACME",
            deriving_org="ACME",
            directivity_code=2,
            elevation=840.1,
            elevation_acc=17.1,
            external_id="OU812",
            facc="AT040",
            feature_code="540",
            feature_description="Powerline Pylon, General",
            feature_name="PYLON",
            feature_type="540",
            height_agl=314.1,
            height_agl_acc=30.1,
            height_msl=1154.1,
            height_msl_acc=34.1,
            horiz_acc=8.1,
            horiz_datum_code="WGS-84",
            init_record_date=parse_date("1991-03-28"),
            keys=["key1", "key2"],
            lighting_code="U",
            line_ne_lat=49.000584,
            line_ne_lon=-122.197891,
            lines_filename="lines.txt",
            line_sw_lat=48.507027,
            line_sw_lon=-122.722946,
            min_height_agl=20.1,
            mult_obs="S",
            next_cycle_date=parse_date("2024-07-11"),
            num_lines=45993,
            num_obs=1,
            num_points=21830590,
            obstacle_remarks="Obstacle remarks",
            orig_id="L0000002289",
            origin="THIRD_PARTY_DATASOURCE",
            owner_country_code="US",
            point_lat=46.757211,
            point_lon=-67.759494,
            points_filename="points.txt",
            process_code="OT",
            producer="ACME",
            province_code="23",
            quality="0",
            rev_date=parse_date("2020-02-26"),
            seg_end_point=359655,
            seg_num=1,
            seg_start_point=359655,
            source_date=parse_date("2016-04-01"),
            surface_mat_code="U",
            transaction_code="V",
            validation_code=3,
            values=["value1", "value2"],
            vectors_filename="vectors.txt",
            wac="262",
            wac_innr="0409-00039",
        )
        assert navigational_obstruction is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert navigational_obstruction is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.navigational_obstruction.with_raw_response.update(
                path_id="",
                classification_marking="U",
                cycle_date=parse_date("2024-06-13"),
                data_mode="TEST",
                obstacle_id="359655",
                obstacle_type="V",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.list()
        assert_matches_type(
            SyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.list(
            cycle_date=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
            obstacle_id="obstacleId",
        )
        assert_matches_type(
            SyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert_matches_type(
            SyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert_matches_type(
                SyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.count()
        assert_matches_type(str, navigational_obstruction, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.count(
            cycle_date=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
            obstacle_id="obstacleId",
        )
        assert_matches_type(str, navigational_obstruction, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert_matches_type(str, navigational_obstruction, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert_matches_type(str, navigational_obstruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cycle_date": parse_date("2024-06-13"),
                    "data_mode": "TEST",
                    "obstacle_id": "359655",
                    "obstacle_type": "V",
                    "source": "Bluestaq",
                }
            ],
        )
        assert navigational_obstruction is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cycle_date": parse_date("2024-06-13"),
                    "data_mode": "TEST",
                    "obstacle_id": "359655",
                    "obstacle_type": "V",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert navigational_obstruction is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cycle_date": parse_date("2024-06-13"),
                    "data_mode": "TEST",
                    "obstacle_id": "359655",
                    "obstacle_type": "V",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.get(
            id="id",
        )
        assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.navigational_obstruction.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.queryhelp()
        assert navigational_obstruction is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert navigational_obstruction is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.tuple(
            columns="columns",
        )
        assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        navigational_obstruction = client.navigational_obstruction.tuple(
            columns="columns",
            cycle_date=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
            obstacle_id="obstacleId",
        )
        assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.navigational_obstruction.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = response.parse()
        assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.navigational_obstruction.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = response.parse()
            assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNavigationalObstruction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )
        assert navigational_obstruction is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            act_del_code="A",
            airac_cycle=2406,
            base_airac_cycle=2405,
            baseline_cutoff_date=parse_date("2024-04-23"),
            bound_ne_lat=29.1,
            bound_ne_lon=99.1,
            bound_sw_lat=-44.1,
            bound_sw_lon=-144.1,
            country_code="US",
            cutoff_date=parse_date("2024-05-21"),
            data_set_remarks="Data set remarks",
            deleting_org="ACME",
            deriving_org="ACME",
            directivity_code=2,
            elevation=840.1,
            elevation_acc=17.1,
            external_id="OU812",
            facc="AT040",
            feature_code="540",
            feature_description="Powerline Pylon, General",
            feature_name="PYLON",
            feature_type="540",
            height_agl=314.1,
            height_agl_acc=30.1,
            height_msl=1154.1,
            height_msl_acc=34.1,
            horiz_acc=8.1,
            horiz_datum_code="WGS-84",
            init_record_date=parse_date("1991-03-28"),
            keys=["key1", "key2"],
            lighting_code="U",
            line_ne_lat=49.000584,
            line_ne_lon=-122.197891,
            lines_filename="lines.txt",
            line_sw_lat=48.507027,
            line_sw_lon=-122.722946,
            min_height_agl=20.1,
            mult_obs="S",
            next_cycle_date=parse_date("2024-07-11"),
            num_lines=45993,
            num_obs=1,
            num_points=21830590,
            obstacle_remarks="Obstacle remarks",
            orig_id="L0000002289",
            origin="THIRD_PARTY_DATASOURCE",
            owner_country_code="US",
            point_lat=46.757211,
            point_lon=-67.759494,
            points_filename="points.txt",
            process_code="OT",
            producer="ACME",
            province_code="23",
            quality="0",
            rev_date=parse_date("2020-02-26"),
            seg_end_point=359655,
            seg_num=1,
            seg_start_point=359655,
            source_date=parse_date("2016-04-01"),
            surface_mat_code="U",
            transaction_code="V",
            validation_code=3,
            values=["value1", "value2"],
            vectors_filename="vectors.txt",
            wac="262",
            wac_innr="0409-00039",
        )
        assert navigational_obstruction is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert navigational_obstruction is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.create(
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )
        assert navigational_obstruction is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            act_del_code="A",
            airac_cycle=2406,
            base_airac_cycle=2405,
            baseline_cutoff_date=parse_date("2024-04-23"),
            bound_ne_lat=29.1,
            bound_ne_lon=99.1,
            bound_sw_lat=-44.1,
            bound_sw_lon=-144.1,
            country_code="US",
            cutoff_date=parse_date("2024-05-21"),
            data_set_remarks="Data set remarks",
            deleting_org="ACME",
            deriving_org="ACME",
            directivity_code=2,
            elevation=840.1,
            elevation_acc=17.1,
            external_id="OU812",
            facc="AT040",
            feature_code="540",
            feature_description="Powerline Pylon, General",
            feature_name="PYLON",
            feature_type="540",
            height_agl=314.1,
            height_agl_acc=30.1,
            height_msl=1154.1,
            height_msl_acc=34.1,
            horiz_acc=8.1,
            horiz_datum_code="WGS-84",
            init_record_date=parse_date("1991-03-28"),
            keys=["key1", "key2"],
            lighting_code="U",
            line_ne_lat=49.000584,
            line_ne_lon=-122.197891,
            lines_filename="lines.txt",
            line_sw_lat=48.507027,
            line_sw_lon=-122.722946,
            min_height_agl=20.1,
            mult_obs="S",
            next_cycle_date=parse_date("2024-07-11"),
            num_lines=45993,
            num_obs=1,
            num_points=21830590,
            obstacle_remarks="Obstacle remarks",
            orig_id="L0000002289",
            origin="THIRD_PARTY_DATASOURCE",
            owner_country_code="US",
            point_lat=46.757211,
            point_lon=-67.759494,
            points_filename="points.txt",
            process_code="OT",
            producer="ACME",
            province_code="23",
            quality="0",
            rev_date=parse_date("2020-02-26"),
            seg_end_point=359655,
            seg_num=1,
            seg_start_point=359655,
            source_date=parse_date("2016-04-01"),
            surface_mat_code="U",
            transaction_code="V",
            validation_code=3,
            values=["value1", "value2"],
            vectors_filename="vectors.txt",
            wac="262",
            wac_innr="0409-00039",
        )
        assert navigational_obstruction is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert navigational_obstruction is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            cycle_date=parse_date("2024-06-13"),
            data_mode="TEST",
            obstacle_id="359655",
            obstacle_type="V",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.navigational_obstruction.with_raw_response.update(
                path_id="",
                classification_marking="U",
                cycle_date=parse_date("2024-06-13"),
                data_mode="TEST",
                obstacle_id="359655",
                obstacle_type="V",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.list()
        assert_matches_type(
            AsyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.list(
            cycle_date=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
            obstacle_id="obstacleId",
        )
        assert_matches_type(
            AsyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[NavigationalObstructionListResponse], navigational_obstruction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.count()
        assert_matches_type(str, navigational_obstruction, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.count(
            cycle_date=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
            obstacle_id="obstacleId",
        )
        assert_matches_type(str, navigational_obstruction, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert_matches_type(str, navigational_obstruction, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert_matches_type(str, navigational_obstruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cycle_date": parse_date("2024-06-13"),
                    "data_mode": "TEST",
                    "obstacle_id": "359655",
                    "obstacle_type": "V",
                    "source": "Bluestaq",
                }
            ],
        )
        assert navigational_obstruction is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cycle_date": parse_date("2024-06-13"),
                    "data_mode": "TEST",
                    "obstacle_id": "359655",
                    "obstacle_type": "V",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert navigational_obstruction is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "cycle_date": parse_date("2024-06-13"),
                    "data_mode": "TEST",
                    "obstacle_id": "359655",
                    "obstacle_type": "V",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.get(
            id="id",
        )
        assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert_matches_type(NavigationalObstructionGetResponse, navigational_obstruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.navigational_obstruction.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.queryhelp()
        assert navigational_obstruction is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert navigational_obstruction is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert navigational_obstruction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.tuple(
            columns="columns",
        )
        assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        navigational_obstruction = await async_client.navigational_obstruction.tuple(
            columns="columns",
            cycle_date=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
            obstacle_id="obstacleId",
        )
        assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.navigational_obstruction.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        navigational_obstruction = await response.parse()
        assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.navigational_obstruction.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            navigational_obstruction = await response.parse()
            assert_matches_type(NavigationalObstructionTupleResponse, navigational_obstruction, path=["response"])

        assert cast(Any, response.is_closed) is True
