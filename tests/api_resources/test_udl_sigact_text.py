# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlSigactText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_sigact_text = client.udl_sigact_text.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert udl_sigact_text is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        udl_sigact_text = client.udl_sigact_text.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            accuracy=0,
            actors=["string"],
            agjson="agjson",
            andims=0,
            area="area",
            asrid=0,
            atext="atext",
            atype="atype",
            avg_tone=0,
            cameo_base_code="cameoBaseCode",
            cameo_code="cameoCode",
            cameo_root_code="cameoRootCode",
            checksum_value="checksumValue",
            city="city",
            civ_abd=0,
            civ_det=0,
            civ_kia=0,
            civ_wound=0,
            clarity=0,
            coal_abd=0,
            coal_det=0,
            coal_kia=0,
            coal_wound=0,
            complex_attack=True,
            confidence=0,
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            district="district",
            document_filename="documentFilename",
            document_source="documentSource",
            enemy_abd=0,
            enemy_det=0,
            enemy_kia=0,
            event_description="eventDescription",
            event_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="eventType",
            filesize=0,
            friendly_abd=0,
            friendly_det=0,
            friendly_kia=0,
            friendly_wound=0,
            goldstein=0,
            has_attachment=True,
            host_nat_abd=0,
            host_nat_det=0,
            host_nat_kia=0,
            host_nat_wound=0,
            id_number="idNumber",
            lat=0,
            lon=0,
            milgrid="milgrid",
            notes="notes",
            num_articles=0,
            num_mentions=0,
            num_sources=0,
            origin="origin",
            orig_network="origNetwork",
            province="province",
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
            rep_unit="repUnit",
            rep_unit_activity="repUnitActivity",
            rep_unit_type="repUnitType",
            side_a_abd=0,
            side_a_det=0,
            side_akia=0,
            side_a_wound=0,
            side_b_abd=0,
            side_b_det=0,
            side_bkia=0,
            side_b_wound=0,
            source_language="sourceLanguage",
            source_url="sourceUrl",
            summary="summary",
            target="target",
            theater="theater",
            type_of_attack="typeOfAttack",
        )
        assert udl_sigact_text is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.udl_sigact_text.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sigact_text = response.parse()
        assert udl_sigact_text is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.udl_sigact_text.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sigact_text = response.parse()
            assert udl_sigact_text is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlSigactText:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sigact_text = await async_client.udl_sigact_text.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert udl_sigact_text is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sigact_text = await async_client.udl_sigact_text.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            accuracy=0,
            actors=["string"],
            agjson="agjson",
            andims=0,
            area="area",
            asrid=0,
            atext="atext",
            atype="atype",
            avg_tone=0,
            cameo_base_code="cameoBaseCode",
            cameo_code="cameoCode",
            cameo_root_code="cameoRootCode",
            checksum_value="checksumValue",
            city="city",
            civ_abd=0,
            civ_det=0,
            civ_kia=0,
            civ_wound=0,
            clarity=0,
            coal_abd=0,
            coal_det=0,
            coal_kia=0,
            coal_wound=0,
            complex_attack=True,
            confidence=0,
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            district="district",
            document_filename="documentFilename",
            document_source="documentSource",
            enemy_abd=0,
            enemy_det=0,
            enemy_kia=0,
            event_description="eventDescription",
            event_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="eventType",
            filesize=0,
            friendly_abd=0,
            friendly_det=0,
            friendly_kia=0,
            friendly_wound=0,
            goldstein=0,
            has_attachment=True,
            host_nat_abd=0,
            host_nat_det=0,
            host_nat_kia=0,
            host_nat_wound=0,
            id_number="idNumber",
            lat=0,
            lon=0,
            milgrid="milgrid",
            notes="notes",
            num_articles=0,
            num_mentions=0,
            num_sources=0,
            origin="origin",
            orig_network="origNetwork",
            province="province",
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
            rep_unit="repUnit",
            rep_unit_activity="repUnitActivity",
            rep_unit_type="repUnitType",
            side_a_abd=0,
            side_a_det=0,
            side_akia=0,
            side_a_wound=0,
            side_b_abd=0,
            side_b_det=0,
            side_bkia=0,
            side_b_wound=0,
            source_language="sourceLanguage",
            source_url="sourceUrl",
            summary="summary",
            target="target",
            theater="theater",
            type_of_attack="typeOfAttack",
        )
        assert udl_sigact_text is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.udl_sigact_text.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sigact_text = await response.parse()
        assert udl_sigact_text is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.udl_sigact_text.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            report_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sigact_text = await response.parse()
            assert udl_sigact_text is None

        assert cast(Any, response.is_closed) is True
