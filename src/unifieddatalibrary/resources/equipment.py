# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import (
    equipment_list_params,
    equipment_count_params,
    equipment_tuple_params,
    equipment_create_params,
    equipment_update_params,
    equipment_retrieve_params,
    equipment_create_bulk_params,
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
from ..types.equipment_full import EquipmentFull
from ..types.equipment_abridged import EquipmentAbridged
from ..types.equipment_tuple_response import EquipmentTupleResponse

__all__ = ["EquipmentResource", "AsyncEquipmentResource"]


class EquipmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EquipmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EquipmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EquipmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EquipmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        lat: float,
        lon: float,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_eqp_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eqp_code: str | NotGiven = NOT_GIVEN,
        eqp_id_num: str | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        function: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_parent_equipment: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        nomen: str | NotGiven = NOT_GIVEN,
        oper_area_primary: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        qty_oh: int | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seq_num: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
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
        Service operation to take a single equipment record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country or political entity to
              which the equipment geographic coordinates reside. This field will be set to
              "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

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

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the equipment owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_eqp_id: Unique identifier of the Equipment record from the originating system.

          class_rating: Indicates the importance of the equipment. Referenced, but not constrained to,
              the following class ratings type classifications.

              0 - Not of significant importance of the system

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
              reference to a fixed figure, system of lines, etc. specified in degrees, minute,
              and seconds.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation, in meters, of the geographic coordinates referenced to (above
              or below) Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy. Confidence level has a range of values
              from 0 to 100, with 100 being highest level of confidence.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation, measured in meters.

          eqp_code: Designated equipment code assigned to the item of equipment or an abbreviation
              record type unique identifier. Users should consult the data provider for
              information on the equipment code structure.

          eqp_id_num: Uniquely identifies each item or group of equipment associated with a unit,
              facility or site.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          function: Indicates the function or mission of this equipment, which may or may not be
              engaged in at any particular time. Typically refers to a unit, organization, or
              installation/facility performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, measured in
              meters.

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

          id_operating_unit: Unique identifier of the operating unit associated with the equipment record.

          id_parent_equipment: Unique identifier of the Parent equipment record associated with this equipment
              record.

          id_site: Unique identifier of the Site Entity associated with the equipment record.

          loc_reason: Indicates the reason that the equipment is at that location. The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

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

          nomen: Generic type this specific piece of equipment belongs to, and the identifying
              nomenclature which describes the equipment.

          oper_area_primary: Internationally recognized water area in which the vessel is most likely to be
              deployed or in which it normally operates most frequently.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          qty_oh: Relative to the parent entity, the total number of military personnel or
              equipment assessed to be on-hand (OH).

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Referenced, but not
              constrained to, the following record status type classifications.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          seq_num: Provider specific sequential number assigned to the equipment.

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this equipment
              record. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. See the corresponding srcTyps array element
              for the data type of the UUID and use the appropriate API operation to retrieve
              that object.

          src_typs: Array of UDL record types such as AIRCRAFT, VESSEL, EO, MTI that are related to
              this equipment record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          wac: World Aeronautical Chart identifier for the area in which a designated place is
              located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/equipment",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "lat": lat,
                    "lon": lon,
                    "source": source,
                    "id": id,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_eqp_id": alt_eqp_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eqp_code": eqp_code,
                    "eqp_id_num": eqp_id_num,
                    "eval": eval,
                    "fpa": fpa,
                    "function": function,
                    "funct_primary": funct_primary,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "ident": ident,
                    "id_operating_unit": id_operating_unit,
                    "id_parent_equipment": id_parent_equipment,
                    "id_site": id_site,
                    "loc_reason": loc_reason,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "nomen": nomen,
                    "oper_area_primary": oper_area_primary,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "qty_oh": qty_oh,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "seq_num": seq_num,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "sym_code": sym_code,
                    "utm": utm,
                    "wac": wac,
                },
                equipment_create_params.EquipmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
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
    ) -> EquipmentFull:
        """
        Service operation to get a single equipment record by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/equipment/{id}",
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
                    equipment_retrieve_params.EquipmentRetrieveParams,
                ),
            ),
            cast_to=EquipmentFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        lat: float,
        lon: float,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_eqp_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eqp_code: str | NotGiven = NOT_GIVEN,
        eqp_id_num: str | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        function: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_parent_equipment: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        nomen: str | NotGiven = NOT_GIVEN,
        oper_area_primary: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        qty_oh: int | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seq_num: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single equipment record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country or political entity to
              which the equipment geographic coordinates reside. This field will be set to
              "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

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

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the equipment owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_eqp_id: Unique identifier of the Equipment record from the originating system.

          class_rating: Indicates the importance of the equipment. Referenced, but not constrained to,
              the following class ratings type classifications.

              0 - Not of significant importance of the system

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
              reference to a fixed figure, system of lines, etc. specified in degrees, minute,
              and seconds.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation, in meters, of the geographic coordinates referenced to (above
              or below) Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy. Confidence level has a range of values
              from 0 to 100, with 100 being highest level of confidence.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation, measured in meters.

          eqp_code: Designated equipment code assigned to the item of equipment or an abbreviation
              record type unique identifier. Users should consult the data provider for
              information on the equipment code structure.

          eqp_id_num: Uniquely identifies each item or group of equipment associated with a unit,
              facility or site.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          function: Indicates the function or mission of this equipment, which may or may not be
              engaged in at any particular time. Typically refers to a unit, organization, or
              installation/facility performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, measured in
              meters.

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

          id_operating_unit: Unique identifier of the operating unit associated with the equipment record.

          id_parent_equipment: Unique identifier of the Parent equipment record associated with this equipment
              record.

          id_site: Unique identifier of the Site Entity associated with the equipment record.

          loc_reason: Indicates the reason that the equipment is at that location. The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

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

          nomen: Generic type this specific piece of equipment belongs to, and the identifying
              nomenclature which describes the equipment.

          oper_area_primary: Internationally recognized water area in which the vessel is most likely to be
              deployed or in which it normally operates most frequently.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          qty_oh: Relative to the parent entity, the total number of military personnel or
              equipment assessed to be on-hand (OH).

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Referenced, but not
              constrained to, the following record status type classifications.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          seq_num: Provider specific sequential number assigned to the equipment.

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this equipment
              record. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. See the corresponding srcTyps array element
              for the data type of the UUID and use the appropriate API operation to retrieve
              that object.

          src_typs: Array of UDL record types such as AIRCRAFT, VESSEL, EO, MTI that are related to
              this equipment record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

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
            f"/udl/equipment/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "lat": lat,
                    "lon": lon,
                    "source": source,
                    "body_id": body_id,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_eqp_id": alt_eqp_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eqp_code": eqp_code,
                    "eqp_id_num": eqp_id_num,
                    "eval": eval,
                    "fpa": fpa,
                    "function": function,
                    "funct_primary": funct_primary,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "ident": ident,
                    "id_operating_unit": id_operating_unit,
                    "id_parent_equipment": id_parent_equipment,
                    "id_site": id_site,
                    "loc_reason": loc_reason,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "nomen": nomen,
                    "oper_area_primary": oper_area_primary,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "qty_oh": qty_oh,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "seq_num": seq_num,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "sym_code": sym_code,
                    "utm": utm,
                    "wac": wac,
                },
                equipment_update_params.EquipmentUpdateParams,
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
    ) -> SyncOffsetPage[EquipmentAbridged]:
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
            "/udl/equipment",
            page=SyncOffsetPage[EquipmentAbridged],
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
                    equipment_list_params.EquipmentListParams,
                ),
            ),
            model=EquipmentAbridged,
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
        Service operation to delete a equipment record specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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
            f"/udl/equipment/{id}",
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
            "/udl/equipment/count",
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
                    equipment_count_params.EquipmentCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[equipment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Equipment records as a POST body and ingest into the database. This operation is
        not intended to be used for automated feeds into UDL. Data providers should
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
            "/udl/equipment/createBulk",
            body=maybe_transform(body, Iterable[equipment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query_help(
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
            "/udl/equipment/queryhelp",
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
    ) -> EquipmentTupleResponse:
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
            "/udl/equipment/tuple",
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
                    equipment_tuple_params.EquipmentTupleParams,
                ),
            ),
            cast_to=EquipmentTupleResponse,
        )


class AsyncEquipmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEquipmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEquipmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEquipmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEquipmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        lat: float,
        lon: float,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_eqp_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eqp_code: str | NotGiven = NOT_GIVEN,
        eqp_id_num: str | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        function: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_parent_equipment: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        nomen: str | NotGiven = NOT_GIVEN,
        oper_area_primary: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        qty_oh: int | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seq_num: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
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
        Service operation to take a single equipment record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country or political entity to
              which the equipment geographic coordinates reside. This field will be set to
              "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

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

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the equipment owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_eqp_id: Unique identifier of the Equipment record from the originating system.

          class_rating: Indicates the importance of the equipment. Referenced, but not constrained to,
              the following class ratings type classifications.

              0 - Not of significant importance of the system

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
              reference to a fixed figure, system of lines, etc. specified in degrees, minute,
              and seconds.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation, in meters, of the geographic coordinates referenced to (above
              or below) Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy. Confidence level has a range of values
              from 0 to 100, with 100 being highest level of confidence.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation, measured in meters.

          eqp_code: Designated equipment code assigned to the item of equipment or an abbreviation
              record type unique identifier. Users should consult the data provider for
              information on the equipment code structure.

          eqp_id_num: Uniquely identifies each item or group of equipment associated with a unit,
              facility or site.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          function: Indicates the function or mission of this equipment, which may or may not be
              engaged in at any particular time. Typically refers to a unit, organization, or
              installation/facility performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, measured in
              meters.

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

          id_operating_unit: Unique identifier of the operating unit associated with the equipment record.

          id_parent_equipment: Unique identifier of the Parent equipment record associated with this equipment
              record.

          id_site: Unique identifier of the Site Entity associated with the equipment record.

          loc_reason: Indicates the reason that the equipment is at that location. The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

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

          nomen: Generic type this specific piece of equipment belongs to, and the identifying
              nomenclature which describes the equipment.

          oper_area_primary: Internationally recognized water area in which the vessel is most likely to be
              deployed or in which it normally operates most frequently.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          qty_oh: Relative to the parent entity, the total number of military personnel or
              equipment assessed to be on-hand (OH).

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Referenced, but not
              constrained to, the following record status type classifications.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          seq_num: Provider specific sequential number assigned to the equipment.

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this equipment
              record. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. See the corresponding srcTyps array element
              for the data type of the UUID and use the appropriate API operation to retrieve
              that object.

          src_typs: Array of UDL record types such as AIRCRAFT, VESSEL, EO, MTI that are related to
              this equipment record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

          wac: World Aeronautical Chart identifier for the area in which a designated place is
              located.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/equipment",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "lat": lat,
                    "lon": lon,
                    "source": source,
                    "id": id,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_eqp_id": alt_eqp_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eqp_code": eqp_code,
                    "eqp_id_num": eqp_id_num,
                    "eval": eval,
                    "fpa": fpa,
                    "function": function,
                    "funct_primary": funct_primary,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "ident": ident,
                    "id_operating_unit": id_operating_unit,
                    "id_parent_equipment": id_parent_equipment,
                    "id_site": id_site,
                    "loc_reason": loc_reason,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "nomen": nomen,
                    "oper_area_primary": oper_area_primary,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "qty_oh": qty_oh,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "seq_num": seq_num,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "sym_code": sym_code,
                    "utm": utm,
                    "wac": wac,
                },
                equipment_create_params.EquipmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
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
    ) -> EquipmentFull:
        """
        Service operation to get a single equipment record by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/equipment/{id}",
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
                    equipment_retrieve_params.EquipmentRetrieveParams,
                ),
            ),
            cast_to=EquipmentFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        lat: float,
        lon: float,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        air_def_area: str | NotGiven = NOT_GIVEN,
        allegiance: str | NotGiven = NOT_GIVEN,
        alt_allegiance: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        alt_eqp_id: str | NotGiven = NOT_GIVEN,
        class_rating: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        condition_avail: str | NotGiven = NOT_GIVEN,
        coord: str | NotGiven = NOT_GIVEN,
        coord_datum: str | NotGiven = NOT_GIVEN,
        coord_deriv_acc: float | NotGiven = NOT_GIVEN,
        elev_msl: float | NotGiven = NOT_GIVEN,
        elev_msl_conf_lvl: int | NotGiven = NOT_GIVEN,
        elev_msl_deriv_acc: float | NotGiven = NOT_GIVEN,
        eqp_code: str | NotGiven = NOT_GIVEN,
        eqp_id_num: str | NotGiven = NOT_GIVEN,
        eval: int | NotGiven = NOT_GIVEN,
        fpa: str | NotGiven = NOT_GIVEN,
        function: str | NotGiven = NOT_GIVEN,
        funct_primary: str | NotGiven = NOT_GIVEN,
        geoidal_msl_sep: float | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_operating_unit: str | NotGiven = NOT_GIVEN,
        id_parent_equipment: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        loc_reason: str | NotGiven = NOT_GIVEN,
        mil_grid: str | NotGiven = NOT_GIVEN,
        mil_grid_sys: str | NotGiven = NOT_GIVEN,
        nomen: str | NotGiven = NOT_GIVEN,
        oper_area_primary: str | NotGiven = NOT_GIVEN,
        oper_status: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pol_subdiv: str | NotGiven = NOT_GIVEN,
        qty_oh: int | NotGiven = NOT_GIVEN,
        rec_status: str | NotGiven = NOT_GIVEN,
        reference_doc: str | NotGiven = NOT_GIVEN,
        res_prod: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seq_num: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        sym_code: str | NotGiven = NOT_GIVEN,
        utm: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single equipment record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country or political entity to
              which the equipment geographic coordinates reside. This field will be set to
              "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

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

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          air_def_area: Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
              coordinates reside.

          allegiance: The DoD Standard Country Code designator for the country or political entity to
              which the equipment owes its allegiance. This field will be set to "OTHR" if the
              source value does not match a UDL Country code value (ISO-3166-ALPHA-2).

          alt_allegiance: Specifies an alternate allegiance code if the data provider code is not part of
              an official Country Code standard such as ISO-3166 or FIPS. This field will be
              set to the value provided by the source and should be used for all Queries
              specifying allegiance.

          alt_country_code: Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS. This field will be set
              to the value provided by the source and should be used for all Queries
              specifying a Country Code.

          alt_eqp_id: Unique identifier of the Equipment record from the originating system.

          class_rating: Indicates the importance of the equipment. Referenced, but not constrained to,
              the following class ratings type classifications.

              0 - Not of significant importance of the system

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
              reference to a fixed figure, system of lines, etc. specified in degrees, minute,
              and seconds.

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

              Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]].

          coord_datum: A mathematical model of the earth used to calculate coordinates on a map. US
              Forces use the World Geodetic System 1984 (WGS 84), but also use maps by allied
              countries with local datums. The datum must be specified to ensure accuracy of
              coordinates. The specific usage and enumerations contained in this field may be
              found in the documentation provided in the referenceDoc field. If referenceDoc
              not provided, users may consult the data provider.

          coord_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              coordinate.

          elev_msl: Ground elevation, in meters, of the geographic coordinates referenced to (above
              or below) Mean Sea Level (MSL) vertical datum.

          elev_msl_conf_lvl: Indicates the confidence level expressed as a percent that a specific geometric
              spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
              to within a specified vertical accuracy. Confidence level has a range of values
              from 0 to 100, with 100 being highest level of confidence.

          elev_msl_deriv_acc: Indicates the plus or minus error assessed against the method used to derive the
              elevation, measured in meters.

          eqp_code: Designated equipment code assigned to the item of equipment or an abbreviation
              record type unique identifier. Users should consult the data provider for
              information on the equipment code structure.

          eqp_id_num: Uniquely identifies each item or group of equipment associated with a unit,
              facility or site.

          eval: Eval represents the Intelligence Confidence Level or the Reliability/degree of
              confidence that the analyst has assigned to the data within this record. The
              numerical range is from 1 to 9 with 1 representing the highest confidence level.

          fpa: Functional Production Area (FPA) under the Shared Production Program (SPP).
              Producers are defined per country per FPA. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          function: Indicates the function or mission of this equipment, which may or may not be
              engaged in at any particular time. Typically refers to a unit, organization, or
              installation/facility performing a specific function or mission such as a
              redistribution center or naval shipyard. The specific usage and enumerations
              contained in this field may be found in the documentation provided in the
              referenceDoc field. If referenceDoc not provided, users may consult the data
              provider.

          funct_primary: Principal operational function being performed. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          geoidal_msl_sep: The distance between Mean Sea Level and a referenced ellipsoid, measured in
              meters.

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

          id_operating_unit: Unique identifier of the operating unit associated with the equipment record.

          id_parent_equipment: Unique identifier of the Parent equipment record associated with this equipment
              record.

          id_site: Unique identifier of the Site Entity associated with the equipment record.

          loc_reason: Indicates the reason that the equipment is at that location. The specific usage
              and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

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

          nomen: Generic type this specific piece of equipment belongs to, and the identifying
              nomenclature which describes the equipment.

          oper_area_primary: Internationally recognized water area in which the vessel is most likely to be
              deployed or in which it normally operates most frequently.

          oper_status: The Degree to which an entity is ready to perform the overall operational
              mission(s) for which it was organized and equipped. The specific usage and
              enumerations contained in this field may be found in the documentation provided
              in the referenceDoc field. If referenceDoc not provided, users may consult the
              data provider.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pol_subdiv: Political subdivision in which the geographic coordinates reside. The specific
              usage and enumerations contained in this field may be found in the documentation
              provided in the referenceDoc field. If referenceDoc not provided, users may
              consult the data provider.

          qty_oh: Relative to the parent entity, the total number of military personnel or
              equipment assessed to be on-hand (OH).

          rec_status: Validity and currency of the data in the record to be used in conjunction with
              the other elements in the record as defined by SOPs. Referenced, but not
              constrained to, the following record status type classifications.

              A - Active

              I - Inactive

              K - Acknowledged

              L - Local

              Q - A nominated (NOM) or Data Change Request (DCR) record

              R - Production reduced by CMD decision

              W - Working Record.

          reference_doc: The reference documentiation that specifies the usage and enumerations contained
              in this record. If referenceDoc not provided, users may consult the data
              provider.

          res_prod: Responsible Producer - Organization that is responsible for the maintenance of
              the record.

          review_date: Date on which the data in the record was last reviewed by the responsible
              analyst for accuracy and currency. This date cannot be greater than the current
              date.

          seq_num: Provider specific sequential number assigned to the equipment.

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this equipment
              record. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. See the corresponding srcTyps array element
              for the data type of the UUID and use the appropriate API operation to retrieve
              that object.

          src_typs: Array of UDL record types such as AIRCRAFT, VESSEL, EO, MTI that are related to
              this equipment record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          sym_code: A standard scheme for symbol coding enabling the transfer, display and use of
              symbols and graphics among information systems, as per MIL-STD 2525B, and
              supported by the element AFFILIATION.

          utm: Universal Transverse Mercator (UTM) grid coordinates.

              Pos. 1-2, UTM Zone Column [01-60

              Pos. 3, UTM Zone Row [C-HJ-NP-X]

              Pos. 4, UTM False Easting [0-9]

              Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

              Pos. 10-11, UTM False Northing [0-9][0-9]

              Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].

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
            f"/udl/equipment/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "lat": lat,
                    "lon": lon,
                    "source": source,
                    "body_id": body_id,
                    "air_def_area": air_def_area,
                    "allegiance": allegiance,
                    "alt_allegiance": alt_allegiance,
                    "alt_country_code": alt_country_code,
                    "alt_eqp_id": alt_eqp_id,
                    "class_rating": class_rating,
                    "condition": condition,
                    "condition_avail": condition_avail,
                    "coord": coord,
                    "coord_datum": coord_datum,
                    "coord_deriv_acc": coord_deriv_acc,
                    "elev_msl": elev_msl,
                    "elev_msl_conf_lvl": elev_msl_conf_lvl,
                    "elev_msl_deriv_acc": elev_msl_deriv_acc,
                    "eqp_code": eqp_code,
                    "eqp_id_num": eqp_id_num,
                    "eval": eval,
                    "fpa": fpa,
                    "function": function,
                    "funct_primary": funct_primary,
                    "geoidal_msl_sep": geoidal_msl_sep,
                    "ident": ident,
                    "id_operating_unit": id_operating_unit,
                    "id_parent_equipment": id_parent_equipment,
                    "id_site": id_site,
                    "loc_reason": loc_reason,
                    "mil_grid": mil_grid,
                    "mil_grid_sys": mil_grid_sys,
                    "nomen": nomen,
                    "oper_area_primary": oper_area_primary,
                    "oper_status": oper_status,
                    "origin": origin,
                    "pol_subdiv": pol_subdiv,
                    "qty_oh": qty_oh,
                    "rec_status": rec_status,
                    "reference_doc": reference_doc,
                    "res_prod": res_prod,
                    "review_date": review_date,
                    "seq_num": seq_num,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "sym_code": sym_code,
                    "utm": utm,
                    "wac": wac,
                },
                equipment_update_params.EquipmentUpdateParams,
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
    ) -> AsyncPaginator[EquipmentAbridged, AsyncOffsetPage[EquipmentAbridged]]:
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
            "/udl/equipment",
            page=AsyncOffsetPage[EquipmentAbridged],
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
                    equipment_list_params.EquipmentListParams,
                ),
            ),
            model=EquipmentAbridged,
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
        Service operation to delete a equipment record specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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
            f"/udl/equipment/{id}",
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
            "/udl/equipment/count",
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
                    equipment_count_params.EquipmentCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[equipment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Equipment records as a POST body and ingest into the database. This operation is
        not intended to be used for automated feeds into UDL. Data providers should
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
            "/udl/equipment/createBulk",
            body=await async_maybe_transform(body, Iterable[equipment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query_help(
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
            "/udl/equipment/queryhelp",
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
    ) -> EquipmentTupleResponse:
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
            "/udl/equipment/tuple",
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
                    equipment_tuple_params.EquipmentTupleParams,
                ),
            ),
            cast_to=EquipmentTupleResponse,
        )


class EquipmentResourceWithRawResponse:
    def __init__(self, equipment: EquipmentResource) -> None:
        self._equipment = equipment

        self.create = to_raw_response_wrapper(
            equipment.create,
        )
        self.retrieve = to_raw_response_wrapper(
            equipment.retrieve,
        )
        self.update = to_raw_response_wrapper(
            equipment.update,
        )
        self.list = to_raw_response_wrapper(
            equipment.list,
        )
        self.delete = to_raw_response_wrapper(
            equipment.delete,
        )
        self.count = to_raw_response_wrapper(
            equipment.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            equipment.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            equipment.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            equipment.tuple,
        )


class AsyncEquipmentResourceWithRawResponse:
    def __init__(self, equipment: AsyncEquipmentResource) -> None:
        self._equipment = equipment

        self.create = async_to_raw_response_wrapper(
            equipment.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            equipment.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            equipment.update,
        )
        self.list = async_to_raw_response_wrapper(
            equipment.list,
        )
        self.delete = async_to_raw_response_wrapper(
            equipment.delete,
        )
        self.count = async_to_raw_response_wrapper(
            equipment.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            equipment.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            equipment.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            equipment.tuple,
        )


class EquipmentResourceWithStreamingResponse:
    def __init__(self, equipment: EquipmentResource) -> None:
        self._equipment = equipment

        self.create = to_streamed_response_wrapper(
            equipment.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            equipment.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            equipment.update,
        )
        self.list = to_streamed_response_wrapper(
            equipment.list,
        )
        self.delete = to_streamed_response_wrapper(
            equipment.delete,
        )
        self.count = to_streamed_response_wrapper(
            equipment.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            equipment.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            equipment.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            equipment.tuple,
        )


class AsyncEquipmentResourceWithStreamingResponse:
    def __init__(self, equipment: AsyncEquipmentResource) -> None:
        self._equipment = equipment

        self.create = async_to_streamed_response_wrapper(
            equipment.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            equipment.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            equipment.update,
        )
        self.list = async_to_streamed_response_wrapper(
            equipment.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            equipment.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            equipment.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            equipment.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            equipment.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            equipment.tuple,
        )
