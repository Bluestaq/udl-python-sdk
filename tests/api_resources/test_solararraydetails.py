# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SolarArrayDetailsFull,
    SolararraydetailListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSolararraydetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solararraydetail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solararraydetail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.solararraydetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = response.parse()
        assert solararraydetail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.solararraydetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = response.parse()
            assert solararraydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solararraydetail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            body_id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solararraydetail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.solararraydetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = response.parse()
        assert solararraydetail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.solararraydetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = response.parse()
            assert solararraydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.solararraydetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_solar_array="SOLARARRAY-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.list()
        assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.list(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.solararraydetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = response.parse()
        assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.solararraydetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = response.parse()
            assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.delete(
            "id",
        )
        assert solararraydetail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.solararraydetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = response.parse()
        assert solararraydetail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.solararraydetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = response.parse()
            assert solararraydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.solararraydetails.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        solararraydetail = client.solararraydetails.get(
            "id",
        )
        assert_matches_type(SolarArrayDetailsFull, solararraydetail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.solararraydetails.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = response.parse()
        assert_matches_type(SolarArrayDetailsFull, solararraydetail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.solararraydetails.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = response.parse()
            assert_matches_type(SolarArrayDetailsFull, solararraydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.solararraydetails.with_raw_response.get(
                "",
            )


class TestAsyncSolararraydetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solararraydetail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solararraydetail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solararraydetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = await response.parse()
        assert solararraydetail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solararraydetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = await response.parse()
            assert solararraydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )
        assert solararraydetail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
            body_id="SOLARARRAYDETAILS-ID",
            area=123.4,
            description="Example notes",
            junction_technology="Triple",
            manufacturer_org_id="MANUFACTURERORG-ID",
            origin="THIRD_PARTY_DATASOURCE",
            span=123.4,
            tags=["TAG1", "TAG2"],
            technology="Ga-As",
            type="U Shaped",
        )
        assert solararraydetail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solararraydetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = await response.parse()
        assert solararraydetail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solararraydetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_solar_array="SOLARARRAY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = await response.parse()
            assert solararraydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.solararraydetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_solar_array="SOLARARRAY-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.list()
        assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.list(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solararraydetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = await response.parse()
        assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solararraydetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = await response.parse()
            assert_matches_type(SolararraydetailListResponse, solararraydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.delete(
            "id",
        )
        assert solararraydetail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solararraydetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = await response.parse()
        assert solararraydetail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solararraydetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = await response.parse()
            assert solararraydetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.solararraydetails.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        solararraydetail = await async_client.solararraydetails.get(
            "id",
        )
        assert_matches_type(SolarArrayDetailsFull, solararraydetail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solararraydetails.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solararraydetail = await response.parse()
        assert_matches_type(SolarArrayDetailsFull, solararraydetail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solararraydetails.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solararraydetail = await response.parse()
            assert_matches_type(SolarArrayDetailsFull, solararraydetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.solararraydetails.with_raw_response.get(
                "",
            )
