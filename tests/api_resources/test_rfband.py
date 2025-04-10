# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    RfbandGetResponse,
    RfbandListResponse,
    RfbandTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRfband:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )
        assert rfband is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
            id="RFBAND-ID",
            band="Ku",
            bandwidth=100.23,
            beamwidth=45.23,
            center_freq=1000.23,
            edge_gain=100.23,
            eirp=2.23,
            erp=2.23,
            freq_max=2000.23,
            freq_min=50.23,
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            peak_gain=120.23,
            polarization="H",
            purpose="TTC",
        )
        assert rfband is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert rfband is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )
        assert rfband is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
            body_id="RFBAND-ID",
            band="Ku",
            bandwidth=100.23,
            beamwidth=45.23,
            center_freq=1000.23,
            edge_gain=100.23,
            eirp=2.23,
            erp=2.23,
            freq_max=2000.23,
            freq_min=50.23,
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            peak_gain=120.23,
            polarization="H",
            purpose="TTC",
        )
        assert rfband is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert rfband is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.rfband.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_entity="ENTITY-ID",
                name="BAND_NAME",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.list()
        assert_matches_type(RfbandListResponse, rfband, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert_matches_type(RfbandListResponse, rfband, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert_matches_type(RfbandListResponse, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.delete(
            "id",
        )
        assert rfband is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert rfband is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rfband.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.count()
        assert_matches_type(str, rfband, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert_matches_type(str, rfband, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert_matches_type(str, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.get(
            "id",
        )
        assert_matches_type(RfbandGetResponse, rfband, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert_matches_type(RfbandGetResponse, rfband, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert_matches_type(RfbandGetResponse, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rfband.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.queryhelp()
        assert rfband is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert rfband is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        rfband = client.rfband.tuple(
            columns="columns",
        )
        assert_matches_type(RfbandTupleResponse, rfband, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.rfband.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = response.parse()
        assert_matches_type(RfbandTupleResponse, rfband, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.rfband.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = response.parse()
            assert_matches_type(RfbandTupleResponse, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRfband:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )
        assert rfband is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
            id="RFBAND-ID",
            band="Ku",
            bandwidth=100.23,
            beamwidth=45.23,
            center_freq=1000.23,
            edge_gain=100.23,
            eirp=2.23,
            erp=2.23,
            freq_max=2000.23,
            freq_min=50.23,
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            peak_gain=120.23,
            polarization="H",
            purpose="TTC",
        )
        assert rfband is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert rfband is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )
        assert rfband is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
            body_id="RFBAND-ID",
            band="Ku",
            bandwidth=100.23,
            beamwidth=45.23,
            center_freq=1000.23,
            edge_gain=100.23,
            eirp=2.23,
            erp=2.23,
            freq_max=2000.23,
            freq_min=50.23,
            mode="TX",
            origin="THIRD_PARTY_DATASOURCE",
            peak_gain=120.23,
            polarization="H",
            purpose="TTC",
        )
        assert rfband is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert rfband is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            name="BAND_NAME",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.rfband.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_entity="ENTITY-ID",
                name="BAND_NAME",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.list()
        assert_matches_type(RfbandListResponse, rfband, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert_matches_type(RfbandListResponse, rfband, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert_matches_type(RfbandListResponse, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.delete(
            "id",
        )
        assert rfband is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert rfband is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rfband.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.count()
        assert_matches_type(str, rfband, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert_matches_type(str, rfband, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert_matches_type(str, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.get(
            "id",
        )
        assert_matches_type(RfbandGetResponse, rfband, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert_matches_type(RfbandGetResponse, rfband, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert_matches_type(RfbandGetResponse, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rfband.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.queryhelp()
        assert rfband is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert rfband is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert rfband is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        rfband = await async_client.rfband.tuple(
            columns="columns",
        )
        assert_matches_type(RfbandTupleResponse, rfband, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.rfband.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rfband = await response.parse()
        assert_matches_type(RfbandTupleResponse, rfband, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.rfband.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rfband = await response.parse()
            assert_matches_type(RfbandTupleResponse, rfband, path=["response"])

        assert cast(Any, response.is_closed) is True
