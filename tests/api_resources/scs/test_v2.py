# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.scs import (
    ScsEntity,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.update(
            path="path",
        )
        assert v2 is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.update(
            path="path",
            send_notification=True,
            classification_marking="U",
            delete_on=0,
            description="A description of the updated folder.",
            read_acl="user.id1,group.id1",
            tags=["TAG1", "TAG2"],
            write_acl="user.id1,group.id1",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.update(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.update(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.list(
            path="path",
        )
        assert_matches_type(SyncOffsetPage[ScsEntity], v2, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.list(
            path="path",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ScsEntity], v2, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(SyncOffsetPage[ScsEntity], v2, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(SyncOffsetPage[ScsEntity], v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.delete(
            path="path",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.delete(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.delete(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_copy(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.copy(
            from_path="fromPath",
            to_path="toPath",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_copy(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.copy(
            from_path="fromPath",
            to_path="toPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_copy(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.copy(
            from_path="fromPath",
            to_path="toPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_file_upload(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
        )
        assert v2 is None

    @parametrize
    def test_method_file_upload_with_all_params(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
            delete_after="deleteAfter",
            description="description",
            overwrite=True,
            send_notification=True,
            tags="tags",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_file_upload(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_file_upload(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_folder_create(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.folder_create(
            path="path",
        )
        assert v2 is None

    @parametrize
    def test_method_folder_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.folder_create(
            path="path",
            send_notification=True,
            classification_marking="U",
            delete_on=0,
            description="My first folder",
            read_acl="user.id1,group.id1",
            tags=["TAG1", "TAG2"],
            write_acl="user.id1,group.id1",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_folder_create(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.folder_create(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_folder_create(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.folder_create(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_move(self, client: Unifieddatalibrary) -> None:
        v2 = client.scs.v2.move(
            from_path="fromPath",
            to_path="toPath",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_move(self, client: Unifieddatalibrary) -> None:
        response = client.scs.v2.with_raw_response.move(
            from_path="fromPath",
            to_path="toPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_move(self, client: Unifieddatalibrary) -> None:
        with client.scs.v2.with_streaming_response.move(
            from_path="fromPath",
            to_path="toPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.update(
            path="path",
        )
        assert v2 is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.update(
            path="path",
            send_notification=True,
            classification_marking="U",
            delete_on=0,
            description="A description of the updated folder.",
            read_acl="user.id1,group.id1",
            tags=["TAG1", "TAG2"],
            write_acl="user.id1,group.id1",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.update(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.update(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.list(
            path="path",
        )
        assert_matches_type(AsyncOffsetPage[ScsEntity], v2, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.list(
            path="path",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ScsEntity], v2, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(AsyncOffsetPage[ScsEntity], v2, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(AsyncOffsetPage[ScsEntity], v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.delete(
            path="path",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.delete(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.delete(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_copy(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.copy(
            from_path="fromPath",
            to_path="toPath",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.copy(
            from_path="fromPath",
            to_path="toPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.copy(
            from_path="fromPath",
            to_path="toPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_file_upload(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
        )
        assert v2 is None

    @parametrize
    async def test_method_file_upload_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
            delete_after="deleteAfter",
            description="description",
            overwrite=True,
            send_notification=True,
            tags="tags",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_file_upload(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_file_upload(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.file_upload(
            file_content=b"raw file contents",
            classification_marking="classificationMarking",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_folder_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.folder_create(
            path="path",
        )
        assert v2 is None

    @parametrize
    async def test_method_folder_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.folder_create(
            path="path",
            send_notification=True,
            classification_marking="U",
            delete_on=0,
            description="My first folder",
            read_acl="user.id1,group.id1",
            tags=["TAG1", "TAG2"],
            write_acl="user.id1,group.id1",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_folder_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.folder_create(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_folder_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.folder_create(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_move(self, async_client: AsyncUnifieddatalibrary) -> None:
        v2 = await async_client.scs.v2.move(
            from_path="fromPath",
            to_path="toPath",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_move(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.v2.with_raw_response.move(
            from_path="fromPath",
            to_path="toPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.v2.with_streaming_response.move(
            from_path="fromPath",
            to_path="toPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True
