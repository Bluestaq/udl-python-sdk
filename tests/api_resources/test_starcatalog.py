# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    StarcatalogGetResponse,
    StarcatalogListResponse,
    StarcatalogTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStarcatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )
        assert starcatalog is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
            id="STAR-CAT-DATASET-ID",
            bpmag=0.04559,
            bpmag_unc=0.2227,
            cat_version="1.23",
            dec_unc=40.996,
            gaiadr3_cat_id=89012345678901,
            gmag=0.0046,
            gmag_unc=0.00292,
            gnc_cat_id=12345,
            hip_cat_id=12345,
            hmag=12.126,
            hmag_unc=5.722,
            jmag=9.515,
            jmag_unc=7.559,
            kmag=13.545,
            kmag_unc=0.052,
            mult_flag=True,
            neighbor_distance=201.406,
            neighbor_flag=False,
            neighbor_id=2456,
            origin="THIRD_PARTY_DATASOURCE",
            parallax=-6.8,
            parallax_unc=82.35,
            pmdec=-970.1003,
            pmdec_unc=1.22,
            pmra=1000.45,
            pmra_unc=5.6,
            pm_unc_flag=False,
            pos_unc_flag=False,
            ra_unc=509.466,
            rpmag=8.0047,
            rpmag_unc=1.233,
            shift=4.548,
            shift_flag=False,
            var_flag=True,
        )
        assert starcatalog is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert starcatalog is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )
        assert starcatalog is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
            body_id="STAR-CAT-DATASET-ID",
            bpmag=0.04559,
            bpmag_unc=0.2227,
            cat_version="1.23",
            dec_unc=40.996,
            gaiadr3_cat_id=89012345678901,
            gmag=0.0046,
            gmag_unc=0.00292,
            gnc_cat_id=12345,
            hip_cat_id=12345,
            hmag=12.126,
            hmag_unc=5.722,
            jmag=9.515,
            jmag_unc=7.559,
            kmag=13.545,
            kmag_unc=0.052,
            mult_flag=True,
            neighbor_distance=201.406,
            neighbor_flag=False,
            neighbor_id=2456,
            origin="THIRD_PARTY_DATASOURCE",
            parallax=-6.8,
            parallax_unc=82.35,
            pmdec=-970.1003,
            pmdec_unc=1.22,
            pmra=1000.45,
            pmra_unc=5.6,
            pm_unc_flag=False,
            pos_unc_flag=False,
            ra_unc=509.466,
            rpmag=8.0047,
            rpmag_unc=1.233,
            shift=4.548,
            shift_flag=False,
            var_flag=True,
        )
        assert starcatalog is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert starcatalog is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.starcatalog.with_raw_response.update(
                path_id="",
                astrometry_origin="GAIADR3",
                classification_marking="U",
                cs_id=12345,
                data_mode="TEST",
                dec=21.8,
                ra=14.43,
                source="Bluestaq",
                star_epoch=2016,
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.list()
        assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.list(
            dec=0,
            ra=0,
        )
        assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.delete(
            "id",
        )
        assert starcatalog is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert starcatalog is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.starcatalog.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.count()
        assert_matches_type(str, starcatalog, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.count(
            dec=0,
            ra=0,
        )
        assert_matches_type(str, starcatalog, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert_matches_type(str, starcatalog, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert_matches_type(str, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.create_bulk(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )
        assert starcatalog is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.create_bulk(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert starcatalog is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.create_bulk(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.get(
            "id",
        )
        assert_matches_type(StarcatalogGetResponse, starcatalog, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert_matches_type(StarcatalogGetResponse, starcatalog, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert_matches_type(StarcatalogGetResponse, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.starcatalog.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.queryhelp()
        assert starcatalog is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert starcatalog is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.tuple(
            columns="columns",
        )
        assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.tuple(
            columns="columns",
            dec=0,
            ra=0,
        )
        assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        starcatalog = client.starcatalog.unvalidated_publish(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )
        assert starcatalog is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.starcatalog.with_raw_response.unvalidated_publish(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = response.parse()
        assert starcatalog is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.starcatalog.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True


class TestAsyncStarcatalog:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )
        assert starcatalog is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
            id="STAR-CAT-DATASET-ID",
            bpmag=0.04559,
            bpmag_unc=0.2227,
            cat_version="1.23",
            dec_unc=40.996,
            gaiadr3_cat_id=89012345678901,
            gmag=0.0046,
            gmag_unc=0.00292,
            gnc_cat_id=12345,
            hip_cat_id=12345,
            hmag=12.126,
            hmag_unc=5.722,
            jmag=9.515,
            jmag_unc=7.559,
            kmag=13.545,
            kmag_unc=0.052,
            mult_flag=True,
            neighbor_distance=201.406,
            neighbor_flag=False,
            neighbor_id=2456,
            origin="THIRD_PARTY_DATASOURCE",
            parallax=-6.8,
            parallax_unc=82.35,
            pmdec=-970.1003,
            pmdec_unc=1.22,
            pmra=1000.45,
            pmra_unc=5.6,
            pm_unc_flag=False,
            pos_unc_flag=False,
            ra_unc=509.466,
            rpmag=8.0047,
            rpmag_unc=1.233,
            shift=4.548,
            shift_flag=False,
            var_flag=True,
        )
        assert starcatalog is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert starcatalog is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.create(
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )
        assert starcatalog is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
            body_id="STAR-CAT-DATASET-ID",
            bpmag=0.04559,
            bpmag_unc=0.2227,
            cat_version="1.23",
            dec_unc=40.996,
            gaiadr3_cat_id=89012345678901,
            gmag=0.0046,
            gmag_unc=0.00292,
            gnc_cat_id=12345,
            hip_cat_id=12345,
            hmag=12.126,
            hmag_unc=5.722,
            jmag=9.515,
            jmag_unc=7.559,
            kmag=13.545,
            kmag_unc=0.052,
            mult_flag=True,
            neighbor_distance=201.406,
            neighbor_flag=False,
            neighbor_id=2456,
            origin="THIRD_PARTY_DATASOURCE",
            parallax=-6.8,
            parallax_unc=82.35,
            pmdec=-970.1003,
            pmdec_unc=1.22,
            pmra=1000.45,
            pmra_unc=5.6,
            pm_unc_flag=False,
            pos_unc_flag=False,
            ra_unc=509.466,
            rpmag=8.0047,
            rpmag_unc=1.233,
            shift=4.548,
            shift_flag=False,
            var_flag=True,
        )
        assert starcatalog is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert starcatalog is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.update(
            path_id="id",
            astrometry_origin="GAIADR3",
            classification_marking="U",
            cs_id=12345,
            data_mode="TEST",
            dec=21.8,
            ra=14.43,
            source="Bluestaq",
            star_epoch=2016,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.starcatalog.with_raw_response.update(
                path_id="",
                astrometry_origin="GAIADR3",
                classification_marking="U",
                cs_id=12345,
                data_mode="TEST",
                dec=21.8,
                ra=14.43,
                source="Bluestaq",
                star_epoch=2016,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.list()
        assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.list(
            dec=0,
            ra=0,
        )
        assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert_matches_type(StarcatalogListResponse, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.delete(
            "id",
        )
        assert starcatalog is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert starcatalog is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.starcatalog.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.count()
        assert_matches_type(str, starcatalog, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.count(
            dec=0,
            ra=0,
        )
        assert_matches_type(str, starcatalog, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert_matches_type(str, starcatalog, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert_matches_type(str, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.create_bulk(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )
        assert starcatalog is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.create_bulk(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert starcatalog is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.create_bulk(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.get(
            "id",
        )
        assert_matches_type(StarcatalogGetResponse, starcatalog, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert_matches_type(StarcatalogGetResponse, starcatalog, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert_matches_type(StarcatalogGetResponse, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.starcatalog.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.queryhelp()
        assert starcatalog is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert starcatalog is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.tuple(
            columns="columns",
        )
        assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.tuple(
            columns="columns",
            dec=0,
            ra=0,
        )
        assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert_matches_type(StarcatalogTupleResponse, starcatalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        starcatalog = await async_client.starcatalog.unvalidated_publish(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )
        assert starcatalog is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.starcatalog.with_raw_response.unvalidated_publish(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starcatalog = await response.parse()
        assert starcatalog is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.starcatalog.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "TEST",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starcatalog = await response.parse()
            assert starcatalog is None

        assert cast(Any, response.is_closed) is True
