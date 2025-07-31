# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AircraftstatusremarkAbridged,
    AircraftStatusRemarkTupleResponse,
    AircraftStatusRemarkQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AircraftstatusremarkFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftStatusRemarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )
        assert aircraft_status_remark is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            alt_rmk_id="GDSSBL022307131714250077",
            last_updated_at=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_updated_by="JOHN SMITH",
            name="DISCREPANCY - 202297501",
            origin="THIRD_PARTY_DATASOURCE",
            timestamp=parse_datetime("2024-01-01T15:00:00.123Z"),
        )
        assert aircraft_status_remark is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert aircraft_status_remark is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert aircraft_status_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.retrieve(
            id="id",
        )
        assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraft_status_remarks.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )
        assert aircraft_status_remark is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            alt_rmk_id="GDSSBL022307131714250077",
            last_updated_at=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_updated_by="JOHN SMITH",
            name="DISCREPANCY - 202297501",
            origin="THIRD_PARTY_DATASOURCE",
            timestamp=parse_datetime("2024-01-01T15:00:00.123Z"),
        )
        assert aircraft_status_remark is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert aircraft_status_remark is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert aircraft_status_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.aircraft_status_remarks.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
                source="Bluestaq",
                text="Remark text",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.list()
        assert_matches_type(SyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert_matches_type(SyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert_matches_type(SyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.delete(
            "id",
        )
        assert aircraft_status_remark is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert aircraft_status_remark is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert aircraft_status_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraft_status_remarks.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.count()
        assert_matches_type(str, aircraft_status_remark, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aircraft_status_remark, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert_matches_type(str, aircraft_status_remark, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert_matches_type(str, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.queryhelp()
        assert_matches_type(AircraftStatusRemarkQueryhelpResponse, aircraft_status_remark, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert_matches_type(AircraftStatusRemarkQueryhelpResponse, aircraft_status_remark, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert_matches_type(AircraftStatusRemarkQueryhelpResponse, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.tuple(
            columns="columns",
        )
        assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraft_status_remark = client.aircraft_status_remarks.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.aircraft_status_remarks.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = response.parse()
        assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.aircraft_status_remarks.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = response.parse()
            assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAircraftStatusRemarks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )
        assert aircraft_status_remark is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            alt_rmk_id="GDSSBL022307131714250077",
            last_updated_at=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_updated_by="JOHN SMITH",
            name="DISCREPANCY - 202297501",
            origin="THIRD_PARTY_DATASOURCE",
            timestamp=parse_datetime("2024-01-01T15:00:00.123Z"),
        )
        assert aircraft_status_remark is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert aircraft_status_remark is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert aircraft_status_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.retrieve(
            id="id",
        )
        assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert_matches_type(AircraftstatusremarkFull, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraft_status_remarks.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )
        assert aircraft_status_remark is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            alt_rmk_id="GDSSBL022307131714250077",
            last_updated_at=parse_datetime("2024-01-01T16:00:00.123Z"),
            last_updated_by="JOHN SMITH",
            name="DISCREPANCY - 202297501",
            origin="THIRD_PARTY_DATASOURCE",
            timestamp=parse_datetime("2024-01-01T15:00:00.123Z"),
        )
        assert aircraft_status_remark is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert aircraft_status_remark is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert aircraft_status_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.aircraft_status_remarks.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
                source="Bluestaq",
                text="Remark text",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.list()
        assert_matches_type(AsyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert_matches_type(AsyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[AircraftstatusremarkAbridged], aircraft_status_remark, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.delete(
            "id",
        )
        assert aircraft_status_remark is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert aircraft_status_remark is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert aircraft_status_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraft_status_remarks.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.count()
        assert_matches_type(str, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert_matches_type(str, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert_matches_type(str, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.queryhelp()
        assert_matches_type(AircraftStatusRemarkQueryhelpResponse, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert_matches_type(AircraftStatusRemarkQueryhelpResponse, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert_matches_type(AircraftStatusRemarkQueryhelpResponse, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.tuple(
            columns="columns",
        )
        assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_status_remark = await async_client.aircraft_status_remarks.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraft_status_remarks.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_status_remark = await response.parse()
        assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraft_status_remarks.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_status_remark = await response.parse()
            assert_matches_type(AircraftStatusRemarkTupleResponse, aircraft_status_remark, path=["response"])

        assert cast(Any, response.is_closed) is True
