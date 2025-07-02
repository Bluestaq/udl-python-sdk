# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbitListResponse,
    OnorbitTupleResponse,
    OnorbitQueryhelpResponse,
    OnorbitGetSignatureResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import OnorbitFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )
        assert onorbit is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
            alt_name="Alternate Name",
            category="Lunar",
            common_name="Example common name",
            constellation="Big Dipper",
            country_code="US",
            decay_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            id_on_orbit="ONORBIT-ID",
            intl_des="2021123ABC",
            launch_date=parse_date("2018-01-01"),
            launch_site_id="LAUNCHSITE-ID",
            lifetime_years=10,
            mission_number="Expedition 1",
            object_type="PAYLOAD",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert onorbit is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert onorbit is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert onorbit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )
        assert onorbit is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
            alt_name="Alternate Name",
            category="Lunar",
            common_name="Example common name",
            constellation="Big Dipper",
            country_code="US",
            decay_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            id_on_orbit="ONORBIT-ID",
            intl_des="2021123ABC",
            launch_date=parse_date("2018-01-01"),
            launch_site_id="LAUNCHSITE-ID",
            lifetime_years=10,
            mission_number="Expedition 1",
            object_type="PAYLOAD",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert onorbit is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert onorbit is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert onorbit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                sat_no=1,
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.list()
        assert_matches_type(SyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert_matches_type(SyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.delete(
            "id",
        )
        assert onorbit is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert onorbit is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert onorbit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.count()
        assert_matches_type(str, onorbit, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbit, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert_matches_type(str, onorbit, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert_matches_type(str, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.get(
            id="id",
        )
        assert_matches_type(OnorbitFull, onorbit, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitFull, onorbit, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert_matches_type(OnorbitFull, onorbit, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert_matches_type(OnorbitFull, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_get_signature(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.get_signature(
            id_on_orbit="idOnOrbit",
        )
        assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

    @parametrize
    def test_method_get_signature_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.get_signature(
            id_on_orbit="idOnOrbit",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

    @parametrize
    def test_raw_response_get_signature(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.get_signature(
            id_on_orbit="idOnOrbit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

    @parametrize
    def test_streaming_response_get_signature(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.get_signature(
            id_on_orbit="idOnOrbit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.queryhelp()
        assert_matches_type(OnorbitQueryhelpResponse, onorbit, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert_matches_type(OnorbitQueryhelpResponse, onorbit, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert_matches_type(OnorbitQueryhelpResponse, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbit = client.onorbit.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = response.parse()
        assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = response.parse()
            assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnorbit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )
        assert onorbit is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
            alt_name="Alternate Name",
            category="Lunar",
            common_name="Example common name",
            constellation="Big Dipper",
            country_code="US",
            decay_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            id_on_orbit="ONORBIT-ID",
            intl_des="2021123ABC",
            launch_date=parse_date("2018-01-01"),
            launch_site_id="LAUNCHSITE-ID",
            lifetime_years=10,
            mission_number="Expedition 1",
            object_type="PAYLOAD",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert onorbit is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert onorbit is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert onorbit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )
        assert onorbit is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
            alt_name="Alternate Name",
            category="Lunar",
            common_name="Example common name",
            constellation="Big Dipper",
            country_code="US",
            decay_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            id_on_orbit="ONORBIT-ID",
            intl_des="2021123ABC",
            launch_date=parse_date("2018-01-01"),
            launch_site_id="LAUNCHSITE-ID",
            lifetime_years=10,
            mission_number="Expedition 1",
            object_type="PAYLOAD",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert onorbit is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert onorbit is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.update(
            id="id",
            classification_marking="U",
            data_mode="TEST",
            sat_no=1,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert onorbit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.with_raw_response.update(
                id="",
                classification_marking="U",
                data_mode="TEST",
                sat_no=1,
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.list()
        assert_matches_type(AsyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert_matches_type(AsyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert_matches_type(AsyncOffsetPage[OnorbitListResponse], onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.delete(
            "id",
        )
        assert onorbit is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert onorbit is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert onorbit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.count()
        assert_matches_type(str, onorbit, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbit, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert_matches_type(str, onorbit, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert_matches_type(str, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.get(
            id="id",
        )
        assert_matches_type(OnorbitFull, onorbit, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitFull, onorbit, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert_matches_type(OnorbitFull, onorbit, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert_matches_type(OnorbitFull, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_get_signature(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.get_signature(
            id_on_orbit="idOnOrbit",
        )
        assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

    @parametrize
    async def test_method_get_signature_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.get_signature(
            id_on_orbit="idOnOrbit",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

    @parametrize
    async def test_raw_response_get_signature(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.get_signature(
            id_on_orbit="idOnOrbit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

    @parametrize
    async def test_streaming_response_get_signature(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.get_signature(
            id_on_orbit="idOnOrbit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert_matches_type(OnorbitGetSignatureResponse, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.queryhelp()
        assert_matches_type(OnorbitQueryhelpResponse, onorbit, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert_matches_type(OnorbitQueryhelpResponse, onorbit, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert_matches_type(OnorbitQueryhelpResponse, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbit = await async_client.onorbit.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbit = await response.parse()
        assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbit = await response.parse()
            assert_matches_type(OnorbitTupleResponse, onorbit, path=["response"])

        assert cast(Any, response.is_closed) is True
