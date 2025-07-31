# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AntennaDetailsFull
from unifieddatalibrary.types.onorbit import (
    AntennaDetailsAbridged,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAntennaDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )
        assert antenna_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
            id="ANTENNADETAILS-ID",
            beam_forming=False,
            beamwidth=14.1,
            description="Description of antenna A",
            diameter=0.01,
            end_frequency=3.3,
            gain=20.1,
            gain_tolerance=5.1,
            manufacturer_org_id="MANUFACTUREORG-ID",
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            polarization=45.1,
            position="Top",
            size=[0.03, 0.05],
            start_frequency=2.1,
            steerable=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            type="Reflector",
        )
        assert antenna_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert antenna_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.retrieve(
            id="id",
        )
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.antenna_details.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )
        assert antenna_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
            body_id="ANTENNADETAILS-ID",
            beam_forming=False,
            beamwidth=14.1,
            description="Description of antenna A",
            diameter=0.01,
            end_frequency=3.3,
            gain=20.1,
            gain_tolerance=5.1,
            manufacturer_org_id="MANUFACTUREORG-ID",
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            polarization=45.1,
            position="Top",
            size=[0.03, 0.05],
            start_frequency=2.1,
            steerable=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            type="Reflector",
        )
        assert antenna_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert antenna_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.onorbit.antenna_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_antenna="ANTENNA-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.list()
        assert_matches_type(SyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert_matches_type(SyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert_matches_type(SyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.delete(
            "id",
        )
        assert antenna_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert antenna_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.antenna_details.with_raw_response.delete(
                "",
            )


class TestAsyncAntennaDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )
        assert antenna_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
            id="ANTENNADETAILS-ID",
            beam_forming=False,
            beamwidth=14.1,
            description="Description of antenna A",
            diameter=0.01,
            end_frequency=3.3,
            gain=20.1,
            gain_tolerance=5.1,
            manufacturer_org_id="MANUFACTUREORG-ID",
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            polarization=45.1,
            position="Top",
            size=[0.03, 0.05],
            start_frequency=2.1,
            steerable=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            type="Reflector",
        )
        assert antenna_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert antenna_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.retrieve(
            id="id",
        )
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.antenna_details.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )
        assert antenna_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
            body_id="ANTENNADETAILS-ID",
            beam_forming=False,
            beamwidth=14.1,
            description="Description of antenna A",
            diameter=0.01,
            end_frequency=3.3,
            gain=20.1,
            gain_tolerance=5.1,
            manufacturer_org_id="MANUFACTUREORG-ID",
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            polarization=45.1,
            position="Top",
            size=[0.03, 0.05],
            start_frequency=2.1,
            steerable=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            type="Reflector",
        )
        assert antenna_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert antenna_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_antenna="ANTENNA-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.onorbit.antenna_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_antenna="ANTENNA-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.list()
        assert_matches_type(AsyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert_matches_type(AsyncOffsetPage[AntennaDetailsAbridged], antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.delete(
            "id",
        )
        assert antenna_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert antenna_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.antenna_details.with_raw_response.delete(
                "",
            )
