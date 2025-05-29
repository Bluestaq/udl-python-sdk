# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import (
    site_get_params,
    site_list_params,
    site_count_params,
    site_tuple_params,
    site_create_params,
    site_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .operations import (
    OperationsResource,
    AsyncOperationsResource,
    OperationsResourceWithRawResponse,
    AsyncOperationsResourceWithRawResponse,
    OperationsResourceWithStreamingResponse,
    AsyncOperationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.site_get_response import SiteGetResponse
from ...types.site_list_response import SiteListResponse
from ...types.entity_ingest_param import EntityIngestParam
from ...types.site_tuple_response import SiteTupleResponse
from ...types.site_queryhelp_response import SiteQueryhelpResponse

__all__ = ["SiteResource", "AsyncSiteResource"]


class SiteResource(SyncAPIResource):
    @cached_property
    def operations(self) -> OperationsResource:
        return OperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SiteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SiteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SiteResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        activity: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        be_number: str | NotGiven = NOT_GIVEN,
        cat_code: str | NotGiven = NOT_GIVEN,
        cat_text: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geo_area: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        grade: int | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        id_parent_site: str | NotGiven = NOT_GIVEN,
        lz_usage: str | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_spec: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        nuc_cap: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_lz_id: str | NotGiven = NOT_GIVEN,
        orig_site_id: str | NotGiven = NOT_GIVEN,
        osuffix: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        pop_area: bool | NotGiven = NOT_GIVEN,
        pop_area_prox: float | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        usage: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        veg_ht: float | NotGiven = NOT_GIVEN,
        veg_type: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Site as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

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

          name: The name of this site.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          activity: Indicates the function or mission of an entity, which that entity may or may not
              be engaged in at any particular time. Typically refers to a unit, organization,
              or installation/site performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the site owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          be_number: The Basic Encyclopedia Number associated with the Site. Uniquely identifies the
              installation of a site. The beNumber is generated based on the value input for
              the COORD to determine the appropriate World Aeronautical Chart (WAC) location
              identifier, the system assigned record originator and a one-up-number.

          cat_code: The category code that represents the associated site purpose within the target
              system.

          cat_text: Textual Description of Site catCode.

          class_rating: Indicates the importance of the entity to the OES or MIR system. This data
              element is restricted to update by DIA (DB-4). Valid values are:

              0 - Does not meet criteria above

              1 - Primary importance to system

              2 - Secondary importance to system

              3 - Tertiary importance to system

              O - Other. Explain in Remarks.

          condition: The physical manner of being or state of existence of the entity. A physical
              condition that must be considered in the determining of a course of action. The
              specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          condition_avail: Availability of the entity relative to its condition. Indicates the reason the
              entity is not fully operational. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          coord: Indicates any of the magnitudes that serve to define the position of a point by
              reference to a fixed figure, system of lines, etc.

              Pos. 1-2. Latitude Degrees [00-90]

              Pos. 3-4. Latitude Minutes [00-59]

              Pos. 5-6. Latitude Seconds [00-59]

              Pos. 7-9. Latitude Thousandths Of Seconds [000-999]

              Pos. 10. Latitude Hemisphere [NS]

              Pos. 11-13. Longitude Degrees [00-180]

              Pos. 14-15. Longitude Minutes [00-59]

              Pos. 16-17. Longitude Seconds [00-59]

              Pos. 18-20. Longitude Thousandths Of Seconds [000-999]

              Pos. 21. Longitude Hemisphere [EW]

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum, in meters.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          faa: The Federal Aviation Administration (FAA) Location ID of this site, if
              applicable.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geo_area: Geographical region code used by the Requirements Management System (RMS) as
              specified by National Geospatial Agency (NGA) in Flight Information Publications
              (FIPS) 10-4, Appendix 3 - Country Code and Geographic Region Codes. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, in meters.

          grade: Indicates the amount or degree of deviation from the horizontal represented as a
              percent. Grade is determined by the formula: vertical distance (VD) divided by
              horizontal distance (HD) times 100. VD is the difference between the highest and
              lowest elevation within the entity. HD is the linear distance between the
              highest and lowest elevation.

          iata: The International Air Transport Association (IATA) code of this site, if
              applicable.

          icao: The International Civil Aviation Organization (ICAO) code of this site, if
              applicable.

          ident: Estimated identity of the Site (ASSUMED FRIEND, FRIEND, HOSTILE, FAKER, JOKER,
              NEUTRAL, PENDING, SUSPECT, UNKNOWN):

              ASSUMED FRIEND: Track assumed to be a friend due to the object characteristics,
              behavior, and/or origin.

              FRIEND: Track object supporting friendly forces and belonging to a declared
              friendly nation or entity.

              HOSTILE: Track object belonging to an opposing nation, party, group, or entity
              deemed to contribute to a threat to friendly forces or their mission due to its
              behavior, characteristics, nationality, or origin.

              FAKER: Friendly track, object, or entity acting as an exercise hostile.

              JOKER: Friendly track, object, or entity acting as an exercise suspect.

              NEUTRAL: Track object whose characteristics, behavior, nationality, and/or
              origin indicate that it is neither supporting nor opposing friendly forces or
              their mission.

              PENDING: Track object which has not been evaluated.

              SUSPECT: Track object deemed potentially hostile due to the object
              characteristics, behavior, nationality, and/or origin.

              UNKNOWN: Track object which has been evaluated and does not meet criteria for
              any standard identity.

          id_entity: Unique identifier of the parent entity. idEntity is required for Put.

          id_parent_site: Unique identifier of the Parent Site record associated with this Site record.

          lz_usage: Indicates the normal usage of the Landing Zone (LZ). Intended as, but not
              constrained to MIDB Helocopter Landing Area usage value definitions:

              AF - Airfield

              FD - Field

              HC - High Crop. 1 meter and over.

              HY - Highway

              LB - Lake Bed

              LC - Low Crop. 0-1 meters

              O - Other. Explain In Remarks.

              PD - Paddy

              PK - Park

              PS - Pasture

              RB - Riverbed

              SP - Sport Field

              U - Unknown

              Z - Inconclusive Analysis.

          max_runway_length: The length of the longest runway at this site, if applicable, in meters.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              4Q (grid zone designator, GZD)

              FJ (the 100,000-meter square identifier)

              12345678 (numerical location; easting is 1234 and northing is 5678, in this case
              specifying a location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator.

          msn_primary: Indicates the principal type of mission that an entity is organized and equipped
              to perform. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          msn_primary_spec: Indicates the principal specialty type of mission that an entity is organized
              and equipped to perform. The specific usage and enumerations contained in this
              field may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          notes: Optional notes/comments for the site.

          nuc_cap:
              A sites ability to conduct nuclear warfare. Valid Values are:

              A - Nuclear Ammo Or Warheads Available

              N - No Nuclear Offense

              O - Other. Explain in Remarks

              U - Unknown

              W - Nuclear Weapons Available

              Y - Nuclear Warfare Offensive Capability

              Z - Inconclusive Analysis.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_lz_id: Unique identifier of the LZ record from the originating system.

          orig_site_id: Unique identifier of the Site record from the originating system.

          osuffix: The O-suffix associated with this site. The O-suffix is a five-character
              alpha/numeric system used to identify a site, or demographic area, within an
              installation. The Installation Basic Encyclopedia (beNumber), in conjunction
              with the O-suffix, uniquely identifies the Site. The Installation beNumber and
              oSuffix are also used in conjunction with the catCode to classify the function
              or purpose of the facility.

          pin: Site number of a specific electronic site or its associated equipment.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          pop_area: Indicates whether the facility is in or outside of a populated area. True, the
              facility is in or within 5 NM of a populated area. False, the facility is
              outside a populated area.

          pop_area_prox: Indicates the distance to nearest populated area (over 1,000 people) in nautical
              miles.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency, in ISO8601 UTC format. This date cannot be
              greater than the current date.

          runways: The number of runways at the site, if applicable.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element ident.

          type: The type of this site (AIRBASE, AIRFIELD, AIRPORT, NAVAL STATION, etc.).

          usage: The use authorization type of this site (e.g MILITARY, CIVIL, JOINT-USE, etc.).

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          veg_ht: Maximum expected height of the vegetation in the Landing Zone (LZ), in meters.

          veg_type: The predominant vegetation found in the Landing Zone (LZ). The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          wac: World Aeronautical Chart identifier for the area in which a designated place is
              located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/site",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "id": id,
                    "activity": activity,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "be_number": be_number,
                    "cat_code": cat_code,
                    "cat_text": cat_text,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "entity": entity,
                    "eval": eval,
                    "faa": faa,
                    "fpa": fpa,
                    "funct_primary": funct_primary,
                    "geo_area": geo_area,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "grade": grade,
                    "iata": iata,
                    "icao": icao,
                    "ident": ident,
                    "id_entity": id_entity,
                    "id_parent_site": id_parent_site,
                    "lz_usage": lz_usage,
                    "max_runway_length": max_runway_length,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_spec": msn_primary_spec,
                    "notes": notes,
                    "nuc_cap": nuc_cap,
                    "oper_status": oper_status,
                    "origin": origin,
                    "orig_lz_id": orig_lz_id,
                    "orig_site_id": orig_site_id,
                    "osuffix": osuffix,
                    "pin": pin,
                    "pol_subdiv": pol_subdiv,
                    "pop_area": pop_area,
                    "pop_area_prox": pop_area_prox,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "runways": runways,
                    "sym_code": sym_code,
                    "type": type,
                    "usage": usage,
                    "utm": utm,
                    "veg_ht": veg_ht,
                    "veg_type": veg_type,
                    "wac": wac,
                },
                site_create_params.SiteCreateParams,
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
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        activity: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        be_number: str | NotGiven = NOT_GIVEN,
        cat_code: str | NotGiven = NOT_GIVEN,
        cat_text: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geo_area: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        grade: int | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        id_parent_site: str | NotGiven = NOT_GIVEN,
        lz_usage: str | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_spec: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        nuc_cap: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_lz_id: str | NotGiven = NOT_GIVEN,
        orig_site_id: str | NotGiven = NOT_GIVEN,
        osuffix: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        pop_area: bool | NotGiven = NOT_GIVEN,
        pop_area_prox: float | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        usage: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        veg_ht: float | NotGiven = NOT_GIVEN,
        veg_type: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Site.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

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

          name: The name of this site.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          activity: Indicates the function or mission of an entity, which that entity may or may not
              be engaged in at any particular time. Typically refers to a unit, organization,
              or installation/site performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the site owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          be_number: The Basic Encyclopedia Number associated with the Site. Uniquely identifies the
              installation of a site. The beNumber is generated based on the value input for
              the COORD to determine the appropriate World Aeronautical Chart (WAC) location
              identifier, the system assigned record originator and a one-up-number.

          cat_code: The category code that represents the associated site purpose within the target
              system.

          cat_text: Textual Description of Site catCode.

          class_rating: Indicates the importance of the entity to the OES or MIR system. This data
              element is restricted to update by DIA (DB-4). Valid values are:

              0 - Does not meet criteria above

              1 - Primary importance to system

              2 - Secondary importance to system

              3 - Tertiary importance to system

              O - Other. Explain in Remarks.

          condition: The physical manner of being or state of existence of the entity. A physical
              condition that must be considered in the determining of a course of action. The
              specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          condition_avail: Availability of the entity relative to its condition. Indicates the reason the
              entity is not fully operational. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          coord: Indicates any of the magnitudes that serve to define the position of a point by
              reference to a fixed figure, system of lines, etc.

              Pos. 1-2. Latitude Degrees [00-90]

              Pos. 3-4. Latitude Minutes [00-59]

              Pos. 5-6. Latitude Seconds [00-59]

              Pos. 7-9. Latitude Thousandths Of Seconds [000-999]

              Pos. 10. Latitude Hemisphere [NS]

              Pos. 11-13. Longitude Degrees [00-180]

              Pos. 14-15. Longitude Minutes [00-59]

              Pos. 16-17. Longitude Seconds [00-59]

              Pos. 18-20. Longitude Thousandths Of Seconds [000-999]

              Pos. 21. Longitude Hemisphere [EW]

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum, in meters.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          faa: The Federal Aviation Administration (FAA) Location ID of this site, if
              applicable.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geo_area: Geographical region code used by the Requirements Management System (RMS) as
              specified by National Geospatial Agency (NGA) in Flight Information Publications
              (FIPS) 10-4, Appendix 3 - Country Code and Geographic Region Codes. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, in meters.

          grade: Indicates the amount or degree of deviation from the horizontal represented as a
              percent. Grade is determined by the formula: vertical distance (VD) divided by
              horizontal distance (HD) times 100. VD is the difference between the highest and
              lowest elevation within the entity. HD is the linear distance between the
              highest and lowest elevation.

          iata: The International Air Transport Association (IATA) code of this site, if
              applicable.

          icao: The International Civil Aviation Organization (ICAO) code of this site, if
              applicable.

          ident: Estimated identity of the Site (ASSUMED FRIEND, FRIEND, HOSTILE, FAKER, JOKER,
              NEUTRAL, PENDING, SUSPECT, UNKNOWN):

              ASSUMED FRIEND: Track assumed to be a friend due to the object characteristics,
              behavior, and/or origin.

              FRIEND: Track object supporting friendly forces and belonging to a declared
              friendly nation or entity.

              HOSTILE: Track object belonging to an opposing nation, party, group, or entity
              deemed to contribute to a threat to friendly forces or their mission due to its
              behavior, characteristics, nationality, or origin.

              FAKER: Friendly track, object, or entity acting as an exercise hostile.

              JOKER: Friendly track, object, or entity acting as an exercise suspect.

              NEUTRAL: Track object whose characteristics, behavior, nationality, and/or
              origin indicate that it is neither supporting nor opposing friendly forces or
              their mission.

              PENDING: Track object which has not been evaluated.

              SUSPECT: Track object deemed potentially hostile due to the object
              characteristics, behavior, nationality, and/or origin.

              UNKNOWN: Track object which has been evaluated and does not meet criteria for
              any standard identity.

          id_entity: Unique identifier of the parent entity. idEntity is required for Put.

          id_parent_site: Unique identifier of the Parent Site record associated with this Site record.

          lz_usage: Indicates the normal usage of the Landing Zone (LZ). Intended as, but not
              constrained to MIDB Helocopter Landing Area usage value definitions:

              AF - Airfield

              FD - Field

              HC - High Crop. 1 meter and over.

              HY - Highway

              LB - Lake Bed

              LC - Low Crop. 0-1 meters

              O - Other. Explain In Remarks.

              PD - Paddy

              PK - Park

              PS - Pasture

              RB - Riverbed

              SP - Sport Field

              U - Unknown

              Z - Inconclusive Analysis.

          max_runway_length: The length of the longest runway at this site, if applicable, in meters.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              4Q (grid zone designator, GZD)

              FJ (the 100,000-meter square identifier)

              12345678 (numerical location; easting is 1234 and northing is 5678, in this case
              specifying a location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator.

          msn_primary: Indicates the principal type of mission that an entity is organized and equipped
              to perform. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          msn_primary_spec: Indicates the principal specialty type of mission that an entity is organized
              and equipped to perform. The specific usage and enumerations contained in this
              field may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          notes: Optional notes/comments for the site.

          nuc_cap:
              A sites ability to conduct nuclear warfare. Valid Values are:

              A - Nuclear Ammo Or Warheads Available

              N - No Nuclear Offense

              O - Other. Explain in Remarks

              U - Unknown

              W - Nuclear Weapons Available

              Y - Nuclear Warfare Offensive Capability

              Z - Inconclusive Analysis.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_lz_id: Unique identifier of the LZ record from the originating system.

          orig_site_id: Unique identifier of the Site record from the originating system.

          osuffix: The O-suffix associated with this site. The O-suffix is a five-character
              alpha/numeric system used to identify a site, or demographic area, within an
              installation. The Installation Basic Encyclopedia (beNumber), in conjunction
              with the O-suffix, uniquely identifies the Site. The Installation beNumber and
              oSuffix are also used in conjunction with the catCode to classify the function
              or purpose of the facility.

          pin: Site number of a specific electronic site or its associated equipment.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          pop_area: Indicates whether the facility is in or outside of a populated area. True, the
              facility is in or within 5 NM of a populated area. False, the facility is
              outside a populated area.

          pop_area_prox: Indicates the distance to nearest populated area (over 1,000 people) in nautical
              miles.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency, in ISO8601 UTC format. This date cannot be
              greater than the current date.

          runways: The number of runways at the site, if applicable.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element ident.

          type: The type of this site (AIRBASE, AIRFIELD, AIRPORT, NAVAL STATION, etc.).

          usage: The use authorization type of this site (e.g MILITARY, CIVIL, JOINT-USE, etc.).

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          veg_ht: Maximum expected height of the vegetation in the Landing Zone (LZ), in meters.

          veg_type: The predominant vegetation found in the Landing Zone (LZ). The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          wac: World Aeronautical Chart identifier for the area in which a designated place is
              located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/site/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "activity": activity,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "be_number": be_number,
                    "cat_code": cat_code,
                    "cat_text": cat_text,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "entity": entity,
                    "eval": eval,
                    "faa": faa,
                    "fpa": fpa,
                    "funct_primary": funct_primary,
                    "geo_area": geo_area,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "grade": grade,
                    "iata": iata,
                    "icao": icao,
                    "ident": ident,
                    "id_entity": id_entity,
                    "id_parent_site": id_parent_site,
                    "lz_usage": lz_usage,
                    "max_runway_length": max_runway_length,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_spec": msn_primary_spec,
                    "notes": notes,
                    "nuc_cap": nuc_cap,
                    "oper_status": oper_status,
                    "origin": origin,
                    "orig_lz_id": orig_lz_id,
                    "orig_site_id": orig_site_id,
                    "osuffix": osuffix,
                    "pin": pin,
                    "pol_subdiv": pol_subdiv,
                    "pop_area": pop_area,
                    "pop_area_prox": pop_area_prox,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "runways": runways,
                    "sym_code": sym_code,
                    "type": type,
                    "usage": usage,
                    "utm": utm,
                    "veg_ht": veg_ht,
                    "veg_type": veg_type,
                    "wac": wac,
                },
                site_update_params.SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SiteListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/site",
            page=SyncOffsetPage[SiteListResponse],
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
                    site_list_params.SiteListParams,
                ),
            ),
            model=SiteListResponse,
        )

    def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/site/count",
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
                    site_count_params.SiteCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> SiteGetResponse:
        """
        Service operation to get a single Site record by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/site/{id}",
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
                    site_get_params.SiteGetParams,
                ),
            ),
            cast_to=SiteGetResponse,
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
    ) -> SiteQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/site/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiteQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/site/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    site_tuple_params.SiteTupleParams,
                ),
            ),
            cast_to=SiteTupleResponse,
        )


class AsyncSiteResource(AsyncAPIResource):
    @cached_property
    def operations(self) -> AsyncOperationsResource:
        return AsyncOperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSiteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSiteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSiteResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        activity: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        be_number: str | NotGiven = NOT_GIVEN,
        cat_code: str | NotGiven = NOT_GIVEN,
        cat_text: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geo_area: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        grade: int | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        id_parent_site: str | NotGiven = NOT_GIVEN,
        lz_usage: str | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_spec: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        nuc_cap: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_lz_id: str | NotGiven = NOT_GIVEN,
        orig_site_id: str | NotGiven = NOT_GIVEN,
        osuffix: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        pop_area: bool | NotGiven = NOT_GIVEN,
        pop_area_prox: float | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        usage: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        veg_ht: float | NotGiven = NOT_GIVEN,
        veg_type: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Site as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

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

          name: The name of this site.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          activity: Indicates the function or mission of an entity, which that entity may or may not
              be engaged in at any particular time. Typically refers to a unit, organization,
              or installation/site performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the site owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          be_number: The Basic Encyclopedia Number associated with the Site. Uniquely identifies the
              installation of a site. The beNumber is generated based on the value input for
              the COORD to determine the appropriate World Aeronautical Chart (WAC) location
              identifier, the system assigned record originator and a one-up-number.

          cat_code: The category code that represents the associated site purpose within the target
              system.

          cat_text: Textual Description of Site catCode.

          class_rating: Indicates the importance of the entity to the OES or MIR system. This data
              element is restricted to update by DIA (DB-4). Valid values are:

              0 - Does not meet criteria above

              1 - Primary importance to system

              2 - Secondary importance to system

              3 - Tertiary importance to system

              O - Other. Explain in Remarks.

          condition: The physical manner of being or state of existence of the entity. A physical
              condition that must be considered in the determining of a course of action. The
              specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          condition_avail: Availability of the entity relative to its condition. Indicates the reason the
              entity is not fully operational. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          coord: Indicates any of the magnitudes that serve to define the position of a point by
              reference to a fixed figure, system of lines, etc.

              Pos. 1-2. Latitude Degrees [00-90]

              Pos. 3-4. Latitude Minutes [00-59]

              Pos. 5-6. Latitude Seconds [00-59]

              Pos. 7-9. Latitude Thousandths Of Seconds [000-999]

              Pos. 10. Latitude Hemisphere [NS]

              Pos. 11-13. Longitude Degrees [00-180]

              Pos. 14-15. Longitude Minutes [00-59]

              Pos. 16-17. Longitude Seconds [00-59]

              Pos. 18-20. Longitude Thousandths Of Seconds [000-999]

              Pos. 21. Longitude Hemisphere [EW]

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum, in meters.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          faa: The Federal Aviation Administration (FAA) Location ID of this site, if
              applicable.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geo_area: Geographical region code used by the Requirements Management System (RMS) as
              specified by National Geospatial Agency (NGA) in Flight Information Publications
              (FIPS) 10-4, Appendix 3 - Country Code and Geographic Region Codes. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, in meters.

          grade: Indicates the amount or degree of deviation from the horizontal represented as a
              percent. Grade is determined by the formula: vertical distance (VD) divided by
              horizontal distance (HD) times 100. VD is the difference between the highest and
              lowest elevation within the entity. HD is the linear distance between the
              highest and lowest elevation.

          iata: The International Air Transport Association (IATA) code of this site, if
              applicable.

          icao: The International Civil Aviation Organization (ICAO) code of this site, if
              applicable.

          ident: Estimated identity of the Site (ASSUMED FRIEND, FRIEND, HOSTILE, FAKER, JOKER,
              NEUTRAL, PENDING, SUSPECT, UNKNOWN):

              ASSUMED FRIEND: Track assumed to be a friend due to the object characteristics,
              behavior, and/or origin.

              FRIEND: Track object supporting friendly forces and belonging to a declared
              friendly nation or entity.

              HOSTILE: Track object belonging to an opposing nation, party, group, or entity
              deemed to contribute to a threat to friendly forces or their mission due to its
              behavior, characteristics, nationality, or origin.

              FAKER: Friendly track, object, or entity acting as an exercise hostile.

              JOKER: Friendly track, object, or entity acting as an exercise suspect.

              NEUTRAL: Track object whose characteristics, behavior, nationality, and/or
              origin indicate that it is neither supporting nor opposing friendly forces or
              their mission.

              PENDING: Track object which has not been evaluated.

              SUSPECT: Track object deemed potentially hostile due to the object
              characteristics, behavior, nationality, and/or origin.

              UNKNOWN: Track object which has been evaluated and does not meet criteria for
              any standard identity.

          id_entity: Unique identifier of the parent entity. idEntity is required for Put.

          id_parent_site: Unique identifier of the Parent Site record associated with this Site record.

          lz_usage: Indicates the normal usage of the Landing Zone (LZ). Intended as, but not
              constrained to MIDB Helocopter Landing Area usage value definitions:

              AF - Airfield

              FD - Field

              HC - High Crop. 1 meter and over.

              HY - Highway

              LB - Lake Bed

              LC - Low Crop. 0-1 meters

              O - Other. Explain In Remarks.

              PD - Paddy

              PK - Park

              PS - Pasture

              RB - Riverbed

              SP - Sport Field

              U - Unknown

              Z - Inconclusive Analysis.

          max_runway_length: The length of the longest runway at this site, if applicable, in meters.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              4Q (grid zone designator, GZD)

              FJ (the 100,000-meter square identifier)

              12345678 (numerical location; easting is 1234 and northing is 5678, in this case
              specifying a location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator.

          msn_primary: Indicates the principal type of mission that an entity is organized and equipped
              to perform. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          msn_primary_spec: Indicates the principal specialty type of mission that an entity is organized
              and equipped to perform. The specific usage and enumerations contained in this
              field may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          notes: Optional notes/comments for the site.

          nuc_cap:
              A sites ability to conduct nuclear warfare. Valid Values are:

              A - Nuclear Ammo Or Warheads Available

              N - No Nuclear Offense

              O - Other. Explain in Remarks

              U - Unknown

              W - Nuclear Weapons Available

              Y - Nuclear Warfare Offensive Capability

              Z - Inconclusive Analysis.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_lz_id: Unique identifier of the LZ record from the originating system.

          orig_site_id: Unique identifier of the Site record from the originating system.

          osuffix: The O-suffix associated with this site. The O-suffix is a five-character
              alpha/numeric system used to identify a site, or demographic area, within an
              installation. The Installation Basic Encyclopedia (beNumber), in conjunction
              with the O-suffix, uniquely identifies the Site. The Installation beNumber and
              oSuffix are also used in conjunction with the catCode to classify the function
              or purpose of the facility.

          pin: Site number of a specific electronic site or its associated equipment.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          pop_area: Indicates whether the facility is in or outside of a populated area. True, the
              facility is in or within 5 NM of a populated area. False, the facility is
              outside a populated area.

          pop_area_prox: Indicates the distance to nearest populated area (over 1,000 people) in nautical
              miles.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency, in ISO8601 UTC format. This date cannot be
              greater than the current date.

          runways: The number of runways at the site, if applicable.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element ident.

          type: The type of this site (AIRBASE, AIRFIELD, AIRPORT, NAVAL STATION, etc.).

          usage: The use authorization type of this site (e.g MILITARY, CIVIL, JOINT-USE, etc.).

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          veg_ht: Maximum expected height of the vegetation in the Landing Zone (LZ), in meters.

          veg_type: The predominant vegetation found in the Landing Zone (LZ). The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          wac: World Aeronautical Chart identifier for the area in which a designated place is
              located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/site",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "id": id,
                    "activity": activity,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "be_number": be_number,
                    "cat_code": cat_code,
                    "cat_text": cat_text,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "entity": entity,
                    "eval": eval,
                    "faa": faa,
                    "fpa": fpa,
                    "funct_primary": funct_primary,
                    "geo_area": geo_area,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "grade": grade,
                    "iata": iata,
                    "icao": icao,
                    "ident": ident,
                    "id_entity": id_entity,
                    "id_parent_site": id_parent_site,
                    "lz_usage": lz_usage,
                    "max_runway_length": max_runway_length,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_spec": msn_primary_spec,
                    "notes": notes,
                    "nuc_cap": nuc_cap,
                    "oper_status": oper_status,
                    "origin": origin,
                    "orig_lz_id": orig_lz_id,
                    "orig_site_id": orig_site_id,
                    "osuffix": osuffix,
                    "pin": pin,
                    "pol_subdiv": pol_subdiv,
                    "pop_area": pop_area,
                    "pop_area_prox": pop_area_prox,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "runways": runways,
                    "sym_code": sym_code,
                    "type": type,
                    "usage": usage,
                    "utm": utm,
                    "veg_ht": veg_ht,
                    "veg_type": veg_type,
                    "wac": wac,
                },
                site_create_params.SiteCreateParams,
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
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        activity: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        be_number: str | NotGiven = NOT_GIVEN,
        cat_code: str | NotGiven = NOT_GIVEN,
        cat_text: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geo_area: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        grade: int | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        id_parent_site: str | NotGiven = NOT_GIVEN,
        lz_usage: str | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_spec: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        nuc_cap: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_lz_id: str | NotGiven = NOT_GIVEN,
        orig_site_id: str | NotGiven = NOT_GIVEN,
        osuffix: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        pop_area: bool | NotGiven = NOT_GIVEN,
        pop_area_prox: float | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        usage: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        veg_ht: float | NotGiven = NOT_GIVEN,
        veg_type: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Site.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

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

          name: The name of this site.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          activity: Indicates the function or mission of an entity, which that entity may or may not
              be engaged in at any particular time. Typically refers to a unit, organization,
              or installation/site performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the site owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          be_number: The Basic Encyclopedia Number associated with the Site. Uniquely identifies the
              installation of a site. The beNumber is generated based on the value input for
              the COORD to determine the appropriate World Aeronautical Chart (WAC) location
              identifier, the system assigned record originator and a one-up-number.

          cat_code: The category code that represents the associated site purpose within the target
              system.

          cat_text: Textual Description of Site catCode.

          class_rating: Indicates the importance of the entity to the OES or MIR system. This data
              element is restricted to update by DIA (DB-4). Valid values are:

              0 - Does not meet criteria above

              1 - Primary importance to system

              2 - Secondary importance to system

              3 - Tertiary importance to system

              O - Other. Explain in Remarks.

          condition: The physical manner of being or state of existence of the entity. A physical
              condition that must be considered in the determining of a course of action. The
              specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          condition_avail: Availability of the entity relative to its condition. Indicates the reason the
              entity is not fully operational. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          coord: Indicates any of the magnitudes that serve to define the position of a point by
              reference to a fixed figure, system of lines, etc.

              Pos. 1-2. Latitude Degrees [00-90]

              Pos. 3-4. Latitude Minutes [00-59]

              Pos. 5-6. Latitude Seconds [00-59]

              Pos. 7-9. Latitude Thousandths Of Seconds [000-999]

              Pos. 10. Latitude Hemisphere [NS]

              Pos. 11-13. Longitude Degrees [00-180]

              Pos. 14-15. Longitude Minutes [00-59]

              Pos. 16-17. Longitude Seconds [00-59]

              Pos. 18-20. Longitude Thousandths Of Seconds [000-999]

              Pos. 21. Longitude Hemisphere [EW]

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum, in meters.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          faa: The Federal Aviation Administration (FAA) Location ID of this site, if
              applicable.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geo_area: Geographical region code used by the Requirements Management System (RMS) as
              specified by National Geospatial Agency (NGA) in Flight Information Publications
              (FIPS) 10-4, Appendix 3 - Country Code and Geographic Region Codes. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, in meters.

          grade: Indicates the amount or degree of deviation from the horizontal represented as a
              percent. Grade is determined by the formula: vertical distance (VD) divided by
              horizontal distance (HD) times 100. VD is the difference between the highest and
              lowest elevation within the entity. HD is the linear distance between the
              highest and lowest elevation.

          iata: The International Air Transport Association (IATA) code of this site, if
              applicable.

          icao: The International Civil Aviation Organization (ICAO) code of this site, if
              applicable.

          ident: Estimated identity of the Site (ASSUMED FRIEND, FRIEND, HOSTILE, FAKER, JOKER,
              NEUTRAL, PENDING, SUSPECT, UNKNOWN):

              ASSUMED FRIEND: Track assumed to be a friend due to the object characteristics,
              behavior, and/or origin.

              FRIEND: Track object supporting friendly forces and belonging to a declared
              friendly nation or entity.

              HOSTILE: Track object belonging to an opposing nation, party, group, or entity
              deemed to contribute to a threat to friendly forces or their mission due to its
              behavior, characteristics, nationality, or origin.

              FAKER: Friendly track, object, or entity acting as an exercise hostile.

              JOKER: Friendly track, object, or entity acting as an exercise suspect.

              NEUTRAL: Track object whose characteristics, behavior, nationality, and/or
              origin indicate that it is neither supporting nor opposing friendly forces or
              their mission.

              PENDING: Track object which has not been evaluated.

              SUSPECT: Track object deemed potentially hostile due to the object
              characteristics, behavior, nationality, and/or origin.

              UNKNOWN: Track object which has been evaluated and does not meet criteria for
              any standard identity.

          id_entity: Unique identifier of the parent entity. idEntity is required for Put.

          id_parent_site: Unique identifier of the Parent Site record associated with this Site record.

          lz_usage: Indicates the normal usage of the Landing Zone (LZ). Intended as, but not
              constrained to MIDB Helocopter Landing Area usage value definitions:

              AF - Airfield

              FD - Field

              HC - High Crop. 1 meter and over.

              HY - Highway

              LB - Lake Bed

              LC - Low Crop. 0-1 meters

              O - Other. Explain In Remarks.

              PD - Paddy

              PK - Park

              PS - Pasture

              RB - Riverbed

              SP - Sport Field

              U - Unknown

              Z - Inconclusive Analysis.

          max_runway_length: The length of the longest runway at this site, if applicable, in meters.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              4Q (grid zone designator, GZD)

              FJ (the 100,000-meter square identifier)

              12345678 (numerical location; easting is 1234 and northing is 5678, in this case
              specifying a location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator.

          msn_primary: Indicates the principal type of mission that an entity is organized and equipped
              to perform. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          msn_primary_spec: Indicates the principal specialty type of mission that an entity is organized
              and equipped to perform. The specific usage and enumerations contained in this
              field may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          notes: Optional notes/comments for the site.

          nuc_cap:
              A sites ability to conduct nuclear warfare. Valid Values are:

              A - Nuclear Ammo Or Warheads Available

              N - No Nuclear Offense

              O - Other. Explain in Remarks

              U - Unknown

              W - Nuclear Weapons Available

              Y - Nuclear Warfare Offensive Capability

              Z - Inconclusive Analysis.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_lz_id: Unique identifier of the LZ record from the originating system.

          orig_site_id: Unique identifier of the Site record from the originating system.

          osuffix: The O-suffix associated with this site. The O-suffix is a five-character
              alpha/numeric system used to identify a site, or demographic area, within an
              installation. The Installation Basic Encyclopedia (beNumber), in conjunction
              with the O-suffix, uniquely identifies the Site. The Installation beNumber and
              oSuffix are also used in conjunction with the catCode to classify the function
              or purpose of the facility.

          pin: Site number of a specific electronic site or its associated equipment.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          pop_area: Indicates whether the facility is in or outside of a populated area. True, the
              facility is in or within 5 NM of a populated area. False, the facility is
              outside a populated area.

          pop_area_prox: Indicates the distance to nearest populated area (over 1,000 people) in nautical
              miles.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency, in ISO8601 UTC format. This date cannot be
              greater than the current date.

          runways: The number of runways at the site, if applicable.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element ident.

          type: The type of this site (AIRBASE, AIRFIELD, AIRPORT, NAVAL STATION, etc.).

          usage: The use authorization type of this site (e.g MILITARY, CIVIL, JOINT-USE, etc.).

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          veg_ht: Maximum expected height of the vegetation in the Landing Zone (LZ), in meters.

          veg_type: The predominant vegetation found in the Landing Zone (LZ). The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          wac: World Aeronautical Chart identifier for the area in which a designated place is
              located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/site/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "activity": activity,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "be_number": be_number,
                    "cat_code": cat_code,
                    "cat_text": cat_text,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "entity": entity,
                    "eval": eval,
                    "faa": faa,
                    "fpa": fpa,
                    "funct_primary": funct_primary,
                    "geo_area": geo_area,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "grade": grade,
                    "iata": iata,
                    "icao": icao,
                    "ident": ident,
                    "id_entity": id_entity,
                    "id_parent_site": id_parent_site,
                    "lz_usage": lz_usage,
                    "max_runway_length": max_runway_length,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_spec": msn_primary_spec,
                    "notes": notes,
                    "nuc_cap": nuc_cap,
                    "oper_status": oper_status,
                    "origin": origin,
                    "orig_lz_id": orig_lz_id,
                    "orig_site_id": orig_site_id,
                    "osuffix": osuffix,
                    "pin": pin,
                    "pol_subdiv": pol_subdiv,
                    "pop_area": pop_area,
                    "pop_area_prox": pop_area_prox,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "runways": runways,
                    "sym_code": sym_code,
                    "type": type,
                    "usage": usage,
                    "utm": utm,
                    "veg_ht": veg_ht,
                    "veg_type": veg_type,
                    "wac": wac,
                },
                site_update_params.SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SiteListResponse, AsyncOffsetPage[SiteListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/site",
            page=AsyncOffsetPage[SiteListResponse],
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
                    site_list_params.SiteListParams,
                ),
            ),
            model=SiteListResponse,
        )

    async def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/site/count",
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
                    site_count_params.SiteCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> SiteGetResponse:
        """
        Service operation to get a single Site record by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/site/{id}",
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
                    site_get_params.SiteGetParams,
                ),
            ),
            cast_to=SiteGetResponse,
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
    ) -> SiteQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/site/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiteQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/site/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    site_tuple_params.SiteTupleParams,
                ),
            ),
            cast_to=SiteTupleResponse,
        )


class SiteResourceWithRawResponse:
    def __init__(self, site: SiteResource) -> None:
        self._site = site

        self.create = to_raw_response_wrapper(
            site.create,
        )
        self.update = to_raw_response_wrapper(
            site.update,
        )
        self.list = to_raw_response_wrapper(
            site.list,
        )
        self.count = to_raw_response_wrapper(
            site.count,
        )
        self.get = to_raw_response_wrapper(
            site.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            site.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            site.tuple,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self._site.operations)


class AsyncSiteResourceWithRawResponse:
    def __init__(self, site: AsyncSiteResource) -> None:
        self._site = site

        self.create = async_to_raw_response_wrapper(
            site.create,
        )
        self.update = async_to_raw_response_wrapper(
            site.update,
        )
        self.list = async_to_raw_response_wrapper(
            site.list,
        )
        self.count = async_to_raw_response_wrapper(
            site.count,
        )
        self.get = async_to_raw_response_wrapper(
            site.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            site.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            site.tuple,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self._site.operations)


class SiteResourceWithStreamingResponse:
    def __init__(self, site: SiteResource) -> None:
        self._site = site

        self.create = to_streamed_response_wrapper(
            site.create,
        )
        self.update = to_streamed_response_wrapper(
            site.update,
        )
        self.list = to_streamed_response_wrapper(
            site.list,
        )
        self.count = to_streamed_response_wrapper(
            site.count,
        )
        self.get = to_streamed_response_wrapper(
            site.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            site.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            site.tuple,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self._site.operations)


class AsyncSiteResourceWithStreamingResponse:
    def __init__(self, site: AsyncSiteResource) -> None:
        self._site = site

        self.create = async_to_streamed_response_wrapper(
            site.create,
        )
        self.update = async_to_streamed_response_wrapper(
            site.update,
        )
        self.list = async_to_streamed_response_wrapper(
            site.list,
        )
        self.count = async_to_streamed_response_wrapper(
            site.count,
        )
        self.get = async_to_streamed_response_wrapper(
            site.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            site.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            site.tuple,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self._site.operations)
