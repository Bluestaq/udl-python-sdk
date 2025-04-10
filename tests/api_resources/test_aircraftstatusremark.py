# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftstatusremark:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        aircraftstatusremark = client.aircraftstatusremark.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )
        assert aircraftstatusremark is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        aircraftstatusremark = client.aircraftstatusremark.update(
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
        assert aircraftstatusremark is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.aircraftstatusremark.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraftstatusremark = response.parse()
        assert aircraftstatusremark is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.aircraftstatusremark.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraftstatusremark = response.parse()
            assert aircraftstatusremark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.aircraftstatusremark.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
                source="Bluestaq",
                text="Remark text",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        aircraftstatusremark = client.aircraftstatusremark.delete(
            "id",
        )
        assert aircraftstatusremark is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.aircraftstatusremark.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraftstatusremark = response.parse()
        assert aircraftstatusremark is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.aircraftstatusremark.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraftstatusremark = response.parse()
            assert aircraftstatusremark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aircraftstatusremark.with_raw_response.delete(
                "",
            )


class TestAsyncAircraftstatusremark:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraftstatusremark = await async_client.aircraftstatusremark.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )
        assert aircraftstatusremark is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraftstatusremark = await async_client.aircraftstatusremark.update(
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
        assert aircraftstatusremark is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraftstatusremark.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraftstatusremark = await response.parse()
        assert aircraftstatusremark is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraftstatusremark.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
            source="Bluestaq",
            text="Remark text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraftstatusremark = await response.parse()
            assert aircraftstatusremark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.aircraftstatusremark.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_aircraft_status="388b1f64-ccff-4113-b049-3cf5542c2a42",
                source="Bluestaq",
                text="Remark text",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraftstatusremark = await async_client.aircraftstatusremark.delete(
            "id",
        )
        assert aircraftstatusremark is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.aircraftstatusremark.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraftstatusremark = await response.parse()
        assert aircraftstatusremark is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.aircraftstatusremark.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraftstatusremark = await response.parse()
            assert aircraftstatusremark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aircraftstatusremark.with_raw_response.delete(
                "",
            )
