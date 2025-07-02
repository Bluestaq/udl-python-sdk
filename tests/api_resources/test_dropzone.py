# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    DropzoneQueryResponse,
    DropzoneTupleResponse,
    DropzoneRetrieveResponse,
    DropzoneQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDropzone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )
        assert dropzone is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
            id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_country_code="USA",
            alt_country_name="United States of America",
            approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            code="DZ",
            country_code="US",
            country_name="United States",
            expiration_date=parse_datetime("2022-12-09T16:00:00.123Z"),
            ext_identifier="1001",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            last_update=parse_datetime("2022-11-07T18:44:41.123Z"),
            length=549.1,
            majcom="United States Northern Command",
            nearest_loc="March AFB",
            operational_approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            point_name="CENTER POINT",
            radius=495.1,
            recert_date=parse_datetime("2022-07-05T16:00:00.123Z"),
            remark="The text of the remark.",
            state_abbr="CA",
            state_name="CALIFORNIA",
            survey_date=parse_datetime("2017-12-09T16:00:00.123Z"),
            width=549.1,
            zar_id="1001",
        )
        assert dropzone is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert dropzone is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.retrieve(
            id="id",
        )
        assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dropzone.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )
        assert dropzone is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
            body_id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_country_code="USA",
            alt_country_name="United States of America",
            approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            code="DZ",
            country_code="US",
            country_name="United States",
            expiration_date=parse_datetime("2022-12-09T16:00:00.123Z"),
            ext_identifier="1001",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            last_update=parse_datetime("2022-11-07T18:44:41.123Z"),
            length=549.1,
            majcom="United States Northern Command",
            nearest_loc="March AFB",
            operational_approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            point_name="CENTER POINT",
            radius=495.1,
            recert_date=parse_datetime("2022-07-05T16:00:00.123Z"),
            remark="The text of the remark.",
            state_abbr="CA",
            state_name="CALIFORNIA",
            survey_date=parse_datetime("2017-12-09T16:00:00.123Z"),
            width=549.1,
            zar_id="1001",
        )
        assert dropzone is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert dropzone is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.dropzone.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                lat=33.54,
                lon=-117.162,
                name="Viper DZ",
                source="Bluestaq",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.delete(
            "id",
        )
        assert dropzone is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert dropzone is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dropzone.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.count()
        assert_matches_type(str, dropzone, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, dropzone, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert_matches_type(str, dropzone, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert_matches_type(str, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )
        assert dropzone is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert dropzone is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.query()
        assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.query(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.query_help()
        assert_matches_type(DropzoneQueryHelpResponse, dropzone, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert_matches_type(DropzoneQueryHelpResponse, dropzone, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert_matches_type(DropzoneQueryHelpResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.tuple(
            columns="columns",
        )
        assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        dropzone = client.dropzone.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )
        assert dropzone is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.dropzone.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = response.parse()
        assert dropzone is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.dropzone.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDropzone:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )
        assert dropzone is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
            id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_country_code="USA",
            alt_country_name="United States of America",
            approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            code="DZ",
            country_code="US",
            country_name="United States",
            expiration_date=parse_datetime("2022-12-09T16:00:00.123Z"),
            ext_identifier="1001",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            last_update=parse_datetime("2022-11-07T18:44:41.123Z"),
            length=549.1,
            majcom="United States Northern Command",
            nearest_loc="March AFB",
            operational_approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            point_name="CENTER POINT",
            radius=495.1,
            recert_date=parse_datetime("2022-07-05T16:00:00.123Z"),
            remark="The text of the remark.",
            state_abbr="CA",
            state_name="CALIFORNIA",
            survey_date=parse_datetime("2017-12-09T16:00:00.123Z"),
            width=549.1,
            zar_id="1001",
        )
        assert dropzone is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert dropzone is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.retrieve(
            id="id",
        )
        assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert_matches_type(DropzoneRetrieveResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dropzone.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )
        assert dropzone is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
            body_id="3f28f60b-3a50-2aef-ac88-8e9d0e39912b",
            alt_country_code="USA",
            alt_country_name="United States of America",
            approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            code="DZ",
            country_code="US",
            country_name="United States",
            expiration_date=parse_datetime("2022-12-09T16:00:00.123Z"),
            ext_identifier="1001",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            last_update=parse_datetime("2022-11-07T18:44:41.123Z"),
            length=549.1,
            majcom="United States Northern Command",
            nearest_loc="March AFB",
            operational_approval_date=parse_datetime("2018-01-05T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            point_name="CENTER POINT",
            radius=495.1,
            recert_date=parse_datetime("2022-07-05T16:00:00.123Z"),
            remark="The text of the remark.",
            state_abbr="CA",
            state_name="CALIFORNIA",
            survey_date=parse_datetime("2017-12-09T16:00:00.123Z"),
            width=549.1,
            zar_id="1001",
        )
        assert dropzone is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert dropzone is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            lat=33.54,
            lon=-117.162,
            name="Viper DZ",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.dropzone.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                lat=33.54,
                lon=-117.162,
                name="Viper DZ",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.delete(
            "id",
        )
        assert dropzone is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert dropzone is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dropzone.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.count()
        assert_matches_type(str, dropzone, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, dropzone, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert_matches_type(str, dropzone, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert_matches_type(str, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )
        assert dropzone is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert dropzone is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.query()
        assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.query(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert_matches_type(DropzoneQueryResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.query_help()
        assert_matches_type(DropzoneQueryHelpResponse, dropzone, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert_matches_type(DropzoneQueryHelpResponse, dropzone, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert_matches_type(DropzoneQueryHelpResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.tuple(
            columns="columns",
        )
        assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert_matches_type(DropzoneTupleResponse, dropzone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        dropzone = await async_client.dropzone.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )
        assert dropzone is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.dropzone.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dropzone = await response.parse()
        assert dropzone is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.dropzone.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 33.54,
                    "lon": -117.162,
                    "name": "Viper DZ",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dropzone = await response.parse()
            assert dropzone is None

        assert cast(Any, response.is_closed) is True
