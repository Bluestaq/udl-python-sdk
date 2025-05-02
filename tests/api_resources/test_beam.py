# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    BeamFull,
    BeamAbridged,
    BeamTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeam:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert beam is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="BEAM-ID",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert beam is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert beam is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.retrieve(
            id="id",
        )
        assert_matches_type(BeamFull, beam, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamFull, beam, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert_matches_type(BeamFull, beam, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert_matches_type(BeamFull, beam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.beam.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert beam is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="BEAM-ID",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert beam is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert beam is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.beam.with_raw_response.update(
                path_id="",
                beam_name="BEAMNAME-ID",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.list()
        assert_matches_type(SyncOffsetPage[BeamAbridged], beam, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[BeamAbridged], beam, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert_matches_type(SyncOffsetPage[BeamAbridged], beam, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert_matches_type(SyncOffsetPage[BeamAbridged], beam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.delete(
            "id",
        )
        assert beam is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert beam is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.beam.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.count()
        assert_matches_type(str, beam, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, beam, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert_matches_type(str, beam, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert_matches_type(str, beam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.query_help()
        assert beam is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert beam is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.tuple(
            columns="columns",
        )
        assert_matches_type(BeamTupleResponse, beam, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam = client.beam.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamTupleResponse, beam, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.beam.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = response.parse()
        assert_matches_type(BeamTupleResponse, beam, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.beam.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = response.parse()
            assert_matches_type(BeamTupleResponse, beam, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeam:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert beam is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="BEAM-ID",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert beam is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert beam is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.create(
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.retrieve(
            id="id",
        )
        assert_matches_type(BeamFull, beam, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamFull, beam, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert_matches_type(BeamFull, beam, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert_matches_type(BeamFull, beam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.beam.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert beam is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="BEAM-ID",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert beam is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert beam is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.update(
            path_id="id",
            beam_name="BEAMNAME-ID",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.beam.with_raw_response.update(
                path_id="",
                beam_name="BEAMNAME-ID",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.list()
        assert_matches_type(AsyncOffsetPage[BeamAbridged], beam, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[BeamAbridged], beam, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert_matches_type(AsyncOffsetPage[BeamAbridged], beam, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert_matches_type(AsyncOffsetPage[BeamAbridged], beam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.delete(
            "id",
        )
        assert beam is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert beam is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.beam.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.count()
        assert_matches_type(str, beam, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, beam, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert_matches_type(str, beam, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert_matches_type(str, beam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.query_help()
        assert beam is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert beam is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert beam is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.tuple(
            columns="columns",
        )
        assert_matches_type(BeamTupleResponse, beam, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam = await async_client.beam.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamTupleResponse, beam, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam = await response.parse()
        assert_matches_type(BeamTupleResponse, beam, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam = await response.parse()
            assert_matches_type(BeamTupleResponse, beam, path=["response"])

        assert cast(Any, response.is_closed) is True
