# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import (
    operatingunit_get_params,
    operatingunit_list_params,
    operatingunit_count_params,
    operatingunit_tuple_params,
    operatingunit_create_params,
    operatingunit_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.operatingunit_get_response import OperatingunitGetResponse
from ..types.operatingunit_list_response import OperatingunitListResponse
from ..types.operatingunit_tuple_response import OperatingunitTupleResponse

__all__ = ["OperatingunitResource", "AsyncOperatingunitResource"]


class OperatingunitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperatingunitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OperatingunitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperatingunitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OperatingunitResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_operating_unit_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        deploy_status: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        div_cat: str | NotGiven = NOT_GIVEN,
        echelon: str | NotGiven = NOT_GIVEN,
        echelon_tier: str | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        flag_flown: str | NotGiven = NOT_GIVEN,
        fleet_id: str | NotGiven = NOT_GIVEN,
        force: str | NotGiven = NOT_GIVEN,
        force_name: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_role: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        id_contact: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_location: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_organization: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        loc_name: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        master_unit: bool | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_specialty: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        stylized_unit: bool | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        unit_identifier: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Operatingunit as a POST body and ingest into
        the database. Operatingunit defines a unit or organization which operates or
        controls a space-related Entity. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          name: Name of the operating unit.

          source: Source of the data.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard country code designator for the country or political entity to
              which the operating unit owes its allegiance. This field will be set to "OTHR"
              if the source value does not match a UDL country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_operating_unit_id: Unique identifier of the operating unit record from the originating system.

          class_rating: Indicates the importance of the operating unit to the OES or MIR system. This
              data element is restricted to update by DIA (DB-4). Valid values are: 0 - Does
              not meet criteria above 1 - Primary importance to system 2 - Secondary
              importance to system 3 - Tertiary importance to system O - Other. Explain in
              Remarks.

          condition: The physical manner of being or state of existence of the operating unit. A
              physical condition that must be considered in the determining of a course of
              action. The specific usage and enumerations contained in this field may be found
              in the documentation provided in the referenceDoc field. If referenceDoc not
              provided, users may consult the data provider.

          condition_avail: Availability of the operating unit relative to its condition. Indicates the
              reason the operating unit is not fully operational. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          country_code: The DoD Standard country code designator for the country or political entity to
              which the operating unit geographic coordinates reside . This field will be set
              to "OTHR" if the source value does not match a UDL country code value
              (ISO-3166-ALPHA-2).

          deploy_status: A code describing the amount of operating unit participation in a deployment.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          description: Description of the operating unit.

          div_cat: Combat status of a divisional or equivalent operating unit. Currently, this data
              element applies only to operating units of the Former Soviet Union. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          echelon: Organizational level of the operating unit. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          echelon_tier: Indicates the major group or level to which an echelon belongs. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          eval: The Intelligence Confidence Level or the Reliability/degree of confidence that
              the analyst has assigned to the data within this record. The numerical range is
              from 1 to 9 with 1 representing the highest confidence level.

          flag_flown: The country code of the observed flag flown.

          fleet_id: Naval fleet to which an operating unit is assigned. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          force: An aggregation of military units within a single service (i.e., ARMY, AIR FORCE,
              etc.) which operates under a single authority to accomplish a common mission.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          force_name: The specific name for a given force. For example, Force = ADF (Air Defense
              Force) and Force Name = Army Air Defense Force.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_role: Principal combat-related role that an operating unit is organized, structured
              and equipped to perform. Or, the specialized military or paramilitary branch in
              which an individual serves, their specialization. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid.

          id_contact: Unique identifier of the contact for this operating unit.

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

          id_location: Unique identifier of the location record for this operating unit.

          id_operating_unit: Unique identifier of the record, auto-generated by the system.

          id_organization: Unique identifier of the organization record for this operating unit.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          loc_name: Location name for the coordinates.

          loc_reason: Indicates the reason that the operating unit is at that location. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          master_unit: This field contains a value indicating whether the record is a master unit
              record (True) or a detail record (False). Master records contain basic
              information that does not change over time for each unit that has been selected
              to be projected.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts: 4Q (grid zone
              designator, GZD) FJ (the 100,000-meter square identifier) 12345678 (numerical
              location; easting is 1234 and northing is 5678, in this case specifying a
              location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator

          msn_primary: Indicates the principal type of mission that an operating unit is organized and
              equipped to perform. The specific usage and enumerations contained in this field
              may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          msn_primary_specialty: Indicates the principal specialty type of mission that an operating unit is
              organized and equipped to perform. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          oper_status: The Degree to which an operating unit is ready to perform the overall
              operational mission(s) for which it was organized and equipped. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Values are: A - Active I -
              Inactive K - Acknowledged L - Local Q - A nominated (NOM) or Data Change Request
              (DCR) record R - Production reduced by CMD decision W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          stylized_unit: This field contains a value indicating whether the record is a stylized
              operating unit record (True) or a regular operating unit record (False). A
              stylized operating unit is a type of operating unit with one set of equipment
              that can be assigned to one or more superiors. A stylized operating unit is
              generally useful for lower echelon operating units where the number of operating
              units and types of equipment are equal for multiple organizations. In lieu of
              creating unique operating unit records for each operating unit, a template is
              created for the operating unit and its equipment. This template enables the user
              to assign the operating unit to multiple organizations.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          unit_identifier: An optional identifier for this operating unit that may be composed from items
              such as the originating organization, allegiance, one-up number, etc.

          utm: Universal Transverse Mercator (UTM) grid coordinates. Pos. 1-2, UTM Zone Column
              [01-60 Pos. 3, UTM Zone Row [C-HJ-NP-X] Pos. 4, UTM False Easting [0-9] Pos.
              5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9] Pos. 10-11, UTM False Northing
              [0-9][0-9] Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          wac: World Aeronautical Chart identifier for the area in which a designated operating
              unit is located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/operatingunit",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_operating_unit_id": alt_operating_unit_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "country_code": country_code,
                    "deploy_status": deploy_status,
                    "description": description,
                    "div_cat": div_cat,
                    "echelon": echelon,
                    "echelon_tier": echelon_tier,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eval": eval,
                    "flag_flown": flag_flown,
                    "fleet_id": fleet_id,
                    "force": force,
                    "force_name": force_name,
                    "fpa": fpa,
                    "funct_role": funct_role,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "id_contact": id_contact,
                    "ident": ident,
                    "id_location": id_location,
                    "id_operating_unit": id_operating_unit,
                    "id_organization": id_organization,
                    "lat": lat,
                    "loc_name": loc_name,
                    "loc_reason": loc_reason,
                    "lon": lon,
                    "master_unit": master_unit,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_specialty": msn_primary_specialty,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "stylized_unit": stylized_unit,
                    "sym_code": sym_code,
                    "unit_identifier": unit_identifier,
                    "utm": utm,
                    "wac": wac,
                },
                operatingunit_create_params.OperatingunitCreateParams,
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
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_operating_unit_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        deploy_status: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        div_cat: str | NotGiven = NOT_GIVEN,
        echelon: str | NotGiven = NOT_GIVEN,
        echelon_tier: str | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        flag_flown: str | NotGiven = NOT_GIVEN,
        fleet_id: str | NotGiven = NOT_GIVEN,
        force: str | NotGiven = NOT_GIVEN,
        force_name: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_role: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        id_contact: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_location: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_organization: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        loc_name: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        master_unit: bool | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_specialty: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        stylized_unit: bool | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        unit_identifier: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Operatingunit.

        Operatingunit defines a unit
        or organization which operates or controls a space-related Entity. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

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

          name: Name of the operating unit.

          source: Source of the data.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard country code designator for the country or political entity to
              which the operating unit owes its allegiance. This field will be set to "OTHR"
              if the source value does not match a UDL country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_operating_unit_id: Unique identifier of the operating unit record from the originating system.

          class_rating: Indicates the importance of the operating unit to the OES or MIR system. This
              data element is restricted to update by DIA (DB-4). Valid values are: 0 - Does
              not meet criteria above 1 - Primary importance to system 2 - Secondary
              importance to system 3 - Tertiary importance to system O - Other. Explain in
              Remarks.

          condition: The physical manner of being or state of existence of the operating unit. A
              physical condition that must be considered in the determining of a course of
              action. The specific usage and enumerations contained in this field may be found
              in the documentation provided in the referenceDoc field. If referenceDoc not
              provided, users may consult the data provider.

          condition_avail: Availability of the operating unit relative to its condition. Indicates the
              reason the operating unit is not fully operational. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          country_code: The DoD Standard country code designator for the country or political entity to
              which the operating unit geographic coordinates reside . This field will be set
              to "OTHR" if the source value does not match a UDL country code value
              (ISO-3166-ALPHA-2).

          deploy_status: A code describing the amount of operating unit participation in a deployment.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          description: Description of the operating unit.

          div_cat: Combat status of a divisional or equivalent operating unit. Currently, this data
              element applies only to operating units of the Former Soviet Union. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          echelon: Organizational level of the operating unit. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          echelon_tier: Indicates the major group or level to which an echelon belongs. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          eval: The Intelligence Confidence Level or the Reliability/degree of confidence that
              the analyst has assigned to the data within this record. The numerical range is
              from 1 to 9 with 1 representing the highest confidence level.

          flag_flown: The country code of the observed flag flown.

          fleet_id: Naval fleet to which an operating unit is assigned. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          force: An aggregation of military units within a single service (i.e., ARMY, AIR FORCE,
              etc.) which operates under a single authority to accomplish a common mission.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          force_name: The specific name for a given force. For example, Force = ADF (Air Defense
              Force) and Force Name = Army Air Defense Force.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_role: Principal combat-related role that an operating unit is organized, structured
              and equipped to perform. Or, the specialized military or paramilitary branch in
              which an individual serves, their specialization. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid.

          id_contact: Unique identifier of the contact for this operating unit.

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

          id_location: Unique identifier of the location record for this operating unit.

          id_operating_unit: Unique identifier of the record, auto-generated by the system.

          id_organization: Unique identifier of the organization record for this operating unit.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          loc_name: Location name for the coordinates.

          loc_reason: Indicates the reason that the operating unit is at that location. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          master_unit: This field contains a value indicating whether the record is a master unit
              record (True) or a detail record (False). Master records contain basic
              information that does not change over time for each unit that has been selected
              to be projected.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts: 4Q (grid zone
              designator, GZD) FJ (the 100,000-meter square identifier) 12345678 (numerical
              location; easting is 1234 and northing is 5678, in this case specifying a
              location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator

          msn_primary: Indicates the principal type of mission that an operating unit is organized and
              equipped to perform. The specific usage and enumerations contained in this field
              may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          msn_primary_specialty: Indicates the principal specialty type of mission that an operating unit is
              organized and equipped to perform. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          oper_status: The Degree to which an operating unit is ready to perform the overall
              operational mission(s) for which it was organized and equipped. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Values are: A - Active I -
              Inactive K - Acknowledged L - Local Q - A nominated (NOM) or Data Change Request
              (DCR) record R - Production reduced by CMD decision W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          stylized_unit: This field contains a value indicating whether the record is a stylized
              operating unit record (True) or a regular operating unit record (False). A
              stylized operating unit is a type of operating unit with one set of equipment
              that can be assigned to one or more superiors. A stylized operating unit is
              generally useful for lower echelon operating units where the number of operating
              units and types of equipment are equal for multiple organizations. In lieu of
              creating unique operating unit records for each operating unit, a template is
              created for the operating unit and its equipment. This template enables the user
              to assign the operating unit to multiple organizations.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          unit_identifier: An optional identifier for this operating unit that may be composed from items
              such as the originating organization, allegiance, one-up number, etc.

          utm: Universal Transverse Mercator (UTM) grid coordinates. Pos. 1-2, UTM Zone Column
              [01-60 Pos. 3, UTM Zone Row [C-HJ-NP-X] Pos. 4, UTM False Easting [0-9] Pos.
              5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9] Pos. 10-11, UTM False Northing
              [0-9][0-9] Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          wac: World Aeronautical Chart identifier for the area in which a designated operating
              unit is located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/operatingunit/{id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_operating_unit_id": alt_operating_unit_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "country_code": country_code,
                    "deploy_status": deploy_status,
                    "description": description,
                    "div_cat": div_cat,
                    "echelon": echelon,
                    "echelon_tier": echelon_tier,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eval": eval,
                    "flag_flown": flag_flown,
                    "fleet_id": fleet_id,
                    "force": force,
                    "force_name": force_name,
                    "fpa": fpa,
                    "funct_role": funct_role,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "id_contact": id_contact,
                    "ident": ident,
                    "id_location": id_location,
                    "id_operating_unit": id_operating_unit,
                    "id_organization": id_organization,
                    "lat": lat,
                    "loc_name": loc_name,
                    "loc_reason": loc_reason,
                    "lon": lon,
                    "master_unit": master_unit,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_specialty": msn_primary_specialty,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "stylized_unit": stylized_unit,
                    "sym_code": sym_code,
                    "unit_identifier": unit_identifier,
                    "utm": utm,
                    "wac": wac,
                },
                operatingunit_update_params.OperatingunitUpdateParams,
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
    ) -> SyncOffsetPage[OperatingunitListResponse]:
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
            "/udl/operatingunit",
            page=SyncOffsetPage[OperatingunitListResponse],
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
                    operatingunit_list_params.OperatingunitListParams,
                ),
            ),
            model=OperatingunitListResponse,
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
        Service operation to delete an Operatingunit object specified by the passed ID
        path parameter. Operatingunit defines a unit or organization which operates or
        controls a space-related Entity. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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
            f"/udl/operatingunit/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/operatingunit/count",
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
                    operatingunit_count_params.OperatingunitCountParams,
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
    ) -> OperatingunitGetResponse:
        """
        Service operation to get a single Operatingunit record by its unique ID passed
        as a path parameter. Operatingunit defines a unit or organization which operates
        or controls a space-related Entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/operatingunit/{id}",
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
                    operatingunit_get_params.OperatingunitGetParams,
                ),
            ),
            cast_to=OperatingunitGetResponse,
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/operatingunit/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> OperatingunitTupleResponse:
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
            "/udl/operatingunit/tuple",
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
                    operatingunit_tuple_params.OperatingunitTupleParams,
                ),
            ),
            cast_to=OperatingunitTupleResponse,
        )


class AsyncOperatingunitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperatingunitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOperatingunitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperatingunitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOperatingunitResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_operating_unit_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        deploy_status: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        div_cat: str | NotGiven = NOT_GIVEN,
        echelon: str | NotGiven = NOT_GIVEN,
        echelon_tier: str | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        flag_flown: str | NotGiven = NOT_GIVEN,
        fleet_id: str | NotGiven = NOT_GIVEN,
        force: str | NotGiven = NOT_GIVEN,
        force_name: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_role: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        id_contact: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_location: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_organization: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        loc_name: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        master_unit: bool | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_specialty: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        stylized_unit: bool | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        unit_identifier: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Operatingunit as a POST body and ingest into
        the database. Operatingunit defines a unit or organization which operates or
        controls a space-related Entity. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          name: Name of the operating unit.

          source: Source of the data.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard country code designator for the country or political entity to
              which the operating unit owes its allegiance. This field will be set to "OTHR"
              if the source value does not match a UDL country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_operating_unit_id: Unique identifier of the operating unit record from the originating system.

          class_rating: Indicates the importance of the operating unit to the OES or MIR system. This
              data element is restricted to update by DIA (DB-4). Valid values are: 0 - Does
              not meet criteria above 1 - Primary importance to system 2 - Secondary
              importance to system 3 - Tertiary importance to system O - Other. Explain in
              Remarks.

          condition: The physical manner of being or state of existence of the operating unit. A
              physical condition that must be considered in the determining of a course of
              action. The specific usage and enumerations contained in this field may be found
              in the documentation provided in the referenceDoc field. If referenceDoc not
              provided, users may consult the data provider.

          condition_avail: Availability of the operating unit relative to its condition. Indicates the
              reason the operating unit is not fully operational. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          country_code: The DoD Standard country code designator for the country or political entity to
              which the operating unit geographic coordinates reside . This field will be set
              to "OTHR" if the source value does not match a UDL country code value
              (ISO-3166-ALPHA-2).

          deploy_status: A code describing the amount of operating unit participation in a deployment.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          description: Description of the operating unit.

          div_cat: Combat status of a divisional or equivalent operating unit. Currently, this data
              element applies only to operating units of the Former Soviet Union. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          echelon: Organizational level of the operating unit. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          echelon_tier: Indicates the major group or level to which an echelon belongs. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          eval: The Intelligence Confidence Level or the Reliability/degree of confidence that
              the analyst has assigned to the data within this record. The numerical range is
              from 1 to 9 with 1 representing the highest confidence level.

          flag_flown: The country code of the observed flag flown.

          fleet_id: Naval fleet to which an operating unit is assigned. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          force: An aggregation of military units within a single service (i.e., ARMY, AIR FORCE,
              etc.) which operates under a single authority to accomplish a common mission.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          force_name: The specific name for a given force. For example, Force = ADF (Air Defense
              Force) and Force Name = Army Air Defense Force.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_role: Principal combat-related role that an operating unit is organized, structured
              and equipped to perform. Or, the specialized military or paramilitary branch in
              which an individual serves, their specialization. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid.

          id_contact: Unique identifier of the contact for this operating unit.

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

          id_location: Unique identifier of the location record for this operating unit.

          id_operating_unit: Unique identifier of the record, auto-generated by the system.

          id_organization: Unique identifier of the organization record for this operating unit.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          loc_name: Location name for the coordinates.

          loc_reason: Indicates the reason that the operating unit is at that location. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          master_unit: This field contains a value indicating whether the record is a master unit
              record (True) or a detail record (False). Master records contain basic
              information that does not change over time for each unit that has been selected
              to be projected.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts: 4Q (grid zone
              designator, GZD) FJ (the 100,000-meter square identifier) 12345678 (numerical
              location; easting is 1234 and northing is 5678, in this case specifying a
              location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator

          msn_primary: Indicates the principal type of mission that an operating unit is organized and
              equipped to perform. The specific usage and enumerations contained in this field
              may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          msn_primary_specialty: Indicates the principal specialty type of mission that an operating unit is
              organized and equipped to perform. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          oper_status: The Degree to which an operating unit is ready to perform the overall
              operational mission(s) for which it was organized and equipped. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Values are: A - Active I -
              Inactive K - Acknowledged L - Local Q - A nominated (NOM) or Data Change Request
              (DCR) record R - Production reduced by CMD decision W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          stylized_unit: This field contains a value indicating whether the record is a stylized
              operating unit record (True) or a regular operating unit record (False). A
              stylized operating unit is a type of operating unit with one set of equipment
              that can be assigned to one or more superiors. A stylized operating unit is
              generally useful for lower echelon operating units where the number of operating
              units and types of equipment are equal for multiple organizations. In lieu of
              creating unique operating unit records for each operating unit, a template is
              created for the operating unit and its equipment. This template enables the user
              to assign the operating unit to multiple organizations.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          unit_identifier: An optional identifier for this operating unit that may be composed from items
              such as the originating organization, allegiance, one-up number, etc.

          utm: Universal Transverse Mercator (UTM) grid coordinates. Pos. 1-2, UTM Zone Column
              [01-60 Pos. 3, UTM Zone Row [C-HJ-NP-X] Pos. 4, UTM False Easting [0-9] Pos.
              5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9] Pos. 10-11, UTM False Northing
              [0-9][0-9] Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          wac: World Aeronautical Chart identifier for the area in which a designated operating
              unit is located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/operatingunit",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_operating_unit_id": alt_operating_unit_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "country_code": country_code,
                    "deploy_status": deploy_status,
                    "description": description,
                    "div_cat": div_cat,
                    "echelon": echelon,
                    "echelon_tier": echelon_tier,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eval": eval,
                    "flag_flown": flag_flown,
                    "fleet_id": fleet_id,
                    "force": force,
                    "force_name": force_name,
                    "fpa": fpa,
                    "funct_role": funct_role,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "id_contact": id_contact,
                    "ident": ident,
                    "id_location": id_location,
                    "id_operating_unit": id_operating_unit,
                    "id_organization": id_organization,
                    "lat": lat,
                    "loc_name": loc_name,
                    "loc_reason": loc_reason,
                    "lon": lon,
                    "master_unit": master_unit,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_specialty": msn_primary_specialty,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "stylized_unit": stylized_unit,
                    "sym_code": sym_code,
                    "unit_identifier": unit_identifier,
                    "utm": utm,
                    "wac": wac,
                },
                operatingunit_create_params.OperatingunitCreateParams,
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
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_operating_unit_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        deploy_status: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        div_cat: str | NotGiven = NOT_GIVEN,
        echelon: str | NotGiven = NOT_GIVEN,
        echelon_tier: str | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        flag_flown: str | NotGiven = NOT_GIVEN,
        fleet_id: str | NotGiven = NOT_GIVEN,
        force: str | NotGiven = NOT_GIVEN,
        force_name: str | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        funct_role: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        id_contact: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_location: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_organization: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        loc_name: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        master_unit: bool | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        msn_primary: str | NotGiven = NOT_GIVEN,
        msn_primary_specialty: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        stylized_unit: bool | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        unit_identifier: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Operatingunit.

        Operatingunit defines a unit
        or organization which operates or controls a space-related Entity. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

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

          name: Name of the operating unit.

          source: Source of the data.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard country code designator for the country or political entity to
              which the operating unit owes its allegiance. This field will be set to "OTHR"
              if the source value does not match a UDL country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_operating_unit_id: Unique identifier of the operating unit record from the originating system.

          class_rating: Indicates the importance of the operating unit to the OES or MIR system. This
              data element is restricted to update by DIA (DB-4). Valid values are: 0 - Does
              not meet criteria above 1 - Primary importance to system 2 - Secondary
              importance to system 3 - Tertiary importance to system O - Other. Explain in
              Remarks.

          condition: The physical manner of being or state of existence of the operating unit. A
              physical condition that must be considered in the determining of a course of
              action. The specific usage and enumerations contained in this field may be found
              in the documentation provided in the referenceDoc field. If referenceDoc not
              provided, users may consult the data provider.

          condition_avail: Availability of the operating unit relative to its condition. Indicates the
              reason the operating unit is not fully operational. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          country_code: The DoD Standard country code designator for the country or political entity to
              which the operating unit geographic coordinates reside . This field will be set
              to "OTHR" if the source value does not match a UDL country code value
              (ISO-3166-ALPHA-2).

          deploy_status: A code describing the amount of operating unit participation in a deployment.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          description: Description of the operating unit.

          div_cat: Combat status of a divisional or equivalent operating unit. Currently, this data
              element applies only to operating units of the Former Soviet Union. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          echelon: Organizational level of the operating unit. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          echelon_tier: Indicates the major group or level to which an echelon belongs. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          elev_msl: Ground elevation of the geographic coordinates referenced to (above or below)
              Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation.

          eval: The Intelligence Confidence Level or the Reliability/degree of confidence that
              the analyst has assigned to the data within this record. The numerical range is
              from 1 to 9 with 1 representing the highest confidence level.

          flag_flown: The country code of the observed flag flown.

          fleet_id: Naval fleet to which an operating unit is assigned. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          force: An aggregation of military units within a single service (i.e., ARMY, AIR FORCE,
              etc.) which operates under a single authority to accomplish a common mission.
              The specific usage and enumerations contained in this field may be found in the
              documentation provided in the referenceDoc field. If referenceDoc not provided,
              users may consult the data provider.

          force_name: The specific name for a given force. For example, Force = ADF (Air Defense
              Force) and Force Name = Army Air Defense Force.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_role: Principal combat-related role that an operating unit is organized, structured
              and equipped to perform. Or, the specialized military or paramilitary branch in
              which an individual serves, their specialization. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid.

          id_contact: Unique identifier of the contact for this operating unit.

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

          id_location: Unique identifier of the location record for this operating unit.

          id_operating_unit: Unique identifier of the record, auto-generated by the system.

          id_organization: Unique identifier of the organization record for this operating unit.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          loc_name: Location name for the coordinates.

          loc_reason: Indicates the reason that the operating unit is at that location. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          master_unit: This field contains a value indicating whether the record is a master unit
              record (True) or a detail record (False). Master records contain basic
              information that does not change over time for each unit that has been selected
              to be projected.

          mil_grid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts: 4Q (grid zone
              designator, GZD) FJ (the 100,000-meter square identifier) 12345678 (numerical
              location; easting is 1234 and northing is 5678, in this case specifying a
              location with 10 m resolution).

          mil_grid_sys: Indicates the grid system used in the development of the milGrid coordinates.
              Values are:

              UPS - Universal Polar System

              UTM - Universal Transverse Mercator

          msn_primary: Indicates the principal type of mission that an operating unit is organized and
              equipped to perform. The specific usage and enumerations contained in this field
              may be found in the documentation provided in the referenceDoc field. If
              referenceDoc not provided, users may consult the data provider.

          msn_primary_specialty: Indicates the principal specialty type of mission that an operating unit is
              organized and equipped to perform. The specific usage and enumerations contained
              in this field may be found in the documentation provided in the referenceDoc
              field. If referenceDoc not provided, users may consult the data provider.

          oper_status: The Degree to which an operating unit is ready to perform the overall
              operational mission(s) for which it was organized and equipped. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Values are: A - Active I -
              Inactive K - Acknowledged L - Local Q - A nominated (NOM) or Data Change Request
              (DCR) record R - Production reduced by CMD decision W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          stylized_unit: This field contains a value indicating whether the record is a stylized
              operating unit record (True) or a regular operating unit record (False). A
              stylized operating unit is a type of operating unit with one set of equipment
              that can be assigned to one or more superiors. A stylized operating unit is
              generally useful for lower echelon operating units where the number of operating
              units and types of equipment are equal for multiple organizations. In lieu of
              creating unique operating unit records for each operating unit, a template is
              created for the operating unit and its equipment. This template enables the user
              to assign the operating unit to multiple organizations.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          unit_identifier: An optional identifier for this operating unit that may be composed from items
              such as the originating organization, allegiance, one-up number, etc.

          utm: Universal Transverse Mercator (UTM) grid coordinates. Pos. 1-2, UTM Zone Column
              [01-60 Pos. 3, UTM Zone Row [C-HJ-NP-X] Pos. 4, UTM False Easting [0-9] Pos.
              5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9] Pos. 10-11, UTM False Northing
              [0-9][0-9] Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          wac: World Aeronautical Chart identifier for the area in which a designated operating
              unit is located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/operatingunit/{id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_operating_unit_id": alt_operating_unit_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "country_code": country_code,
                    "deploy_status": deploy_status,
                    "description": description,
                    "div_cat": div_cat,
                    "echelon": echelon,
                    "echelon_tier": echelon_tier,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eval": eval,
                    "flag_flown": flag_flown,
                    "fleet_id": fleet_id,
                    "force": force,
                    "force_name": force_name,
                    "fpa": fpa,
                    "funct_role": funct_role,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "id_contact": id_contact,
                    "ident": ident,
                    "id_location": id_location,
                    "id_operating_unit": id_operating_unit,
                    "id_organization": id_organization,
                    "lat": lat,
                    "loc_name": loc_name,
                    "loc_reason": loc_reason,
                    "lon": lon,
                    "master_unit": master_unit,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "msn_primary": msn_primary,
                    "msn_primary_specialty": msn_primary_specialty,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "stylized_unit": stylized_unit,
                    "sym_code": sym_code,
                    "unit_identifier": unit_identifier,
                    "utm": utm,
                    "wac": wac,
                },
                operatingunit_update_params.OperatingunitUpdateParams,
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
    ) -> AsyncPaginator[OperatingunitListResponse, AsyncOffsetPage[OperatingunitListResponse]]:
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
            "/udl/operatingunit",
            page=AsyncOffsetPage[OperatingunitListResponse],
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
                    operatingunit_list_params.OperatingunitListParams,
                ),
            ),
            model=OperatingunitListResponse,
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
        Service operation to delete an Operatingunit object specified by the passed ID
        path parameter. Operatingunit defines a unit or organization which operates or
        controls a space-related Entity. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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
            f"/udl/operatingunit/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/operatingunit/count",
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
                    operatingunit_count_params.OperatingunitCountParams,
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
    ) -> OperatingunitGetResponse:
        """
        Service operation to get a single Operatingunit record by its unique ID passed
        as a path parameter. Operatingunit defines a unit or organization which operates
        or controls a space-related Entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/operatingunit/{id}",
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
                    operatingunit_get_params.OperatingunitGetParams,
                ),
            ),
            cast_to=OperatingunitGetResponse,
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/operatingunit/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> OperatingunitTupleResponse:
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
            "/udl/operatingunit/tuple",
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
                    operatingunit_tuple_params.OperatingunitTupleParams,
                ),
            ),
            cast_to=OperatingunitTupleResponse,
        )


class OperatingunitResourceWithRawResponse:
    def __init__(self, operatingunit: OperatingunitResource) -> None:
        self._operatingunit = operatingunit

        self.create = to_raw_response_wrapper(
            operatingunit.create,
        )
        self.update = to_raw_response_wrapper(
            operatingunit.update,
        )
        self.list = to_raw_response_wrapper(
            operatingunit.list,
        )
        self.delete = to_raw_response_wrapper(
            operatingunit.delete,
        )
        self.count = to_raw_response_wrapper(
            operatingunit.count,
        )
        self.get = to_raw_response_wrapper(
            operatingunit.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            operatingunit.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            operatingunit.tuple,
        )


class AsyncOperatingunitResourceWithRawResponse:
    def __init__(self, operatingunit: AsyncOperatingunitResource) -> None:
        self._operatingunit = operatingunit

        self.create = async_to_raw_response_wrapper(
            operatingunit.create,
        )
        self.update = async_to_raw_response_wrapper(
            operatingunit.update,
        )
        self.list = async_to_raw_response_wrapper(
            operatingunit.list,
        )
        self.delete = async_to_raw_response_wrapper(
            operatingunit.delete,
        )
        self.count = async_to_raw_response_wrapper(
            operatingunit.count,
        )
        self.get = async_to_raw_response_wrapper(
            operatingunit.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            operatingunit.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            operatingunit.tuple,
        )


class OperatingunitResourceWithStreamingResponse:
    def __init__(self, operatingunit: OperatingunitResource) -> None:
        self._operatingunit = operatingunit

        self.create = to_streamed_response_wrapper(
            operatingunit.create,
        )
        self.update = to_streamed_response_wrapper(
            operatingunit.update,
        )
        self.list = to_streamed_response_wrapper(
            operatingunit.list,
        )
        self.delete = to_streamed_response_wrapper(
            operatingunit.delete,
        )
        self.count = to_streamed_response_wrapper(
            operatingunit.count,
        )
        self.get = to_streamed_response_wrapper(
            operatingunit.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            operatingunit.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            operatingunit.tuple,
        )


class AsyncOperatingunitResourceWithStreamingResponse:
    def __init__(self, operatingunit: AsyncOperatingunitResource) -> None:
        self._operatingunit = operatingunit

        self.create = async_to_streamed_response_wrapper(
            operatingunit.create,
        )
        self.update = async_to_streamed_response_wrapper(
            operatingunit.update,
        )
        self.list = async_to_streamed_response_wrapper(
            operatingunit.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            operatingunit.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            operatingunit.count,
        )
        self.get = async_to_streamed_response_wrapper(
            operatingunit.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            operatingunit.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            operatingunit.tuple,
        )
