# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    airfield_list_params,
    airfield_count_params,
    airfield_tuple_params,
    airfield_create_params,
    airfield_update_params,
    airfield_retrieve_params,
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
from ..types.airfield_full import AirfieldFull
from ..types.airfield_abridged import AirfieldAbridged
from ..types.airfield_tuple_response import AirfieldTupleResponse

__all__ = ["AirfieldsResource", "AsyncAirfieldsResource"]


class AirfieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirfieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirfieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirfieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirfieldsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        alternative_names: List[str] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        dst_info: str | NotGiven = NOT_GIVEN,
        elev_ft: float | NotGiven = NOT_GIVEN,
        elev_m: float | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        geoloc: str | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        host_nat_code: str | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        info_url: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mag_dec: float | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        misc_codes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        regional_authority: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        secondary_icao: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        state_province_code: str | NotGiven = NOT_GIVEN,
        suitability_code_descs: List[str] | NotGiven = NOT_GIVEN,
        suitability_codes: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        zar_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Airfield as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          name: The name of the airfield.

          source: Source of the data.

          type: The airfield activity use type (e.g. Commercial, Airport, Heliport, Gliderport,
              etc.).

          id: Unique identifier of the record, auto-generated by the system.

          alt_airfield_id: Alternate Airfield identifier provided by source.

          alternative_names: Alternative names for this airfield.

          city: The closest city to the location of this airfield.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL’s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          country_name: The country name where this airfield is located.

          dst_info: Information regarding daylight saving time as is relevant to the location and
              operation of this airfield.

          elev_ft: Elevation of the airfield above mean sea level, in feet. Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          elev_m: Elevation of the airfield above mean sea level, in meters. Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          faa: The Federal Aviation Administration (FAA) location identifier of this airfield.

          geoloc: Air Force geographic location code of the airfield.

          gmt_offset: Time difference between the location of the airfield and the Greenwich Mean Time
              (GMT), expressed as +/-HH:MM. Time zones east of Greenwich have positive offsets
              and time zones west of Greenwich are negative.

          host_nat_code: The host nation code of this airfield, used for non-DoD/FAA locations.

          iata: The International Aviation Transport Association (IATA) code of the airfield.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield.

          id_site: The ID of the parent site.

          info_url: The URL link to information about airfield.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          mag_dec: The magnetic declination/variation of the airfield's location from true north,
              in degrees. Positive values east of true north and negative values west of true
              north.

          max_runway_length: The length of the longest runway at this airfield in feet.

          misc_codes: Applicable miscellaneous codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          regional_authority: The regional authority of the airfield.

          region_name: Region where the airfield resides.

          runways: The number of runways at the site.

          secondary_icao: The secondary ICAO code for this airfield. Some airfields have two associated
              ICAO codes, this can occur in cases when a single airfield supports both
              military and civilian operations.

          state: State or province of the airfield's location.

          state_province_code: The code for the state or province in which this airfield is located. Intended
              as, but not constrained to, FIPS 10-4 region code designations.

          suitability_code_descs: Array of descriptions for given suitability codes. The index of the description
              corresponds to the position of the letter code in the string provided in the
              suitabilityCodes field.

          suitability_codes: Associated suitability codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          wac_innr: The airfield's World Area Code installation number (WAC-INNR).

          zar_id: Air Mobility Command (AMC) Zone availability Report identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airfield",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "id": id,
                    "alt_airfield_id": alt_airfield_id,
                    "alternative_names": alternative_names,
                    "city": city,
                    "country_code": country_code,
                    "country_name": country_name,
                    "dst_info": dst_info,
                    "elev_ft": elev_ft,
                    "elev_m": elev_m,
                    "faa": faa,
                    "geoloc": geoloc,
                    "gmt_offset": gmt_offset,
                    "host_nat_code": host_nat_code,
                    "iata": iata,
                    "icao": icao,
                    "id_site": id_site,
                    "info_url": info_url,
                    "lat": lat,
                    "lon": lon,
                    "mag_dec": mag_dec,
                    "max_runway_length": max_runway_length,
                    "misc_codes": misc_codes,
                    "origin": origin,
                    "regional_authority": regional_authority,
                    "region_name": region_name,
                    "runways": runways,
                    "secondary_icao": secondary_icao,
                    "state": state,
                    "state_province_code": state_province_code,
                    "suitability_code_descs": suitability_code_descs,
                    "suitability_codes": suitability_codes,
                    "wac_innr": wac_innr,
                    "zar_id": zar_id,
                },
                airfield_create_params.AirfieldCreateParams,
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
    ) -> AirfieldFull:
        """
        Service operation to get a single Airfield by its unique ID passed as a path
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
            f"/udl/airfield/{id}",
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
                    airfield_retrieve_params.AirfieldRetrieveParams,
                ),
            ),
            cast_to=AirfieldFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        alternative_names: List[str] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        dst_info: str | NotGiven = NOT_GIVEN,
        elev_ft: float | NotGiven = NOT_GIVEN,
        elev_m: float | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        geoloc: str | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        host_nat_code: str | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        info_url: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mag_dec: float | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        misc_codes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        regional_authority: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        secondary_icao: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        state_province_code: str | NotGiven = NOT_GIVEN,
        suitability_code_descs: List[str] | NotGiven = NOT_GIVEN,
        suitability_codes: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        zar_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Airfield.

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

          name: The name of the airfield.

          source: Source of the data.

          type: The airfield activity use type (e.g. Commercial, Airport, Heliport, Gliderport,
              etc.).

          body_id: Unique identifier of the record, auto-generated by the system.

          alt_airfield_id: Alternate Airfield identifier provided by source.

          alternative_names: Alternative names for this airfield.

          city: The closest city to the location of this airfield.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL’s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          country_name: The country name where this airfield is located.

          dst_info: Information regarding daylight saving time as is relevant to the location and
              operation of this airfield.

          elev_ft: Elevation of the airfield above mean sea level, in feet. Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          elev_m: Elevation of the airfield above mean sea level, in meters. Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          faa: The Federal Aviation Administration (FAA) location identifier of this airfield.

          geoloc: Air Force geographic location code of the airfield.

          gmt_offset: Time difference between the location of the airfield and the Greenwich Mean Time
              (GMT), expressed as +/-HH:MM. Time zones east of Greenwich have positive offsets
              and time zones west of Greenwich are negative.

          host_nat_code: The host nation code of this airfield, used for non-DoD/FAA locations.

          iata: The International Aviation Transport Association (IATA) code of the airfield.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield.

          id_site: The ID of the parent site.

          info_url: The URL link to information about airfield.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          mag_dec: The magnetic declination/variation of the airfield's location from true north,
              in degrees. Positive values east of true north and negative values west of true
              north.

          max_runway_length: The length of the longest runway at this airfield in feet.

          misc_codes: Applicable miscellaneous codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          regional_authority: The regional authority of the airfield.

          region_name: Region where the airfield resides.

          runways: The number of runways at the site.

          secondary_icao: The secondary ICAO code for this airfield. Some airfields have two associated
              ICAO codes, this can occur in cases when a single airfield supports both
              military and civilian operations.

          state: State or province of the airfield's location.

          state_province_code: The code for the state or province in which this airfield is located. Intended
              as, but not constrained to, FIPS 10-4 region code designations.

          suitability_code_descs: Array of descriptions for given suitability codes. The index of the description
              corresponds to the position of the letter code in the string provided in the
              suitabilityCodes field.

          suitability_codes: Associated suitability codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          wac_innr: The airfield's World Area Code installation number (WAC-INNR).

          zar_id: Air Mobility Command (AMC) Zone availability Report identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airfield/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "alt_airfield_id": alt_airfield_id,
                    "alternative_names": alternative_names,
                    "city": city,
                    "country_code": country_code,
                    "country_name": country_name,
                    "dst_info": dst_info,
                    "elev_ft": elev_ft,
                    "elev_m": elev_m,
                    "faa": faa,
                    "geoloc": geoloc,
                    "gmt_offset": gmt_offset,
                    "host_nat_code": host_nat_code,
                    "iata": iata,
                    "icao": icao,
                    "id_site": id_site,
                    "info_url": info_url,
                    "lat": lat,
                    "lon": lon,
                    "mag_dec": mag_dec,
                    "max_runway_length": max_runway_length,
                    "misc_codes": misc_codes,
                    "origin": origin,
                    "regional_authority": regional_authority,
                    "region_name": region_name,
                    "runways": runways,
                    "secondary_icao": secondary_icao,
                    "state": state,
                    "state_province_code": state_province_code,
                    "suitability_code_descs": suitability_code_descs,
                    "suitability_codes": suitability_codes,
                    "wac_innr": wac_innr,
                    "zar_id": zar_id,
                },
                airfield_update_params.AirfieldUpdateParams,
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
    ) -> SyncOffsetPage[AirfieldAbridged]:
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
            "/udl/airfield",
            page=SyncOffsetPage[AirfieldAbridged],
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
                    airfield_list_params.AirfieldListParams,
                ),
            ),
            model=AirfieldAbridged,
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
            "/udl/airfield/count",
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
                    airfield_count_params.AirfieldCountParams,
                ),
            ),
            cast_to=str,
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
            "/udl/airfield/queryhelp",
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
    ) -> AirfieldTupleResponse:
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
            "/udl/airfield/tuple",
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
                    airfield_tuple_params.AirfieldTupleParams,
                ),
            ),
            cast_to=AirfieldTupleResponse,
        )


class AsyncAirfieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirfieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirfieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirfieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirfieldsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        alternative_names: List[str] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        dst_info: str | NotGiven = NOT_GIVEN,
        elev_ft: float | NotGiven = NOT_GIVEN,
        elev_m: float | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        geoloc: str | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        host_nat_code: str | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        info_url: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mag_dec: float | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        misc_codes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        regional_authority: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        secondary_icao: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        state_province_code: str | NotGiven = NOT_GIVEN,
        suitability_code_descs: List[str] | NotGiven = NOT_GIVEN,
        suitability_codes: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        zar_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Airfield as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          name: The name of the airfield.

          source: Source of the data.

          type: The airfield activity use type (e.g. Commercial, Airport, Heliport, Gliderport,
              etc.).

          id: Unique identifier of the record, auto-generated by the system.

          alt_airfield_id: Alternate Airfield identifier provided by source.

          alternative_names: Alternative names for this airfield.

          city: The closest city to the location of this airfield.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL’s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          country_name: The country name where this airfield is located.

          dst_info: Information regarding daylight saving time as is relevant to the location and
              operation of this airfield.

          elev_ft: Elevation of the airfield above mean sea level, in feet. Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          elev_m: Elevation of the airfield above mean sea level, in meters. Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          faa: The Federal Aviation Administration (FAA) location identifier of this airfield.

          geoloc: Air Force geographic location code of the airfield.

          gmt_offset: Time difference between the location of the airfield and the Greenwich Mean Time
              (GMT), expressed as +/-HH:MM. Time zones east of Greenwich have positive offsets
              and time zones west of Greenwich are negative.

          host_nat_code: The host nation code of this airfield, used for non-DoD/FAA locations.

          iata: The International Aviation Transport Association (IATA) code of the airfield.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield.

          id_site: The ID of the parent site.

          info_url: The URL link to information about airfield.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          mag_dec: The magnetic declination/variation of the airfield's location from true north,
              in degrees. Positive values east of true north and negative values west of true
              north.

          max_runway_length: The length of the longest runway at this airfield in feet.

          misc_codes: Applicable miscellaneous codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          regional_authority: The regional authority of the airfield.

          region_name: Region where the airfield resides.

          runways: The number of runways at the site.

          secondary_icao: The secondary ICAO code for this airfield. Some airfields have two associated
              ICAO codes, this can occur in cases when a single airfield supports both
              military and civilian operations.

          state: State or province of the airfield's location.

          state_province_code: The code for the state or province in which this airfield is located. Intended
              as, but not constrained to, FIPS 10-4 region code designations.

          suitability_code_descs: Array of descriptions for given suitability codes. The index of the description
              corresponds to the position of the letter code in the string provided in the
              suitabilityCodes field.

          suitability_codes: Associated suitability codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          wac_innr: The airfield's World Area Code installation number (WAC-INNR).

          zar_id: Air Mobility Command (AMC) Zone availability Report identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airfield",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "id": id,
                    "alt_airfield_id": alt_airfield_id,
                    "alternative_names": alternative_names,
                    "city": city,
                    "country_code": country_code,
                    "country_name": country_name,
                    "dst_info": dst_info,
                    "elev_ft": elev_ft,
                    "elev_m": elev_m,
                    "faa": faa,
                    "geoloc": geoloc,
                    "gmt_offset": gmt_offset,
                    "host_nat_code": host_nat_code,
                    "iata": iata,
                    "icao": icao,
                    "id_site": id_site,
                    "info_url": info_url,
                    "lat": lat,
                    "lon": lon,
                    "mag_dec": mag_dec,
                    "max_runway_length": max_runway_length,
                    "misc_codes": misc_codes,
                    "origin": origin,
                    "regional_authority": regional_authority,
                    "region_name": region_name,
                    "runways": runways,
                    "secondary_icao": secondary_icao,
                    "state": state,
                    "state_province_code": state_province_code,
                    "suitability_code_descs": suitability_code_descs,
                    "suitability_codes": suitability_codes,
                    "wac_innr": wac_innr,
                    "zar_id": zar_id,
                },
                airfield_create_params.AirfieldCreateParams,
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
    ) -> AirfieldFull:
        """
        Service operation to get a single Airfield by its unique ID passed as a path
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
            f"/udl/airfield/{id}",
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
                    airfield_retrieve_params.AirfieldRetrieveParams,
                ),
            ),
            cast_to=AirfieldFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        alternative_names: List[str] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        dst_info: str | NotGiven = NOT_GIVEN,
        elev_ft: float | NotGiven = NOT_GIVEN,
        elev_m: float | NotGiven = NOT_GIVEN,
        faa: str | NotGiven = NOT_GIVEN,
        geoloc: str | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        host_nat_code: str | NotGiven = NOT_GIVEN,
        iata: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        info_url: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mag_dec: float | NotGiven = NOT_GIVEN,
        max_runway_length: int | NotGiven = NOT_GIVEN,
        misc_codes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        regional_authority: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        runways: int | NotGiven = NOT_GIVEN,
        secondary_icao: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        state_province_code: str | NotGiven = NOT_GIVEN,
        suitability_code_descs: List[str] | NotGiven = NOT_GIVEN,
        suitability_codes: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        zar_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Airfield.

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

          name: The name of the airfield.

          source: Source of the data.

          type: The airfield activity use type (e.g. Commercial, Airport, Heliport, Gliderport,
              etc.).

          body_id: Unique identifier of the record, auto-generated by the system.

          alt_airfield_id: Alternate Airfield identifier provided by source.

          alternative_names: Alternative names for this airfield.

          city: The closest city to the location of this airfield.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL’s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          country_name: The country name where this airfield is located.

          dst_info: Information regarding daylight saving time as is relevant to the location and
              operation of this airfield.

          elev_ft: Elevation of the airfield above mean sea level, in feet. Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          elev_m: Elevation of the airfield above mean sea level, in meters. Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          faa: The Federal Aviation Administration (FAA) location identifier of this airfield.

          geoloc: Air Force geographic location code of the airfield.

          gmt_offset: Time difference between the location of the airfield and the Greenwich Mean Time
              (GMT), expressed as +/-HH:MM. Time zones east of Greenwich have positive offsets
              and time zones west of Greenwich are negative.

          host_nat_code: The host nation code of this airfield, used for non-DoD/FAA locations.

          iata: The International Aviation Transport Association (IATA) code of the airfield.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield.

          id_site: The ID of the parent site.

          info_url: The URL link to information about airfield.

          lat: WGS84 latitude of the location, in degrees. -90 to 90 degrees (negative values
              south of equator).

          lon: WGS84 longitude of the location, in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian).

          mag_dec: The magnetic declination/variation of the airfield's location from true north,
              in degrees. Positive values east of true north and negative values west of true
              north.

          max_runway_length: The length of the longest runway at this airfield in feet.

          misc_codes: Applicable miscellaneous codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          regional_authority: The regional authority of the airfield.

          region_name: Region where the airfield resides.

          runways: The number of runways at the site.

          secondary_icao: The secondary ICAO code for this airfield. Some airfields have two associated
              ICAO codes, this can occur in cases when a single airfield supports both
              military and civilian operations.

          state: State or province of the airfield's location.

          state_province_code: The code for the state or province in which this airfield is located. Intended
              as, but not constrained to, FIPS 10-4 region code designations.

          suitability_code_descs: Array of descriptions for given suitability codes. The index of the description
              corresponds to the position of the letter code in the string provided in the
              suitabilityCodes field.

          suitability_codes: Associated suitability codes according to the Airfield Suitability and
              Restrictions Report (ASRR) for this airfield.

          wac_innr: The airfield's World Area Code installation number (WAC-INNR).

          zar_id: Air Mobility Command (AMC) Zone availability Report identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airfield/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "alt_airfield_id": alt_airfield_id,
                    "alternative_names": alternative_names,
                    "city": city,
                    "country_code": country_code,
                    "country_name": country_name,
                    "dst_info": dst_info,
                    "elev_ft": elev_ft,
                    "elev_m": elev_m,
                    "faa": faa,
                    "geoloc": geoloc,
                    "gmt_offset": gmt_offset,
                    "host_nat_code": host_nat_code,
                    "iata": iata,
                    "icao": icao,
                    "id_site": id_site,
                    "info_url": info_url,
                    "lat": lat,
                    "lon": lon,
                    "mag_dec": mag_dec,
                    "max_runway_length": max_runway_length,
                    "misc_codes": misc_codes,
                    "origin": origin,
                    "regional_authority": regional_authority,
                    "region_name": region_name,
                    "runways": runways,
                    "secondary_icao": secondary_icao,
                    "state": state,
                    "state_province_code": state_province_code,
                    "suitability_code_descs": suitability_code_descs,
                    "suitability_codes": suitability_codes,
                    "wac_innr": wac_innr,
                    "zar_id": zar_id,
                },
                airfield_update_params.AirfieldUpdateParams,
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
    ) -> AsyncPaginator[AirfieldAbridged, AsyncOffsetPage[AirfieldAbridged]]:
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
            "/udl/airfield",
            page=AsyncOffsetPage[AirfieldAbridged],
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
                    airfield_list_params.AirfieldListParams,
                ),
            ),
            model=AirfieldAbridged,
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
            "/udl/airfield/count",
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
                    airfield_count_params.AirfieldCountParams,
                ),
            ),
            cast_to=str,
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
            "/udl/airfield/queryhelp",
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
    ) -> AirfieldTupleResponse:
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
            "/udl/airfield/tuple",
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
                    airfield_tuple_params.AirfieldTupleParams,
                ),
            ),
            cast_to=AirfieldTupleResponse,
        )


class AirfieldsResourceWithRawResponse:
    def __init__(self, airfields: AirfieldsResource) -> None:
        self._airfields = airfields

        self.create = to_raw_response_wrapper(
            airfields.create,
        )
        self.retrieve = to_raw_response_wrapper(
            airfields.retrieve,
        )
        self.update = to_raw_response_wrapper(
            airfields.update,
        )
        self.list = to_raw_response_wrapper(
            airfields.list,
        )
        self.count = to_raw_response_wrapper(
            airfields.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            airfields.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            airfields.tuple,
        )


class AsyncAirfieldsResourceWithRawResponse:
    def __init__(self, airfields: AsyncAirfieldsResource) -> None:
        self._airfields = airfields

        self.create = async_to_raw_response_wrapper(
            airfields.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            airfields.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            airfields.update,
        )
        self.list = async_to_raw_response_wrapper(
            airfields.list,
        )
        self.count = async_to_raw_response_wrapper(
            airfields.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            airfields.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            airfields.tuple,
        )


class AirfieldsResourceWithStreamingResponse:
    def __init__(self, airfields: AirfieldsResource) -> None:
        self._airfields = airfields

        self.create = to_streamed_response_wrapper(
            airfields.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            airfields.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            airfields.update,
        )
        self.list = to_streamed_response_wrapper(
            airfields.list,
        )
        self.count = to_streamed_response_wrapper(
            airfields.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            airfields.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            airfields.tuple,
        )


class AsyncAirfieldsResourceWithStreamingResponse:
    def __init__(self, airfields: AsyncAirfieldsResource) -> None:
        self._airfields = airfields

        self.create = async_to_streamed_response_wrapper(
            airfields.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            airfields.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            airfields.update,
        )
        self.list = async_to_streamed_response_wrapper(
            airfields.list,
        )
        self.count = async_to_streamed_response_wrapper(
            airfields.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            airfields.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            airfields.tuple,
        )
