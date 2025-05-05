# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ObjectOfInterestGetResponse,
    ObjectOfInterestListResponse,
    ObjectOfInterestTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjectOfInterest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert object_of_interest is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            id="OBJECTOFINTEREST-ID",
            affected_objects=["AFFECTEDOBJECT1-ID", "AFFECTEDOBJECT2-ID"],
            apogee=123.4,
            arg_of_perigee=123.4,
            b_star=123.4,
            delta_ts=[1.1, 2.2, 3.3],
            delta_vs=[1.1, 2.2, 3.3],
            description="Example description",
            eccentricity=123.4,
            elset_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            inclination=123.4,
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            mean_anomaly=123.4,
            mean_motion=123.4,
            mean_motion_d_dot=123.4,
            mean_motion_dot=123.4,
            missed_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            name="Example_name",
            origin="THIRD_PARTY_DATASOURCE",
            perigee=123.4,
            period=123.4,
            priority=7,
            raan=123.4,
            rev_no=123,
            sat_no=12,
            semi_major_axis=123.4,
            sensor_tasking_stop_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            status="OPEN",
            sv_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            x=123.4,
            xvel=123.4,
            y=123.4,
            yvel=123.4,
            z=123.4,
            zvel=123.4,
        )
        assert object_of_interest is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert object_of_interest is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert object_of_interest is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            body_id="OBJECTOFINTEREST-ID",
            affected_objects=["AFFECTEDOBJECT1-ID", "AFFECTEDOBJECT2-ID"],
            apogee=123.4,
            arg_of_perigee=123.4,
            b_star=123.4,
            delta_ts=[1.1, 2.2, 3.3],
            delta_vs=[1.1, 2.2, 3.3],
            description="Example description",
            eccentricity=123.4,
            elset_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            inclination=123.4,
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            mean_anomaly=123.4,
            mean_motion=123.4,
            mean_motion_d_dot=123.4,
            mean_motion_dot=123.4,
            missed_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            name="Example_name",
            origin="THIRD_PARTY_DATASOURCE",
            perigee=123.4,
            period=123.4,
            priority=7,
            raan=123.4,
            rev_no=123,
            sat_no=12,
            semi_major_axis=123.4,
            sensor_tasking_stop_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            status="OPEN",
            sv_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            x=123.4,
            xvel=123.4,
            y=123.4,
            yvel=123.4,
            z=123.4,
            zvel=123.4,
        )
        assert object_of_interest is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert object_of_interest is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.object_of_interest.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_on_orbit="REF-ONORBIT-ID",
                sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
                source="Bluestaq",
                status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.list()
        assert_matches_type(SyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert_matches_type(SyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert_matches_type(SyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.delete(
            "id",
        )
        assert object_of_interest is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert object_of_interest is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.object_of_interest.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.count()
        assert_matches_type(str, object_of_interest, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, object_of_interest, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert_matches_type(str, object_of_interest, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert_matches_type(str, object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.get(
            id="id",
        )
        assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.object_of_interest.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.queryhelp()
        assert object_of_interest is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert object_of_interest is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.tuple(
            columns="columns",
        )
        assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        object_of_interest = client.object_of_interest.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.object_of_interest.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = response.parse()
        assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.object_of_interest.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = response.parse()
            assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncObjectOfInterest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert object_of_interest is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            id="OBJECTOFINTEREST-ID",
            affected_objects=["AFFECTEDOBJECT1-ID", "AFFECTEDOBJECT2-ID"],
            apogee=123.4,
            arg_of_perigee=123.4,
            b_star=123.4,
            delta_ts=[1.1, 2.2, 3.3],
            delta_vs=[1.1, 2.2, 3.3],
            description="Example description",
            eccentricity=123.4,
            elset_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            inclination=123.4,
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            mean_anomaly=123.4,
            mean_motion=123.4,
            mean_motion_d_dot=123.4,
            mean_motion_dot=123.4,
            missed_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            name="Example_name",
            origin="THIRD_PARTY_DATASOURCE",
            perigee=123.4,
            period=123.4,
            priority=7,
            raan=123.4,
            rev_no=123,
            sat_no=12,
            semi_major_axis=123.4,
            sensor_tasking_stop_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            status="OPEN",
            sv_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            x=123.4,
            xvel=123.4,
            y=123.4,
            yvel=123.4,
            z=123.4,
            zvel=123.4,
        )
        assert object_of_interest is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert object_of_interest is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )
        assert object_of_interest is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            body_id="OBJECTOFINTEREST-ID",
            affected_objects=["AFFECTEDOBJECT1-ID", "AFFECTEDOBJECT2-ID"],
            apogee=123.4,
            arg_of_perigee=123.4,
            b_star=123.4,
            delta_ts=[1.1, 2.2, 3.3],
            delta_vs=[1.1, 2.2, 3.3],
            description="Example description",
            eccentricity=123.4,
            elset_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            inclination=123.4,
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            mean_anomaly=123.4,
            mean_motion=123.4,
            mean_motion_d_dot=123.4,
            mean_motion_dot=123.4,
            missed_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            name="Example_name",
            origin="THIRD_PARTY_DATASOURCE",
            perigee=123.4,
            period=123.4,
            priority=7,
            raan=123.4,
            rev_no=123,
            sat_no=12,
            semi_major_axis=123.4,
            sensor_tasking_stop_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            status="OPEN",
            sv_epoch=parse_datetime("2021-01-01T01:01:01.123456Z"),
            x=123.4,
            xvel=123.4,
            y=123.4,
            yvel=123.4,
            z=123.4,
            zvel=123.4,
        )
        assert object_of_interest is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert object_of_interest is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            source="Bluestaq",
            status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.object_of_interest.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_on_orbit="REF-ONORBIT-ID",
                sensor_tasking_start_time=parse_datetime("2021-01-01T01:01:01.123Z"),
                source="Bluestaq",
                status_date=parse_datetime("2021-01-01T01:01:01.123Z"),
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.list()
        assert_matches_type(AsyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert_matches_type(AsyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert_matches_type(AsyncOffsetPage[ObjectOfInterestListResponse], object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.delete(
            "id",
        )
        assert object_of_interest is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert object_of_interest is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.object_of_interest.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.count()
        assert_matches_type(str, object_of_interest, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, object_of_interest, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert_matches_type(str, object_of_interest, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert_matches_type(str, object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.get(
            id="id",
        )
        assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert_matches_type(ObjectOfInterestGetResponse, object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.object_of_interest.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.queryhelp()
        assert object_of_interest is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert object_of_interest is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert object_of_interest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.tuple(
            columns="columns",
        )
        assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        object_of_interest = await async_client.object_of_interest.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.object_of_interest.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_of_interest = await response.parse()
        assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.object_of_interest.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_of_interest = await response.parse()
            assert_matches_type(ObjectOfInterestTupleResponse, object_of_interest, path=["response"])

        assert cast(Any, response.is_closed) is True
