# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    TrackrouteListResponse,
    TrackrouteTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.trackroute import TrackRouteFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrackroute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.trackroute.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
                source="Bluestaq",
                type="AIR REFUELING",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.list(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackrouteListResponse, trackroute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.list(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert_matches_type(TrackrouteListResponse, trackroute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.list(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert_matches_type(TrackrouteListResponse, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.delete(
            "id",
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.trackroute.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.count(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, trackroute, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.count(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert_matches_type(str, trackroute, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.count(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert_matches_type(str, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "last_update_date": parse_datetime("2024-09-17T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "AIR REFUELING",
                }
            ],
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "last_update_date": parse_datetime("2024-09-17T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "AIR REFUELING",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "last_update_date": parse_datetime("2024-09-17T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "AIR REFUELING",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.get(
            "id",
        )
        assert_matches_type(TrackRouteFull, trackroute, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert_matches_type(TrackRouteFull, trackroute, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert_matches_type(TrackRouteFull, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.trackroute.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.queryhelp()
        assert trackroute is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.tuple(
            columns="columns",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackrouteTupleResponse, trackroute, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.tuple(
            columns="columns",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert_matches_type(TrackrouteTupleResponse, trackroute, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.tuple(
            columns="columns",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert_matches_type(TrackrouteTupleResponse, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    def test_method_unvalidated_publish_with_all_params(self, client: Unifieddatalibrary) -> None:
        trackroute = client.trackroute.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.trackroute.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = response.parse()
        assert trackroute is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.trackroute.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTrackroute:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.trackroute.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
                source="Bluestaq",
                type="AIR REFUELING",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.list(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackrouteListResponse, trackroute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.list(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert_matches_type(TrackrouteListResponse, trackroute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.list(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert_matches_type(TrackrouteListResponse, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.delete(
            "id",
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.trackroute.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.count(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, trackroute, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.count(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert_matches_type(str, trackroute, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.count(
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert_matches_type(str, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "last_update_date": parse_datetime("2024-09-17T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "AIR REFUELING",
                }
            ],
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "last_update_date": parse_datetime("2024-09-17T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "AIR REFUELING",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "last_update_date": parse_datetime("2024-09-17T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "AIR REFUELING",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.get(
            "id",
        )
        assert_matches_type(TrackRouteFull, trackroute, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert_matches_type(TrackRouteFull, trackroute, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert_matches_type(TrackRouteFull, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.trackroute.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.queryhelp()
        assert trackroute is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.tuple(
            columns="columns",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackrouteTupleResponse, trackroute, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.tuple(
            columns="columns",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert_matches_type(TrackrouteTupleResponse, trackroute, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.tuple(
            columns="columns",
            last_update_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert_matches_type(TrackrouteTupleResponse, trackroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )
        assert trackroute is None

    @parametrize
    async def test_method_unvalidated_publish_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackroute = await async_client.trackroute.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            altitude_blocks=[
                {
                    "altitude_sequence_id": "A1",
                    "lower_altitude": 27000.1,
                    "upper_altitude": 27200.5,
                }
            ],
            apn_setting="1-3-1",
            apx_beacon_code="5/1",
            artcc_message="OAKLAND CTR/GUAM CERAP",
            creating_org="HQPAC",
            direction="NE",
            effective_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            external_id="GDSSMH121004232315303094",
            last_used_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            location_track_id="POACHR",
            origin="THIRD_PARTY_DATASOURCE",
            poc=[
                {
                    "office": "A34",
                    "phone": "8675309",
                    "poc_name": "Fred Smith",
                    "poc_org": "HQAF",
                    "poc_sequence_id": 1,
                    "poc_type_name": "Originator",
                    "rank": "Capt",
                    "remark": "POC remark.",
                    "username": "fgsmith",
                }
            ],
            pri_freq=357.5,
            receiver_tanker_ch_code="31/094",
            region_code="5",
            region_name="North America",
            review_date=parse_datetime("2024-09-16T16:00:00.123Z"),
            route_points=[
                {
                    "alt_country_code": "IZ",
                    "country_code": "NL",
                    "dafif_pt": True,
                    "mag_dec": 7.35,
                    "navaid": "HTO",
                    "navaid_length": 100.2,
                    "navaid_type": "VORTAC",
                    "pt_lat": 45.23,
                    "pt_lon": 179.1,
                    "pt_sequence_id": 1,
                    "pt_type_code": "EP",
                    "pt_type_name": "ENTRY POINT",
                    "waypoint_name": "KCHS",
                }
            ],
            scheduler_org_name="97 OSS/OSOS DSN 866-5555",
            scheduler_org_unit="612 AOC",
            sec_freq=319.7,
            short_name="CH61",
            sic="N",
            track_id="CH61A",
            track_name="CH61 POST",
            type_code="V",
        )
        assert trackroute is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackroute.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackroute = await response.parse()
        assert trackroute is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackroute.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            last_update_date=parse_datetime("2024-09-17T16:00:00.123Z"),
            source="Bluestaq",
            type="AIR REFUELING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackroute = await response.parse()
            assert trackroute is None

        assert cast(Any, response.is_closed) is True
