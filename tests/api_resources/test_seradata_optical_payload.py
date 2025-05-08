# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeradataOpticalPayloadGetResponse,
    SeradataOpticalPayloadListResponse,
    SeradataOpticalPayloadTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeradataOpticalPayload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradata_optical_payload is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATAOPTICALPAYLOAD-ID",
            best_resolution=1.23,
            field_of_regard=1.23,
            field_of_view=1.23,
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="idSensor",
            imaging_payload_category="Infrared",
            manufacturer_org_id="manufacturerOrgId",
            name="TOURNESOL",
            notes="Sample Notes",
            number_of_film_return_canisters=1,
            origin="THIRD_PARTY_DATASOURCE",
            pointing_method="Spacecraft",
            recorder_size="1024",
            spectral_band="Green",
            spectral_frequency_limits="0.51",
            swath_width=1.23,
        )
        assert seradata_optical_payload is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert seradata_optical_payload is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradata_optical_payload is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATAOPTICALPAYLOAD-ID",
            best_resolution=1.23,
            field_of_regard=1.23,
            field_of_view=1.23,
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="idSensor",
            imaging_payload_category="Infrared",
            manufacturer_org_id="manufacturerOrgId",
            name="TOURNESOL",
            notes="Sample Notes",
            number_of_film_return_canisters=1,
            origin="THIRD_PARTY_DATASOURCE",
            pointing_method="Spacecraft",
            recorder_size="1024",
            spectral_band="Green",
            spectral_frequency_limits="0.51",
            swath_width=1.23,
        )
        assert seradata_optical_payload is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert seradata_optical_payload is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.seradata_optical_payload.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.list()
        assert_matches_type(
            SyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            SyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert_matches_type(
            SyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert_matches_type(
                SyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.delete(
            "id",
        )
        assert seradata_optical_payload is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert seradata_optical_payload is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradata_optical_payload.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.count()
        assert_matches_type(str, seradata_optical_payload, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, seradata_optical_payload, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert_matches_type(str, seradata_optical_payload, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert_matches_type(str, seradata_optical_payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.get(
            id="id",
        )
        assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradata_optical_payload.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.queryhelp()
        assert seradata_optical_payload is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert seradata_optical_payload is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.tuple(
            columns="columns",
        )
        assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradata_optical_payload = client.seradata_optical_payload.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.seradata_optical_payload.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = response.parse()
        assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.seradata_optical_payload.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = response.parse()
            assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeradataOpticalPayload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradata_optical_payload is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATAOPTICALPAYLOAD-ID",
            best_resolution=1.23,
            field_of_regard=1.23,
            field_of_view=1.23,
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="idSensor",
            imaging_payload_category="Infrared",
            manufacturer_org_id="manufacturerOrgId",
            name="TOURNESOL",
            notes="Sample Notes",
            number_of_film_return_canisters=1,
            origin="THIRD_PARTY_DATASOURCE",
            pointing_method="Spacecraft",
            recorder_size="1024",
            spectral_band="Green",
            spectral_frequency_limits="0.51",
            swath_width=1.23,
        )
        assert seradata_optical_payload is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert seradata_optical_payload is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradata_optical_payload is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATAOPTICALPAYLOAD-ID",
            best_resolution=1.23,
            field_of_regard=1.23,
            field_of_view=1.23,
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="idSensor",
            imaging_payload_category="Infrared",
            manufacturer_org_id="manufacturerOrgId",
            name="TOURNESOL",
            notes="Sample Notes",
            number_of_film_return_canisters=1,
            origin="THIRD_PARTY_DATASOURCE",
            pointing_method="Spacecraft",
            recorder_size="1024",
            spectral_band="Green",
            spectral_frequency_limits="0.51",
            swath_width=1.23,
        )
        assert seradata_optical_payload is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert seradata_optical_payload is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.seradata_optical_payload.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.list()
        assert_matches_type(
            AsyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            AsyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[SeradataOpticalPayloadListResponse], seradata_optical_payload, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.delete(
            "id",
        )
        assert seradata_optical_payload is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert seradata_optical_payload is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradata_optical_payload.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.count()
        assert_matches_type(str, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert_matches_type(str, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert_matches_type(str, seradata_optical_payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.get(
            id="id",
        )
        assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert_matches_type(SeradataOpticalPayloadGetResponse, seradata_optical_payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradata_optical_payload.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.queryhelp()
        assert seradata_optical_payload is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert seradata_optical_payload is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert seradata_optical_payload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.tuple(
            columns="columns",
        )
        assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradata_optical_payload = await async_client.seradata_optical_payload.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradata_optical_payload.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradata_optical_payload = await response.parse()
        assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradata_optical_payload.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradata_optical_payload = await response.parse()
            assert_matches_type(SeradataOpticalPayloadTupleResponse, seradata_optical_payload, path=["response"])

        assert cast(Any, response.is_closed) is True
