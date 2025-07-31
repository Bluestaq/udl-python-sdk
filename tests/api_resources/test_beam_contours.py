# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    BeamcontourAbridged,
    BeamContourTupleResponse,
    BeamContourQueryHelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import BeamcontourFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeamContours:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )
        assert beam_contour is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
            id="BEAMCONTOUR-ID",
            contour_idx=1,
            gain=17.1,
            geography="POLYGON((26.156175339112 67.3291113966927,26.0910220642717 67.2580009640721,26.6637992964562 67.1795862381682,26.730115808233 67.2501237475598,26.156175339112 67.3291113966927))",
            geography_json='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            geography_ndims=2,
            geography_srid=4326,
            geography_text="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            geography_type="ST_Polygon",
            origin="THIRD_PARTY_DATASOURCE",
            region_name="Example region name",
        )
        assert beam_contour is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert beam_contour is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.retrieve(
            id="id",
        )
        assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.beam_contours.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )
        assert beam_contour is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
            body_id="BEAMCONTOUR-ID",
            contour_idx=1,
            gain=17.1,
            geography="POLYGON((26.156175339112 67.3291113966927,26.0910220642717 67.2580009640721,26.6637992964562 67.1795862381682,26.730115808233 67.2501237475598,26.156175339112 67.3291113966927))",
            geography_json='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            geography_ndims=2,
            geography_srid=4326,
            geography_text="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            geography_type="ST_Polygon",
            origin="THIRD_PARTY_DATASOURCE",
            region_name="Example region name",
        )
        assert beam_contour is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert beam_contour is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.beam_contours.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_beam="REF-BEAM-ID",
                source="Bluestaq",
                type="BORESIGHT",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.list(
            id_beam="idBeam",
        )
        assert_matches_type(SyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.list(
            id_beam="idBeam",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.list(
            id_beam="idBeam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert_matches_type(SyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.list(
            id_beam="idBeam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert_matches_type(SyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.delete(
            "id",
        )
        assert beam_contour is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert beam_contour is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.beam_contours.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.count(
            id_beam="idBeam",
        )
        assert_matches_type(str, beam_contour, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.count(
            id_beam="idBeam",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, beam_contour, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.count(
            id_beam="idBeam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert_matches_type(str, beam_contour, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.count(
            id_beam="idBeam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert_matches_type(str, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_beam": "REF-BEAM-ID",
                    "source": "Bluestaq",
                    "type": "BORESIGHT",
                }
            ],
        )
        assert beam_contour is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_beam": "REF-BEAM-ID",
                    "source": "Bluestaq",
                    "type": "BORESIGHT",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert beam_contour is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_beam": "REF-BEAM-ID",
                    "source": "Bluestaq",
                    "type": "BORESIGHT",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.query_help()
        assert_matches_type(BeamContourQueryHelpResponse, beam_contour, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert_matches_type(BeamContourQueryHelpResponse, beam_contour, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert_matches_type(BeamContourQueryHelpResponse, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.tuple(
            columns="columns",
            id_beam="idBeam",
        )
        assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        beam_contour = client.beam_contours.tuple(
            columns="columns",
            id_beam="idBeam",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.beam_contours.with_raw_response.tuple(
            columns="columns",
            id_beam="idBeam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = response.parse()
        assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.beam_contours.with_streaming_response.tuple(
            columns="columns",
            id_beam="idBeam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = response.parse()
            assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeamContours:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )
        assert beam_contour is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
            id="BEAMCONTOUR-ID",
            contour_idx=1,
            gain=17.1,
            geography="POLYGON((26.156175339112 67.3291113966927,26.0910220642717 67.2580009640721,26.6637992964562 67.1795862381682,26.730115808233 67.2501237475598,26.156175339112 67.3291113966927))",
            geography_json='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            geography_ndims=2,
            geography_srid=4326,
            geography_text="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            geography_type="ST_Polygon",
            origin="THIRD_PARTY_DATASOURCE",
            region_name="Example region name",
        )
        assert beam_contour is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert beam_contour is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.retrieve(
            id="id",
        )
        assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert_matches_type(BeamcontourFull, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.beam_contours.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )
        assert beam_contour is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
            body_id="BEAMCONTOUR-ID",
            contour_idx=1,
            gain=17.1,
            geography="POLYGON((26.156175339112 67.3291113966927,26.0910220642717 67.2580009640721,26.6637992964562 67.1795862381682,26.730115808233 67.2501237475598,26.156175339112 67.3291113966927))",
            geography_json='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            geography_ndims=2,
            geography_srid=4326,
            geography_text="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            geography_type="ST_Polygon",
            origin="THIRD_PARTY_DATASOURCE",
            region_name="Example region name",
        )
        assert beam_contour is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert beam_contour is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_beam="REF-BEAM-ID",
            source="Bluestaq",
            type="BORESIGHT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.beam_contours.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_beam="REF-BEAM-ID",
                source="Bluestaq",
                type="BORESIGHT",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.list(
            id_beam="idBeam",
        )
        assert_matches_type(AsyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.list(
            id_beam="idBeam",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.list(
            id_beam="idBeam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert_matches_type(AsyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.list(
            id_beam="idBeam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert_matches_type(AsyncOffsetPage[BeamcontourAbridged], beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.delete(
            "id",
        )
        assert beam_contour is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert beam_contour is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.beam_contours.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.count(
            id_beam="idBeam",
        )
        assert_matches_type(str, beam_contour, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.count(
            id_beam="idBeam",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, beam_contour, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.count(
            id_beam="idBeam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert_matches_type(str, beam_contour, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.count(
            id_beam="idBeam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert_matches_type(str, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_beam": "REF-BEAM-ID",
                    "source": "Bluestaq",
                    "type": "BORESIGHT",
                }
            ],
        )
        assert beam_contour is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_beam": "REF-BEAM-ID",
                    "source": "Bluestaq",
                    "type": "BORESIGHT",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert beam_contour is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_beam": "REF-BEAM-ID",
                    "source": "Bluestaq",
                    "type": "BORESIGHT",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert beam_contour is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.query_help()
        assert_matches_type(BeamContourQueryHelpResponse, beam_contour, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert_matches_type(BeamContourQueryHelpResponse, beam_contour, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert_matches_type(BeamContourQueryHelpResponse, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.tuple(
            columns="columns",
            id_beam="idBeam",
        )
        assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        beam_contour = await async_client.beam_contours.tuple(
            columns="columns",
            id_beam="idBeam",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.beam_contours.with_raw_response.tuple(
            columns="columns",
            id_beam="idBeam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beam_contour = await response.parse()
        assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.beam_contours.with_streaming_response.tuple(
            columns="columns",
            id_beam="idBeam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beam_contour = await response.parse()
            assert_matches_type(BeamContourTupleResponse, beam_contour, path=["response"])

        assert cast(Any, response.is_closed) is True
