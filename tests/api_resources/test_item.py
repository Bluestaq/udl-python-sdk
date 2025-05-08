# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ItemGetResponse,
    ItemListResponse,
    ItemTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        item = client.item.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )
        assert item is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        item = client.item.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
            id="22f1f6da-a568-655a-ea37-76d013d04853",
            acc_sys_keys=["System key1", "System key2"],
            acc_sys_notes="Accepting System Notes",
            acc_system="Accepting System",
            acc_sys_values=["System value1", "System value2"],
            airdrop=True,
            alt_data_format="Alt Data Format",
            cargo_type="PALLET",
            centerline_offset=3.1,
            cg=112.014,
            commodity_code="2304116",
            commodity_sys="STCC",
            container=True,
            departure="CHS",
            destination="RMS",
            dv_code="DV-2",
            fs=412.1,
            haz_codes=[1.1, 1.2],
            height=1.1,
            id_air_load_plan="1038c389-d38e-270f-51cc-6a12e905abe8",
            item_contains=["2UJ8843K", "745YV1T65"],
            keys=["key1", "key2"],
            last_arr_date=parse_date("2023-03-13"),
            length=1.1,
            moment=4000.1,
            name="Product Name",
            net_exp_wt=51.437,
            notes="Example notes",
            num_pallet_pos=2,
            origin="THIRD_PARTY_DATASOURCE",
            product_code="530500234",
            product_sys="NSN",
            receiving_branch="Air Force",
            receiving_unit="50 SBN",
            sc_gen_tool="bID",
            tcn="M1358232245912XXX",
            uln="T01ME01",
            values=["value1", "value2"],
            volume=7.8902,
            weight=5443.335,
            weight_ts=parse_datetime("2023-03-13T16:06:00.123Z"),
            width=1.1,
        )
        assert item is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        item = client.item.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )
        assert item is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        item = client.item.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
            body_id="22f1f6da-a568-655a-ea37-76d013d04853",
            acc_sys_keys=["System key1", "System key2"],
            acc_sys_notes="Accepting System Notes",
            acc_system="Accepting System",
            acc_sys_values=["System value1", "System value2"],
            airdrop=True,
            alt_data_format="Alt Data Format",
            cargo_type="PALLET",
            centerline_offset=3.1,
            cg=112.014,
            commodity_code="2304116",
            commodity_sys="STCC",
            container=True,
            departure="CHS",
            destination="RMS",
            dv_code="DV-2",
            fs=412.1,
            haz_codes=[1.1, 1.2],
            height=1.1,
            id_air_load_plan="1038c389-d38e-270f-51cc-6a12e905abe8",
            item_contains=["2UJ8843K", "745YV1T65"],
            keys=["key1", "key2"],
            last_arr_date=parse_date("2023-03-13"),
            length=1.1,
            moment=4000.1,
            name="Product Name",
            net_exp_wt=51.437,
            notes="Example notes",
            num_pallet_pos=2,
            origin="THIRD_PARTY_DATASOURCE",
            product_code="530500234",
            product_sys="NSN",
            receiving_branch="Air Force",
            receiving_unit="50 SBN",
            sc_gen_tool="bID",
            tcn="M1358232245912XXX",
            uln="T01ME01",
            values=["value1", "value2"],
            volume=7.8902,
            weight=5443.335,
            weight_ts=parse_datetime("2023-03-13T16:06:00.123Z"),
            width=1.1,
        )
        assert item is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.item.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                scan_code="12345ABCD",
                source="Bluestaq",
                type="CARGO",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        item = client.item.list()
        assert_matches_type(SyncOffsetPage[ItemListResponse], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        item = client.item.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ItemListResponse], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncOffsetPage[ItemListResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncOffsetPage[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        item = client.item.delete(
            "id",
        )
        assert item is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.item.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        item = client.item.count()
        assert_matches_type(str, item, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        item = client.item.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, item, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(str, item, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(str, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        item = client.item.get(
            id="id",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        item = client.item.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.item.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        item = client.item.queryhelp()
        assert item is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        item = client.item.tuple(
            columns="columns",
        )
        assert_matches_type(ItemTupleResponse, item, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        item = client.item.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemTupleResponse, item, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemTupleResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemTupleResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        item = client.item.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "12345ABCD",
                    "source": "Bluestaq",
                    "type": "CARGO",
                }
            ],
        )
        assert item is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.item.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "12345ABCD",
                    "source": "Bluestaq",
                    "type": "CARGO",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.item.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "12345ABCD",
                    "source": "Bluestaq",
                    "type": "CARGO",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True


class TestAsyncItem:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )
        assert item is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
            id="22f1f6da-a568-655a-ea37-76d013d04853",
            acc_sys_keys=["System key1", "System key2"],
            acc_sys_notes="Accepting System Notes",
            acc_system="Accepting System",
            acc_sys_values=["System value1", "System value2"],
            airdrop=True,
            alt_data_format="Alt Data Format",
            cargo_type="PALLET",
            centerline_offset=3.1,
            cg=112.014,
            commodity_code="2304116",
            commodity_sys="STCC",
            container=True,
            departure="CHS",
            destination="RMS",
            dv_code="DV-2",
            fs=412.1,
            haz_codes=[1.1, 1.2],
            height=1.1,
            id_air_load_plan="1038c389-d38e-270f-51cc-6a12e905abe8",
            item_contains=["2UJ8843K", "745YV1T65"],
            keys=["key1", "key2"],
            last_arr_date=parse_date("2023-03-13"),
            length=1.1,
            moment=4000.1,
            name="Product Name",
            net_exp_wt=51.437,
            notes="Example notes",
            num_pallet_pos=2,
            origin="THIRD_PARTY_DATASOURCE",
            product_code="530500234",
            product_sys="NSN",
            receiving_branch="Air Force",
            receiving_unit="50 SBN",
            sc_gen_tool="bID",
            tcn="M1358232245912XXX",
            uln="T01ME01",
            values=["value1", "value2"],
            volume=7.8902,
            weight=5443.335,
            weight_ts=parse_datetime("2023-03-13T16:06:00.123Z"),
            width=1.1,
        )
        assert item is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )
        assert item is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
            body_id="22f1f6da-a568-655a-ea37-76d013d04853",
            acc_sys_keys=["System key1", "System key2"],
            acc_sys_notes="Accepting System Notes",
            acc_system="Accepting System",
            acc_sys_values=["System value1", "System value2"],
            airdrop=True,
            alt_data_format="Alt Data Format",
            cargo_type="PALLET",
            centerline_offset=3.1,
            cg=112.014,
            commodity_code="2304116",
            commodity_sys="STCC",
            container=True,
            departure="CHS",
            destination="RMS",
            dv_code="DV-2",
            fs=412.1,
            haz_codes=[1.1, 1.2],
            height=1.1,
            id_air_load_plan="1038c389-d38e-270f-51cc-6a12e905abe8",
            item_contains=["2UJ8843K", "745YV1T65"],
            keys=["key1", "key2"],
            last_arr_date=parse_date("2023-03-13"),
            length=1.1,
            moment=4000.1,
            name="Product Name",
            net_exp_wt=51.437,
            notes="Example notes",
            num_pallet_pos=2,
            origin="THIRD_PARTY_DATASOURCE",
            product_code="530500234",
            product_sys="NSN",
            receiving_branch="Air Force",
            receiving_unit="50 SBN",
            sc_gen_tool="bID",
            tcn="M1358232245912XXX",
            uln="T01ME01",
            values=["value1", "value2"],
            volume=7.8902,
            weight=5443.335,
            weight_ts=parse_datetime("2023-03-13T16:06:00.123Z"),
            width=1.1,
        )
        assert item is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            scan_code="12345ABCD",
            source="Bluestaq",
            type="CARGO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.item.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                scan_code="12345ABCD",
                source="Bluestaq",
                type="CARGO",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.list()
        assert_matches_type(AsyncOffsetPage[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AsyncOffsetPage[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncOffsetPage[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.delete(
            "id",
        )
        assert item is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.item.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.count()
        assert_matches_type(str, item, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, item, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(str, item, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(str, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.get(
            id="id",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.item.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.queryhelp()
        assert item is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.tuple(
            columns="columns",
        )
        assert_matches_type(ItemTupleResponse, item, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemTupleResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemTupleResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemTupleResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        item = await async_client.item.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "12345ABCD",
                    "source": "Bluestaq",
                    "type": "CARGO",
                }
            ],
        )
        assert item is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "12345ABCD",
                    "source": "Bluestaq",
                    "type": "CARGO",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "12345ABCD",
                    "source": "Bluestaq",
                    "type": "CARGO",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True
