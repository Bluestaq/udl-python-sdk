# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ChannelFull,
    ChannelAbridged,
    ChannelTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )
        assert channel is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
            id="CHANNEL-ID",
            apid="AP-ID",
            beam_name="B8VD",
            compression="Example compression",
            encryption="Example encryption",
            id_beam="REF-BEAM-ID",
            id_rf_band="REF-RFBAND-ID",
            origin="example_origin",
            owner="example_owner",
            pkg="Example pkg",
            res="Example res",
            sid="S-ID",
            type="Example type",
            vpid="VP-ID",
        )
        assert channel is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert channel is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.retrieve(
            id="id",
        )
        assert_matches_type(ChannelFull, channel, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ChannelFull, channel, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelFull, channel, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelFull, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.channels.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )
        assert channel is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
            body_id="CHANNEL-ID",
            apid="AP-ID",
            beam_name="B8VD",
            compression="Example compression",
            encryption="Example encryption",
            id_beam="REF-BEAM-ID",
            id_rf_band="REF-RFBAND-ID",
            origin="example_origin",
            owner="example_owner",
            pkg="Example pkg",
            res="Example res",
            sid="S-ID",
            type="Example type",
            vpid="VP-ID",
        )
        assert channel is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert channel is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.channels.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_transponder="REF-TRANSPONDER-ID",
                name="Example name",
                source="system.source",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.list()
        assert_matches_type(SyncOffsetPage[ChannelAbridged], channel, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ChannelAbridged], channel, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncOffsetPage[ChannelAbridged], channel, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncOffsetPage[ChannelAbridged], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.delete(
            "id",
        )
        assert channel is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert channel is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.channels.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.count()
        assert_matches_type(str, channel, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, channel, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(str, channel, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(str, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.queryhelp()
        assert channel is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert channel is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.tuple(
            columns="columns",
        )
        assert_matches_type(ChannelTupleResponse, channel, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        channel = client.channels.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ChannelTupleResponse, channel, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.channels.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelTupleResponse, channel, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.channels.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelTupleResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChannels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )
        assert channel is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
            id="CHANNEL-ID",
            apid="AP-ID",
            beam_name="B8VD",
            compression="Example compression",
            encryption="Example encryption",
            id_beam="REF-BEAM-ID",
            id_rf_band="REF-RFBAND-ID",
            origin="example_origin",
            owner="example_owner",
            pkg="Example pkg",
            res="Example res",
            sid="S-ID",
            type="Example type",
            vpid="VP-ID",
        )
        assert channel is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert channel is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.retrieve(
            id="id",
        )
        assert_matches_type(ChannelFull, channel, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ChannelFull, channel, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelFull, channel, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelFull, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.channels.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )
        assert channel is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
            body_id="CHANNEL-ID",
            apid="AP-ID",
            beam_name="B8VD",
            compression="Example compression",
            encryption="Example encryption",
            id_beam="REF-BEAM-ID",
            id_rf_band="REF-RFBAND-ID",
            origin="example_origin",
            owner="example_owner",
            pkg="Example pkg",
            res="Example res",
            sid="S-ID",
            type="Example type",
            vpid="VP-ID",
        )
        assert channel is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert channel is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_transponder="REF-TRANSPONDER-ID",
            name="Example name",
            source="system.source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.channels.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_transponder="REF-TRANSPONDER-ID",
                name="Example name",
                source="system.source",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.list()
        assert_matches_type(AsyncOffsetPage[ChannelAbridged], channel, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ChannelAbridged], channel, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncOffsetPage[ChannelAbridged], channel, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncOffsetPage[ChannelAbridged], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.delete(
            "id",
        )
        assert channel is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert channel is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.channels.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.count()
        assert_matches_type(str, channel, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, channel, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(str, channel, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(str, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.queryhelp()
        assert channel is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert channel is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.tuple(
            columns="columns",
        )
        assert_matches_type(ChannelTupleResponse, channel, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        channel = await async_client.channels.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ChannelTupleResponse, channel, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.channels.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelTupleResponse, channel, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.channels.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelTupleResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True
