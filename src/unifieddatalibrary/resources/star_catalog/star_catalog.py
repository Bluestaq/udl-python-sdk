# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    star_catalog_get_params,
    star_catalog_list_params,
    star_catalog_count_params,
    star_catalog_tuple_params,
    star_catalog_create_params,
    star_catalog_update_params,
    star_catalog_create_bulk_params,
    star_catalog_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.star_catalog_get_response import StarCatalogGetResponse
from ...types.star_catalog_list_response import StarCatalogListResponse
from ...types.star_catalog_tuple_response import StarCatalogTupleResponse
from ...types.star_catalog_queryhelp_response import StarCatalogQueryhelpResponse

__all__ = ["StarCatalogResource", "AsyncStarCatalogResource"]


class StarCatalogResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> StarCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return StarCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StarCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return StarCatalogResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        astrometry_origin: Literal["GAIADR3", "HIPPARCOS", "USNOBSC"],
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        id: str | NotGiven = NOT_GIVEN,
        bpmag: float | NotGiven = NOT_GIVEN,
        bpmag_unc: float | NotGiven = NOT_GIVEN,
        cat_version: str | NotGiven = NOT_GIVEN,
        dec_unc: float | NotGiven = NOT_GIVEN,
        gaiadr3_cat_id: int | NotGiven = NOT_GIVEN,
        gmag: float | NotGiven = NOT_GIVEN,
        gmag_unc: float | NotGiven = NOT_GIVEN,
        gnc_cat_id: int | NotGiven = NOT_GIVEN,
        hip_cat_id: int | NotGiven = NOT_GIVEN,
        hmag: float | NotGiven = NOT_GIVEN,
        hmag_unc: float | NotGiven = NOT_GIVEN,
        jmag: float | NotGiven = NOT_GIVEN,
        jmag_unc: float | NotGiven = NOT_GIVEN,
        kmag: float | NotGiven = NOT_GIVEN,
        kmag_unc: float | NotGiven = NOT_GIVEN,
        mult_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_distance: float | NotGiven = NOT_GIVEN,
        neighbor_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_id: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parallax: float | NotGiven = NOT_GIVEN,
        parallax_unc: float | NotGiven = NOT_GIVEN,
        pmdec: float | NotGiven = NOT_GIVEN,
        pmdec_unc: float | NotGiven = NOT_GIVEN,
        pmra: float | NotGiven = NOT_GIVEN,
        pmra_unc: float | NotGiven = NOT_GIVEN,
        pm_unc_flag: bool | NotGiven = NOT_GIVEN,
        pos_unc_flag: bool | NotGiven = NOT_GIVEN,
        ra_unc: float | NotGiven = NOT_GIVEN,
        rpmag: float | NotGiven = NOT_GIVEN,
        rpmag_unc: float | NotGiven = NOT_GIVEN,
        shift: float | NotGiven = NOT_GIVEN,
        shift_flag: bool | NotGiven = NOT_GIVEN,
        var_flag: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single StarCatalog record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object. Enum: [GAIADR3, HIPPARCOS,
              USNOBSC].

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          id: Unique identifier of the record, auto-generated by the system.

          bpmag: Gaia DR3 optical photometric Bp-band magnitude in the Vega scale.

          bpmag_unc: Gaia DR3 optical Bp-band magnitude uncertainty in the Vega scale.

          cat_version: The version of the catalog associated with this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          gaiadr3_cat_id: The ID of this object in the Gaia DR3 Catalog.

          gmag: Gaia DR3 optical photometric G-band magnitude in the Vega scale.

          gmag_unc: Gaia DR3 optical photometric G-band magnitude uncertainty in the Vega scale.

          gnc_cat_id: The ID of this object in the Guidance and Navagation Control (GNC) Catalog.

          hip_cat_id: The ID of this object in the Hipparcos Catalog.

          hmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude in the Vega scale.

          hmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude uncertainty in the Vega scale.

          jmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude in the Vega scale.

          jmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude uncertainty in the Vega scale.

          kmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude in the Vega scale.

          kmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude uncertainty in the Vega scale.

          mult_flag: Flag indicating that this is a multiple object source.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds/year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds/year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds/year, at the
              reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds/year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds/year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rpmag: Gaia DR3 optical Rp-band magnitude in the Vega scale.

          rpmag_unc: Gaia DR3 optical photometric Rp-band magnitude uncertainty in the Vega scale.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/starcatalog",
            body=maybe_transform(
                {
                    "astrometry_origin": astrometry_origin,
                    "classification_marking": classification_marking,
                    "cs_id": cs_id,
                    "data_mode": data_mode,
                    "dec": dec,
                    "ra": ra,
                    "source": source,
                    "star_epoch": star_epoch,
                    "id": id,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "cat_version": cat_version,
                    "dec_unc": dec_unc,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_unc": hmag_unc,
                    "jmag": jmag,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_unc": kmag_unc,
                    "mult_flag": mult_flag,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "origin": origin,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ra_unc": ra_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "var_flag": var_flag,
                },
                star_catalog_create_params.StarCatalogCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        path_id: str,
        *,
        astrometry_origin: Literal["GAIADR3", "HIPPARCOS", "USNOBSC"],
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        body_id: str | NotGiven = NOT_GIVEN,
        bpmag: float | NotGiven = NOT_GIVEN,
        bpmag_unc: float | NotGiven = NOT_GIVEN,
        cat_version: str | NotGiven = NOT_GIVEN,
        dec_unc: float | NotGiven = NOT_GIVEN,
        gaiadr3_cat_id: int | NotGiven = NOT_GIVEN,
        gmag: float | NotGiven = NOT_GIVEN,
        gmag_unc: float | NotGiven = NOT_GIVEN,
        gnc_cat_id: int | NotGiven = NOT_GIVEN,
        hip_cat_id: int | NotGiven = NOT_GIVEN,
        hmag: float | NotGiven = NOT_GIVEN,
        hmag_unc: float | NotGiven = NOT_GIVEN,
        jmag: float | NotGiven = NOT_GIVEN,
        jmag_unc: float | NotGiven = NOT_GIVEN,
        kmag: float | NotGiven = NOT_GIVEN,
        kmag_unc: float | NotGiven = NOT_GIVEN,
        mult_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_distance: float | NotGiven = NOT_GIVEN,
        neighbor_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_id: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parallax: float | NotGiven = NOT_GIVEN,
        parallax_unc: float | NotGiven = NOT_GIVEN,
        pmdec: float | NotGiven = NOT_GIVEN,
        pmdec_unc: float | NotGiven = NOT_GIVEN,
        pmra: float | NotGiven = NOT_GIVEN,
        pmra_unc: float | NotGiven = NOT_GIVEN,
        pm_unc_flag: bool | NotGiven = NOT_GIVEN,
        pos_unc_flag: bool | NotGiven = NOT_GIVEN,
        ra_unc: float | NotGiven = NOT_GIVEN,
        rpmag: float | NotGiven = NOT_GIVEN,
        rpmag_unc: float | NotGiven = NOT_GIVEN,
        shift: float | NotGiven = NOT_GIVEN,
        shift_flag: bool | NotGiven = NOT_GIVEN,
        var_flag: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single starcatalog record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object. Enum: [GAIADR3, HIPPARCOS,
              USNOBSC].

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          body_id: Unique identifier of the record, auto-generated by the system.

          bpmag: Gaia DR3 optical photometric Bp-band magnitude in the Vega scale.

          bpmag_unc: Gaia DR3 optical Bp-band magnitude uncertainty in the Vega scale.

          cat_version: The version of the catalog associated with this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          gaiadr3_cat_id: The ID of this object in the Gaia DR3 Catalog.

          gmag: Gaia DR3 optical photometric G-band magnitude in the Vega scale.

          gmag_unc: Gaia DR3 optical photometric G-band magnitude uncertainty in the Vega scale.

          gnc_cat_id: The ID of this object in the Guidance and Navagation Control (GNC) Catalog.

          hip_cat_id: The ID of this object in the Hipparcos Catalog.

          hmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude in the Vega scale.

          hmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude uncertainty in the Vega scale.

          jmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude in the Vega scale.

          jmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude uncertainty in the Vega scale.

          kmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude in the Vega scale.

          kmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude uncertainty in the Vega scale.

          mult_flag: Flag indicating that this is a multiple object source.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds/year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds/year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds/year, at the
              reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds/year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds/year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rpmag: Gaia DR3 optical Rp-band magnitude in the Vega scale.

          rpmag_unc: Gaia DR3 optical photometric Rp-band magnitude uncertainty in the Vega scale.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/starcatalog/{path_id}",
            body=maybe_transform(
                {
                    "astrometry_origin": astrometry_origin,
                    "classification_marking": classification_marking,
                    "cs_id": cs_id,
                    "data_mode": data_mode,
                    "dec": dec,
                    "ra": ra,
                    "source": source,
                    "star_epoch": star_epoch,
                    "body_id": body_id,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "cat_version": cat_version,
                    "dec_unc": dec_unc,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_unc": hmag_unc,
                    "jmag": jmag,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_unc": kmag_unc,
                    "mult_flag": mult_flag,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "origin": origin,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ra_unc": ra_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "var_flag": var_flag,
                },
                star_catalog_update_params.StarCatalogUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        dec: float | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[StarCatalogListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          dec: (One or more of fields 'dec, ra' are required.) Barycentric declination of the
              source in International Celestial Reference System (ICRS) at the reference
              epoch, in degrees.

          ra: (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
              the source in the International Celestial Reference System (ICRS) frame at the
              reference epoch, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/starcatalog",
            page=SyncOffsetPage[StarCatalogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dec": dec,
                        "first_result": first_result,
                        "max_results": max_results,
                        "ra": ra,
                    },
                    star_catalog_list_params.StarCatalogListParams,
                ),
            ),
            model=StarCatalogListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete a dataset specified by the passed ID path parameter.
        A specific role is required to perform this service operation. Please contact
        the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/udl/starcatalog/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        dec: float | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          dec: (One or more of fields 'dec, ra' are required.) Barycentric declination of the
              source in International Celestial Reference System (ICRS) at the reference
              epoch, in degrees.

          ra: (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
              the source in the International Celestial Reference System (ICRS) frame at the
              reference epoch, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/starcatalog/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dec": dec,
                        "first_result": first_result,
                        "max_results": max_results,
                        "ra": ra,
                    },
                    star_catalog_count_params.StarCatalogCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[star_catalog_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        StarCatalog records as a POST body and ingest into the database. This operation
        is not intended to be used for automated feeds into UDL. Data providers should
        contact the UDL team for specific role assignments and for instructions on
        setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/starcatalog/createBulk",
            body=maybe_transform(body, Iterable[star_catalog_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StarCatalogGetResponse:
        """
        Service operation to get a single StarCatalog record by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/starcatalog/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    star_catalog_get_params.StarCatalogGetParams,
                ),
            ),
            cast_to=StarCatalogGetResponse,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StarCatalogQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/starcatalog/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StarCatalogQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        dec: float | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StarCatalogTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          dec: (One or more of fields 'dec, ra' are required.) Barycentric declination of the
              source in International Celestial Reference System (ICRS) at the reference
              epoch, in degrees.

          ra: (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
              the source in the International Celestial Reference System (ICRS) frame at the
              reference epoch, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/starcatalog/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "dec": dec,
                        "first_result": first_result,
                        "max_results": max_results,
                        "ra": ra,
                    },
                    star_catalog_tuple_params.StarCatalogTupleParams,
                ),
            ),
            cast_to=StarCatalogTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[star_catalog_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple StarCatalog records as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-starcatalog",
            body=maybe_transform(body, Iterable[star_catalog_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncStarCatalogResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStarCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStarCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStarCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncStarCatalogResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        astrometry_origin: Literal["GAIADR3", "HIPPARCOS", "USNOBSC"],
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        id: str | NotGiven = NOT_GIVEN,
        bpmag: float | NotGiven = NOT_GIVEN,
        bpmag_unc: float | NotGiven = NOT_GIVEN,
        cat_version: str | NotGiven = NOT_GIVEN,
        dec_unc: float | NotGiven = NOT_GIVEN,
        gaiadr3_cat_id: int | NotGiven = NOT_GIVEN,
        gmag: float | NotGiven = NOT_GIVEN,
        gmag_unc: float | NotGiven = NOT_GIVEN,
        gnc_cat_id: int | NotGiven = NOT_GIVEN,
        hip_cat_id: int | NotGiven = NOT_GIVEN,
        hmag: float | NotGiven = NOT_GIVEN,
        hmag_unc: float | NotGiven = NOT_GIVEN,
        jmag: float | NotGiven = NOT_GIVEN,
        jmag_unc: float | NotGiven = NOT_GIVEN,
        kmag: float | NotGiven = NOT_GIVEN,
        kmag_unc: float | NotGiven = NOT_GIVEN,
        mult_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_distance: float | NotGiven = NOT_GIVEN,
        neighbor_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_id: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parallax: float | NotGiven = NOT_GIVEN,
        parallax_unc: float | NotGiven = NOT_GIVEN,
        pmdec: float | NotGiven = NOT_GIVEN,
        pmdec_unc: float | NotGiven = NOT_GIVEN,
        pmra: float | NotGiven = NOT_GIVEN,
        pmra_unc: float | NotGiven = NOT_GIVEN,
        pm_unc_flag: bool | NotGiven = NOT_GIVEN,
        pos_unc_flag: bool | NotGiven = NOT_GIVEN,
        ra_unc: float | NotGiven = NOT_GIVEN,
        rpmag: float | NotGiven = NOT_GIVEN,
        rpmag_unc: float | NotGiven = NOT_GIVEN,
        shift: float | NotGiven = NOT_GIVEN,
        shift_flag: bool | NotGiven = NOT_GIVEN,
        var_flag: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single StarCatalog record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object. Enum: [GAIADR3, HIPPARCOS,
              USNOBSC].

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          id: Unique identifier of the record, auto-generated by the system.

          bpmag: Gaia DR3 optical photometric Bp-band magnitude in the Vega scale.

          bpmag_unc: Gaia DR3 optical Bp-band magnitude uncertainty in the Vega scale.

          cat_version: The version of the catalog associated with this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          gaiadr3_cat_id: The ID of this object in the Gaia DR3 Catalog.

          gmag: Gaia DR3 optical photometric G-band magnitude in the Vega scale.

          gmag_unc: Gaia DR3 optical photometric G-band magnitude uncertainty in the Vega scale.

          gnc_cat_id: The ID of this object in the Guidance and Navagation Control (GNC) Catalog.

          hip_cat_id: The ID of this object in the Hipparcos Catalog.

          hmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude in the Vega scale.

          hmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude uncertainty in the Vega scale.

          jmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude in the Vega scale.

          jmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude uncertainty in the Vega scale.

          kmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude in the Vega scale.

          kmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude uncertainty in the Vega scale.

          mult_flag: Flag indicating that this is a multiple object source.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds/year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds/year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds/year, at the
              reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds/year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds/year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rpmag: Gaia DR3 optical Rp-band magnitude in the Vega scale.

          rpmag_unc: Gaia DR3 optical photometric Rp-band magnitude uncertainty in the Vega scale.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/starcatalog",
            body=await async_maybe_transform(
                {
                    "astrometry_origin": astrometry_origin,
                    "classification_marking": classification_marking,
                    "cs_id": cs_id,
                    "data_mode": data_mode,
                    "dec": dec,
                    "ra": ra,
                    "source": source,
                    "star_epoch": star_epoch,
                    "id": id,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "cat_version": cat_version,
                    "dec_unc": dec_unc,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_unc": hmag_unc,
                    "jmag": jmag,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_unc": kmag_unc,
                    "mult_flag": mult_flag,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "origin": origin,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ra_unc": ra_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "var_flag": var_flag,
                },
                star_catalog_create_params.StarCatalogCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        path_id: str,
        *,
        astrometry_origin: Literal["GAIADR3", "HIPPARCOS", "USNOBSC"],
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        body_id: str | NotGiven = NOT_GIVEN,
        bpmag: float | NotGiven = NOT_GIVEN,
        bpmag_unc: float | NotGiven = NOT_GIVEN,
        cat_version: str | NotGiven = NOT_GIVEN,
        dec_unc: float | NotGiven = NOT_GIVEN,
        gaiadr3_cat_id: int | NotGiven = NOT_GIVEN,
        gmag: float | NotGiven = NOT_GIVEN,
        gmag_unc: float | NotGiven = NOT_GIVEN,
        gnc_cat_id: int | NotGiven = NOT_GIVEN,
        hip_cat_id: int | NotGiven = NOT_GIVEN,
        hmag: float | NotGiven = NOT_GIVEN,
        hmag_unc: float | NotGiven = NOT_GIVEN,
        jmag: float | NotGiven = NOT_GIVEN,
        jmag_unc: float | NotGiven = NOT_GIVEN,
        kmag: float | NotGiven = NOT_GIVEN,
        kmag_unc: float | NotGiven = NOT_GIVEN,
        mult_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_distance: float | NotGiven = NOT_GIVEN,
        neighbor_flag: bool | NotGiven = NOT_GIVEN,
        neighbor_id: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parallax: float | NotGiven = NOT_GIVEN,
        parallax_unc: float | NotGiven = NOT_GIVEN,
        pmdec: float | NotGiven = NOT_GIVEN,
        pmdec_unc: float | NotGiven = NOT_GIVEN,
        pmra: float | NotGiven = NOT_GIVEN,
        pmra_unc: float | NotGiven = NOT_GIVEN,
        pm_unc_flag: bool | NotGiven = NOT_GIVEN,
        pos_unc_flag: bool | NotGiven = NOT_GIVEN,
        ra_unc: float | NotGiven = NOT_GIVEN,
        rpmag: float | NotGiven = NOT_GIVEN,
        rpmag_unc: float | NotGiven = NOT_GIVEN,
        shift: float | NotGiven = NOT_GIVEN,
        shift_flag: bool | NotGiven = NOT_GIVEN,
        var_flag: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single starcatalog record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object. Enum: [GAIADR3, HIPPARCOS,
              USNOBSC].

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          body_id: Unique identifier of the record, auto-generated by the system.

          bpmag: Gaia DR3 optical photometric Bp-band magnitude in the Vega scale.

          bpmag_unc: Gaia DR3 optical Bp-band magnitude uncertainty in the Vega scale.

          cat_version: The version of the catalog associated with this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          gaiadr3_cat_id: The ID of this object in the Gaia DR3 Catalog.

          gmag: Gaia DR3 optical photometric G-band magnitude in the Vega scale.

          gmag_unc: Gaia DR3 optical photometric G-band magnitude uncertainty in the Vega scale.

          gnc_cat_id: The ID of this object in the Guidance and Navagation Control (GNC) Catalog.

          hip_cat_id: The ID of this object in the Hipparcos Catalog.

          hmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude in the Vega scale.

          hmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric H-band magnitude uncertainty in the Vega scale.

          jmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude in the Vega scale.

          jmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric J-band magnitude uncertainty in the Vega scale.

          kmag: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude in the Vega scale.

          kmag_unc: Two Micron All Sky Survey (2MASS) Point Source Catalog (PSC) near-infrared
              photometric K-band magnitude uncertainty in the Vega scale.

          mult_flag: Flag indicating that this is a multiple object source.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds/year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds/year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds/year, at the
              reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds/year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds/year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rpmag: Gaia DR3 optical Rp-band magnitude in the Vega scale.

          rpmag_unc: Gaia DR3 optical photometric Rp-band magnitude uncertainty in the Vega scale.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/starcatalog/{path_id}",
            body=await async_maybe_transform(
                {
                    "astrometry_origin": astrometry_origin,
                    "classification_marking": classification_marking,
                    "cs_id": cs_id,
                    "data_mode": data_mode,
                    "dec": dec,
                    "ra": ra,
                    "source": source,
                    "star_epoch": star_epoch,
                    "body_id": body_id,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "cat_version": cat_version,
                    "dec_unc": dec_unc,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_unc": hmag_unc,
                    "jmag": jmag,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_unc": kmag_unc,
                    "mult_flag": mult_flag,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "origin": origin,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ra_unc": ra_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "var_flag": var_flag,
                },
                star_catalog_update_params.StarCatalogUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        dec: float | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[StarCatalogListResponse, AsyncOffsetPage[StarCatalogListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          dec: (One or more of fields 'dec, ra' are required.) Barycentric declination of the
              source in International Celestial Reference System (ICRS) at the reference
              epoch, in degrees.

          ra: (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
              the source in the International Celestial Reference System (ICRS) frame at the
              reference epoch, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/starcatalog",
            page=AsyncOffsetPage[StarCatalogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dec": dec,
                        "first_result": first_result,
                        "max_results": max_results,
                        "ra": ra,
                    },
                    star_catalog_list_params.StarCatalogListParams,
                ),
            ),
            model=StarCatalogListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete a dataset specified by the passed ID path parameter.
        A specific role is required to perform this service operation. Please contact
        the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/udl/starcatalog/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        dec: float | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          dec: (One or more of fields 'dec, ra' are required.) Barycentric declination of the
              source in International Celestial Reference System (ICRS) at the reference
              epoch, in degrees.

          ra: (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
              the source in the International Celestial Reference System (ICRS) frame at the
              reference epoch, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/starcatalog/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dec": dec,
                        "first_result": first_result,
                        "max_results": max_results,
                        "ra": ra,
                    },
                    star_catalog_count_params.StarCatalogCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[star_catalog_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        StarCatalog records as a POST body and ingest into the database. This operation
        is not intended to be used for automated feeds into UDL. Data providers should
        contact the UDL team for specific role assignments and for instructions on
        setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/starcatalog/createBulk",
            body=await async_maybe_transform(body, Iterable[star_catalog_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StarCatalogGetResponse:
        """
        Service operation to get a single StarCatalog record by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/starcatalog/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    star_catalog_get_params.StarCatalogGetParams,
                ),
            ),
            cast_to=StarCatalogGetResponse,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StarCatalogQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/starcatalog/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StarCatalogQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        dec: float | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StarCatalogTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          dec: (One or more of fields 'dec, ra' are required.) Barycentric declination of the
              source in International Celestial Reference System (ICRS) at the reference
              epoch, in degrees.

          ra: (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
              the source in the International Celestial Reference System (ICRS) frame at the
              reference epoch, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/starcatalog/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "dec": dec,
                        "first_result": first_result,
                        "max_results": max_results,
                        "ra": ra,
                    },
                    star_catalog_tuple_params.StarCatalogTupleParams,
                ),
            ),
            cast_to=StarCatalogTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[star_catalog_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple StarCatalog records as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-starcatalog",
            body=await async_maybe_transform(body, Iterable[star_catalog_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class StarCatalogResourceWithRawResponse:
    def __init__(self, star_catalog: StarCatalogResource) -> None:
        self._star_catalog = star_catalog

        self.create = to_raw_response_wrapper(
            star_catalog.create,
        )
        self.update = to_raw_response_wrapper(
            star_catalog.update,
        )
        self.list = to_raw_response_wrapper(
            star_catalog.list,
        )
        self.delete = to_raw_response_wrapper(
            star_catalog.delete,
        )
        self.count = to_raw_response_wrapper(
            star_catalog.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            star_catalog.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            star_catalog.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            star_catalog.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            star_catalog.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            star_catalog.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._star_catalog.history)


class AsyncStarCatalogResourceWithRawResponse:
    def __init__(self, star_catalog: AsyncStarCatalogResource) -> None:
        self._star_catalog = star_catalog

        self.create = async_to_raw_response_wrapper(
            star_catalog.create,
        )
        self.update = async_to_raw_response_wrapper(
            star_catalog.update,
        )
        self.list = async_to_raw_response_wrapper(
            star_catalog.list,
        )
        self.delete = async_to_raw_response_wrapper(
            star_catalog.delete,
        )
        self.count = async_to_raw_response_wrapper(
            star_catalog.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            star_catalog.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            star_catalog.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            star_catalog.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            star_catalog.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            star_catalog.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._star_catalog.history)


class StarCatalogResourceWithStreamingResponse:
    def __init__(self, star_catalog: StarCatalogResource) -> None:
        self._star_catalog = star_catalog

        self.create = to_streamed_response_wrapper(
            star_catalog.create,
        )
        self.update = to_streamed_response_wrapper(
            star_catalog.update,
        )
        self.list = to_streamed_response_wrapper(
            star_catalog.list,
        )
        self.delete = to_streamed_response_wrapper(
            star_catalog.delete,
        )
        self.count = to_streamed_response_wrapper(
            star_catalog.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            star_catalog.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            star_catalog.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            star_catalog.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            star_catalog.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            star_catalog.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._star_catalog.history)


class AsyncStarCatalogResourceWithStreamingResponse:
    def __init__(self, star_catalog: AsyncStarCatalogResource) -> None:
        self._star_catalog = star_catalog

        self.create = async_to_streamed_response_wrapper(
            star_catalog.create,
        )
        self.update = async_to_streamed_response_wrapper(
            star_catalog.update,
        )
        self.list = async_to_streamed_response_wrapper(
            star_catalog.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            star_catalog.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            star_catalog.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            star_catalog.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            star_catalog.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            star_catalog.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            star_catalog.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            star_catalog.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._star_catalog.history)
