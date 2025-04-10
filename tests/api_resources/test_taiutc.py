# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    TaiutcListResponse,
    TaiutcTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.taiutc import TaiutcFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaiutc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert taiutc is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="TAIUTC-ID",
            multiplication_factor=0.001296,
            origin="THIRD_PARTY_DATASOURCE",
            raw_file_uri="/TAI/2019/01/22/4318471007562436-tai-utc.dat",
            tai_utc=1.422818,
        )
        assert taiutc is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert taiutc is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert taiutc is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="TAIUTC-ID",
            multiplication_factor=0.001296,
            origin="THIRD_PARTY_DATASOURCE",
            raw_file_uri="/TAI/2019/01/22/4318471007562436-tai-utc.dat",
            tai_utc=1.422818,
        )
        assert taiutc is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert taiutc is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.taiutc.with_raw_response.update(
                path_id="",
                adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.list(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TaiutcListResponse, taiutc, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.list(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert_matches_type(TaiutcListResponse, taiutc, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.list(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert_matches_type(TaiutcListResponse, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.delete(
            "id",
        )
        assert taiutc is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert taiutc is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.taiutc.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.count(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, taiutc, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.count(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert_matches_type(str, taiutc, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.count(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert_matches_type(str, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.get(
            "id",
        )
        assert_matches_type(TaiutcFull, taiutc, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert_matches_type(TaiutcFull, taiutc, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert_matches_type(TaiutcFull, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.taiutc.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.queryhelp()
        assert taiutc is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert taiutc is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        taiutc = client.taiutc.tuple(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(TaiutcTupleResponse, taiutc, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.taiutc.with_raw_response.tuple(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = response.parse()
        assert_matches_type(TaiutcTupleResponse, taiutc, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.taiutc.with_streaming_response.tuple(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = response.parse()
            assert_matches_type(TaiutcTupleResponse, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTaiutc:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert taiutc is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="TAIUTC-ID",
            multiplication_factor=0.001296,
            origin="THIRD_PARTY_DATASOURCE",
            raw_file_uri="/TAI/2019/01/22/4318471007562436-tai-utc.dat",
            tai_utc=1.422818,
        )
        assert taiutc is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert taiutc is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.create(
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert taiutc is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="TAIUTC-ID",
            multiplication_factor=0.001296,
            origin="THIRD_PARTY_DATASOURCE",
            raw_file_uri="/TAI/2019/01/22/4318471007562436-tai-utc.dat",
            tai_utc=1.422818,
        )
        assert taiutc is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert taiutc is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.update(
            path_id="id",
            adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.taiutc.with_raw_response.update(
                path_id="",
                adjustment_date=parse_datetime("2017-01-01T00:00:00.123Z"),
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.list(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TaiutcListResponse, taiutc, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.list(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert_matches_type(TaiutcListResponse, taiutc, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.list(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert_matches_type(TaiutcListResponse, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.delete(
            "id",
        )
        assert taiutc is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert taiutc is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.taiutc.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.count(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, taiutc, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.count(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert_matches_type(str, taiutc, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.count(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert_matches_type(str, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.get(
            "id",
        )
        assert_matches_type(TaiutcFull, taiutc, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert_matches_type(TaiutcFull, taiutc, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert_matches_type(TaiutcFull, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.taiutc.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.queryhelp()
        assert taiutc is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert taiutc is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert taiutc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        taiutc = await async_client.taiutc.tuple(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(TaiutcTupleResponse, taiutc, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.taiutc.with_raw_response.tuple(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taiutc = await response.parse()
        assert_matches_type(TaiutcTupleResponse, taiutc, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.taiutc.with_streaming_response.tuple(
            adjustment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taiutc = await response.parse()
            assert_matches_type(TaiutcTupleResponse, taiutc, path=["response"])

        assert cast(Any, response.is_closed) is True
