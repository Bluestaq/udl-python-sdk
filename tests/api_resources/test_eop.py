# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EopAbridged,
    EopListTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import EopFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert eop is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="EOP-ID",
            d_epsilon=-0.917,
            d_epsilon_b=-1.7,
            d_epsilon_unc=0.165,
            d_psi=-10.437,
            d_psib=-9.9,
            d_psi_unc=0.507,
            d_x=-0.086,
            d_xb=0.129,
            d_x_unc=0.202,
            d_y=0.13,
            d_yb=-0.653,
            d_y_unc=0.165,
            lod=1.8335,
            lod_unc=0.0201,
            nutation_state="I",
            origin="THIRD_PARTY_DATASOURCE",
            polar_motion_state="I",
            polar_motion_x=0.182987,
            polar_motion_xb=0.1824,
            polar_motion_x_unc=0.000672,
            polar_motion_y=0.168775,
            polar_motion_yb=0.1679,
            polar_motion_y_unc=0.000345,
            precession_nutation_std="IAU1980",
            raw_file_uri="Example URI",
            ut1_utc=-0.1251659,
            ut1_utcb=-0.1253,
            ut1_utc_state="I",
            ut1_utc_unc=0.0000207,
        )
        assert eop is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert eop is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.retrieve(
            id="id",
        )
        assert_matches_type(EopFull, eop, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EopFull, eop, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert_matches_type(EopFull, eop, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert_matches_type(EopFull, eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.eop.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert eop is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="EOP-ID",
            d_epsilon=-0.917,
            d_epsilon_b=-1.7,
            d_epsilon_unc=0.165,
            d_psi=-10.437,
            d_psib=-9.9,
            d_psi_unc=0.507,
            d_x=-0.086,
            d_xb=0.129,
            d_x_unc=0.202,
            d_y=0.13,
            d_yb=-0.653,
            d_y_unc=0.165,
            lod=1.8335,
            lod_unc=0.0201,
            nutation_state="I",
            origin="THIRD_PARTY_DATASOURCE",
            polar_motion_state="I",
            polar_motion_x=0.182987,
            polar_motion_xb=0.1824,
            polar_motion_x_unc=0.000672,
            polar_motion_y=0.168775,
            polar_motion_yb=0.1679,
            polar_motion_y_unc=0.000345,
            precession_nutation_std="IAU1980",
            raw_file_uri="Example URI",
            ut1_utc=-0.1251659,
            ut1_utcb=-0.1253,
            ut1_utc_state="I",
            ut1_utc_unc=0.0000207,
        )
        assert eop is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert eop is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.eop.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EopAbridged], eop, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EopAbridged], eop, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert_matches_type(SyncOffsetPage[EopAbridged], eop, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert_matches_type(SyncOffsetPage[EopAbridged], eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.delete(
            "id",
        )
        assert eop is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert eop is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.eop.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, eop, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, eop, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert_matches_type(str, eop, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert_matches_type(str, eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_tuple(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EopListTupleResponse, eop, path=["response"])

    @parametrize
    def test_method_list_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EopListTupleResponse, eop, path=["response"])

    @parametrize
    def test_raw_response_list_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert_matches_type(EopListTupleResponse, eop, path=["response"])

    @parametrize
    def test_streaming_response_list_tuple(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert_matches_type(EopListTupleResponse, eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        eop = client.eop.queryhelp()
        assert eop is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.eop.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = response.parse()
        assert eop is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.eop.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert eop is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="EOP-ID",
            d_epsilon=-0.917,
            d_epsilon_b=-1.7,
            d_epsilon_unc=0.165,
            d_psi=-10.437,
            d_psib=-9.9,
            d_psi_unc=0.507,
            d_x=-0.086,
            d_xb=0.129,
            d_x_unc=0.202,
            d_y=0.13,
            d_yb=-0.653,
            d_y_unc=0.165,
            lod=1.8335,
            lod_unc=0.0201,
            nutation_state="I",
            origin="THIRD_PARTY_DATASOURCE",
            polar_motion_state="I",
            polar_motion_x=0.182987,
            polar_motion_xb=0.1824,
            polar_motion_x_unc=0.000672,
            polar_motion_y=0.168775,
            polar_motion_yb=0.1679,
            polar_motion_y_unc=0.000345,
            precession_nutation_std="IAU1980",
            raw_file_uri="Example URI",
            ut1_utc=-0.1251659,
            ut1_utcb=-0.1253,
            ut1_utc_state="I",
            ut1_utc_unc=0.0000207,
        )
        assert eop is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert eop is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.retrieve(
            id="id",
        )
        assert_matches_type(EopFull, eop, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EopFull, eop, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert_matches_type(EopFull, eop, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert_matches_type(EopFull, eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.eop.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert eop is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="EOP-ID",
            d_epsilon=-0.917,
            d_epsilon_b=-1.7,
            d_epsilon_unc=0.165,
            d_psi=-10.437,
            d_psib=-9.9,
            d_psi_unc=0.507,
            d_x=-0.086,
            d_xb=0.129,
            d_x_unc=0.202,
            d_y=0.13,
            d_yb=-0.653,
            d_y_unc=0.165,
            lod=1.8335,
            lod_unc=0.0201,
            nutation_state="I",
            origin="THIRD_PARTY_DATASOURCE",
            polar_motion_state="I",
            polar_motion_x=0.182987,
            polar_motion_xb=0.1824,
            polar_motion_x_unc=0.000672,
            polar_motion_y=0.168775,
            polar_motion_yb=0.1679,
            polar_motion_y_unc=0.000345,
            precession_nutation_std="IAU1980",
            raw_file_uri="Example URI",
            ut1_utc=-0.1251659,
            ut1_utcb=-0.1253,
            ut1_utc_state="I",
            ut1_utc_unc=0.0000207,
        )
        assert eop is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert eop is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.eop.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                eop_date=parse_datetime("2018-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EopAbridged], eop, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EopAbridged], eop, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert_matches_type(AsyncOffsetPage[EopAbridged], eop, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.list(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert_matches_type(AsyncOffsetPage[EopAbridged], eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.delete(
            "id",
        )
        assert eop is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert eop is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.eop.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, eop, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, eop, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert_matches_type(str, eop, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.count(
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert_matches_type(str, eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EopListTupleResponse, eop, path=["response"])

    @parametrize
    async def test_method_list_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EopListTupleResponse, eop, path=["response"])

    @parametrize
    async def test_raw_response_list_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert_matches_type(EopListTupleResponse, eop, path=["response"])

    @parametrize
    async def test_streaming_response_list_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.list_tuple(
            columns="columns",
            eop_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert_matches_type(EopListTupleResponse, eop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        eop = await async_client.eop.queryhelp()
        assert eop is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eop.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eop = await response.parse()
        assert eop is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eop.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eop = await response.parse()
            assert eop is None

        assert cast(Any, response.is_closed) is True
