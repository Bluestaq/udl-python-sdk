# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import FileData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        file = client.scs.file.retrieve(
            id="id",
        )
        assert_matches_type(FileData, file, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        file = client.scs.file.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FileData, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.scs.file.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileData, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.scs.file.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileData, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        file = client.scs.file.update()
        assert file is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        file = client.scs.file.update(
            file_data_list=[
                {
                    "id": "/example/folder/example_file.txt",
                    "attributes": {
                        "id": "id",
                        "classification": "U",
                        "classification_marking": "classificationMarking",
                        "created_by": "createdBy",
                        "created_date": "createdDate",
                        "delete_on": 0,
                        "description": "A new Example description",
                        "doc_title": "docTitle",
                        "doc_type": "docType",
                        "doi": ["string"],
                        "ellipse_lat": 0,
                        "ellipse_lon": 0,
                        "file_name": "fileName",
                        "intrinsic_title": "intrinsicTitle",
                        "keywords": "keywords",
                        "media_title": "mediaTitle",
                        "meta_info": "A new Example metaInfo",
                        "milgrid": "milgrid",
                        "milgrid_lat": 0,
                        "milgrid_lon": 0,
                        "modified_by": "modifiedBy",
                        "modified_date": "modifiedDate",
                        "name": "name",
                        "path": "path",
                        "read": "read",
                        "searchable": True,
                        "search_after": "searchAfter",
                        "serial_number": "serialNumber",
                        "size": 0,
                        "tags": ["string"],
                        "write": "write",
                    },
                    "content_action": "UPDATE",
                    "target_name": "targetName",
                    "target_path": "targetPath",
                    "type": "file",
                }
            ],
        )
        assert file is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.scs.file.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.scs.file.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        file = client.scs.file.list(
            path="path",
        )
        assert_matches_type(SyncOffsetPage[FileData], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        file = client.scs.file.list(
            path="path",
            count=0,
            first_result=0,
            max_results=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[FileData], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.scs.file.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncOffsetPage[FileData], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.scs.file.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncOffsetPage[FileData], file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.file.retrieve(
            id="id",
        )
        assert_matches_type(FileData, file, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.file.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FileData, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.file.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileData, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.file.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileData, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.file.update()
        assert file is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.file.update(
            file_data_list=[
                {
                    "id": "/example/folder/example_file.txt",
                    "attributes": {
                        "id": "id",
                        "classification": "U",
                        "classification_marking": "classificationMarking",
                        "created_by": "createdBy",
                        "created_date": "createdDate",
                        "delete_on": 0,
                        "description": "A new Example description",
                        "doc_title": "docTitle",
                        "doc_type": "docType",
                        "doi": ["string"],
                        "ellipse_lat": 0,
                        "ellipse_lon": 0,
                        "file_name": "fileName",
                        "intrinsic_title": "intrinsicTitle",
                        "keywords": "keywords",
                        "media_title": "mediaTitle",
                        "meta_info": "A new Example metaInfo",
                        "milgrid": "milgrid",
                        "milgrid_lat": 0,
                        "milgrid_lon": 0,
                        "modified_by": "modifiedBy",
                        "modified_date": "modifiedDate",
                        "name": "name",
                        "path": "path",
                        "read": "read",
                        "searchable": True,
                        "search_after": "searchAfter",
                        "serial_number": "serialNumber",
                        "size": 0,
                        "tags": ["string"],
                        "write": "write",
                    },
                    "content_action": "UPDATE",
                    "target_name": "targetName",
                    "target_path": "targetPath",
                    "type": "file",
                }
            ],
        )
        assert file is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.file.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.file.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.file.list(
            path="path",
        )
        assert_matches_type(AsyncOffsetPage[FileData], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.file.list(
            path="path",
            count=0,
            first_result=0,
            max_results=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[FileData], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.file.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncOffsetPage[FileData], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.file.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncOffsetPage[FileData], file, path=["response"])

        assert cast(Any, response.is_closed) is True
