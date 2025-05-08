# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SurfaceGetResponse,
    SurfaceListResponse,
    SurfaceTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSurface:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )
        assert surface is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_site_id="ORIG-SITE-ID",
            condition="GOOD",
            ddt_wt_kip=833.5,
            ddt_wt_kip_mod=625.125,
            ddt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            ddt_wt_kn=3705.44,
            dd_wt_kip=416.25,
            dd_wt_kip_mod=312.1875,
            dd_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            dd_wt_kn=1850.1,
            end_lat=45.844,
            end_lon=-67.0094,
            id_site="SITE-ID",
            lcn=50,
            lda_ft=475.2,
            lda_m=145.75,
            length_ft=1500.75,
            length_m=457.5,
            lighting=True,
            lights_aprch=True,
            lights_cl=True,
            lights_ols=True,
            lights_papi=True,
            lights_reil=True,
            lights_rwy=True,
            lights_seqfl=True,
            lights_tdzl=True,
            lights_unkn=False,
            lights_vasi=True,
            material="Concrete",
            obstacle=True,
            origin="THIRD_PARTY_DATASOURCE",
            pcn="73RBWT",
            point_reference="Reference Point Example",
            primary=True,
            raw_wbc="LCN 42",
            sbtt_wt_kip=603.025,
            sbtt_wt_kip_mod=452.269,
            sbtt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            sbtt_wt_kn=2682.05,
            start_lat=46.757211,
            start_lon=-67.759494,
            st_wt_kip=195.75,
            st_wt_kip_mod=146.8125,
            st_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            st_wt_kn=867.6,
            s_wt_kip=143.5,
            s_wt_kip_mod=107.625,
            s_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            s_wt_kn=636.4,
            tdt_wtkip=870.2,
            tdt_wt_kip_mod=652.65,
            tdt_wt_kip_mod_note="Serious 25 percent reduction.",
            tdt_wt_kn=3870.05,
            trt_wt_kip=622.85,
            trt_wt_kip_mod=467.1375,
            trt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            trt_wt_kn=2767.15,
            tt_wt_kip=414.9,
            tt_wt_kip_mod=311.175,
            tt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            tt_wt_kn=1842.55,
            t_wt_kip=188.2,
            t_wt_kip_mod=141.15,
            t_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            t_wt_kn=836.45,
            width_ft=220.3,
            width_m=67.25,
        )
        assert surface is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert surface is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )
        assert surface is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
            body_id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_site_id="ORIG-SITE-ID",
            condition="GOOD",
            ddt_wt_kip=833.5,
            ddt_wt_kip_mod=625.125,
            ddt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            ddt_wt_kn=3705.44,
            dd_wt_kip=416.25,
            dd_wt_kip_mod=312.1875,
            dd_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            dd_wt_kn=1850.1,
            end_lat=45.844,
            end_lon=-67.0094,
            id_site="SITE-ID",
            lcn=50,
            lda_ft=475.2,
            lda_m=145.75,
            length_ft=1500.75,
            length_m=457.5,
            lighting=True,
            lights_aprch=True,
            lights_cl=True,
            lights_ols=True,
            lights_papi=True,
            lights_reil=True,
            lights_rwy=True,
            lights_seqfl=True,
            lights_tdzl=True,
            lights_unkn=False,
            lights_vasi=True,
            material="Concrete",
            obstacle=True,
            origin="THIRD_PARTY_DATASOURCE",
            pcn="73RBWT",
            point_reference="Reference Point Example",
            primary=True,
            raw_wbc="LCN 42",
            sbtt_wt_kip=603.025,
            sbtt_wt_kip_mod=452.269,
            sbtt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            sbtt_wt_kn=2682.05,
            start_lat=46.757211,
            start_lon=-67.759494,
            st_wt_kip=195.75,
            st_wt_kip_mod=146.8125,
            st_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            st_wt_kn=867.6,
            s_wt_kip=143.5,
            s_wt_kip_mod=107.625,
            s_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            s_wt_kn=636.4,
            tdt_wtkip=870.2,
            tdt_wt_kip_mod=652.65,
            tdt_wt_kip_mod_note="Serious 25 percent reduction.",
            tdt_wt_kn=3870.05,
            trt_wt_kip=622.85,
            trt_wt_kip_mod=467.1375,
            trt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            trt_wt_kn=2767.15,
            tt_wt_kip=414.9,
            tt_wt_kip_mod=311.175,
            tt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            tt_wt_kn=1842.55,
            t_wt_kip=188.2,
            t_wt_kip_mod=141.15,
            t_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            t_wt_kn=836.45,
            width_ft=220.3,
            width_m=67.25,
        )
        assert surface is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert surface is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.surface.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="West lot",
                source="Bluestaq",
                type="PARKING",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.list()
        assert_matches_type(SyncOffsetPage[SurfaceListResponse], surface, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SurfaceListResponse], surface, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert_matches_type(SyncOffsetPage[SurfaceListResponse], surface, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert_matches_type(SyncOffsetPage[SurfaceListResponse], surface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.delete(
            "id",
        )
        assert surface is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert surface is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.surface.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.count()
        assert_matches_type(str, surface, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, surface, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert_matches_type(str, surface, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert_matches_type(str, surface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.get(
            id="id",
        )
        assert_matches_type(SurfaceGetResponse, surface, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SurfaceGetResponse, surface, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert_matches_type(SurfaceGetResponse, surface, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert_matches_type(SurfaceGetResponse, surface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.surface.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.queryhelp()
        assert surface is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert surface is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.tuple(
            columns="columns",
        )
        assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        surface = client.surface.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.surface.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = response.parse()
        assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.surface.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = response.parse()
            assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSurface:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )
        assert surface is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_site_id="ORIG-SITE-ID",
            condition="GOOD",
            ddt_wt_kip=833.5,
            ddt_wt_kip_mod=625.125,
            ddt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            ddt_wt_kn=3705.44,
            dd_wt_kip=416.25,
            dd_wt_kip_mod=312.1875,
            dd_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            dd_wt_kn=1850.1,
            end_lat=45.844,
            end_lon=-67.0094,
            id_site="SITE-ID",
            lcn=50,
            lda_ft=475.2,
            lda_m=145.75,
            length_ft=1500.75,
            length_m=457.5,
            lighting=True,
            lights_aprch=True,
            lights_cl=True,
            lights_ols=True,
            lights_papi=True,
            lights_reil=True,
            lights_rwy=True,
            lights_seqfl=True,
            lights_tdzl=True,
            lights_unkn=False,
            lights_vasi=True,
            material="Concrete",
            obstacle=True,
            origin="THIRD_PARTY_DATASOURCE",
            pcn="73RBWT",
            point_reference="Reference Point Example",
            primary=True,
            raw_wbc="LCN 42",
            sbtt_wt_kip=603.025,
            sbtt_wt_kip_mod=452.269,
            sbtt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            sbtt_wt_kn=2682.05,
            start_lat=46.757211,
            start_lon=-67.759494,
            st_wt_kip=195.75,
            st_wt_kip_mod=146.8125,
            st_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            st_wt_kn=867.6,
            s_wt_kip=143.5,
            s_wt_kip_mod=107.625,
            s_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            s_wt_kn=636.4,
            tdt_wtkip=870.2,
            tdt_wt_kip_mod=652.65,
            tdt_wt_kip_mod_note="Serious 25 percent reduction.",
            tdt_wt_kn=3870.05,
            trt_wt_kip=622.85,
            trt_wt_kip_mod=467.1375,
            trt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            trt_wt_kn=2767.15,
            tt_wt_kip=414.9,
            tt_wt_kip_mod=311.175,
            tt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            tt_wt_kn=1842.55,
            t_wt_kip=188.2,
            t_wt_kip_mod=141.15,
            t_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            t_wt_kn=836.45,
            width_ft=220.3,
            width_m=67.25,
        )
        assert surface is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert surface is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )
        assert surface is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
            body_id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_site_id="ORIG-SITE-ID",
            condition="GOOD",
            ddt_wt_kip=833.5,
            ddt_wt_kip_mod=625.125,
            ddt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            ddt_wt_kn=3705.44,
            dd_wt_kip=416.25,
            dd_wt_kip_mod=312.1875,
            dd_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            dd_wt_kn=1850.1,
            end_lat=45.844,
            end_lon=-67.0094,
            id_site="SITE-ID",
            lcn=50,
            lda_ft=475.2,
            lda_m=145.75,
            length_ft=1500.75,
            length_m=457.5,
            lighting=True,
            lights_aprch=True,
            lights_cl=True,
            lights_ols=True,
            lights_papi=True,
            lights_reil=True,
            lights_rwy=True,
            lights_seqfl=True,
            lights_tdzl=True,
            lights_unkn=False,
            lights_vasi=True,
            material="Concrete",
            obstacle=True,
            origin="THIRD_PARTY_DATASOURCE",
            pcn="73RBWT",
            point_reference="Reference Point Example",
            primary=True,
            raw_wbc="LCN 42",
            sbtt_wt_kip=603.025,
            sbtt_wt_kip_mod=452.269,
            sbtt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            sbtt_wt_kn=2682.05,
            start_lat=46.757211,
            start_lon=-67.759494,
            st_wt_kip=195.75,
            st_wt_kip_mod=146.8125,
            st_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            st_wt_kn=867.6,
            s_wt_kip=143.5,
            s_wt_kip_mod=107.625,
            s_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            s_wt_kn=636.4,
            tdt_wtkip=870.2,
            tdt_wt_kip_mod=652.65,
            tdt_wt_kip_mod_note="Serious 25 percent reduction.",
            tdt_wt_kn=3870.05,
            trt_wt_kip=622.85,
            trt_wt_kip_mod=467.1375,
            trt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            trt_wt_kn=2767.15,
            tt_wt_kip=414.9,
            tt_wt_kip_mod=311.175,
            tt_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            tt_wt_kn=1842.55,
            t_wt_kip=188.2,
            t_wt_kip_mod=141.15,
            t_wt_kip_mod_note="Observed 25% reduction in surface integrity.",
            t_wt_kn=836.45,
            width_ft=220.3,
            width_m=67.25,
        )
        assert surface is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert surface is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="West lot",
            source="Bluestaq",
            type="PARKING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.surface.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="West lot",
                source="Bluestaq",
                type="PARKING",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.list()
        assert_matches_type(AsyncOffsetPage[SurfaceListResponse], surface, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SurfaceListResponse], surface, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert_matches_type(AsyncOffsetPage[SurfaceListResponse], surface, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert_matches_type(AsyncOffsetPage[SurfaceListResponse], surface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.delete(
            "id",
        )
        assert surface is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert surface is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.surface.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.count()
        assert_matches_type(str, surface, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, surface, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert_matches_type(str, surface, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert_matches_type(str, surface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.get(
            id="id",
        )
        assert_matches_type(SurfaceGetResponse, surface, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SurfaceGetResponse, surface, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert_matches_type(SurfaceGetResponse, surface, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert_matches_type(SurfaceGetResponse, surface, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.surface.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.queryhelp()
        assert surface is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert surface is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert surface is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.tuple(
            columns="columns",
        )
        assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        surface = await async_client.surface.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.surface.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surface = await response.parse()
        assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.surface.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surface = await response.parse()
            assert_matches_type(SurfaceTupleResponse, surface, path=["response"])

        assert cast(Any, response.is_closed) is True
