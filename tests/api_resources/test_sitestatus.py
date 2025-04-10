# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SitestatusListResponse,
    SitestatusTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.udl.sitestatus import SitestatusFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSitestatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )
        assert sitestatus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
            id="SITESTATUS-ID",
            cat="COLD",
            cold_inventory=1,
            comm_impairment="commImpairment",
            cpcon="4",
            eoc="WARM",
            fpcon="BRAVO",
            hot_inventory=1,
            hpcon="CHARLIE",
            inst_status="PMC",
            link=["ATDL", "IJMS", "LINK-1"],
            link_status=["AVAILABLE", "DEGRADED", "NOT AVAILABLE"],
            missile=["GMD", "HARPOON", "JAVELIN"],
            missile_inventory=[5, 10, 100],
            mobile_alt_id="MOBILEALT-ID",
            ops_capability="Fully Operational",
            ops_impairment="opsImpairment",
            origin="THIRD_PARTY_DATASOURCE",
            pes=True,
            poiid="d4a91864-6140-4b8d-67cd-45421c75f696",
            radar_status=["OPERATIONAL", "OFF", "NON-OPERATIONAL"],
            radar_system=["ILLUMINATING", "MODE-4", "MODE-3"],
            radiate_mode="Active",
            report_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            sam_mode="Initialization",
            site_type="ADOC",
            time_function="Activation",
            track_id="PCM4923-1656174732-4-1-257",
            track_ref_l16="TrkNm",
            weather_message="Heavy rain",
        )
        assert sitestatus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert sitestatus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )
        assert sitestatus is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
            body_id="SITESTATUS-ID",
            cat="COLD",
            cold_inventory=1,
            comm_impairment="commImpairment",
            cpcon="4",
            eoc="WARM",
            fpcon="BRAVO",
            hot_inventory=1,
            hpcon="CHARLIE",
            inst_status="PMC",
            link=["ATDL", "IJMS", "LINK-1"],
            link_status=["AVAILABLE", "DEGRADED", "NOT AVAILABLE"],
            missile=["GMD", "HARPOON", "JAVELIN"],
            missile_inventory=[5, 10, 100],
            mobile_alt_id="MOBILEALT-ID",
            ops_capability="Fully Operational",
            ops_impairment="opsImpairment",
            origin="THIRD_PARTY_DATASOURCE",
            pes=True,
            poiid="d4a91864-6140-4b8d-67cd-45421c75f696",
            radar_status=["OPERATIONAL", "OFF", "NON-OPERATIONAL"],
            radar_system=["ILLUMINATING", "MODE-4", "MODE-3"],
            radiate_mode="Active",
            report_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            sam_mode="Initialization",
            site_type="ADOC",
            time_function="Activation",
            track_id="PCM4923-1656174732-4-1-257",
            track_ref_l16="TrkNm",
            weather_message="Heavy rain",
        )
        assert sitestatus is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert sitestatus is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sitestatus.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.list()
        assert_matches_type(SitestatusListResponse, sitestatus, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert_matches_type(SitestatusListResponse, sitestatus, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert_matches_type(SitestatusListResponse, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.delete(
            "id",
        )
        assert sitestatus is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert sitestatus is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sitestatus.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.count()
        assert_matches_type(str, sitestatus, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert_matches_type(str, sitestatus, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert_matches_type(str, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.get(
            "id",
        )
        assert_matches_type(SitestatusFull, sitestatus, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert_matches_type(SitestatusFull, sitestatus, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert_matches_type(SitestatusFull, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sitestatus.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.queryhelp()
        assert sitestatus is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert sitestatus is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sitestatus = client.sitestatus.tuple(
            columns="columns",
        )
        assert_matches_type(SitestatusTupleResponse, sitestatus, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sitestatus.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = response.parse()
        assert_matches_type(SitestatusTupleResponse, sitestatus, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sitestatus.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = response.parse()
            assert_matches_type(SitestatusTupleResponse, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSitestatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )
        assert sitestatus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
            id="SITESTATUS-ID",
            cat="COLD",
            cold_inventory=1,
            comm_impairment="commImpairment",
            cpcon="4",
            eoc="WARM",
            fpcon="BRAVO",
            hot_inventory=1,
            hpcon="CHARLIE",
            inst_status="PMC",
            link=["ATDL", "IJMS", "LINK-1"],
            link_status=["AVAILABLE", "DEGRADED", "NOT AVAILABLE"],
            missile=["GMD", "HARPOON", "JAVELIN"],
            missile_inventory=[5, 10, 100],
            mobile_alt_id="MOBILEALT-ID",
            ops_capability="Fully Operational",
            ops_impairment="opsImpairment",
            origin="THIRD_PARTY_DATASOURCE",
            pes=True,
            poiid="d4a91864-6140-4b8d-67cd-45421c75f696",
            radar_status=["OPERATIONAL", "OFF", "NON-OPERATIONAL"],
            radar_system=["ILLUMINATING", "MODE-4", "MODE-3"],
            radiate_mode="Active",
            report_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            sam_mode="Initialization",
            site_type="ADOC",
            time_function="Activation",
            track_id="PCM4923-1656174732-4-1-257",
            track_ref_l16="TrkNm",
            weather_message="Heavy rain",
        )
        assert sitestatus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert sitestatus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )
        assert sitestatus is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
            body_id="SITESTATUS-ID",
            cat="COLD",
            cold_inventory=1,
            comm_impairment="commImpairment",
            cpcon="4",
            eoc="WARM",
            fpcon="BRAVO",
            hot_inventory=1,
            hpcon="CHARLIE",
            inst_status="PMC",
            link=["ATDL", "IJMS", "LINK-1"],
            link_status=["AVAILABLE", "DEGRADED", "NOT AVAILABLE"],
            missile=["GMD", "HARPOON", "JAVELIN"],
            missile_inventory=[5, 10, 100],
            mobile_alt_id="MOBILEALT-ID",
            ops_capability="Fully Operational",
            ops_impairment="opsImpairment",
            origin="THIRD_PARTY_DATASOURCE",
            pes=True,
            poiid="d4a91864-6140-4b8d-67cd-45421c75f696",
            radar_status=["OPERATIONAL", "OFF", "NON-OPERATIONAL"],
            radar_system=["ILLUMINATING", "MODE-4", "MODE-3"],
            radiate_mode="Active",
            report_time=parse_datetime("2021-01-01T01:01:01.123Z"),
            sam_mode="Initialization",
            site_type="ADOC",
            time_function="Activation",
            track_id="PCM4923-1656174732-4-1-257",
            track_ref_l16="TrkNm",
            weather_message="Heavy rain",
        )
        assert sitestatus is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert sitestatus is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sitestatus.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_site="41e3e554-9790-40b9-bd7b-f30d864dcad8",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.list()
        assert_matches_type(SitestatusListResponse, sitestatus, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert_matches_type(SitestatusListResponse, sitestatus, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert_matches_type(SitestatusListResponse, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.delete(
            "id",
        )
        assert sitestatus is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert sitestatus is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sitestatus.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.count()
        assert_matches_type(str, sitestatus, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert_matches_type(str, sitestatus, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert_matches_type(str, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.get(
            "id",
        )
        assert_matches_type(SitestatusFull, sitestatus, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert_matches_type(SitestatusFull, sitestatus, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert_matches_type(SitestatusFull, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sitestatus.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.queryhelp()
        assert sitestatus is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert sitestatus is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert sitestatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sitestatus = await async_client.sitestatus.tuple(
            columns="columns",
        )
        assert_matches_type(SitestatusTupleResponse, sitestatus, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sitestatus.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitestatus = await response.parse()
        assert_matches_type(SitestatusTupleResponse, sitestatus, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sitestatus.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitestatus = await response.parse()
            assert_matches_type(SitestatusTupleResponse, sitestatus, path=["response"])

        assert cast(Any, response.is_closed) is True
