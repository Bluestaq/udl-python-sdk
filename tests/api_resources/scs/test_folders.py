# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.shared import FileData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        folder = client.scs.folders.create(
            id="id",
            classification_marking="classificationMarking",
        )
        assert_matches_type(str, folder, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        folder = client.scs.folders.create(
            id="id",
            classification_marking="classificationMarking",
            description="description",
            read="read",
            tags="tags",
            write="write",
        )
        assert_matches_type(str, folder, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.scs.folders.with_raw_response.create(
            id="id",
            classification_marking="classificationMarking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(str, folder, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.scs.folders.with_streaming_response.create(
            id="id",
            classification_marking="classificationMarking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(str, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        folder = client.scs.folders.retrieve(
            id="id",
        )
        assert_matches_type(FileData, folder, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        folder = client.scs.folders.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FileData, folder, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.scs.folders.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FileData, folder, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.scs.folders.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FileData, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        folder = client.scs.folders.update()
        assert folder is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        folder = client.scs.folders.update(
            id="/example/folder/",
            attributes={
                "id": "id",
                "classification": "U",
                "classification_marking": "classificationMarking",
                "created_by": "createdBy",
                "created_date": "createdDate",
                "description": "A new Example Description",
                "doc_title": "docTitle",
                "doc_type": "docType",
                "doi": ["string"],
                "ellipse_lat": 0,
                "ellipse_lon": 0,
                "file_name": "fileName",
                "intrinsic_title": "intrinsicTitle",
                "keywords": "keywords",
                "media_title": "mediaTitle",
                "meta_info": "A new Example Meta Info",
                "milgrid": "milgrid",
                "milgrid_lat": 0,
                "milgrid_lon": 0,
                "modified_by": "modifiedBy",
                "modified_date": "modifiedDate",
                "name": "name",
                "path": "/example/folder/",
                "read": "read",
                "searchable": True,
                "search_after": "searchAfter",
                "serial_number": "serialNumber",
                "size": 0,
                "tags": ["string"],
                "write": "write",
            },
            content_action="UPDATE",
            target_name="targetName",
            target_path="targetPath",
            type="file",
        )
        assert folder is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.scs.folders.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.scs.folders.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        folder = await async_client.scs.folders.create(
            id="id",
            classification_marking="classificationMarking",
        )
        assert_matches_type(str, folder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        folder = await async_client.scs.folders.create(
            id="id",
            classification_marking="classificationMarking",
            description="description",
            read="read",
            tags="tags",
            write="write",
        )
        assert_matches_type(str, folder, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.folders.with_raw_response.create(
            id="id",
            classification_marking="classificationMarking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(str, folder, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.folders.with_streaming_response.create(
            id="id",
            classification_marking="classificationMarking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(str, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        folder = await async_client.scs.folders.retrieve(
            id="id",
        )
        assert_matches_type(FileData, folder, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        folder = await async_client.scs.folders.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FileData, folder, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.folders.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FileData, folder, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.folders.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FileData, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        folder = await async_client.scs.folders.update()
        assert folder is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        folder = await async_client.scs.folders.update(
            id="/example/folder/",
            attributes={
                "id": "id",
                "classification": "U",
                "classification_marking": "classificationMarking",
                "created_by": "createdBy",
                "created_date": "createdDate",
                "description": "A new Example Description",
                "doc_title": "docTitle",
                "doc_type": "docType",
                "doi": ["string"],
                "ellipse_lat": 0,
                "ellipse_lon": 0,
                "file_name": "fileName",
                "intrinsic_title": "intrinsicTitle",
                "keywords": "keywords",
                "media_title": "mediaTitle",
                "meta_info": "A new Example Meta Info",
                "milgrid": "milgrid",
                "milgrid_lat": 0,
                "milgrid_lon": 0,
                "modified_by": "modifiedBy",
                "modified_date": "modifiedDate",
                "name": "name",
                "path": "/example/folder/",
                "read": "read",
                "searchable": True,
                "search_after": "searchAfter",
                "serial_number": "serialNumber",
                "size": 0,
                "tags": ["string"],
                "write": "write",
            },
            content_action="UPDATE",
            target_name="targetName",
            target_path="targetPath",
            type="file",
        )
        assert folder is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.folders.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.folders.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True
