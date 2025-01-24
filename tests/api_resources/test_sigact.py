# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SigactListResponse,
    SigactTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSigact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.list(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SigactListResponse, sigact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sigact.with_raw_response.list(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = response.parse()
        assert_matches_type(SigactListResponse, sigact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sigact.with_streaming_response.list(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = response.parse()
            assert_matches_type(SigactListResponse, sigact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.count(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sigact, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sigact.with_raw_response.count(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = response.parse()
        assert_matches_type(str, sigact, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sigact.with_streaming_response.count(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = response.parse()
            assert_matches_type(str, sigact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sigact is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sigact.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = response.parse()
        assert sigact is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sigact.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = response.parse()
            assert sigact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_file_create(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert sigact is None

    @parametrize
    def test_method_file_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="SIGACT-ID",
            accuracy=13,
            actors=["US", "CAN"],
            agjson='{"type":"Polygon","coordinates":[[[67.3291113966927,26.156175339112],[67.2580009640721,26.091022064271],[67.1795862381682,26.6637992964562],[67.2501237475598,26.730115808233],[67.3291113966927,26.156175339112]]]}',
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="Type1",
            avg_tone=8.23,
            cameo_base_code="Example_cameoBaseCode",
            cameo_code="CAMEO_CODE",
            cameo_root_code="Example_cameoRootCode",
            checksum_value="120EA8A25E5D487BF68B5F7096440019",
            city="Austin",
            civ_abd=423,
            civ_det=234,
            civ_kia=2,
            civ_wound=123,
            clarity=1,
            coal_abd=123,
            coal_det=123,
            coal_kia=123,
            coal_wound=123,
            complex_attack=False,
            confidence=13,
            country_code="US",
            district="district 12",
            document_filename="Example_documentFilename",
            document_source="Example_documentSource",
            enemy_abd=123,
            enemy_det=123,
            enemy_kia=123,
            event_description="Example_Description",
            event_end=parse_datetime("2021-01-01T01:02:03.123Z"),
            event_start=parse_datetime("2021-01-01T01:02:03.123Z"),
            event_type="Military",
            filesize=0,
            friendly_abd=123,
            friendly_det=123,
            friendly_kia=123,
            friendly_wound=123,
            goldstein=9.32,
            has_attachment=True,
            host_nat_abd=123,
            host_nat_det=123,
            host_nat_kia=123,
            host_nat_wound=123,
            id_number="NUMBER-ID",
            lat=45.31,
            lon=90.23,
            milgrid="4QFJ12345678",
            notes="Example_Notes",
            num_articles=8,
            num_mentions=8,
            num_sources=8,
            origin="THIRD_PARTY_DATASOURCE",
            province="Province_Example",
            related_docs=[
                {
                    "data_source_refs": [
                        {
                            "data_source_id": "dataSourceId",
                            "end_position": "endPosition",
                            "paragraph_number": "paragraphNumber",
                            "sentence_number": "sentenceNumber",
                            "start_position": "startPosition",
                        }
                    ],
                    "document_id": "documentId",
                }
            ],
            rep_unit="Unit_1",
            rep_unit_activity="Example_Activity",
            rep_unit_type="Example_repUnitType",
            side_a_abd=123,
            side_a_det=123,
            side_akia=123,
            side_a_wound=123,
            side_b_abd=123,
            side_b_det=123,
            side_bkia=123,
            side_b_wound=123,
            source_language="eng",
            source_url="Example_URL",
            summary="Example_Summary",
            target="US",
            theater="Kabul",
            type_of_attack="IED Explosion",
        )
        assert sigact is None

    @parametrize
    def test_raw_response_file_create(self, client: Unifieddatalibrary) -> None:
        response = client.sigact.with_raw_response.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = response.parse()
        assert sigact is None

    @parametrize
    def test_streaming_response_file_create(self, client: Unifieddatalibrary) -> None:
        with client.sigact.with_streaming_response.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = response.parse()
            assert sigact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.queryhelp()
        assert sigact is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sigact.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = response.parse()
        assert sigact is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sigact.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = response.parse()
            assert sigact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sigact = client.sigact.tuple(
            columns="columns",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SigactTupleResponse, sigact, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sigact.with_raw_response.tuple(
            columns="columns",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = response.parse()
        assert_matches_type(SigactTupleResponse, sigact, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sigact.with_streaming_response.tuple(
            columns="columns",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = response.parse()
            assert_matches_type(SigactTupleResponse, sigact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSigact:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.list(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SigactListResponse, sigact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sigact.with_raw_response.list(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = await response.parse()
        assert_matches_type(SigactListResponse, sigact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sigact.with_streaming_response.list(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = await response.parse()
            assert_matches_type(SigactListResponse, sigact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.count(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, sigact, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sigact.with_raw_response.count(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = await response.parse()
        assert_matches_type(str, sigact, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sigact.with_streaming_response.count(
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = await response.parse()
            assert_matches_type(str, sigact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sigact is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sigact.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = await response.parse()
        assert sigact is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sigact.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = await response.parse()
            assert sigact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )
        assert sigact is None

    @parametrize
    async def test_method_file_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
            id="SIGACT-ID",
            accuracy=13,
            actors=["US", "CAN"],
            agjson='{"type":"Polygon","coordinates":[[[67.3291113966927,26.156175339112],[67.2580009640721,26.091022064271],[67.1795862381682,26.6637992964562],[67.2501237475598,26.730115808233],[67.3291113966927,26.156175339112]]]}',
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="Type1",
            avg_tone=8.23,
            cameo_base_code="Example_cameoBaseCode",
            cameo_code="CAMEO_CODE",
            cameo_root_code="Example_cameoRootCode",
            checksum_value="120EA8A25E5D487BF68B5F7096440019",
            city="Austin",
            civ_abd=423,
            civ_det=234,
            civ_kia=2,
            civ_wound=123,
            clarity=1,
            coal_abd=123,
            coal_det=123,
            coal_kia=123,
            coal_wound=123,
            complex_attack=False,
            confidence=13,
            country_code="US",
            district="district 12",
            document_filename="Example_documentFilename",
            document_source="Example_documentSource",
            enemy_abd=123,
            enemy_det=123,
            enemy_kia=123,
            event_description="Example_Description",
            event_end=parse_datetime("2021-01-01T01:02:03.123Z"),
            event_start=parse_datetime("2021-01-01T01:02:03.123Z"),
            event_type="Military",
            filesize=0,
            friendly_abd=123,
            friendly_det=123,
            friendly_kia=123,
            friendly_wound=123,
            goldstein=9.32,
            has_attachment=True,
            host_nat_abd=123,
            host_nat_det=123,
            host_nat_kia=123,
            host_nat_wound=123,
            id_number="NUMBER-ID",
            lat=45.31,
            lon=90.23,
            milgrid="4QFJ12345678",
            notes="Example_Notes",
            num_articles=8,
            num_mentions=8,
            num_sources=8,
            origin="THIRD_PARTY_DATASOURCE",
            province="Province_Example",
            related_docs=[
                {
                    "data_source_refs": [
                        {
                            "data_source_id": "dataSourceId",
                            "end_position": "endPosition",
                            "paragraph_number": "paragraphNumber",
                            "sentence_number": "sentenceNumber",
                            "start_position": "startPosition",
                        }
                    ],
                    "document_id": "documentId",
                }
            ],
            rep_unit="Unit_1",
            rep_unit_activity="Example_Activity",
            rep_unit_type="Example_repUnitType",
            side_a_abd=123,
            side_a_det=123,
            side_akia=123,
            side_a_wound=123,
            side_b_abd=123,
            side_b_det=123,
            side_bkia=123,
            side_b_wound=123,
            source_language="eng",
            source_url="Example_URL",
            summary="Example_Summary",
            target="US",
            theater="Kabul",
            type_of_attack="IED Explosion",
        )
        assert sigact is None

    @parametrize
    async def test_raw_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sigact.with_raw_response.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = await response.parse()
        assert sigact is None

    @parametrize
    async def test_streaming_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sigact.with_streaming_response.file_create(
            classification_marking="U",
            data_mode="REAL",
            report_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = await response.parse()
            assert sigact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.queryhelp()
        assert sigact is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sigact.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = await response.parse()
        assert sigact is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sigact.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = await response.parse()
            assert sigact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sigact = await async_client.sigact.tuple(
            columns="columns",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SigactTupleResponse, sigact, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sigact.with_raw_response.tuple(
            columns="columns",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sigact = await response.parse()
        assert_matches_type(SigactTupleResponse, sigact, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sigact.with_streaming_response.tuple(
            columns="columns",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sigact = await response.parse()
            assert_matches_type(SigactTupleResponse, sigact, path=["response"])

        assert cast(Any, response.is_closed) is True
