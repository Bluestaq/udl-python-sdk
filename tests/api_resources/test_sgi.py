# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SgiGetResponse,
    SgiListResponse,
    SgiTupleResponse,
    SgiQueryhelpResponse,
    SgiGetDataByEffectiveAsOfDateResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSgi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert sgi is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="SGI-ID",
            analyzer_attenuation=5.1,
            ap=1.23,
            ap_duration=3,
            coeff_degree=[1, 2, 3],
            coeff_order=[1, 2, 3],
            ctce=[1.23, 342.3, 1.32],
            ctci=[1.23, 342.3, 1.32],
            dst=1.23,
            dtc=1.23,
            e10=1.23,
            e54=1.23,
            f10=1.23,
            f10_high=187.5,
            f10_low=185.5,
            f54=1.23,
            f81=1.23,
            frequencies=[25, 25.125, 25.25, 25.375, 25.5, 25.625, 25.75, 25.875],
            gamma=25,
            id_sensor="57c96c97-e076-48af-a068-73ee2cb37e65",
            k_index=1,
            kp=4.66,
            kp_duration=3,
            m10=1.23,
            m54=1.23,
            mode=1,
            norm_factor=2.12679e-7,
            observed_baseline=[15, 32, 25, 134, 0, 6, 19, 8],
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            powers=[67.1, 65.2, 68.1, 74.3, 68.1, 96.4, 97.3, 68.1],
            precedence="R",
            raw_file_uri="rawFileURI",
            rb_duration=24,
            rb_index=1.02947164506,
            rb_region_code=2,
            s10=1.23,
            s54=1.23,
            state="I",
            station_name="Boulder",
            stce=[1.23, 342.3, 1.32],
            stci=[1.23, 342.3, 1.32],
            sunspot_num=151.1,
            sunspot_num_high=152.1,
            sunspot_num_low=150.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            type="JBH09",
            y10=1.23,
            y54=1.23,
        )
        assert sgi is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert sgi is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert sgi is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="SGI-ID",
            analyzer_attenuation=5.1,
            ap=1.23,
            ap_duration=3,
            coeff_degree=[1, 2, 3],
            coeff_order=[1, 2, 3],
            ctce=[1.23, 342.3, 1.32],
            ctci=[1.23, 342.3, 1.32],
            dst=1.23,
            dtc=1.23,
            e10=1.23,
            e54=1.23,
            f10=1.23,
            f10_high=187.5,
            f10_low=185.5,
            f54=1.23,
            f81=1.23,
            frequencies=[25, 25.125, 25.25, 25.375, 25.5, 25.625, 25.75, 25.875],
            gamma=25,
            id_sensor="57c96c97-e076-48af-a068-73ee2cb37e65",
            k_index=1,
            kp=4.66,
            kp_duration=3,
            m10=1.23,
            m54=1.23,
            mode=1,
            norm_factor=2.12679e-7,
            observed_baseline=[15, 32, 25, 134, 0, 6, 19, 8],
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            powers=[67.1, 65.2, 68.1, 74.3, 68.1, 96.4, 97.3, 68.1],
            precedence="R",
            raw_file_uri="rawFileURI",
            rb_duration=24,
            rb_index=1.02947164506,
            rb_region_code=2,
            s10=1.23,
            s54=1.23,
            state="I",
            station_name="Boulder",
            stce=[1.23, 342.3, 1.32],
            stci=[1.23, 342.3, 1.32],
            sunspot_num=151.1,
            sunspot_num_high=152.1,
            sunspot_num_low=150.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            type="JBH09",
            y10=1.23,
            y54=1.23,
        )
        assert sgi is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert sgi is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sgi.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
                sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.list()
        assert_matches_type(SyncOffsetPage[SgiListResponse], sgi, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.list(
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[SgiListResponse], sgi, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert_matches_type(SyncOffsetPage[SgiListResponse], sgi, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert_matches_type(SyncOffsetPage[SgiListResponse], sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.delete(
            "id",
        )
        assert sgi is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert sgi is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sgi.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.count()
        assert_matches_type(str, sgi, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.count(
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sgi, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert_matches_type(str, sgi, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert_matches_type(str, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert sgi is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert sgi is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.get(
            id="id",
        )
        assert_matches_type(SgiGetResponse, sgi, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SgiGetResponse, sgi, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert_matches_type(SgiGetResponse, sgi, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert_matches_type(SgiGetResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sgi.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_get_data_by_effective_as_of_date(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.get_data_by_effective_as_of_date()
        assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

    @parametrize
    def test_method_get_data_by_effective_as_of_date_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.get_data_by_effective_as_of_date(
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

    @parametrize
    def test_raw_response_get_data_by_effective_as_of_date(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.get_data_by_effective_as_of_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

    @parametrize
    def test_streaming_response_get_data_by_effective_as_of_date(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.get_data_by_effective_as_of_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.queryhelp()
        assert_matches_type(SgiQueryhelpResponse, sgi, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert_matches_type(SgiQueryhelpResponse, sgi, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert_matches_type(SgiQueryhelpResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.tuple(
            columns="columns",
        )
        assert_matches_type(SgiTupleResponse, sgi, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.tuple(
            columns="columns",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SgiTupleResponse, sgi, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert_matches_type(SgiTupleResponse, sgi, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert_matches_type(SgiTupleResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        sgi = client.sgi.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert sgi is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.sgi.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = response.parse()
        assert sgi is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.sgi.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSgi:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert sgi is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="SGI-ID",
            analyzer_attenuation=5.1,
            ap=1.23,
            ap_duration=3,
            coeff_degree=[1, 2, 3],
            coeff_order=[1, 2, 3],
            ctce=[1.23, 342.3, 1.32],
            ctci=[1.23, 342.3, 1.32],
            dst=1.23,
            dtc=1.23,
            e10=1.23,
            e54=1.23,
            f10=1.23,
            f10_high=187.5,
            f10_low=185.5,
            f54=1.23,
            f81=1.23,
            frequencies=[25, 25.125, 25.25, 25.375, 25.5, 25.625, 25.75, 25.875],
            gamma=25,
            id_sensor="57c96c97-e076-48af-a068-73ee2cb37e65",
            k_index=1,
            kp=4.66,
            kp_duration=3,
            m10=1.23,
            m54=1.23,
            mode=1,
            norm_factor=2.12679e-7,
            observed_baseline=[15, 32, 25, 134, 0, 6, 19, 8],
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            powers=[67.1, 65.2, 68.1, 74.3, 68.1, 96.4, 97.3, 68.1],
            precedence="R",
            raw_file_uri="rawFileURI",
            rb_duration=24,
            rb_index=1.02947164506,
            rb_region_code=2,
            s10=1.23,
            s54=1.23,
            state="I",
            station_name="Boulder",
            stce=[1.23, 342.3, 1.32],
            stci=[1.23, 342.3, 1.32],
            sunspot_num=151.1,
            sunspot_num_high=152.1,
            sunspot_num_low=150.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            type="JBH09",
            y10=1.23,
            y54=1.23,
        )
        assert sgi is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert sgi is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert sgi is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            body_id="SGI-ID",
            analyzer_attenuation=5.1,
            ap=1.23,
            ap_duration=3,
            coeff_degree=[1, 2, 3],
            coeff_order=[1, 2, 3],
            ctce=[1.23, 342.3, 1.32],
            ctci=[1.23, 342.3, 1.32],
            dst=1.23,
            dtc=1.23,
            e10=1.23,
            e54=1.23,
            f10=1.23,
            f10_high=187.5,
            f10_low=185.5,
            f54=1.23,
            f81=1.23,
            frequencies=[25, 25.125, 25.25, 25.375, 25.5, 25.625, 25.75, 25.875],
            gamma=25,
            id_sensor="57c96c97-e076-48af-a068-73ee2cb37e65",
            k_index=1,
            kp=4.66,
            kp_duration=3,
            m10=1.23,
            m54=1.23,
            mode=1,
            norm_factor=2.12679e-7,
            observed_baseline=[15, 32, 25, 134, 0, 6, 19, 8],
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            powers=[67.1, 65.2, 68.1, 74.3, 68.1, 96.4, 97.3, 68.1],
            precedence="R",
            raw_file_uri="rawFileURI",
            rb_duration=24,
            rb_index=1.02947164506,
            rb_region_code=2,
            s10=1.23,
            s54=1.23,
            state="I",
            station_name="Boulder",
            stce=[1.23, 342.3, 1.32],
            stci=[1.23, 342.3, 1.32],
            sunspot_num=151.1,
            sunspot_num_high=152.1,
            sunspot_num_low=150.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="TRANSACTION-ID",
            type="JBH09",
            y10=1.23,
            y54=1.23,
        )
        assert sgi is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert sgi is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sgi.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                effective_date=parse_datetime("2018-01-01T16:00:00.123Z"),
                sgi_date=parse_datetime("2018-01-01T16:00:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.list()
        assert_matches_type(AsyncOffsetPage[SgiListResponse], sgi, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.list(
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[SgiListResponse], sgi, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert_matches_type(AsyncOffsetPage[SgiListResponse], sgi, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert_matches_type(AsyncOffsetPage[SgiListResponse], sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.delete(
            "id",
        )
        assert sgi is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert sgi is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sgi.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.count()
        assert_matches_type(str, sgi, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.count(
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sgi, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert_matches_type(str, sgi, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert_matches_type(str, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert sgi is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert sgi is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.get(
            id="id",
        )
        assert_matches_type(SgiGetResponse, sgi, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SgiGetResponse, sgi, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert_matches_type(SgiGetResponse, sgi, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert_matches_type(SgiGetResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sgi.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_get_data_by_effective_as_of_date(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.get_data_by_effective_as_of_date()
        assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

    @parametrize
    async def test_method_get_data_by_effective_as_of_date_with_all_params(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        sgi = await async_client.sgi.get_data_by_effective_as_of_date(
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

    @parametrize
    async def test_raw_response_get_data_by_effective_as_of_date(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.get_data_by_effective_as_of_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

    @parametrize
    async def test_streaming_response_get_data_by_effective_as_of_date(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        async with async_client.sgi.with_streaming_response.get_data_by_effective_as_of_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert_matches_type(SgiGetDataByEffectiveAsOfDateResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.queryhelp()
        assert_matches_type(SgiQueryhelpResponse, sgi, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert_matches_type(SgiQueryhelpResponse, sgi, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert_matches_type(SgiQueryhelpResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.tuple(
            columns="columns",
        )
        assert_matches_type(SgiTupleResponse, sgi, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.tuple(
            columns="columns",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
            sgi_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SgiTupleResponse, sgi, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert_matches_type(SgiTupleResponse, sgi, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert_matches_type(SgiTupleResponse, sgi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        sgi = await async_client.sgi.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert sgi is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sgi.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sgi = await response.parse()
        assert sgi is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sgi.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "effective_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "sgi_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sgi = await response.parse()
            assert sgi is None

        assert cast(Any, response.is_closed) is True
