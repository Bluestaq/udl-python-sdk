# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SarObservationGetResponse,
    SarObservationListResponse,
    SarObservationTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSarObservation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
        )
        assert sar_observation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
            id="SAROBSERVATION-ID",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="POLYGON",
            azimuth_angle=285.4481793,
            center_time=parse_datetime("2023-04-22T17:36:35.100885Z"),
            collection_id="COLLECTION-ID",
            continuous_spot_angle=45.1,
            coord_sys="ECEF",
            detection_end=parse_datetime("2023-07-08T17:35:20.772190Z"),
            detection_id="DETECTION-ID",
            detection_start=parse_datetime("2023-07-08T17:35:01.615396Z"),
            dwell_time=79.156794,
            external_id="EXTERNAL-ID",
            far_range=34.1,
            graze_angle=45.1,
            ground_resolution_projection=0.5,
            id_sensor="36036-1L",
            incidence_angle=45.1,
            looks_azimuth=2,
            looks_range=1,
            multilook_number=5,
            near_range=12.1,
            ob_direction="RIGHT",
            operating_band="L",
            operating_freq=2345.6,
            orbit_state="ASCENDING",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="36036",
            orig_sensor_id="SMOS-1L",
            pulse_bandwidth=500.1,
            pulse_duration=0.000011,
            resolution_azimuth=0.123,
            resolution_range=0.123,
            rx_polarization="H",
            sat_no=36036,
            senalt=1.1,
            senlat_end=45.1,
            senlat_start=45.1,
            senlon_end=179.1,
            senlon_start=179.1,
            senvelx=1.1,
            senvely=1.1,
            senvelz=1.1,
            slant_range=60.1,
            snr=10.1,
            spacing_azimuth=0.123,
            spacing_range=0.123,
            squint_angle=1.2,
            src_ids=["f7e01cd4-626b-441f-a423-17b160eb78ba", "223833c4-be0d-4fdb-a2e4-325a48eccced"],
            src_typs=["ESID", "GROUNDIMAGE"],
            swath_length=12.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            targetposx=50.23,
            targetposy=50.23,
            targetposz=50.23,
            transaction_id="TRANSACTION-ID",
            tx_polarization="H",
        )
        assert sar_observation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert sar_observation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert_matches_type(SyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert_matches_type(SyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sar_observation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sar_observation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert_matches_type(str, sar_observation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert_matches_type(str, sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sar_observation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert sar_observation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.get(
            id="id",
        )
        assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sar_observation.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.queryhelp()
        assert sar_observation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert sar_observation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        sar_observation = client.sar_observation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sar_observation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.sar_observation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = response.parse()
        assert sar_observation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.sar_observation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSarObservation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
        )
        assert sar_observation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
            id="SAROBSERVATION-ID",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="POLYGON",
            azimuth_angle=285.4481793,
            center_time=parse_datetime("2023-04-22T17:36:35.100885Z"),
            collection_id="COLLECTION-ID",
            continuous_spot_angle=45.1,
            coord_sys="ECEF",
            detection_end=parse_datetime("2023-07-08T17:35:20.772190Z"),
            detection_id="DETECTION-ID",
            detection_start=parse_datetime("2023-07-08T17:35:01.615396Z"),
            dwell_time=79.156794,
            external_id="EXTERNAL-ID",
            far_range=34.1,
            graze_angle=45.1,
            ground_resolution_projection=0.5,
            id_sensor="36036-1L",
            incidence_angle=45.1,
            looks_azimuth=2,
            looks_range=1,
            multilook_number=5,
            near_range=12.1,
            ob_direction="RIGHT",
            operating_band="L",
            operating_freq=2345.6,
            orbit_state="ASCENDING",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="36036",
            orig_sensor_id="SMOS-1L",
            pulse_bandwidth=500.1,
            pulse_duration=0.000011,
            resolution_azimuth=0.123,
            resolution_range=0.123,
            rx_polarization="H",
            sat_no=36036,
            senalt=1.1,
            senlat_end=45.1,
            senlat_start=45.1,
            senlon_end=179.1,
            senlon_start=179.1,
            senvelx=1.1,
            senvely=1.1,
            senvelz=1.1,
            slant_range=60.1,
            snr=10.1,
            spacing_azimuth=0.123,
            spacing_range=0.123,
            squint_angle=1.2,
            src_ids=["f7e01cd4-626b-441f-a423-17b160eb78ba", "223833c4-be0d-4fdb-a2e4-325a48eccced"],
            src_typs=["ESID", "GROUNDIMAGE"],
            swath_length=12.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            targetposx=50.23,
            targetposy=50.23,
            targetposz=50.23,
            transaction_id="TRANSACTION-ID",
            tx_polarization="H",
        )
        assert sar_observation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert sar_observation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.create(
            classification_marking="U",
            collection_end=parse_datetime("2023-04-22T17:38:10.201770Z"),
            collection_start=parse_datetime("2023-04-22T17:35:00.123456Z"),
            data_mode="TEST",
            sar_mode="SPOTLIGHT",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert_matches_type(AsyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.list(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert_matches_type(AsyncOffsetPage[SarObservationListResponse], sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sar_observation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sar_observation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert_matches_type(str, sar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.count(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert_matches_type(str, sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sar_observation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert sar_observation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.get(
            id="id",
        )
        assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert_matches_type(SarObservationGetResponse, sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sar_observation.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.queryhelp()
        assert sar_observation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert sar_observation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.tuple(
            collection_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert_matches_type(SarObservationTupleResponse, sar_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        sar_observation = await async_client.sar_observation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sar_observation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sar_observation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sar_observation = await response.parse()
        assert sar_observation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sar_observation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": parse_datetime("2023-04-22T17:38:10.201770Z"),
                    "collection_start": parse_datetime("2023-04-22T17:35:00.123456Z"),
                    "data_mode": "TEST",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sar_observation = await response.parse()
            assert sar_observation is None

        assert cast(Any, response.is_closed) is True
