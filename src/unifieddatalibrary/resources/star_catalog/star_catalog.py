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
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
    """These services provide operations for posting and querying Star Catalog data.

    The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
    """

    @cached_property
    def history(self) -> HistoryResource:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
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
        astrometry_origin: str,
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "EXERCISE", "SIMULATED"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        aavso_vsx_id: int | Omit = omit,
        abgmag: float | Omit = omit,
        abgmag_origin: str | Omit = omit,
        abgmag_unc: float | Omit = omit,
        abimag: float | Omit = omit,
        abimag_origin: str | Omit = omit,
        abimag_unc: float | Omit = omit,
        abrmag: float | Omit = omit,
        abrmag_origin: str | Omit = omit,
        abrmag_unc: float | Omit = omit,
        abymag: float | Omit = omit,
        abymag_origin: str | Omit = omit,
        abymag_unc: float | Omit = omit,
        abzmag: float | Omit = omit,
        abzmag_origin: str | Omit = omit,
        abzmag_unc: float | Omit = omit,
        all_wis_ecc_ind: str | Omit = omit,
        all_wise_id: str | Omit = omit,
        all_wis_ena_ind: int | Omit = omit,
        all_wis_eph_qual_ind: str | Omit = omit,
        apass_id: str | Omit = omit,
        astrometric_excess_noise: float | Omit = omit,
        astrometric_excess_noise_sig: float | Omit = omit,
        bmag: float | Omit = omit,
        bmag_origin: str | Omit = omit,
        bmag_unc: float | Omit = omit,
        bpmag: float | Omit = omit,
        bpmag_unc: float | Omit = omit,
        carrasco_cat_id: int | Omit = omit,
        cat_version: str | Omit = omit,
        cat_wise2020_id: str | Omit = omit,
        dec_unc: float | Omit = omit,
        ducati_cat_id: str | Omit = omit,
        gaiadr3_cat_id: int | Omit = omit,
        gmag: float | Omit = omit,
        gmag_unc: float | Omit = omit,
        gnc_cat_id: int | Omit = omit,
        healpix_index: int | Omit = omit,
        hip_cat_id: int | Omit = omit,
        hmag: float | Omit = omit,
        hmag_origin: str | Omit = omit,
        hmag_unc: float | Omit = omit,
        imag: float | Omit = omit,
        imag_origin: str | Omit = omit,
        imag_unc: float | Omit = omit,
        jmag: float | Omit = omit,
        jmag_origin: str | Omit = omit,
        jmag_unc: float | Omit = omit,
        kmag: float | Omit = omit,
        kmag_origin: str | Omit = omit,
        kmag_unc: float | Omit = omit,
        morphology_ind: int | Omit = omit,
        mult_flag: bool | Omit = omit,
        multiplicity: str | Omit = omit,
        neighbor_dec: float | Omit = omit,
        neighbor_distance: float | Omit = omit,
        neighbor_flag: bool | Omit = omit,
        neighbor_id: int | Omit = omit,
        neighbor_ra: float | Omit = omit,
        non_single_star: str | Omit = omit,
        num_neighbors: int | Omit = omit,
        origin: str | Omit = omit,
        pan_starrs_id: int | Omit = omit,
        parallax: float | Omit = omit,
        parallax_unc: float | Omit = omit,
        pmdec: float | Omit = omit,
        pmdec_unc: float | Omit = omit,
        pmra: float | Omit = omit,
        pmra_unc: float | Omit = omit,
        pm_unc_flag: bool | Omit = omit,
        pos_unc_flag: bool | Omit = omit,
        ps1astrometry_correction_flag: int | Omit = omit,
        ps1_obj_info_flag: int | Omit = omit,
        ps1_quality_flag: int | Omit = omit,
        ra_unc: float | Omit = omit,
        rmag: float | Omit = omit,
        rmag_origin: str | Omit = omit,
        rmag_unc: float | Omit = omit,
        rpmag: float | Omit = omit,
        rpmag_unc: float | Omit = omit,
        ruwe: float | Omit = omit,
        sda_cat_id: int | Omit = omit,
        sgmag: float | Omit = omit,
        sgmag_unc: float | Omit = omit,
        shift: float | Omit = omit,
        shift_flag: bool | Omit = omit,
        shift_fwhm1: float | Omit = omit,
        shift_fwhm6: float | Omit = omit,
        sky_mapper_id: int | Omit = omit,
        two_mass_id: str | Omit = omit,
        two_mass_ph_qual_ind: str | Omit = omit,
        two_mass_read_flag: str | Omit = omit,
        two_mass_xsc_id: str | Omit = omit,
        tycho_dsc_id: int | Omit = omit,
        uhs_id: int | Omit = omit,
        ukidss_gcs_id: int | Omit = omit,
        ukidss_gps_id: int | Omit = omit,
        ukidss_las_id: int | Omit = omit,
        var_flag: bool | Omit = omit,
        variability: str | Omit = omit,
        vhs_id: int | Omit = omit,
        vmag: float | Omit = omit,
        vmag_origin: str | Omit = omit,
        vmag_unc: float | Omit = omit,
        w1mag: float | Omit = omit,
        w1mag_origin: str | Omit = omit,
        w1mag_unc: float | Omit = omit,
        w1sat: float | Omit = omit,
        w2mag: float | Omit = omit,
        w2mag_origin: str | Omit = omit,
        w2mag_unc: float | Omit = omit,
        w2sat: float | Omit = omit,
        w3mag: float | Omit = omit,
        w3mag_origin: str | Omit = omit,
        w3mag_unc: float | Omit = omit,
        w3sat: float | Omit = omit,
        w4mag: float | Omit = omit,
        w4mag_origin: str | Omit = omit,
        w4mag_unc: float | Omit = omit,
        w4sat: float | Omit = omit,
        wds_cat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single StarCatalog record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object (GA (GAIA), HI (HIPPARCOS), UB
              (USNOBSC), AL, AP, CA, CR, DU, FK6_I, FK6_III, PS, SK, TD, TP, TX, UC, UL, UH,
              UP, VH, VS, WD).

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record. This
              field will either contain the value in the gncCatId or sdaCatId field.

          data_mode:
              Indicator of whether the data is REAL, TEST, EXERCISE, or SIMULATED data:

              REAL: Data collected or produced that pertains to real-world objects, events,
              and analysis.

              TEST: Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

              EXERCISE: Data pertaining to a government or military exercise. The data may
              include both real and simulated data.

              SIMULATED: Synthetic data generated by a model to mimic real-world datasets.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          aavso_vsx_id: The American Association of Variable Star Observers (AAVSO) Variable Star Index
              (VSX) (VX) object ID of this object.

          abgmag: Optical AB g magnitude.

          abgmag_origin: Catalog of origin of optical AB g magnitude.

          abgmag_unc: Uncertainty of optical AB g magnitude.

          abimag: Optical AB i magnitude.

          abimag_origin: Catalog of origin of optical AB i magnitude.

          abimag_unc: Uncertainty of optical AB i magnitude.

          abrmag: Optical AB r magnitude.

          abrmag_origin: Catalog of origin of optical AB r magnitude.

          abrmag_unc: Uncertainty of optical AB r magnitude.

          abymag: Optical AB y magnitude.

          abymag_origin: Catalog of origin of optical AB y magnitude.

          abymag_unc: Uncertainty of optical AB y magnitude.

          abzmag: Optical AB z magnitude.

          abzmag_origin: Catalog of origin of optical AB z magnitude.

          abzmag_unc: Uncertainty of optical AB z magnitude.

          all_wis_ecc_ind: Contamination and confusion indicator in AllWISE.

          all_wise_id: The designation of this object in the All Wide-field Infrared Survey Explorer
              (AllWISE) catalog (AL).

          all_wis_ena_ind: Active deblending indicator in AllWISE.

          all_wis_eph_qual_ind: Photometric quality indicator in AllWISE.

          apass_id: The American Association of Variable Star Observers (AAVSO) Photometric All-Sky
              Survey (APASS) (AP) name of this object.

          astrometric_excess_noise: Astrometric excess noise in the Gaia catalog measured in milliarcseconds.

          astrometric_excess_noise_sig: Astrometric excess noise sigma in Gaia.

          bmag: Optical Johnson B magnitude measured in magnitudes.

          bmag_origin: Catalog of origin of optical Johnson B magnitude (AP, CR, HI).

          bmag_unc: Uncertainty of optical Johnson B magnitude measured in magnitudes.

          bpmag: Gaia optical photometric Bp-band in the Vega scale measured in magnitudes.

          bpmag_unc: Gaia optical Bp-band uncertainty in the Vega scale measured in magnitudes.

          carrasco_cat_id: The Carrasco catalog (CR) identifier of this object.

          cat_version: The version of the catalog associated with this object.

          cat_wise2020_id: The CatWISE2020 (CA) catalog source ID of this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          ducati_cat_id: The Ducati catalog (DU) name of this object.

          gaiadr3_cat_id: The source ID of this object in the Gaia DR3 Catalog (GA).

          gmag: Gaia optical photometric G-band in the Vega scale measured in magnitudes.

          gmag_unc: Gaia optical photometric G-band uncertainty in the Vega scale measured in
              magnitudes.

          gnc_cat_id: The ID of this object in the Guidance and Navigation Control (GNC) Catalog. If
              this field is populated it shall match the csId field.

          healpix_index: The Healpix index. Consumers should contact the provider for details on the
              indexing scheme.

          hip_cat_id: The HIP ID of this object in the Hipparcos Catalog (HI).

          hmag: Near-infrared photometric H-band magnitude in the Vega scale measured in
              magnitudes.

          hmag_origin: Near-infrared photometric H-band catalog of origin in the Vega scale (TP, UC,
              UL, UP, VH).

          hmag_unc: Near-infrared photometric H-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          imag: Optical Johnson I magnitude measured in magnitudes.

          imag_origin: Catalog of origin of optical Johnson I magnitude (CR, GA, HI).

          imag_unc: Uncertainty of optical Johnson I magnitude measured in magnitudes.

          jmag: Near-infrared photometric J-band magnitude in the Vega scale measured in
              magnitudes.

          jmag_origin: Near-infrared photometric J-band catalog of origin in the Vega scale (TP, UH,
              UL, UP, VH).

          jmag_unc: Near-infrared photometric J-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          kmag: Near-infrared photometric K-band magnitude in the Vega scale measured in
              magnitudes.

          kmag_origin: Near-infrared photometric K-band catalog of origin in the Vega scale (TP, UC,
              UH, UL, UP, VH).

          kmag_unc: Near-infrared photometric K-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          morphology_ind: Morphology indicator. Consumers should contact the provider for details on the
              specifications.

          mult_flag: Flag indicating that this is a multiple object source.

          multiplicity: Identifier indicating multiplicity is detected. Consumers should contact the
              provider for details on the specifications.

          neighbor_dec: Dec of nearest neighbor measured in degrees.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          neighbor_ra: RA of nearest neighbor measured in degrees.

          non_single_star: Identifier indicating the source is a non-single star in gaia (additional
              information is available in non-single star tables. Consumers should contact the
              provider for details on the specifications).

          num_neighbors: Number of neighbors.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pan_starrs_id: The Panoramic Survey Telescope and Rapid Response System (Pan-STARRS) (PS)
              object ID.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds per year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds per year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds per year, at
              the reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds per year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds per year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ps1astrometry_correction_flag: Astrometry correction flag in Pan-STARRS.

          ps1_obj_info_flag: Object information flag in Pan-STARRS.

          ps1_quality_flag: Quality flag in Pan-STARRS.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rmag: Optical Johnson R magnitude measured in magnitudes.

          rmag_origin: Catalog of origin of the Optical Johnson R magnitude (CR, GA).

          rmag_unc: Uncertainty of the Optical Johnson R magnitude measured in magnitudes.

          rpmag: Gaia optical Rp-band in the Vega scale measured in magnitudes.

          rpmag_unc: Gaia optical photometric Rp-band uncertainty in the Vega scale measured in
              magnitudes.

          ruwe: RUWE in Gaia.

          sda_cat_id: The ID of this object in the Space Domain Awareness (SDA) Catalog. If this field
              is populated it shall match the csId field.

          sgmag: Original G magnitude if the source is in Gaia, otherwise the magnitude is
              converted from other photometric passbands, when possible, measured in
              magnitudes.

          sgmag_unc: Uncertainty of sgmag measured in magnitudes.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          shift_fwhm1: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of one
              arcsecond.

          shift_fwhm6: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of six
              arcseconds.

          sky_mapper_id: The SkyMapper (SK) catalog object ID.

          two_mass_id: The designation of this object in the Two Micron All Sky Survey (2MASS) Point
              Source Catalog (TP).

          two_mass_ph_qual_ind: Photometric (PH) quality indicator in 2MASS PSC.

          two_mass_read_flag: Read flag in 2MASS PSC.

          two_mass_xsc_id: The Two Micron All Sky Survey (2MASS) Extended Source Catalog (XSC) (TX)
              designation of this object.

          tycho_dsc_id: The Tycho Double Star Catalog (TD) identifier (specified as Tycho-2 ID) of this
              object.

          uhs_id: The United Kingdom Infrared Telescope (UKIRT) Hemispheric Survey (UHS) (UH)
              source ID of this object.

          ukidss_gcs_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Clusters Survey
              (GCS) (UC) source ID of this object.

          ukidss_gps_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Plane Survey (GPS)
              (UP) source ID of this object.

          ukidss_las_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Large Area Survey (LAS)
              (UL) source ID of this object.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          variability: Identifier indicating variability is present in the photometric data. Consumers
              should contact the provider for details on the specifications.

          vhs_id: The Visible and Infrared Survey Telescope for Astronomy (VISTA) Hemisphere
              Survey (VHS) (VS) source ID of this object.

          vmag: Optical Johnson V magnitude measured in magnitudes.

          vmag_origin: Catalog of origin of Optical Johnson V magnitude (AP, CR, DU, GA, HI).

          vmag_unc: Uncertainty of the Optical Johnson V magnitude measured in magnitudes.

          w1mag: Mid-infrared photometric W1-band (3.4 microns) magnitude in the Vega system
              measured in magnitudes.

          w1mag_origin: Mid-infrared photometric W1-band (3.4 microns) catalog of origin in the Vega
              system (AL, CA).

          w1mag_unc: Mid-infrared photometric W1-band (3.4 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w1sat: Mid-infrared photometric W1-band (3.4 microns) saturated pixel fraction in the
              Vega system.

          w2mag: Mid-infrared photometric W2-band (4.6 microns) magnitude in the Vega system
              measured in magnitudes.

          w2mag_origin: Mid-infrared photometric W2-band (4.6 microns) catalog of origin in the Vega
              system (AL, CA).

          w2mag_unc: Mid-infrared photometric W2-band (4.6 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w2sat: Mid-infrared photometric W2-band (4.6 microns) saturated pixel fraction in the
              Vega system.

          w3mag: Mid-infrared photometric W3-band (12 microns) magnitude in the Vega system
              measured in magnitudes.

          w3mag_origin: Mid-infrared photometric W3-band (12 microns) catalog of origin in the Vega
              system (AL).

          w3mag_unc: Mid-infrared photometric W3-band (12 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w3sat: Mid-infrared photometric W3-band (12 microns) saturated pixel fraction in the
              Vega system.

          w4mag: Mid-infrared photometric W4-band (22 microns) magnitude in the Vega system
              measured in magnitudes.

          w4mag_origin: Mid-infrared photometric W4-band (22 microns) catalog of origin in the Vega
              system (AL).

          w4mag_unc: Mid-infrared photometric W4-band (22 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w4sat: Mid-infrared photometric W4-band (22 microns) saturated pixel fraction in the
              Vega system.

          wds_cat_id: The Washington Double Star Catalog (WD) identifier of this object.

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
                    "aavso_vsx_id": aavso_vsx_id,
                    "abgmag": abgmag,
                    "abgmag_origin": abgmag_origin,
                    "abgmag_unc": abgmag_unc,
                    "abimag": abimag,
                    "abimag_origin": abimag_origin,
                    "abimag_unc": abimag_unc,
                    "abrmag": abrmag,
                    "abrmag_origin": abrmag_origin,
                    "abrmag_unc": abrmag_unc,
                    "abymag": abymag,
                    "abymag_origin": abymag_origin,
                    "abymag_unc": abymag_unc,
                    "abzmag": abzmag,
                    "abzmag_origin": abzmag_origin,
                    "abzmag_unc": abzmag_unc,
                    "all_wis_ecc_ind": all_wis_ecc_ind,
                    "all_wise_id": all_wise_id,
                    "all_wis_ena_ind": all_wis_ena_ind,
                    "all_wis_eph_qual_ind": all_wis_eph_qual_ind,
                    "apass_id": apass_id,
                    "astrometric_excess_noise": astrometric_excess_noise,
                    "astrometric_excess_noise_sig": astrometric_excess_noise_sig,
                    "bmag": bmag,
                    "bmag_origin": bmag_origin,
                    "bmag_unc": bmag_unc,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "carrasco_cat_id": carrasco_cat_id,
                    "cat_version": cat_version,
                    "cat_wise2020_id": cat_wise2020_id,
                    "dec_unc": dec_unc,
                    "ducati_cat_id": ducati_cat_id,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "healpix_index": healpix_index,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_origin": hmag_origin,
                    "hmag_unc": hmag_unc,
                    "imag": imag,
                    "imag_origin": imag_origin,
                    "imag_unc": imag_unc,
                    "jmag": jmag,
                    "jmag_origin": jmag_origin,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_origin": kmag_origin,
                    "kmag_unc": kmag_unc,
                    "morphology_ind": morphology_ind,
                    "mult_flag": mult_flag,
                    "multiplicity": multiplicity,
                    "neighbor_dec": neighbor_dec,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "neighbor_ra": neighbor_ra,
                    "non_single_star": non_single_star,
                    "num_neighbors": num_neighbors,
                    "origin": origin,
                    "pan_starrs_id": pan_starrs_id,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ps1astrometry_correction_flag": ps1astrometry_correction_flag,
                    "ps1_obj_info_flag": ps1_obj_info_flag,
                    "ps1_quality_flag": ps1_quality_flag,
                    "ra_unc": ra_unc,
                    "rmag": rmag,
                    "rmag_origin": rmag_origin,
                    "rmag_unc": rmag_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "ruwe": ruwe,
                    "sda_cat_id": sda_cat_id,
                    "sgmag": sgmag,
                    "sgmag_unc": sgmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "shift_fwhm1": shift_fwhm1,
                    "shift_fwhm6": shift_fwhm6,
                    "sky_mapper_id": sky_mapper_id,
                    "two_mass_id": two_mass_id,
                    "two_mass_ph_qual_ind": two_mass_ph_qual_ind,
                    "two_mass_read_flag": two_mass_read_flag,
                    "two_mass_xsc_id": two_mass_xsc_id,
                    "tycho_dsc_id": tycho_dsc_id,
                    "uhs_id": uhs_id,
                    "ukidss_gcs_id": ukidss_gcs_id,
                    "ukidss_gps_id": ukidss_gps_id,
                    "ukidss_las_id": ukidss_las_id,
                    "var_flag": var_flag,
                    "variability": variability,
                    "vhs_id": vhs_id,
                    "vmag": vmag,
                    "vmag_origin": vmag_origin,
                    "vmag_unc": vmag_unc,
                    "w1mag": w1mag,
                    "w1mag_origin": w1mag_origin,
                    "w1mag_unc": w1mag_unc,
                    "w1sat": w1sat,
                    "w2mag": w2mag,
                    "w2mag_origin": w2mag_origin,
                    "w2mag_unc": w2mag_unc,
                    "w2sat": w2sat,
                    "w3mag": w3mag,
                    "w3mag_origin": w3mag_origin,
                    "w3mag_unc": w3mag_unc,
                    "w3sat": w3sat,
                    "w4mag": w4mag,
                    "w4mag_origin": w4mag_origin,
                    "w4mag_unc": w4mag_unc,
                    "w4sat": w4sat,
                    "wds_cat_id": wds_cat_id,
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
        id: str,
        *,
        astrometry_origin: str,
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "EXERCISE", "SIMULATED"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        aavso_vsx_id: int | Omit = omit,
        abgmag: float | Omit = omit,
        abgmag_origin: str | Omit = omit,
        abgmag_unc: float | Omit = omit,
        abimag: float | Omit = omit,
        abimag_origin: str | Omit = omit,
        abimag_unc: float | Omit = omit,
        abrmag: float | Omit = omit,
        abrmag_origin: str | Omit = omit,
        abrmag_unc: float | Omit = omit,
        abymag: float | Omit = omit,
        abymag_origin: str | Omit = omit,
        abymag_unc: float | Omit = omit,
        abzmag: float | Omit = omit,
        abzmag_origin: str | Omit = omit,
        abzmag_unc: float | Omit = omit,
        all_wis_ecc_ind: str | Omit = omit,
        all_wise_id: str | Omit = omit,
        all_wis_ena_ind: int | Omit = omit,
        all_wis_eph_qual_ind: str | Omit = omit,
        apass_id: str | Omit = omit,
        astrometric_excess_noise: float | Omit = omit,
        astrometric_excess_noise_sig: float | Omit = omit,
        bmag: float | Omit = omit,
        bmag_origin: str | Omit = omit,
        bmag_unc: float | Omit = omit,
        bpmag: float | Omit = omit,
        bpmag_unc: float | Omit = omit,
        carrasco_cat_id: int | Omit = omit,
        cat_version: str | Omit = omit,
        cat_wise2020_id: str | Omit = omit,
        dec_unc: float | Omit = omit,
        ducati_cat_id: str | Omit = omit,
        gaiadr3_cat_id: int | Omit = omit,
        gmag: float | Omit = omit,
        gmag_unc: float | Omit = omit,
        gnc_cat_id: int | Omit = omit,
        healpix_index: int | Omit = omit,
        hip_cat_id: int | Omit = omit,
        hmag: float | Omit = omit,
        hmag_origin: str | Omit = omit,
        hmag_unc: float | Omit = omit,
        imag: float | Omit = omit,
        imag_origin: str | Omit = omit,
        imag_unc: float | Omit = omit,
        jmag: float | Omit = omit,
        jmag_origin: str | Omit = omit,
        jmag_unc: float | Omit = omit,
        kmag: float | Omit = omit,
        kmag_origin: str | Omit = omit,
        kmag_unc: float | Omit = omit,
        morphology_ind: int | Omit = omit,
        mult_flag: bool | Omit = omit,
        multiplicity: str | Omit = omit,
        neighbor_dec: float | Omit = omit,
        neighbor_distance: float | Omit = omit,
        neighbor_flag: bool | Omit = omit,
        neighbor_id: int | Omit = omit,
        neighbor_ra: float | Omit = omit,
        non_single_star: str | Omit = omit,
        num_neighbors: int | Omit = omit,
        origin: str | Omit = omit,
        pan_starrs_id: int | Omit = omit,
        parallax: float | Omit = omit,
        parallax_unc: float | Omit = omit,
        pmdec: float | Omit = omit,
        pmdec_unc: float | Omit = omit,
        pmra: float | Omit = omit,
        pmra_unc: float | Omit = omit,
        pm_unc_flag: bool | Omit = omit,
        pos_unc_flag: bool | Omit = omit,
        ps1astrometry_correction_flag: int | Omit = omit,
        ps1_obj_info_flag: int | Omit = omit,
        ps1_quality_flag: int | Omit = omit,
        ra_unc: float | Omit = omit,
        rmag: float | Omit = omit,
        rmag_origin: str | Omit = omit,
        rmag_unc: float | Omit = omit,
        rpmag: float | Omit = omit,
        rpmag_unc: float | Omit = omit,
        ruwe: float | Omit = omit,
        sda_cat_id: int | Omit = omit,
        sgmag: float | Omit = omit,
        sgmag_unc: float | Omit = omit,
        shift: float | Omit = omit,
        shift_flag: bool | Omit = omit,
        shift_fwhm1: float | Omit = omit,
        shift_fwhm6: float | Omit = omit,
        sky_mapper_id: int | Omit = omit,
        two_mass_id: str | Omit = omit,
        two_mass_ph_qual_ind: str | Omit = omit,
        two_mass_read_flag: str | Omit = omit,
        two_mass_xsc_id: str | Omit = omit,
        tycho_dsc_id: int | Omit = omit,
        uhs_id: int | Omit = omit,
        ukidss_gcs_id: int | Omit = omit,
        ukidss_gps_id: int | Omit = omit,
        ukidss_las_id: int | Omit = omit,
        var_flag: bool | Omit = omit,
        variability: str | Omit = omit,
        vhs_id: int | Omit = omit,
        vmag: float | Omit = omit,
        vmag_origin: str | Omit = omit,
        vmag_unc: float | Omit = omit,
        w1mag: float | Omit = omit,
        w1mag_origin: str | Omit = omit,
        w1mag_unc: float | Omit = omit,
        w1sat: float | Omit = omit,
        w2mag: float | Omit = omit,
        w2mag_origin: str | Omit = omit,
        w2mag_unc: float | Omit = omit,
        w2sat: float | Omit = omit,
        w3mag: float | Omit = omit,
        w3mag_origin: str | Omit = omit,
        w3mag_unc: float | Omit = omit,
        w3sat: float | Omit = omit,
        w4mag: float | Omit = omit,
        w4mag_origin: str | Omit = omit,
        w4mag_unc: float | Omit = omit,
        w4sat: float | Omit = omit,
        wds_cat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Service operation to update a single starcatalog record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object (GA (GAIA), HI (HIPPARCOS), UB
              (USNOBSC), AL, AP, CA, CR, DU, FK6_I, FK6_III, PS, SK, TD, TP, TX, UC, UL, UH,
              UP, VH, VS, WD).

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record. This
              field will either contain the value in the gncCatId or sdaCatId field.

          data_mode:
              Indicator of whether the data is REAL, TEST, EXERCISE, or SIMULATED data:

              REAL: Data collected or produced that pertains to real-world objects, events,
              and analysis.

              TEST: Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

              EXERCISE: Data pertaining to a government or military exercise. The data may
              include both real and simulated data.

              SIMULATED: Synthetic data generated by a model to mimic real-world datasets.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          aavso_vsx_id: The American Association of Variable Star Observers (AAVSO) Variable Star Index
              (VSX) (VX) object ID of this object.

          abgmag: Optical AB g magnitude.

          abgmag_origin: Catalog of origin of optical AB g magnitude.

          abgmag_unc: Uncertainty of optical AB g magnitude.

          abimag: Optical AB i magnitude.

          abimag_origin: Catalog of origin of optical AB i magnitude.

          abimag_unc: Uncertainty of optical AB i magnitude.

          abrmag: Optical AB r magnitude.

          abrmag_origin: Catalog of origin of optical AB r magnitude.

          abrmag_unc: Uncertainty of optical AB r magnitude.

          abymag: Optical AB y magnitude.

          abymag_origin: Catalog of origin of optical AB y magnitude.

          abymag_unc: Uncertainty of optical AB y magnitude.

          abzmag: Optical AB z magnitude.

          abzmag_origin: Catalog of origin of optical AB z magnitude.

          abzmag_unc: Uncertainty of optical AB z magnitude.

          all_wis_ecc_ind: Contamination and confusion indicator in AllWISE.

          all_wise_id: The designation of this object in the All Wide-field Infrared Survey Explorer
              (AllWISE) catalog (AL).

          all_wis_ena_ind: Active deblending indicator in AllWISE.

          all_wis_eph_qual_ind: Photometric quality indicator in AllWISE.

          apass_id: The American Association of Variable Star Observers (AAVSO) Photometric All-Sky
              Survey (APASS) (AP) name of this object.

          astrometric_excess_noise: Astrometric excess noise in the Gaia catalog measured in milliarcseconds.

          astrometric_excess_noise_sig: Astrometric excess noise sigma in Gaia.

          bmag: Optical Johnson B magnitude measured in magnitudes.

          bmag_origin: Catalog of origin of optical Johnson B magnitude (AP, CR, HI).

          bmag_unc: Uncertainty of optical Johnson B magnitude measured in magnitudes.

          bpmag: Gaia optical photometric Bp-band in the Vega scale measured in magnitudes.

          bpmag_unc: Gaia optical Bp-band uncertainty in the Vega scale measured in magnitudes.

          carrasco_cat_id: The Carrasco catalog (CR) identifier of this object.

          cat_version: The version of the catalog associated with this object.

          cat_wise2020_id: The CatWISE2020 (CA) catalog source ID of this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          ducati_cat_id: The Ducati catalog (DU) name of this object.

          gaiadr3_cat_id: The source ID of this object in the Gaia DR3 Catalog (GA).

          gmag: Gaia optical photometric G-band in the Vega scale measured in magnitudes.

          gmag_unc: Gaia optical photometric G-band uncertainty in the Vega scale measured in
              magnitudes.

          gnc_cat_id: The ID of this object in the Guidance and Navigation Control (GNC) Catalog. If
              this field is populated it shall match the csId field.

          healpix_index: The Healpix index. Consumers should contact the provider for details on the
              indexing scheme.

          hip_cat_id: The HIP ID of this object in the Hipparcos Catalog (HI).

          hmag: Near-infrared photometric H-band magnitude in the Vega scale measured in
              magnitudes.

          hmag_origin: Near-infrared photometric H-band catalog of origin in the Vega scale (TP, UC,
              UL, UP, VH).

          hmag_unc: Near-infrared photometric H-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          imag: Optical Johnson I magnitude measured in magnitudes.

          imag_origin: Catalog of origin of optical Johnson I magnitude (CR, GA, HI).

          imag_unc: Uncertainty of optical Johnson I magnitude measured in magnitudes.

          jmag: Near-infrared photometric J-band magnitude in the Vega scale measured in
              magnitudes.

          jmag_origin: Near-infrared photometric J-band catalog of origin in the Vega scale (TP, UH,
              UL, UP, VH).

          jmag_unc: Near-infrared photometric J-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          kmag: Near-infrared photometric K-band magnitude in the Vega scale measured in
              magnitudes.

          kmag_origin: Near-infrared photometric K-band catalog of origin in the Vega scale (TP, UC,
              UH, UL, UP, VH).

          kmag_unc: Near-infrared photometric K-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          morphology_ind: Morphology indicator. Consumers should contact the provider for details on the
              specifications.

          mult_flag: Flag indicating that this is a multiple object source.

          multiplicity: Identifier indicating multiplicity is detected. Consumers should contact the
              provider for details on the specifications.

          neighbor_dec: Dec of nearest neighbor measured in degrees.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          neighbor_ra: RA of nearest neighbor measured in degrees.

          non_single_star: Identifier indicating the source is a non-single star in gaia (additional
              information is available in non-single star tables. Consumers should contact the
              provider for details on the specifications).

          num_neighbors: Number of neighbors.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pan_starrs_id: The Panoramic Survey Telescope and Rapid Response System (Pan-STARRS) (PS)
              object ID.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds per year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds per year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds per year, at
              the reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds per year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds per year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ps1astrometry_correction_flag: Astrometry correction flag in Pan-STARRS.

          ps1_obj_info_flag: Object information flag in Pan-STARRS.

          ps1_quality_flag: Quality flag in Pan-STARRS.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rmag: Optical Johnson R magnitude measured in magnitudes.

          rmag_origin: Catalog of origin of the Optical Johnson R magnitude (CR, GA).

          rmag_unc: Uncertainty of the Optical Johnson R magnitude measured in magnitudes.

          rpmag: Gaia optical Rp-band in the Vega scale measured in magnitudes.

          rpmag_unc: Gaia optical photometric Rp-band uncertainty in the Vega scale measured in
              magnitudes.

          ruwe: RUWE in Gaia.

          sda_cat_id: The ID of this object in the Space Domain Awareness (SDA) Catalog. If this field
              is populated it shall match the csId field.

          sgmag: Original G magnitude if the source is in Gaia, otherwise the magnitude is
              converted from other photometric passbands, when possible, measured in
              magnitudes.

          sgmag_unc: Uncertainty of sgmag measured in magnitudes.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          shift_fwhm1: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of one
              arcsecond.

          shift_fwhm6: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of six
              arcseconds.

          sky_mapper_id: The SkyMapper (SK) catalog object ID.

          two_mass_id: The designation of this object in the Two Micron All Sky Survey (2MASS) Point
              Source Catalog (TP).

          two_mass_ph_qual_ind: Photometric (PH) quality indicator in 2MASS PSC.

          two_mass_read_flag: Read flag in 2MASS PSC.

          two_mass_xsc_id: The Two Micron All Sky Survey (2MASS) Extended Source Catalog (XSC) (TX)
              designation of this object.

          tycho_dsc_id: The Tycho Double Star Catalog (TD) identifier (specified as Tycho-2 ID) of this
              object.

          uhs_id: The United Kingdom Infrared Telescope (UKIRT) Hemispheric Survey (UHS) (UH)
              source ID of this object.

          ukidss_gcs_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Clusters Survey
              (GCS) (UC) source ID of this object.

          ukidss_gps_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Plane Survey (GPS)
              (UP) source ID of this object.

          ukidss_las_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Large Area Survey (LAS)
              (UL) source ID of this object.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          variability: Identifier indicating variability is present in the photometric data. Consumers
              should contact the provider for details on the specifications.

          vhs_id: The Visible and Infrared Survey Telescope for Astronomy (VISTA) Hemisphere
              Survey (VHS) (VS) source ID of this object.

          vmag: Optical Johnson V magnitude measured in magnitudes.

          vmag_origin: Catalog of origin of Optical Johnson V magnitude (AP, CR, DU, GA, HI).

          vmag_unc: Uncertainty of the Optical Johnson V magnitude measured in magnitudes.

          w1mag: Mid-infrared photometric W1-band (3.4 microns) magnitude in the Vega system
              measured in magnitudes.

          w1mag_origin: Mid-infrared photometric W1-band (3.4 microns) catalog of origin in the Vega
              system (AL, CA).

          w1mag_unc: Mid-infrared photometric W1-band (3.4 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w1sat: Mid-infrared photometric W1-band (3.4 microns) saturated pixel fraction in the
              Vega system.

          w2mag: Mid-infrared photometric W2-band (4.6 microns) magnitude in the Vega system
              measured in magnitudes.

          w2mag_origin: Mid-infrared photometric W2-band (4.6 microns) catalog of origin in the Vega
              system (AL, CA).

          w2mag_unc: Mid-infrared photometric W2-band (4.6 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w2sat: Mid-infrared photometric W2-band (4.6 microns) saturated pixel fraction in the
              Vega system.

          w3mag: Mid-infrared photometric W3-band (12 microns) magnitude in the Vega system
              measured in magnitudes.

          w3mag_origin: Mid-infrared photometric W3-band (12 microns) catalog of origin in the Vega
              system (AL).

          w3mag_unc: Mid-infrared photometric W3-band (12 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w3sat: Mid-infrared photometric W3-band (12 microns) saturated pixel fraction in the
              Vega system.

          w4mag: Mid-infrared photometric W4-band (22 microns) magnitude in the Vega system
              measured in magnitudes.

          w4mag_origin: Mid-infrared photometric W4-band (22 microns) catalog of origin in the Vega
              system (AL).

          w4mag_unc: Mid-infrared photometric W4-band (22 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w4sat: Mid-infrared photometric W4-band (22 microns) saturated pixel fraction in the
              Vega system.

          wds_cat_id: The Washington Double Star Catalog (WD) identifier of this object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/udl/starcatalog/{id}", id=id),
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
                    "aavso_vsx_id": aavso_vsx_id,
                    "abgmag": abgmag,
                    "abgmag_origin": abgmag_origin,
                    "abgmag_unc": abgmag_unc,
                    "abimag": abimag,
                    "abimag_origin": abimag_origin,
                    "abimag_unc": abimag_unc,
                    "abrmag": abrmag,
                    "abrmag_origin": abrmag_origin,
                    "abrmag_unc": abrmag_unc,
                    "abymag": abymag,
                    "abymag_origin": abymag_origin,
                    "abymag_unc": abymag_unc,
                    "abzmag": abzmag,
                    "abzmag_origin": abzmag_origin,
                    "abzmag_unc": abzmag_unc,
                    "all_wis_ecc_ind": all_wis_ecc_ind,
                    "all_wise_id": all_wise_id,
                    "all_wis_ena_ind": all_wis_ena_ind,
                    "all_wis_eph_qual_ind": all_wis_eph_qual_ind,
                    "apass_id": apass_id,
                    "astrometric_excess_noise": astrometric_excess_noise,
                    "astrometric_excess_noise_sig": astrometric_excess_noise_sig,
                    "bmag": bmag,
                    "bmag_origin": bmag_origin,
                    "bmag_unc": bmag_unc,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "carrasco_cat_id": carrasco_cat_id,
                    "cat_version": cat_version,
                    "cat_wise2020_id": cat_wise2020_id,
                    "dec_unc": dec_unc,
                    "ducati_cat_id": ducati_cat_id,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "healpix_index": healpix_index,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_origin": hmag_origin,
                    "hmag_unc": hmag_unc,
                    "imag": imag,
                    "imag_origin": imag_origin,
                    "imag_unc": imag_unc,
                    "jmag": jmag,
                    "jmag_origin": jmag_origin,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_origin": kmag_origin,
                    "kmag_unc": kmag_unc,
                    "morphology_ind": morphology_ind,
                    "mult_flag": mult_flag,
                    "multiplicity": multiplicity,
                    "neighbor_dec": neighbor_dec,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "neighbor_ra": neighbor_ra,
                    "non_single_star": non_single_star,
                    "num_neighbors": num_neighbors,
                    "origin": origin,
                    "pan_starrs_id": pan_starrs_id,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ps1astrometry_correction_flag": ps1astrometry_correction_flag,
                    "ps1_obj_info_flag": ps1_obj_info_flag,
                    "ps1_quality_flag": ps1_quality_flag,
                    "ra_unc": ra_unc,
                    "rmag": rmag,
                    "rmag_origin": rmag_origin,
                    "rmag_unc": rmag_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "ruwe": ruwe,
                    "sda_cat_id": sda_cat_id,
                    "sgmag": sgmag,
                    "sgmag_unc": sgmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "shift_fwhm1": shift_fwhm1,
                    "shift_fwhm6": shift_fwhm6,
                    "sky_mapper_id": sky_mapper_id,
                    "two_mass_id": two_mass_id,
                    "two_mass_ph_qual_ind": two_mass_ph_qual_ind,
                    "two_mass_read_flag": two_mass_read_flag,
                    "two_mass_xsc_id": two_mass_xsc_id,
                    "tycho_dsc_id": tycho_dsc_id,
                    "uhs_id": uhs_id,
                    "ukidss_gcs_id": ukidss_gcs_id,
                    "ukidss_gps_id": ukidss_gps_id,
                    "ukidss_las_id": ukidss_las_id,
                    "var_flag": var_flag,
                    "variability": variability,
                    "vhs_id": vhs_id,
                    "vmag": vmag,
                    "vmag_origin": vmag_origin,
                    "vmag_unc": vmag_unc,
                    "w1mag": w1mag,
                    "w1mag_origin": w1mag_origin,
                    "w1mag_unc": w1mag_unc,
                    "w1sat": w1sat,
                    "w2mag": w2mag,
                    "w2mag_origin": w2mag_origin,
                    "w2mag_unc": w2mag_unc,
                    "w2sat": w2sat,
                    "w3mag": w3mag,
                    "w3mag_origin": w3mag_origin,
                    "w3mag_unc": w3mag_unc,
                    "w3sat": w3sat,
                    "w4mag": w4mag,
                    "w4mag_origin": w4mag_origin,
                    "w4mag_unc": w4mag_unc,
                    "w4sat": w4sat,
                    "wds_cat_id": wds_cat_id,
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
        dec: float | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        ra: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[StarCatalogListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (`/udl/<datatype>/queryhelp`) for more details on valid/required query parameter
        information.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/udl/starcatalog/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        dec: float | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        ra: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (`/udl/<datatype>/queryhelp`) for more details on
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/udl/starcatalog/{id}", id=id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        dec: float | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        ra: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StarCatalogTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (`/udl/<datatype>/queryhelp`) for more details on valid/required query parameter
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    """These services provide operations for posting and querying Star Catalog data.

    The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
    """

    @cached_property
    def history(self) -> AsyncHistoryResource:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
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
        astrometry_origin: str,
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "EXERCISE", "SIMULATED"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        aavso_vsx_id: int | Omit = omit,
        abgmag: float | Omit = omit,
        abgmag_origin: str | Omit = omit,
        abgmag_unc: float | Omit = omit,
        abimag: float | Omit = omit,
        abimag_origin: str | Omit = omit,
        abimag_unc: float | Omit = omit,
        abrmag: float | Omit = omit,
        abrmag_origin: str | Omit = omit,
        abrmag_unc: float | Omit = omit,
        abymag: float | Omit = omit,
        abymag_origin: str | Omit = omit,
        abymag_unc: float | Omit = omit,
        abzmag: float | Omit = omit,
        abzmag_origin: str | Omit = omit,
        abzmag_unc: float | Omit = omit,
        all_wis_ecc_ind: str | Omit = omit,
        all_wise_id: str | Omit = omit,
        all_wis_ena_ind: int | Omit = omit,
        all_wis_eph_qual_ind: str | Omit = omit,
        apass_id: str | Omit = omit,
        astrometric_excess_noise: float | Omit = omit,
        astrometric_excess_noise_sig: float | Omit = omit,
        bmag: float | Omit = omit,
        bmag_origin: str | Omit = omit,
        bmag_unc: float | Omit = omit,
        bpmag: float | Omit = omit,
        bpmag_unc: float | Omit = omit,
        carrasco_cat_id: int | Omit = omit,
        cat_version: str | Omit = omit,
        cat_wise2020_id: str | Omit = omit,
        dec_unc: float | Omit = omit,
        ducati_cat_id: str | Omit = omit,
        gaiadr3_cat_id: int | Omit = omit,
        gmag: float | Omit = omit,
        gmag_unc: float | Omit = omit,
        gnc_cat_id: int | Omit = omit,
        healpix_index: int | Omit = omit,
        hip_cat_id: int | Omit = omit,
        hmag: float | Omit = omit,
        hmag_origin: str | Omit = omit,
        hmag_unc: float | Omit = omit,
        imag: float | Omit = omit,
        imag_origin: str | Omit = omit,
        imag_unc: float | Omit = omit,
        jmag: float | Omit = omit,
        jmag_origin: str | Omit = omit,
        jmag_unc: float | Omit = omit,
        kmag: float | Omit = omit,
        kmag_origin: str | Omit = omit,
        kmag_unc: float | Omit = omit,
        morphology_ind: int | Omit = omit,
        mult_flag: bool | Omit = omit,
        multiplicity: str | Omit = omit,
        neighbor_dec: float | Omit = omit,
        neighbor_distance: float | Omit = omit,
        neighbor_flag: bool | Omit = omit,
        neighbor_id: int | Omit = omit,
        neighbor_ra: float | Omit = omit,
        non_single_star: str | Omit = omit,
        num_neighbors: int | Omit = omit,
        origin: str | Omit = omit,
        pan_starrs_id: int | Omit = omit,
        parallax: float | Omit = omit,
        parallax_unc: float | Omit = omit,
        pmdec: float | Omit = omit,
        pmdec_unc: float | Omit = omit,
        pmra: float | Omit = omit,
        pmra_unc: float | Omit = omit,
        pm_unc_flag: bool | Omit = omit,
        pos_unc_flag: bool | Omit = omit,
        ps1astrometry_correction_flag: int | Omit = omit,
        ps1_obj_info_flag: int | Omit = omit,
        ps1_quality_flag: int | Omit = omit,
        ra_unc: float | Omit = omit,
        rmag: float | Omit = omit,
        rmag_origin: str | Omit = omit,
        rmag_unc: float | Omit = omit,
        rpmag: float | Omit = omit,
        rpmag_unc: float | Omit = omit,
        ruwe: float | Omit = omit,
        sda_cat_id: int | Omit = omit,
        sgmag: float | Omit = omit,
        sgmag_unc: float | Omit = omit,
        shift: float | Omit = omit,
        shift_flag: bool | Omit = omit,
        shift_fwhm1: float | Omit = omit,
        shift_fwhm6: float | Omit = omit,
        sky_mapper_id: int | Omit = omit,
        two_mass_id: str | Omit = omit,
        two_mass_ph_qual_ind: str | Omit = omit,
        two_mass_read_flag: str | Omit = omit,
        two_mass_xsc_id: str | Omit = omit,
        tycho_dsc_id: int | Omit = omit,
        uhs_id: int | Omit = omit,
        ukidss_gcs_id: int | Omit = omit,
        ukidss_gps_id: int | Omit = omit,
        ukidss_las_id: int | Omit = omit,
        var_flag: bool | Omit = omit,
        variability: str | Omit = omit,
        vhs_id: int | Omit = omit,
        vmag: float | Omit = omit,
        vmag_origin: str | Omit = omit,
        vmag_unc: float | Omit = omit,
        w1mag: float | Omit = omit,
        w1mag_origin: str | Omit = omit,
        w1mag_unc: float | Omit = omit,
        w1sat: float | Omit = omit,
        w2mag: float | Omit = omit,
        w2mag_origin: str | Omit = omit,
        w2mag_unc: float | Omit = omit,
        w2sat: float | Omit = omit,
        w3mag: float | Omit = omit,
        w3mag_origin: str | Omit = omit,
        w3mag_unc: float | Omit = omit,
        w3sat: float | Omit = omit,
        w4mag: float | Omit = omit,
        w4mag_origin: str | Omit = omit,
        w4mag_unc: float | Omit = omit,
        w4sat: float | Omit = omit,
        wds_cat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single StarCatalog record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object (GA (GAIA), HI (HIPPARCOS), UB
              (USNOBSC), AL, AP, CA, CR, DU, FK6_I, FK6_III, PS, SK, TD, TP, TX, UC, UL, UH,
              UP, VH, VS, WD).

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record. This
              field will either contain the value in the gncCatId or sdaCatId field.

          data_mode:
              Indicator of whether the data is REAL, TEST, EXERCISE, or SIMULATED data:

              REAL: Data collected or produced that pertains to real-world objects, events,
              and analysis.

              TEST: Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

              EXERCISE: Data pertaining to a government or military exercise. The data may
              include both real and simulated data.

              SIMULATED: Synthetic data generated by a model to mimic real-world datasets.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          aavso_vsx_id: The American Association of Variable Star Observers (AAVSO) Variable Star Index
              (VSX) (VX) object ID of this object.

          abgmag: Optical AB g magnitude.

          abgmag_origin: Catalog of origin of optical AB g magnitude.

          abgmag_unc: Uncertainty of optical AB g magnitude.

          abimag: Optical AB i magnitude.

          abimag_origin: Catalog of origin of optical AB i magnitude.

          abimag_unc: Uncertainty of optical AB i magnitude.

          abrmag: Optical AB r magnitude.

          abrmag_origin: Catalog of origin of optical AB r magnitude.

          abrmag_unc: Uncertainty of optical AB r magnitude.

          abymag: Optical AB y magnitude.

          abymag_origin: Catalog of origin of optical AB y magnitude.

          abymag_unc: Uncertainty of optical AB y magnitude.

          abzmag: Optical AB z magnitude.

          abzmag_origin: Catalog of origin of optical AB z magnitude.

          abzmag_unc: Uncertainty of optical AB z magnitude.

          all_wis_ecc_ind: Contamination and confusion indicator in AllWISE.

          all_wise_id: The designation of this object in the All Wide-field Infrared Survey Explorer
              (AllWISE) catalog (AL).

          all_wis_ena_ind: Active deblending indicator in AllWISE.

          all_wis_eph_qual_ind: Photometric quality indicator in AllWISE.

          apass_id: The American Association of Variable Star Observers (AAVSO) Photometric All-Sky
              Survey (APASS) (AP) name of this object.

          astrometric_excess_noise: Astrometric excess noise in the Gaia catalog measured in milliarcseconds.

          astrometric_excess_noise_sig: Astrometric excess noise sigma in Gaia.

          bmag: Optical Johnson B magnitude measured in magnitudes.

          bmag_origin: Catalog of origin of optical Johnson B magnitude (AP, CR, HI).

          bmag_unc: Uncertainty of optical Johnson B magnitude measured in magnitudes.

          bpmag: Gaia optical photometric Bp-band in the Vega scale measured in magnitudes.

          bpmag_unc: Gaia optical Bp-band uncertainty in the Vega scale measured in magnitudes.

          carrasco_cat_id: The Carrasco catalog (CR) identifier of this object.

          cat_version: The version of the catalog associated with this object.

          cat_wise2020_id: The CatWISE2020 (CA) catalog source ID of this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          ducati_cat_id: The Ducati catalog (DU) name of this object.

          gaiadr3_cat_id: The source ID of this object in the Gaia DR3 Catalog (GA).

          gmag: Gaia optical photometric G-band in the Vega scale measured in magnitudes.

          gmag_unc: Gaia optical photometric G-band uncertainty in the Vega scale measured in
              magnitudes.

          gnc_cat_id: The ID of this object in the Guidance and Navigation Control (GNC) Catalog. If
              this field is populated it shall match the csId field.

          healpix_index: The Healpix index. Consumers should contact the provider for details on the
              indexing scheme.

          hip_cat_id: The HIP ID of this object in the Hipparcos Catalog (HI).

          hmag: Near-infrared photometric H-band magnitude in the Vega scale measured in
              magnitudes.

          hmag_origin: Near-infrared photometric H-band catalog of origin in the Vega scale (TP, UC,
              UL, UP, VH).

          hmag_unc: Near-infrared photometric H-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          imag: Optical Johnson I magnitude measured in magnitudes.

          imag_origin: Catalog of origin of optical Johnson I magnitude (CR, GA, HI).

          imag_unc: Uncertainty of optical Johnson I magnitude measured in magnitudes.

          jmag: Near-infrared photometric J-band magnitude in the Vega scale measured in
              magnitudes.

          jmag_origin: Near-infrared photometric J-band catalog of origin in the Vega scale (TP, UH,
              UL, UP, VH).

          jmag_unc: Near-infrared photometric J-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          kmag: Near-infrared photometric K-band magnitude in the Vega scale measured in
              magnitudes.

          kmag_origin: Near-infrared photometric K-band catalog of origin in the Vega scale (TP, UC,
              UH, UL, UP, VH).

          kmag_unc: Near-infrared photometric K-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          morphology_ind: Morphology indicator. Consumers should contact the provider for details on the
              specifications.

          mult_flag: Flag indicating that this is a multiple object source.

          multiplicity: Identifier indicating multiplicity is detected. Consumers should contact the
              provider for details on the specifications.

          neighbor_dec: Dec of nearest neighbor measured in degrees.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          neighbor_ra: RA of nearest neighbor measured in degrees.

          non_single_star: Identifier indicating the source is a non-single star in gaia (additional
              information is available in non-single star tables. Consumers should contact the
              provider for details on the specifications).

          num_neighbors: Number of neighbors.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pan_starrs_id: The Panoramic Survey Telescope and Rapid Response System (Pan-STARRS) (PS)
              object ID.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds per year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds per year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds per year, at
              the reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds per year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds per year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ps1astrometry_correction_flag: Astrometry correction flag in Pan-STARRS.

          ps1_obj_info_flag: Object information flag in Pan-STARRS.

          ps1_quality_flag: Quality flag in Pan-STARRS.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rmag: Optical Johnson R magnitude measured in magnitudes.

          rmag_origin: Catalog of origin of the Optical Johnson R magnitude (CR, GA).

          rmag_unc: Uncertainty of the Optical Johnson R magnitude measured in magnitudes.

          rpmag: Gaia optical Rp-band in the Vega scale measured in magnitudes.

          rpmag_unc: Gaia optical photometric Rp-band uncertainty in the Vega scale measured in
              magnitudes.

          ruwe: RUWE in Gaia.

          sda_cat_id: The ID of this object in the Space Domain Awareness (SDA) Catalog. If this field
              is populated it shall match the csId field.

          sgmag: Original G magnitude if the source is in Gaia, otherwise the magnitude is
              converted from other photometric passbands, when possible, measured in
              magnitudes.

          sgmag_unc: Uncertainty of sgmag measured in magnitudes.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          shift_fwhm1: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of one
              arcsecond.

          shift_fwhm6: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of six
              arcseconds.

          sky_mapper_id: The SkyMapper (SK) catalog object ID.

          two_mass_id: The designation of this object in the Two Micron All Sky Survey (2MASS) Point
              Source Catalog (TP).

          two_mass_ph_qual_ind: Photometric (PH) quality indicator in 2MASS PSC.

          two_mass_read_flag: Read flag in 2MASS PSC.

          two_mass_xsc_id: The Two Micron All Sky Survey (2MASS) Extended Source Catalog (XSC) (TX)
              designation of this object.

          tycho_dsc_id: The Tycho Double Star Catalog (TD) identifier (specified as Tycho-2 ID) of this
              object.

          uhs_id: The United Kingdom Infrared Telescope (UKIRT) Hemispheric Survey (UHS) (UH)
              source ID of this object.

          ukidss_gcs_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Clusters Survey
              (GCS) (UC) source ID of this object.

          ukidss_gps_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Plane Survey (GPS)
              (UP) source ID of this object.

          ukidss_las_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Large Area Survey (LAS)
              (UL) source ID of this object.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          variability: Identifier indicating variability is present in the photometric data. Consumers
              should contact the provider for details on the specifications.

          vhs_id: The Visible and Infrared Survey Telescope for Astronomy (VISTA) Hemisphere
              Survey (VHS) (VS) source ID of this object.

          vmag: Optical Johnson V magnitude measured in magnitudes.

          vmag_origin: Catalog of origin of Optical Johnson V magnitude (AP, CR, DU, GA, HI).

          vmag_unc: Uncertainty of the Optical Johnson V magnitude measured in magnitudes.

          w1mag: Mid-infrared photometric W1-band (3.4 microns) magnitude in the Vega system
              measured in magnitudes.

          w1mag_origin: Mid-infrared photometric W1-band (3.4 microns) catalog of origin in the Vega
              system (AL, CA).

          w1mag_unc: Mid-infrared photometric W1-band (3.4 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w1sat: Mid-infrared photometric W1-band (3.4 microns) saturated pixel fraction in the
              Vega system.

          w2mag: Mid-infrared photometric W2-band (4.6 microns) magnitude in the Vega system
              measured in magnitudes.

          w2mag_origin: Mid-infrared photometric W2-band (4.6 microns) catalog of origin in the Vega
              system (AL, CA).

          w2mag_unc: Mid-infrared photometric W2-band (4.6 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w2sat: Mid-infrared photometric W2-band (4.6 microns) saturated pixel fraction in the
              Vega system.

          w3mag: Mid-infrared photometric W3-band (12 microns) magnitude in the Vega system
              measured in magnitudes.

          w3mag_origin: Mid-infrared photometric W3-band (12 microns) catalog of origin in the Vega
              system (AL).

          w3mag_unc: Mid-infrared photometric W3-band (12 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w3sat: Mid-infrared photometric W3-band (12 microns) saturated pixel fraction in the
              Vega system.

          w4mag: Mid-infrared photometric W4-band (22 microns) magnitude in the Vega system
              measured in magnitudes.

          w4mag_origin: Mid-infrared photometric W4-band (22 microns) catalog of origin in the Vega
              system (AL).

          w4mag_unc: Mid-infrared photometric W4-band (22 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w4sat: Mid-infrared photometric W4-band (22 microns) saturated pixel fraction in the
              Vega system.

          wds_cat_id: The Washington Double Star Catalog (WD) identifier of this object.

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
                    "aavso_vsx_id": aavso_vsx_id,
                    "abgmag": abgmag,
                    "abgmag_origin": abgmag_origin,
                    "abgmag_unc": abgmag_unc,
                    "abimag": abimag,
                    "abimag_origin": abimag_origin,
                    "abimag_unc": abimag_unc,
                    "abrmag": abrmag,
                    "abrmag_origin": abrmag_origin,
                    "abrmag_unc": abrmag_unc,
                    "abymag": abymag,
                    "abymag_origin": abymag_origin,
                    "abymag_unc": abymag_unc,
                    "abzmag": abzmag,
                    "abzmag_origin": abzmag_origin,
                    "abzmag_unc": abzmag_unc,
                    "all_wis_ecc_ind": all_wis_ecc_ind,
                    "all_wise_id": all_wise_id,
                    "all_wis_ena_ind": all_wis_ena_ind,
                    "all_wis_eph_qual_ind": all_wis_eph_qual_ind,
                    "apass_id": apass_id,
                    "astrometric_excess_noise": astrometric_excess_noise,
                    "astrometric_excess_noise_sig": astrometric_excess_noise_sig,
                    "bmag": bmag,
                    "bmag_origin": bmag_origin,
                    "bmag_unc": bmag_unc,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "carrasco_cat_id": carrasco_cat_id,
                    "cat_version": cat_version,
                    "cat_wise2020_id": cat_wise2020_id,
                    "dec_unc": dec_unc,
                    "ducati_cat_id": ducati_cat_id,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "healpix_index": healpix_index,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_origin": hmag_origin,
                    "hmag_unc": hmag_unc,
                    "imag": imag,
                    "imag_origin": imag_origin,
                    "imag_unc": imag_unc,
                    "jmag": jmag,
                    "jmag_origin": jmag_origin,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_origin": kmag_origin,
                    "kmag_unc": kmag_unc,
                    "morphology_ind": morphology_ind,
                    "mult_flag": mult_flag,
                    "multiplicity": multiplicity,
                    "neighbor_dec": neighbor_dec,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "neighbor_ra": neighbor_ra,
                    "non_single_star": non_single_star,
                    "num_neighbors": num_neighbors,
                    "origin": origin,
                    "pan_starrs_id": pan_starrs_id,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ps1astrometry_correction_flag": ps1astrometry_correction_flag,
                    "ps1_obj_info_flag": ps1_obj_info_flag,
                    "ps1_quality_flag": ps1_quality_flag,
                    "ra_unc": ra_unc,
                    "rmag": rmag,
                    "rmag_origin": rmag_origin,
                    "rmag_unc": rmag_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "ruwe": ruwe,
                    "sda_cat_id": sda_cat_id,
                    "sgmag": sgmag,
                    "sgmag_unc": sgmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "shift_fwhm1": shift_fwhm1,
                    "shift_fwhm6": shift_fwhm6,
                    "sky_mapper_id": sky_mapper_id,
                    "two_mass_id": two_mass_id,
                    "two_mass_ph_qual_ind": two_mass_ph_qual_ind,
                    "two_mass_read_flag": two_mass_read_flag,
                    "two_mass_xsc_id": two_mass_xsc_id,
                    "tycho_dsc_id": tycho_dsc_id,
                    "uhs_id": uhs_id,
                    "ukidss_gcs_id": ukidss_gcs_id,
                    "ukidss_gps_id": ukidss_gps_id,
                    "ukidss_las_id": ukidss_las_id,
                    "var_flag": var_flag,
                    "variability": variability,
                    "vhs_id": vhs_id,
                    "vmag": vmag,
                    "vmag_origin": vmag_origin,
                    "vmag_unc": vmag_unc,
                    "w1mag": w1mag,
                    "w1mag_origin": w1mag_origin,
                    "w1mag_unc": w1mag_unc,
                    "w1sat": w1sat,
                    "w2mag": w2mag,
                    "w2mag_origin": w2mag_origin,
                    "w2mag_unc": w2mag_unc,
                    "w2sat": w2sat,
                    "w3mag": w3mag,
                    "w3mag_origin": w3mag_origin,
                    "w3mag_unc": w3mag_unc,
                    "w3sat": w3sat,
                    "w4mag": w4mag,
                    "w4mag_origin": w4mag_origin,
                    "w4mag_unc": w4mag_unc,
                    "w4sat": w4sat,
                    "wds_cat_id": wds_cat_id,
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
        id: str,
        *,
        astrometry_origin: str,
        classification_marking: str,
        cs_id: int,
        data_mode: Literal["REAL", "TEST", "EXERCISE", "SIMULATED"],
        dec: float,
        ra: float,
        source: str,
        star_epoch: float,
        aavso_vsx_id: int | Omit = omit,
        abgmag: float | Omit = omit,
        abgmag_origin: str | Omit = omit,
        abgmag_unc: float | Omit = omit,
        abimag: float | Omit = omit,
        abimag_origin: str | Omit = omit,
        abimag_unc: float | Omit = omit,
        abrmag: float | Omit = omit,
        abrmag_origin: str | Omit = omit,
        abrmag_unc: float | Omit = omit,
        abymag: float | Omit = omit,
        abymag_origin: str | Omit = omit,
        abymag_unc: float | Omit = omit,
        abzmag: float | Omit = omit,
        abzmag_origin: str | Omit = omit,
        abzmag_unc: float | Omit = omit,
        all_wis_ecc_ind: str | Omit = omit,
        all_wise_id: str | Omit = omit,
        all_wis_ena_ind: int | Omit = omit,
        all_wis_eph_qual_ind: str | Omit = omit,
        apass_id: str | Omit = omit,
        astrometric_excess_noise: float | Omit = omit,
        astrometric_excess_noise_sig: float | Omit = omit,
        bmag: float | Omit = omit,
        bmag_origin: str | Omit = omit,
        bmag_unc: float | Omit = omit,
        bpmag: float | Omit = omit,
        bpmag_unc: float | Omit = omit,
        carrasco_cat_id: int | Omit = omit,
        cat_version: str | Omit = omit,
        cat_wise2020_id: str | Omit = omit,
        dec_unc: float | Omit = omit,
        ducati_cat_id: str | Omit = omit,
        gaiadr3_cat_id: int | Omit = omit,
        gmag: float | Omit = omit,
        gmag_unc: float | Omit = omit,
        gnc_cat_id: int | Omit = omit,
        healpix_index: int | Omit = omit,
        hip_cat_id: int | Omit = omit,
        hmag: float | Omit = omit,
        hmag_origin: str | Omit = omit,
        hmag_unc: float | Omit = omit,
        imag: float | Omit = omit,
        imag_origin: str | Omit = omit,
        imag_unc: float | Omit = omit,
        jmag: float | Omit = omit,
        jmag_origin: str | Omit = omit,
        jmag_unc: float | Omit = omit,
        kmag: float | Omit = omit,
        kmag_origin: str | Omit = omit,
        kmag_unc: float | Omit = omit,
        morphology_ind: int | Omit = omit,
        mult_flag: bool | Omit = omit,
        multiplicity: str | Omit = omit,
        neighbor_dec: float | Omit = omit,
        neighbor_distance: float | Omit = omit,
        neighbor_flag: bool | Omit = omit,
        neighbor_id: int | Omit = omit,
        neighbor_ra: float | Omit = omit,
        non_single_star: str | Omit = omit,
        num_neighbors: int | Omit = omit,
        origin: str | Omit = omit,
        pan_starrs_id: int | Omit = omit,
        parallax: float | Omit = omit,
        parallax_unc: float | Omit = omit,
        pmdec: float | Omit = omit,
        pmdec_unc: float | Omit = omit,
        pmra: float | Omit = omit,
        pmra_unc: float | Omit = omit,
        pm_unc_flag: bool | Omit = omit,
        pos_unc_flag: bool | Omit = omit,
        ps1astrometry_correction_flag: int | Omit = omit,
        ps1_obj_info_flag: int | Omit = omit,
        ps1_quality_flag: int | Omit = omit,
        ra_unc: float | Omit = omit,
        rmag: float | Omit = omit,
        rmag_origin: str | Omit = omit,
        rmag_unc: float | Omit = omit,
        rpmag: float | Omit = omit,
        rpmag_unc: float | Omit = omit,
        ruwe: float | Omit = omit,
        sda_cat_id: int | Omit = omit,
        sgmag: float | Omit = omit,
        sgmag_unc: float | Omit = omit,
        shift: float | Omit = omit,
        shift_flag: bool | Omit = omit,
        shift_fwhm1: float | Omit = omit,
        shift_fwhm6: float | Omit = omit,
        sky_mapper_id: int | Omit = omit,
        two_mass_id: str | Omit = omit,
        two_mass_ph_qual_ind: str | Omit = omit,
        two_mass_read_flag: str | Omit = omit,
        two_mass_xsc_id: str | Omit = omit,
        tycho_dsc_id: int | Omit = omit,
        uhs_id: int | Omit = omit,
        ukidss_gcs_id: int | Omit = omit,
        ukidss_gps_id: int | Omit = omit,
        ukidss_las_id: int | Omit = omit,
        var_flag: bool | Omit = omit,
        variability: str | Omit = omit,
        vhs_id: int | Omit = omit,
        vmag: float | Omit = omit,
        vmag_origin: str | Omit = omit,
        vmag_unc: float | Omit = omit,
        w1mag: float | Omit = omit,
        w1mag_origin: str | Omit = omit,
        w1mag_unc: float | Omit = omit,
        w1sat: float | Omit = omit,
        w2mag: float | Omit = omit,
        w2mag_origin: str | Omit = omit,
        w2mag_unc: float | Omit = omit,
        w2sat: float | Omit = omit,
        w3mag: float | Omit = omit,
        w3mag_origin: str | Omit = omit,
        w3mag_unc: float | Omit = omit,
        w3sat: float | Omit = omit,
        w4mag: float | Omit = omit,
        w4mag_origin: str | Omit = omit,
        w4mag_unc: float | Omit = omit,
        w4sat: float | Omit = omit,
        wds_cat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Service operation to update a single starcatalog record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          astrometry_origin: Originating astrometric catalog for this object (GA (GAIA), HI (HIPPARCOS), UB
              (USNOBSC), AL, AP, CA, CR, DU, FK6_I, FK6_III, PS, SK, TD, TP, TX, UC, UL, UH,
              UP, VH, VS, WD).

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cs_id: The ID of this object in the specific catalog associated with this record. This
              field will either contain the value in the gncCatId or sdaCatId field.

          data_mode:
              Indicator of whether the data is REAL, TEST, EXERCISE, or SIMULATED data:

              REAL: Data collected or produced that pertains to real-world objects, events,
              and analysis.

              TEST: Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

              EXERCISE: Data pertaining to a government or military exercise. The data may
              include both real and simulated data.

              SIMULATED: Synthetic data generated by a model to mimic real-world datasets.

          dec: Barycentric declination of the source in International Celestial Reference
              System (ICRS) at the reference epoch, in degrees.

          ra: Barycentric right ascension of the source in the International Celestial
              Reference System (ICRS) frame at the reference epoch, in degrees.

          source: Source of the data.

          star_epoch: Reference epoch to which the astrometric source parameters are referred,
              expressed as Julian Year in Barycentric Coordinate Time (TCB).

          aavso_vsx_id: The American Association of Variable Star Observers (AAVSO) Variable Star Index
              (VSX) (VX) object ID of this object.

          abgmag: Optical AB g magnitude.

          abgmag_origin: Catalog of origin of optical AB g magnitude.

          abgmag_unc: Uncertainty of optical AB g magnitude.

          abimag: Optical AB i magnitude.

          abimag_origin: Catalog of origin of optical AB i magnitude.

          abimag_unc: Uncertainty of optical AB i magnitude.

          abrmag: Optical AB r magnitude.

          abrmag_origin: Catalog of origin of optical AB r magnitude.

          abrmag_unc: Uncertainty of optical AB r magnitude.

          abymag: Optical AB y magnitude.

          abymag_origin: Catalog of origin of optical AB y magnitude.

          abymag_unc: Uncertainty of optical AB y magnitude.

          abzmag: Optical AB z magnitude.

          abzmag_origin: Catalog of origin of optical AB z magnitude.

          abzmag_unc: Uncertainty of optical AB z magnitude.

          all_wis_ecc_ind: Contamination and confusion indicator in AllWISE.

          all_wise_id: The designation of this object in the All Wide-field Infrared Survey Explorer
              (AllWISE) catalog (AL).

          all_wis_ena_ind: Active deblending indicator in AllWISE.

          all_wis_eph_qual_ind: Photometric quality indicator in AllWISE.

          apass_id: The American Association of Variable Star Observers (AAVSO) Photometric All-Sky
              Survey (APASS) (AP) name of this object.

          astrometric_excess_noise: Astrometric excess noise in the Gaia catalog measured in milliarcseconds.

          astrometric_excess_noise_sig: Astrometric excess noise sigma in Gaia.

          bmag: Optical Johnson B magnitude measured in magnitudes.

          bmag_origin: Catalog of origin of optical Johnson B magnitude (AP, CR, HI).

          bmag_unc: Uncertainty of optical Johnson B magnitude measured in magnitudes.

          bpmag: Gaia optical photometric Bp-band in the Vega scale measured in magnitudes.

          bpmag_unc: Gaia optical Bp-band uncertainty in the Vega scale measured in magnitudes.

          carrasco_cat_id: The Carrasco catalog (CR) identifier of this object.

          cat_version: The version of the catalog associated with this object.

          cat_wise2020_id: The CatWISE2020 (CA) catalog source ID of this object.

          dec_unc: Uncertainty of the declination of the source, in milliarcseconds, at the
              reference epoch.

          ducati_cat_id: The Ducati catalog (DU) name of this object.

          gaiadr3_cat_id: The source ID of this object in the Gaia DR3 Catalog (GA).

          gmag: Gaia optical photometric G-band in the Vega scale measured in magnitudes.

          gmag_unc: Gaia optical photometric G-band uncertainty in the Vega scale measured in
              magnitudes.

          gnc_cat_id: The ID of this object in the Guidance and Navigation Control (GNC) Catalog. If
              this field is populated it shall match the csId field.

          healpix_index: The Healpix index. Consumers should contact the provider for details on the
              indexing scheme.

          hip_cat_id: The HIP ID of this object in the Hipparcos Catalog (HI).

          hmag: Near-infrared photometric H-band magnitude in the Vega scale measured in
              magnitudes.

          hmag_origin: Near-infrared photometric H-band catalog of origin in the Vega scale (TP, UC,
              UL, UP, VH).

          hmag_unc: Near-infrared photometric H-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          imag: Optical Johnson I magnitude measured in magnitudes.

          imag_origin: Catalog of origin of optical Johnson I magnitude (CR, GA, HI).

          imag_unc: Uncertainty of optical Johnson I magnitude measured in magnitudes.

          jmag: Near-infrared photometric J-band magnitude in the Vega scale measured in
              magnitudes.

          jmag_origin: Near-infrared photometric J-band catalog of origin in the Vega scale (TP, UH,
              UL, UP, VH).

          jmag_unc: Near-infrared photometric J-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          kmag: Near-infrared photometric K-band magnitude in the Vega scale measured in
              magnitudes.

          kmag_origin: Near-infrared photometric K-band catalog of origin in the Vega scale (TP, UC,
              UH, UL, UP, VH).

          kmag_unc: Near-infrared photometric K-band magnitude uncertainty in the Vega scale
              measured in magnitudes.

          morphology_ind: Morphology indicator. Consumers should contact the provider for details on the
              specifications.

          mult_flag: Flag indicating that this is a multiple object source.

          multiplicity: Identifier indicating multiplicity is detected. Consumers should contact the
              provider for details on the specifications.

          neighbor_dec: Dec of nearest neighbor measured in degrees.

          neighbor_distance: Distance between source and nearest neighbor, in arcseconds.

          neighbor_flag: Flag indicating that the nearest catalog neighbor is closer than 4.6 arcseconds.

          neighbor_id: The catalog ID of the nearest neighbor to this source.

          neighbor_ra: RA of nearest neighbor measured in degrees.

          non_single_star: Identifier indicating the source is a non-single star in gaia (additional
              information is available in non-single star tables. Consumers should contact the
              provider for details on the specifications).

          num_neighbors: Number of neighbors.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pan_starrs_id: The Panoramic Survey Telescope and Rapid Response System (Pan-STARRS) (PS)
              object ID.

          parallax: Absolute stellar parallax of the source, in milliarcseconds.

          parallax_unc: Uncertainty of the stellar parallax, in milliarcseconds.

          pmdec: Proper motion in declination of the source, in milliarcseconds per year, at the
              reference epoch.

          pmdec_unc: Uncertainty of proper motion in declination, in milliarcseconds per year.

          pmra: Proper motion in right ascension of the source, in milliarcseconds per year, at
              the reference epoch.

          pmra_unc: Uncertainty of proper motion in right ascension, in milliarcseconds per year.

          pm_unc_flag: Flag indicating that the proper motion uncertainty in either ra or dec is
              greater than 10 milliarcseconds per year.

          pos_unc_flag: Flag indicating that the position uncertainty in either ra or dec is greater
              than 100 milliarcseconds.

          ps1astrometry_correction_flag: Astrometry correction flag in Pan-STARRS.

          ps1_obj_info_flag: Object information flag in Pan-STARRS.

          ps1_quality_flag: Quality flag in Pan-STARRS.

          ra_unc: Uncertainty of the right ascension of the source, in milliarcseconds, at the
              reference epoch.

          rmag: Optical Johnson R magnitude measured in magnitudes.

          rmag_origin: Catalog of origin of the Optical Johnson R magnitude (CR, GA).

          rmag_unc: Uncertainty of the Optical Johnson R magnitude measured in magnitudes.

          rpmag: Gaia optical Rp-band in the Vega scale measured in magnitudes.

          rpmag_unc: Gaia optical photometric Rp-band uncertainty in the Vega scale measured in
              magnitudes.

          ruwe: RUWE in Gaia.

          sda_cat_id: The ID of this object in the Space Domain Awareness (SDA) Catalog. If this field
              is populated it shall match the csId field.

          sgmag: Original G magnitude if the source is in Gaia, otherwise the magnitude is
              converted from other photometric passbands, when possible, measured in
              magnitudes.

          sgmag_unc: Uncertainty of sgmag measured in magnitudes.

          shift: Photocentric shift caused by neighbors, in arcseconds.

          shift_flag: Flag indicating that the photocentric shift is greater than 50 milliarcseconds.

          shift_fwhm1: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of one
              arcsecond.

          shift_fwhm6: Photocentric shift caused by neighbors, in arcseconds. This value is constrained
              to a Point Spread Function (PSF) with Full Width at Half Maximum (FWHM) of six
              arcseconds.

          sky_mapper_id: The SkyMapper (SK) catalog object ID.

          two_mass_id: The designation of this object in the Two Micron All Sky Survey (2MASS) Point
              Source Catalog (TP).

          two_mass_ph_qual_ind: Photometric (PH) quality indicator in 2MASS PSC.

          two_mass_read_flag: Read flag in 2MASS PSC.

          two_mass_xsc_id: The Two Micron All Sky Survey (2MASS) Extended Source Catalog (XSC) (TX)
              designation of this object.

          tycho_dsc_id: The Tycho Double Star Catalog (TD) identifier (specified as Tycho-2 ID) of this
              object.

          uhs_id: The United Kingdom Infrared Telescope (UKIRT) Hemispheric Survey (UHS) (UH)
              source ID of this object.

          ukidss_gcs_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Clusters Survey
              (GCS) (UC) source ID of this object.

          ukidss_gps_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Galactic Plane Survey (GPS)
              (UP) source ID of this object.

          ukidss_las_id: The United Kingdom Infrared Deep Sky Survey (UKIDSS) Large Area Survey (LAS)
              (UL) source ID of this object.

          var_flag: Flag indicating that the source exhibits variable magnitude.

          variability: Identifier indicating variability is present in the photometric data. Consumers
              should contact the provider for details on the specifications.

          vhs_id: The Visible and Infrared Survey Telescope for Astronomy (VISTA) Hemisphere
              Survey (VHS) (VS) source ID of this object.

          vmag: Optical Johnson V magnitude measured in magnitudes.

          vmag_origin: Catalog of origin of Optical Johnson V magnitude (AP, CR, DU, GA, HI).

          vmag_unc: Uncertainty of the Optical Johnson V magnitude measured in magnitudes.

          w1mag: Mid-infrared photometric W1-band (3.4 microns) magnitude in the Vega system
              measured in magnitudes.

          w1mag_origin: Mid-infrared photometric W1-band (3.4 microns) catalog of origin in the Vega
              system (AL, CA).

          w1mag_unc: Mid-infrared photometric W1-band (3.4 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w1sat: Mid-infrared photometric W1-band (3.4 microns) saturated pixel fraction in the
              Vega system.

          w2mag: Mid-infrared photometric W2-band (4.6 microns) magnitude in the Vega system
              measured in magnitudes.

          w2mag_origin: Mid-infrared photometric W2-band (4.6 microns) catalog of origin in the Vega
              system (AL, CA).

          w2mag_unc: Mid-infrared photometric W2-band (4.6 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w2sat: Mid-infrared photometric W2-band (4.6 microns) saturated pixel fraction in the
              Vega system.

          w3mag: Mid-infrared photometric W3-band (12 microns) magnitude in the Vega system
              measured in magnitudes.

          w3mag_origin: Mid-infrared photometric W3-band (12 microns) catalog of origin in the Vega
              system (AL).

          w3mag_unc: Mid-infrared photometric W3-band (12 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w3sat: Mid-infrared photometric W3-band (12 microns) saturated pixel fraction in the
              Vega system.

          w4mag: Mid-infrared photometric W4-band (22 microns) magnitude in the Vega system
              measured in magnitudes.

          w4mag_origin: Mid-infrared photometric W4-band (22 microns) catalog of origin in the Vega
              system (AL).

          w4mag_unc: Mid-infrared photometric W4-band (22 microns) magnitude uncertainty in the Vega
              system measured in magnitudes.

          w4sat: Mid-infrared photometric W4-band (22 microns) saturated pixel fraction in the
              Vega system.

          wds_cat_id: The Washington Double Star Catalog (WD) identifier of this object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/udl/starcatalog/{id}", id=id),
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
                    "aavso_vsx_id": aavso_vsx_id,
                    "abgmag": abgmag,
                    "abgmag_origin": abgmag_origin,
                    "abgmag_unc": abgmag_unc,
                    "abimag": abimag,
                    "abimag_origin": abimag_origin,
                    "abimag_unc": abimag_unc,
                    "abrmag": abrmag,
                    "abrmag_origin": abrmag_origin,
                    "abrmag_unc": abrmag_unc,
                    "abymag": abymag,
                    "abymag_origin": abymag_origin,
                    "abymag_unc": abymag_unc,
                    "abzmag": abzmag,
                    "abzmag_origin": abzmag_origin,
                    "abzmag_unc": abzmag_unc,
                    "all_wis_ecc_ind": all_wis_ecc_ind,
                    "all_wise_id": all_wise_id,
                    "all_wis_ena_ind": all_wis_ena_ind,
                    "all_wis_eph_qual_ind": all_wis_eph_qual_ind,
                    "apass_id": apass_id,
                    "astrometric_excess_noise": astrometric_excess_noise,
                    "astrometric_excess_noise_sig": astrometric_excess_noise_sig,
                    "bmag": bmag,
                    "bmag_origin": bmag_origin,
                    "bmag_unc": bmag_unc,
                    "bpmag": bpmag,
                    "bpmag_unc": bpmag_unc,
                    "carrasco_cat_id": carrasco_cat_id,
                    "cat_version": cat_version,
                    "cat_wise2020_id": cat_wise2020_id,
                    "dec_unc": dec_unc,
                    "ducati_cat_id": ducati_cat_id,
                    "gaiadr3_cat_id": gaiadr3_cat_id,
                    "gmag": gmag,
                    "gmag_unc": gmag_unc,
                    "gnc_cat_id": gnc_cat_id,
                    "healpix_index": healpix_index,
                    "hip_cat_id": hip_cat_id,
                    "hmag": hmag,
                    "hmag_origin": hmag_origin,
                    "hmag_unc": hmag_unc,
                    "imag": imag,
                    "imag_origin": imag_origin,
                    "imag_unc": imag_unc,
                    "jmag": jmag,
                    "jmag_origin": jmag_origin,
                    "jmag_unc": jmag_unc,
                    "kmag": kmag,
                    "kmag_origin": kmag_origin,
                    "kmag_unc": kmag_unc,
                    "morphology_ind": morphology_ind,
                    "mult_flag": mult_flag,
                    "multiplicity": multiplicity,
                    "neighbor_dec": neighbor_dec,
                    "neighbor_distance": neighbor_distance,
                    "neighbor_flag": neighbor_flag,
                    "neighbor_id": neighbor_id,
                    "neighbor_ra": neighbor_ra,
                    "non_single_star": non_single_star,
                    "num_neighbors": num_neighbors,
                    "origin": origin,
                    "pan_starrs_id": pan_starrs_id,
                    "parallax": parallax,
                    "parallax_unc": parallax_unc,
                    "pmdec": pmdec,
                    "pmdec_unc": pmdec_unc,
                    "pmra": pmra,
                    "pmra_unc": pmra_unc,
                    "pm_unc_flag": pm_unc_flag,
                    "pos_unc_flag": pos_unc_flag,
                    "ps1astrometry_correction_flag": ps1astrometry_correction_flag,
                    "ps1_obj_info_flag": ps1_obj_info_flag,
                    "ps1_quality_flag": ps1_quality_flag,
                    "ra_unc": ra_unc,
                    "rmag": rmag,
                    "rmag_origin": rmag_origin,
                    "rmag_unc": rmag_unc,
                    "rpmag": rpmag,
                    "rpmag_unc": rpmag_unc,
                    "ruwe": ruwe,
                    "sda_cat_id": sda_cat_id,
                    "sgmag": sgmag,
                    "sgmag_unc": sgmag_unc,
                    "shift": shift,
                    "shift_flag": shift_flag,
                    "shift_fwhm1": shift_fwhm1,
                    "shift_fwhm6": shift_fwhm6,
                    "sky_mapper_id": sky_mapper_id,
                    "two_mass_id": two_mass_id,
                    "two_mass_ph_qual_ind": two_mass_ph_qual_ind,
                    "two_mass_read_flag": two_mass_read_flag,
                    "two_mass_xsc_id": two_mass_xsc_id,
                    "tycho_dsc_id": tycho_dsc_id,
                    "uhs_id": uhs_id,
                    "ukidss_gcs_id": ukidss_gcs_id,
                    "ukidss_gps_id": ukidss_gps_id,
                    "ukidss_las_id": ukidss_las_id,
                    "var_flag": var_flag,
                    "variability": variability,
                    "vhs_id": vhs_id,
                    "vmag": vmag,
                    "vmag_origin": vmag_origin,
                    "vmag_unc": vmag_unc,
                    "w1mag": w1mag,
                    "w1mag_origin": w1mag_origin,
                    "w1mag_unc": w1mag_unc,
                    "w1sat": w1sat,
                    "w2mag": w2mag,
                    "w2mag_origin": w2mag_origin,
                    "w2mag_unc": w2mag_unc,
                    "w2sat": w2sat,
                    "w3mag": w3mag,
                    "w3mag_origin": w3mag_origin,
                    "w3mag_unc": w3mag_unc,
                    "w3sat": w3sat,
                    "w4mag": w4mag,
                    "w4mag_origin": w4mag_origin,
                    "w4mag_unc": w4mag_unc,
                    "w4sat": w4sat,
                    "wds_cat_id": wds_cat_id,
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
        dec: float | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        ra: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[StarCatalogListResponse, AsyncOffsetPage[StarCatalogListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (`/udl/<datatype>/queryhelp`) for more details on valid/required query parameter
        information.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/udl/starcatalog/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        dec: float | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        ra: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (`/udl/<datatype>/queryhelp`) for more details on
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/udl/starcatalog/{id}", id=id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        dec: float | Omit = omit,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        ra: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StarCatalogTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (`/udl/<datatype>/queryhelp`) for more details on valid/required query parameter
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
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
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
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
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
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
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        return AsyncHistoryResourceWithStreamingResponse(self._star_catalog.history)
