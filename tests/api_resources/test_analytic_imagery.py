# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AnalyticImageryFull,
    AnalyticImageryListResponse,
    AnalyticImageryTupleResponse,
    AnalyticImageryHistoryResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalyticImagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert analytic_imagery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            agjson="agjson",
            andims=0,
            ann_lims=[[0]],
            ann_text=["string"],
            area="area",
            asrid=0,
            atext="atext",
            atype="atype",
            checksum_value="checksumValue",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            data_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            data_stop=parse_datetime("2019-12-27T18:11:19.117Z"),
            image_set_id="imageSetId",
            image_set_length=0,
            img_height=0,
            img_width=0,
            keywords=["string"],
            origin="origin",
            orig_network="origNetwork",
            sat_id=["string"],
            sat_id_conf=[0],
            sequence_id=0,
            source_dl="sourceDL",
            src_ids=["string"],
            src_typs=["string"],
            tags=["string"],
            transaction_id="transactionId",
            x_units="xUnits",
            y_units="yUnits",
            z_units="zUnits",
        )
        assert analytic_imagery is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert analytic_imagery is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.retrieve(
            "id",
        )
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.analytic_imagery.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryListResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryListResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryListResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history_aodr(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert analytic_imagery is None

    @parametrize
    def test_method_history_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert analytic_imagery is None

    @parametrize
    def test_raw_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert analytic_imagery is None

    @parametrize
    def test_streaming_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history_count(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_history_count(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_history_count(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.queryhelp()
        assert analytic_imagery is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert analytic_imagery is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        analytic_imagery = client.analytic_imagery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.analytic_imagery.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = response.parse()
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.analytic_imagery.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = response.parse()
            assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalyticImagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert analytic_imagery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            agjson="agjson",
            andims=0,
            ann_lims=[[0]],
            ann_text=["string"],
            area="area",
            asrid=0,
            atext="atext",
            atype="atype",
            checksum_value="checksumValue",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            data_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            data_stop=parse_datetime("2019-12-27T18:11:19.117Z"),
            image_set_id="imageSetId",
            image_set_length=0,
            img_height=0,
            img_width=0,
            keywords=["string"],
            origin="origin",
            orig_network="origNetwork",
            sat_id=["string"],
            sat_id_conf=[0],
            sequence_id=0,
            source_dl="sourceDL",
            src_ids=["string"],
            src_typs=["string"],
            tags=["string"],
            transaction_id="transactionId",
            x_units="xUnits",
            y_units="yUnits",
            z_units="zUnits",
        )
        assert analytic_imagery is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert analytic_imagery is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.create(
            classification_marking="classificationMarking",
            content="content",
            data_mode="dataMode",
            description="description",
            filename="filename",
            filesize=0,
            image_type="imageType",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.retrieve(
            "id",
        )
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryFull, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.analytic_imagery.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryListResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryListResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryListResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
        )
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.history(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryHistoryResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert analytic_imagery is None

    @parametrize
    async def test_method_history_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert analytic_imagery is None

    @parametrize
    async def test_raw_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert analytic_imagery is None

    @parametrize
    async def test_streaming_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.history_aodr(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(str, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_history_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.history_count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(str, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.queryhelp()
        assert analytic_imagery is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert analytic_imagery is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert analytic_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        analytic_imagery = await async_client.analytic_imagery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.analytic_imagery.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytic_imagery = await response.parse()
        assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.analytic_imagery.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytic_imagery = await response.parse()
            assert_matches_type(AnalyticImageryTupleResponse, analytic_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True
