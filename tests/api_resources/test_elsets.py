# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    Elset,
    ElsetAbridged,
    ElsetTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestElsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )
        assert elset is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            agom=0.0126,
            algorithm="Example algorithm",
            apogee=1.1,
            arg_of_perigee=1.1,
            ballistic_coeff=0.00815,
            b_star=1.1,
            descriptor="Example description",
            eccentricity=0.333,
            ephem_type=1,
            id_elset="ELSET-ID",
            id_orbit_determination="026dd511-8ba5-47d3-9909-836149f87686",
            inclination=45.1,
            mean_anomaly=179.1,
            mean_motion=1.1,
            mean_motion_d_dot=1.1,
            mean_motion_dot=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            perigee=1.1,
            period=1.1,
            raan=1.1,
            raw_file_uri="Example URI",
            rev_no=111,
            sat_no=12,
            semi_major_axis=1.1,
            sourced_data=["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
            sourced_data_types=["RADAR", "RF"],
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            uct=False,
        )
        assert elset is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert elset is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.retrieve(
            id="id",
        )
        assert_matches_type(Elset, elset, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(Elset, elset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert_matches_type(Elset, elset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert_matches_type(Elset, elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.elsets.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[ElsetAbridged], elset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ElsetAbridged], elset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert_matches_type(SyncOffsetPage[ElsetAbridged], elset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert_matches_type(SyncOffsetPage[ElsetAbridged], elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, elset, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, elset, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert_matches_type(str, elset, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert_matches_type(str, elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert elset is None

    @parametrize
    def test_method_create_bulk_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "agom": 0.0126,
                    "algorithm": "Example algorithm",
                    "apogee": 1.1,
                    "arg_of_perigee": 1.1,
                    "ballistic_coeff": 0.00815,
                    "b_star": 1.1,
                    "descriptor": "Example description",
                    "eccentricity": 0.333,
                    "ephem_type": 1,
                    "id_elset": "ELSET-ID",
                    "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                    "inclination": 45.1,
                    "mean_anomaly": 179.1,
                    "mean_motion": 1.1,
                    "mean_motion_d_dot": 1.1,
                    "mean_motion_dot": 1.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "perigee": 1.1,
                    "period": 1.1,
                    "raan": 1.1,
                    "raw_file_uri": "Example URI",
                    "rev_no": 111,
                    "sat_no": 12,
                    "semi_major_axis": 1.1,
                    "sourced_data": ["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
                    "sourced_data_types": ["RADAR", "RF"],
                    "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                    "transaction_id": "TRANSACTION-ID",
                    "uct": False,
                }
            ],
            dupe_check=True,
        )
        assert elset is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert elset is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk_from_tle(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
        )
        assert elset is None

    @parametrize
    def test_method_create_bulk_from_tle_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
            auto_create_sats=True,
            control="control",
            origin="origin",
            tags="tags",
        )
        assert elset is None

    @parametrize
    def test_raw_response_create_bulk_from_tle(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert elset is None

    @parametrize
    def test_streaming_response_create_bulk_from_tle(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_current_elset_help(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.query_current_elset_help()
        assert elset is None

    @parametrize
    def test_raw_response_query_current_elset_help(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.query_current_elset_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert elset is None

    @parametrize
    def test_streaming_response_query_current_elset_help(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.query_current_elset_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.queryhelp()
        assert elset is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert elset is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ElsetTupleResponse, elset, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ElsetTupleResponse, elset, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert_matches_type(ElsetTupleResponse, elset, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert_matches_type(ElsetTupleResponse, elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        elset = client.elsets.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert elset is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.elsets.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = response.parse()
        assert elset is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.elsets.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncElsets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )
        assert elset is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            agom=0.0126,
            algorithm="Example algorithm",
            apogee=1.1,
            arg_of_perigee=1.1,
            ballistic_coeff=0.00815,
            b_star=1.1,
            descriptor="Example description",
            eccentricity=0.333,
            ephem_type=1,
            id_elset="ELSET-ID",
            id_orbit_determination="026dd511-8ba5-47d3-9909-836149f87686",
            inclination=45.1,
            mean_anomaly=179.1,
            mean_motion=1.1,
            mean_motion_d_dot=1.1,
            mean_motion_dot=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            perigee=1.1,
            period=1.1,
            raan=1.1,
            raw_file_uri="Example URI",
            rev_no=111,
            sat_no=12,
            semi_major_axis=1.1,
            sourced_data=["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
            sourced_data_types=["RADAR", "RF"],
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            uct=False,
        )
        assert elset is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert elset is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.retrieve(
            id="id",
        )
        assert_matches_type(Elset, elset, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(Elset, elset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert_matches_type(Elset, elset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert_matches_type(Elset, elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.elsets.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[ElsetAbridged], elset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ElsetAbridged], elset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert_matches_type(AsyncOffsetPage[ElsetAbridged], elset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.list(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert_matches_type(AsyncOffsetPage[ElsetAbridged], elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, elset, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, elset, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert_matches_type(str, elset, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.count(
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert_matches_type(str, elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert elset is None

    @parametrize
    async def test_method_create_bulk_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "agom": 0.0126,
                    "algorithm": "Example algorithm",
                    "apogee": 1.1,
                    "arg_of_perigee": 1.1,
                    "ballistic_coeff": 0.00815,
                    "b_star": 1.1,
                    "descriptor": "Example description",
                    "eccentricity": 0.333,
                    "ephem_type": 1,
                    "id_elset": "ELSET-ID",
                    "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                    "inclination": 45.1,
                    "mean_anomaly": 179.1,
                    "mean_motion": 1.1,
                    "mean_motion_d_dot": 1.1,
                    "mean_motion_dot": 1.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "perigee": 1.1,
                    "period": 1.1,
                    "raan": 1.1,
                    "raw_file_uri": "Example URI",
                    "rev_no": 111,
                    "sat_no": 12,
                    "semi_major_axis": 1.1,
                    "sourced_data": ["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
                    "sourced_data_types": ["RADAR", "RF"],
                    "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                    "transaction_id": "TRANSACTION-ID",
                    "uct": False,
                }
            ],
            dupe_check=True,
        )
        assert elset is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert elset is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk_from_tle(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
        )
        assert elset is None

    @parametrize
    async def test_method_create_bulk_from_tle_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
            auto_create_sats=True,
            control="control",
            origin="origin",
            tags="tags",
        )
        assert elset is None

    @parametrize
    async def test_raw_response_create_bulk_from_tle(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert elset is None

    @parametrize
    async def test_streaming_response_create_bulk_from_tle(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.create_bulk_from_tle(
            data_mode="dataMode",
            make_current=True,
            source="source",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_current_elset_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.query_current_elset_help()
        assert elset is None

    @parametrize
    async def test_raw_response_query_current_elset_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.query_current_elset_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert elset is None

    @parametrize
    async def test_streaming_response_query_current_elset_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.query_current_elset_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.queryhelp()
        assert elset is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert elset is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ElsetTupleResponse, elset, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ElsetTupleResponse, elset, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert_matches_type(ElsetTupleResponse, elset, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.tuple(
            columns="columns",
            epoch=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert_matches_type(ElsetTupleResponse, elset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        elset = await async_client.elsets.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert elset is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.elsets.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elset = await response.parse()
        assert elset is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.elsets.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elset = await response.parse()
            assert elset is None

        assert cast(Any, response.is_closed) is True
