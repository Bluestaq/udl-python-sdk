# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirfieldslotFull,
    AirfieldslotTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfieldslots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.retrieve(
            "id",
        )
        assert_matches_type(AirfieldslotFull, airfieldslot, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldslots.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = response.parse()
        assert_matches_type(AirfieldslotFull, airfieldslot, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airfieldslots.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = response.parse()
            assert_matches_type(AirfieldslotFull, airfieldslot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfieldslots.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )
        assert airfieldslot is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
            body_id="be831d39-1822-da9f-7ace-6cc5643397dc",
            ac_slot_cat="WIDE",
            alt_airfield_id="ALT-AIRFIELD-ID",
            capacity=5,
            end_time="2359Z",
            icao="KCOS",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            min_separation=7,
            notes="Notes for an airfield slot.",
            origin="THIRD_PARTY_DATASOURCE",
            start_time="0000Z",
            type="WORKING",
        )
        assert airfieldslot is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldslots.with_raw_response.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = response.parse()
        assert airfieldslot is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.airfieldslots.with_streaming_response.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = response.parse()
            assert airfieldslot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.airfieldslots.with_raw_response.update(
                path_id="",
                airfield_name="USAF Academy AFLD",
                classification_marking="U",
                data_mode="TEST",
                name="Apron 5",
                source="Bluestaq",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.delete(
            "id",
        )
        assert airfieldslot is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldslots.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = response.parse()
        assert airfieldslot is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.airfieldslots.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = response.parse()
            assert airfieldslot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airfieldslots.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.count()
        assert_matches_type(str, airfieldslot, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldslots.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = response.parse()
        assert_matches_type(str, airfieldslot, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.airfieldslots.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = response.parse()
            assert_matches_type(str, airfieldslot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.queryhelp()
        assert airfieldslot is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldslots.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = response.parse()
        assert airfieldslot is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.airfieldslots.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = response.parse()
            assert airfieldslot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        airfieldslot = client.airfieldslots.tuple(
            columns="columns",
        )
        assert_matches_type(AirfieldslotTupleResponse, airfieldslot, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldslots.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = response.parse()
        assert_matches_type(AirfieldslotTupleResponse, airfieldslot, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.airfieldslots.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = response.parse()
            assert_matches_type(AirfieldslotTupleResponse, airfieldslot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirfieldslots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.retrieve(
            "id",
        )
        assert_matches_type(AirfieldslotFull, airfieldslot, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldslots.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = await response.parse()
        assert_matches_type(AirfieldslotFull, airfieldslot, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldslots.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = await response.parse()
            assert_matches_type(AirfieldslotFull, airfieldslot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfieldslots.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )
        assert airfieldslot is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
            body_id="be831d39-1822-da9f-7ace-6cc5643397dc",
            ac_slot_cat="WIDE",
            alt_airfield_id="ALT-AIRFIELD-ID",
            capacity=5,
            end_time="2359Z",
            icao="KCOS",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            min_separation=7,
            notes="Notes for an airfield slot.",
            origin="THIRD_PARTY_DATASOURCE",
            start_time="0000Z",
            type="WORKING",
        )
        assert airfieldslot is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldslots.with_raw_response.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = await response.parse()
        assert airfieldslot is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldslots.with_streaming_response.update(
            path_id="id",
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = await response.parse()
            assert airfieldslot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.airfieldslots.with_raw_response.update(
                path_id="",
                airfield_name="USAF Academy AFLD",
                classification_marking="U",
                data_mode="TEST",
                name="Apron 5",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.delete(
            "id",
        )
        assert airfieldslot is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldslots.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = await response.parse()
        assert airfieldslot is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldslots.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = await response.parse()
            assert airfieldslot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airfieldslots.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.count()
        assert_matches_type(str, airfieldslot, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldslots.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = await response.parse()
        assert_matches_type(str, airfieldslot, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldslots.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = await response.parse()
            assert_matches_type(str, airfieldslot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.queryhelp()
        assert airfieldslot is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldslots.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = await response.parse()
        assert airfieldslot is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldslots.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = await response.parse()
            assert airfieldslot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldslot = await async_client.airfieldslots.tuple(
            columns="columns",
        )
        assert_matches_type(AirfieldslotTupleResponse, airfieldslot, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldslots.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldslot = await response.parse()
        assert_matches_type(AirfieldslotTupleResponse, airfieldslot, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldslots.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldslot = await response.parse()
            assert_matches_type(AirfieldslotTupleResponse, airfieldslot, path=["response"])

        assert cast(Any, response.is_closed) is True
