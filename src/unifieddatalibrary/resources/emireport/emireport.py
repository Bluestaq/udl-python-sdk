# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    emireport_get_params,
    emireport_list_params,
    emireport_count_params,
    emireport_tuple_params,
    emireport_create_params,
    emireport_create_bulk_params,
    emireport_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.emireport_get_response import EmireportGetResponse
from ...types.emireport_list_response import EmireportListResponse
from ...types.emireport_tuple_response import EmireportTupleResponse
from ...types.emireport_queryhelp_response import EmireportQueryhelpResponse

__all__ = ["EmireportResource", "AsyncEmireportResource"]


class EmireportResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmireportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EmireportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmireportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EmireportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        isr: bool,
        report_id: str,
        report_time: Union[str, datetime],
        report_type: str,
        request_assist: bool,
        source: str,
        start_time: Union[str, datetime],
        id: str | Omit = omit,
        actions_taken: str | Omit = omit,
        aff_activity: str | Omit = omit,
        alt: float | Omit = omit,
        aor: str | Omit = omit,
        band: str | Omit = omit,
        beam_pattern: str | Omit = omit,
        channel: str | Omit = omit,
        chan_pirate: bool | Omit = omit,
        description: str | Omit = omit,
        dne_impact: str | Omit = omit,
        emi_type: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        frequency: float | Omit = omit,
        geo_loc_err_ellp: Iterable[float] | Omit = omit,
        gps_encrypted: bool | Omit = omit,
        gps_freq: str | Omit = omit,
        high_affected_frequency: float | Omit = omit,
        intercept: bool | Omit = omit,
        intercept_lang: str | Omit = omit,
        intercept_type: str | Omit = omit,
        int_src_amplitude: float | Omit = omit,
        int_src_bandwidth: float | Omit = omit,
        int_src_cent_freq: float | Omit = omit,
        int_src_encrypted: bool | Omit = omit,
        int_src_modulation: str | Omit = omit,
        isr_collection_impact: bool | Omit = omit,
        kill_box: str | Omit = omit,
        lat: float | Omit = omit,
        link: str | Omit = omit,
        lon: float | Omit = omit,
        mil_grid: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        persistence: str | Omit = omit,
        platform: str | Omit = omit,
        rcvr_demod: str | Omit = omit,
        rcvr_gain: float | Omit = omit,
        rcvr_location: str | Omit = omit,
        rcvr_type: str | Omit = omit,
        resp_service: str | Omit = omit,
        satcom_priority: str | Omit = omit,
        sat_downlink_frequency: float | Omit = omit,
        sat_downlink_polarization: str | Omit = omit,
        sat_name: str | Omit = omit,
        sat_no: int | Omit = omit,
        sat_transponder_id: str | Omit = omit,
        sat_uplink_frequency: float | Omit = omit,
        sat_uplink_polarization: str | Omit = omit,
        status: str | Omit = omit,
        supported_isr_role: str | Omit = omit,
        system: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        victim_alt_country: str | Omit = omit,
        victim_country_code: str | Omit = omit,
        victim_func_impacts: str | Omit = omit,
        victim_poc_mail: str | Omit = omit,
        victim_poc_name: str | Omit = omit,
        victim_poc_phone: str | Omit = omit,
        victim_poc_unit: str | Omit = omit,
        victim_reaction: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single EMIReport record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          isr: Flag indicating whether the affected mission is an ISR mission.

          report_id: User generated report identifier. This ID should remain the same on subsequent
              updates to this report.

          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision.

          report_type: The type of Electromagnetic Interference (EMI) being reported (GPS, SATCOM,
              TERRESTRIAL).

          request_assist: Flag indicating whether assistance is being requested to address this EMI.

          source: Source of the data.

          start_time: The EMI start time in ISO 8601 UTC format, with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          actions_taken: Actions(s) taken to troubleshoot, mitigate, work-around, and/or resolve the EMI
              impacts.

          aff_activity: The specific type of activity affected by the reported EMI (e.g. UPLINK,
              DOWNLINK, HF COMM, etc.).

          alt: Altitude of the affected receiver, expressed in meters above WGS-84 ellipsoid.

          aor: The Area Of Responsibility (AOR), Organization, or Combatant Command under which
              the reported EMI pertains (AFRICOM, CENTCOM, EUCOM, INDOPACOM, NORTHCOM, SOCOM,
              SOUTHCOM, SPACECOM, STRATCOM, TRANSCOM, UNKNOWN).

          band: The band (EHF, SHF, UHF, etc.) affected by the EMI.

          beam_pattern: The beam pattern in use.

          channel: The channel affected by the EMI.

          chan_pirate: Flag indicating whether this interference appears to be illegally passing
              traffic over a known channel.

          description: Text description of the EMI particulars and other supporting information which
              may be relevant to the cause and/or possible resolution of the issue.

          dne_impact: Duration, Nature, Extent of impact.

          emi_type: The type of EMI (i.e. BARRAGE, CARRIER WAVE, etc.), if known.

          end_time: The EMI end time in ISO 8601 UTC format, with millisecond precision. The endTime
              may be excluded if EMI is ongoing.

          frequency: The affected frequency, in MHz.

          geo_loc_err_ellp: Confidence ellipse centered about the detection location [semi-major axis (m),
              semi-minor axis (m), orientation (deg) measured clockwise (0 - 360) from true
              North].

          gps_encrypted: Flag indicating whether encryption is in use on the affected GPS frequency.

          gps_freq: The affected GPS Frequency (L1, L2, etc.).

          high_affected_frequency: The highest affected frequency, in MHz.

          intercept: Flag indicating whether the EMI is a decipherable intercept over the affected
              receiver. Additional information may be included in the description field
              content of this record.

          intercept_lang: The language heard over the intercepted source. Applicable when interceptType =
              VOICE.

          intercept_type: The type of transmission being intercepted (e.g. VOICE, etc.). Applicable when
              intercept = TRUE.

          int_src_amplitude: The relative amplitude, in decibels (dB), of the interfering source, if known.

          int_src_bandwidth: The bandwidth, in MHz, of the interfering source, if known.

          int_src_cent_freq: The center frequency, in MHz, of the interfering source, if known.

          int_src_encrypted: Flag indicating whether the interfering source is encrypted.

          int_src_modulation: The modulation method (e.g. AM, FM, FSK, PSK, etc.) of the interfering source,
              if known.

          isr_collection_impact: Flag indicating whether this EMI is impacting ISR collection.

          kill_box: The location of the affected receiver, reported as a kill box.

          lat: WGS-84 latitude of the affected receiver, represented as -90 to 90 degrees
              (negative values south of equator).

          link: The name or identifier of the affected link.

          lon: WGS-84 longitude of the affected receiver, represented as -180 to 180 degrees
              (negative values west of Prime Meridian).

          mil_grid: The Military Grid Reference System (MGRS) location of the affected receiver. The
              Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of a milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              4Q (grid zone designator, GZD) FJ (the 100,000-meter square identifier) 12345678
              (numerical location; easting is 1234 and northing is 5678, in this case
              specifying a location with 10 m resolution).

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the reporting source to indicate the affected
              object of this report. This may be an internal identifier and not necessarily
              map to a valid satellite number.

          persistence: The persistence status (e.g. CONTINUOUS, INTERMITTENT, RANDOM, etc.) of the EMI.

          platform: The name or identifier of the affected platform.

          rcvr_demod: The demodulation method (e.g. AM, FM, FSK, PSK, etc.) setting of the affected
              receiver.

          rcvr_gain: The gain setting of the affected receiver, in decibels (dB).

          rcvr_location: Description of the affected receiver location.

          rcvr_type: The affected antenna type (e.g. DISH, OMNI, PHASED ARRAY, etc.) experiencing the
              EMI.

          resp_service: The responsible service branch under which this EMI falls (AIR FORCE, ARMY,
              COAST GUARD, MARINES, NAVY).

          satcom_priority: The priority (LOW, MEDIUM, HIGH) of the affected SATCOM.

          sat_downlink_frequency: The downlink frequency, in MHz, of the impacted link.

          sat_downlink_polarization: The downlink polarization e.g. H - (Horizontally Polarized), V - (Vertically
              Polarized), L - (Left Hand Circularly Polarized), R - (Right Hand Circularly
              Polarized).

          sat_name: The name of the spacecraft whose link is being affected by the EMI.

          sat_no: Satellite/Catalog number of the affected OnOrbit object.

          sat_transponder_id: The name or identifier of the affected sat transponder.

          sat_uplink_frequency: The uplink frequency, in MHz, of the impacted link.

          sat_uplink_polarization: The uplink polarization e.g. H - (Horizontally Polarized), V - (Vertically
              Polarized), L - (Left Hand Circularly Polarized), R - (Right Hand Circularly
              Polarized).

          status: The reporting status (INITIAL, UPDATE, RESOLVED) of this EMI issue.

          supported_isr_role: The ISR role of the impacted asset.

          system: The name or identifier of the affected system.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          victim_alt_country: The alternate country identifier in which the EMI occurred or is occurring.
              Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS.

          victim_country_code: The country code in which the EMI occurred or is occurring. This value is
              typically the ISO 3166 Alpha-2 two-character country code, however it can also
              represent various consortiums that do not appear in the ISO document. The code
              must correspond to an existing country in the UDL’s country API. Call
              udl/country/{code} to get any associated FIPS code, ISO Alpha-3 code, or
              alternate code values that exist for the specified country code.

          victim_func_impacts: The victim functional impacts (e.g. C2, COMM DATA LINK, ISR SENSOR, PNT, etc.).

          victim_poc_mail: The e-mail contact of the reporting POC.

          victim_poc_name: The Point of Contact (POC) for this EMI Report.

          victim_poc_phone: The phone number of the reporting POC, represented as digits only, no spaces or
              special characters.

          victim_poc_unit: The Unit or Organization of the reporting POC.

          victim_reaction: The victim reaction (e.g. LOITER ORBIT, RETASK ASSET, RETURN TO BASE,
              TROUBLESHOOT, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/emireport",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "isr": isr,
                    "report_id": report_id,
                    "report_time": report_time,
                    "report_type": report_type,
                    "request_assist": request_assist,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "actions_taken": actions_taken,
                    "aff_activity": aff_activity,
                    "alt": alt,
                    "aor": aor,
                    "band": band,
                    "beam_pattern": beam_pattern,
                    "channel": channel,
                    "chan_pirate": chan_pirate,
                    "description": description,
                    "dne_impact": dne_impact,
                    "emi_type": emi_type,
                    "end_time": end_time,
                    "frequency": frequency,
                    "geo_loc_err_ellp": geo_loc_err_ellp,
                    "gps_encrypted": gps_encrypted,
                    "gps_freq": gps_freq,
                    "high_affected_frequency": high_affected_frequency,
                    "intercept": intercept,
                    "intercept_lang": intercept_lang,
                    "intercept_type": intercept_type,
                    "int_src_amplitude": int_src_amplitude,
                    "int_src_bandwidth": int_src_bandwidth,
                    "int_src_cent_freq": int_src_cent_freq,
                    "int_src_encrypted": int_src_encrypted,
                    "int_src_modulation": int_src_modulation,
                    "isr_collection_impact": isr_collection_impact,
                    "kill_box": kill_box,
                    "lat": lat,
                    "link": link,
                    "lon": lon,
                    "mil_grid": mil_grid,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "persistence": persistence,
                    "platform": platform,
                    "rcvr_demod": rcvr_demod,
                    "rcvr_gain": rcvr_gain,
                    "rcvr_location": rcvr_location,
                    "rcvr_type": rcvr_type,
                    "resp_service": resp_service,
                    "satcom_priority": satcom_priority,
                    "sat_downlink_frequency": sat_downlink_frequency,
                    "sat_downlink_polarization": sat_downlink_polarization,
                    "sat_name": sat_name,
                    "sat_no": sat_no,
                    "sat_transponder_id": sat_transponder_id,
                    "sat_uplink_frequency": sat_uplink_frequency,
                    "sat_uplink_polarization": sat_uplink_polarization,
                    "status": status,
                    "supported_isr_role": supported_isr_role,
                    "system": system,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "victim_alt_country": victim_alt_country,
                    "victim_country_code": victim_country_code,
                    "victim_func_impacts": victim_func_impacts,
                    "victim_poc_mail": victim_poc_mail,
                    "victim_poc_name": victim_poc_name,
                    "victim_poc_phone": victim_poc_phone,
                    "victim_poc_unit": victim_poc_unit,
                    "victim_reaction": victim_reaction,
                },
                emireport_create_params.EmireportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        report_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[EmireportListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/emireport",
            page=SyncOffsetPage[EmireportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_time": report_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emireport_list_params.EmireportListParams,
                ),
            ),
            model=EmireportListResponse,
        )

    def count(
        self,
        *,
        report_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
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
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/emireport/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_time": report_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emireport_count_params.EmireportCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[emireport_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        EMIReport records as a POST body and ingest into the database. This operation is
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
            "/udl/emireport/createBulk",
            body=maybe_transform(body, Iterable[emireport_create_bulk_params.Body]),
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
    ) -> EmireportGetResponse:
        """
        Service operation to get a single EMIReport record by its unique ID passed as a
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
            f"/udl/emireport/{id}",
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
                    emireport_get_params.EmireportGetParams,
                ),
            ),
            cast_to=EmireportGetResponse,
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
    ) -> EmireportQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/emireport/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmireportQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        report_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmireportTupleResponse:
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

          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/emireport/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "report_time": report_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emireport_tuple_params.EmireportTupleParams,
                ),
            ),
            cast_to=EmireportTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[emireport_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple EMIReport records as a POST body and ingest
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
            "/filedrop/udl-emireport",
            body=maybe_transform(body, Iterable[emireport_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmireportResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmireportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEmireportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmireportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEmireportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        isr: bool,
        report_id: str,
        report_time: Union[str, datetime],
        report_type: str,
        request_assist: bool,
        source: str,
        start_time: Union[str, datetime],
        id: str | Omit = omit,
        actions_taken: str | Omit = omit,
        aff_activity: str | Omit = omit,
        alt: float | Omit = omit,
        aor: str | Omit = omit,
        band: str | Omit = omit,
        beam_pattern: str | Omit = omit,
        channel: str | Omit = omit,
        chan_pirate: bool | Omit = omit,
        description: str | Omit = omit,
        dne_impact: str | Omit = omit,
        emi_type: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        frequency: float | Omit = omit,
        geo_loc_err_ellp: Iterable[float] | Omit = omit,
        gps_encrypted: bool | Omit = omit,
        gps_freq: str | Omit = omit,
        high_affected_frequency: float | Omit = omit,
        intercept: bool | Omit = omit,
        intercept_lang: str | Omit = omit,
        intercept_type: str | Omit = omit,
        int_src_amplitude: float | Omit = omit,
        int_src_bandwidth: float | Omit = omit,
        int_src_cent_freq: float | Omit = omit,
        int_src_encrypted: bool | Omit = omit,
        int_src_modulation: str | Omit = omit,
        isr_collection_impact: bool | Omit = omit,
        kill_box: str | Omit = omit,
        lat: float | Omit = omit,
        link: str | Omit = omit,
        lon: float | Omit = omit,
        mil_grid: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        persistence: str | Omit = omit,
        platform: str | Omit = omit,
        rcvr_demod: str | Omit = omit,
        rcvr_gain: float | Omit = omit,
        rcvr_location: str | Omit = omit,
        rcvr_type: str | Omit = omit,
        resp_service: str | Omit = omit,
        satcom_priority: str | Omit = omit,
        sat_downlink_frequency: float | Omit = omit,
        sat_downlink_polarization: str | Omit = omit,
        sat_name: str | Omit = omit,
        sat_no: int | Omit = omit,
        sat_transponder_id: str | Omit = omit,
        sat_uplink_frequency: float | Omit = omit,
        sat_uplink_polarization: str | Omit = omit,
        status: str | Omit = omit,
        supported_isr_role: str | Omit = omit,
        system: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        victim_alt_country: str | Omit = omit,
        victim_country_code: str | Omit = omit,
        victim_func_impacts: str | Omit = omit,
        victim_poc_mail: str | Omit = omit,
        victim_poc_name: str | Omit = omit,
        victim_poc_phone: str | Omit = omit,
        victim_poc_unit: str | Omit = omit,
        victim_reaction: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single EMIReport record as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          isr: Flag indicating whether the affected mission is an ISR mission.

          report_id: User generated report identifier. This ID should remain the same on subsequent
              updates to this report.

          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision.

          report_type: The type of Electromagnetic Interference (EMI) being reported (GPS, SATCOM,
              TERRESTRIAL).

          request_assist: Flag indicating whether assistance is being requested to address this EMI.

          source: Source of the data.

          start_time: The EMI start time in ISO 8601 UTC format, with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          actions_taken: Actions(s) taken to troubleshoot, mitigate, work-around, and/or resolve the EMI
              impacts.

          aff_activity: The specific type of activity affected by the reported EMI (e.g. UPLINK,
              DOWNLINK, HF COMM, etc.).

          alt: Altitude of the affected receiver, expressed in meters above WGS-84 ellipsoid.

          aor: The Area Of Responsibility (AOR), Organization, or Combatant Command under which
              the reported EMI pertains (AFRICOM, CENTCOM, EUCOM, INDOPACOM, NORTHCOM, SOCOM,
              SOUTHCOM, SPACECOM, STRATCOM, TRANSCOM, UNKNOWN).

          band: The band (EHF, SHF, UHF, etc.) affected by the EMI.

          beam_pattern: The beam pattern in use.

          channel: The channel affected by the EMI.

          chan_pirate: Flag indicating whether this interference appears to be illegally passing
              traffic over a known channel.

          description: Text description of the EMI particulars and other supporting information which
              may be relevant to the cause and/or possible resolution of the issue.

          dne_impact: Duration, Nature, Extent of impact.

          emi_type: The type of EMI (i.e. BARRAGE, CARRIER WAVE, etc.), if known.

          end_time: The EMI end time in ISO 8601 UTC format, with millisecond precision. The endTime
              may be excluded if EMI is ongoing.

          frequency: The affected frequency, in MHz.

          geo_loc_err_ellp: Confidence ellipse centered about the detection location [semi-major axis (m),
              semi-minor axis (m), orientation (deg) measured clockwise (0 - 360) from true
              North].

          gps_encrypted: Flag indicating whether encryption is in use on the affected GPS frequency.

          gps_freq: The affected GPS Frequency (L1, L2, etc.).

          high_affected_frequency: The highest affected frequency, in MHz.

          intercept: Flag indicating whether the EMI is a decipherable intercept over the affected
              receiver. Additional information may be included in the description field
              content of this record.

          intercept_lang: The language heard over the intercepted source. Applicable when interceptType =
              VOICE.

          intercept_type: The type of transmission being intercepted (e.g. VOICE, etc.). Applicable when
              intercept = TRUE.

          int_src_amplitude: The relative amplitude, in decibels (dB), of the interfering source, if known.

          int_src_bandwidth: The bandwidth, in MHz, of the interfering source, if known.

          int_src_cent_freq: The center frequency, in MHz, of the interfering source, if known.

          int_src_encrypted: Flag indicating whether the interfering source is encrypted.

          int_src_modulation: The modulation method (e.g. AM, FM, FSK, PSK, etc.) of the interfering source,
              if known.

          isr_collection_impact: Flag indicating whether this EMI is impacting ISR collection.

          kill_box: The location of the affected receiver, reported as a kill box.

          lat: WGS-84 latitude of the affected receiver, represented as -90 to 90 degrees
              (negative values south of equator).

          link: The name or identifier of the affected link.

          lon: WGS-84 longitude of the affected receiver, represented as -180 to 180 degrees
              (negative values west of Prime Meridian).

          mil_grid: The Military Grid Reference System (MGRS) location of the affected receiver. The
              Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of a milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              4Q (grid zone designator, GZD) FJ (the 100,000-meter square identifier) 12345678
              (numerical location; easting is 1234 and northing is 5678, in this case
              specifying a location with 10 m resolution).

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the reporting source to indicate the affected
              object of this report. This may be an internal identifier and not necessarily
              map to a valid satellite number.

          persistence: The persistence status (e.g. CONTINUOUS, INTERMITTENT, RANDOM, etc.) of the EMI.

          platform: The name or identifier of the affected platform.

          rcvr_demod: The demodulation method (e.g. AM, FM, FSK, PSK, etc.) setting of the affected
              receiver.

          rcvr_gain: The gain setting of the affected receiver, in decibels (dB).

          rcvr_location: Description of the affected receiver location.

          rcvr_type: The affected antenna type (e.g. DISH, OMNI, PHASED ARRAY, etc.) experiencing the
              EMI.

          resp_service: The responsible service branch under which this EMI falls (AIR FORCE, ARMY,
              COAST GUARD, MARINES, NAVY).

          satcom_priority: The priority (LOW, MEDIUM, HIGH) of the affected SATCOM.

          sat_downlink_frequency: The downlink frequency, in MHz, of the impacted link.

          sat_downlink_polarization: The downlink polarization e.g. H - (Horizontally Polarized), V - (Vertically
              Polarized), L - (Left Hand Circularly Polarized), R - (Right Hand Circularly
              Polarized).

          sat_name: The name of the spacecraft whose link is being affected by the EMI.

          sat_no: Satellite/Catalog number of the affected OnOrbit object.

          sat_transponder_id: The name or identifier of the affected sat transponder.

          sat_uplink_frequency: The uplink frequency, in MHz, of the impacted link.

          sat_uplink_polarization: The uplink polarization e.g. H - (Horizontally Polarized), V - (Vertically
              Polarized), L - (Left Hand Circularly Polarized), R - (Right Hand Circularly
              Polarized).

          status: The reporting status (INITIAL, UPDATE, RESOLVED) of this EMI issue.

          supported_isr_role: The ISR role of the impacted asset.

          system: The name or identifier of the affected system.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          victim_alt_country: The alternate country identifier in which the EMI occurred or is occurring.
              Specifies an alternate country code if the data provider code is not part of an
              official Country Code standard such as ISO-3166 or FIPS.

          victim_country_code: The country code in which the EMI occurred or is occurring. This value is
              typically the ISO 3166 Alpha-2 two-character country code, however it can also
              represent various consortiums that do not appear in the ISO document. The code
              must correspond to an existing country in the UDL’s country API. Call
              udl/country/{code} to get any associated FIPS code, ISO Alpha-3 code, or
              alternate code values that exist for the specified country code.

          victim_func_impacts: The victim functional impacts (e.g. C2, COMM DATA LINK, ISR SENSOR, PNT, etc.).

          victim_poc_mail: The e-mail contact of the reporting POC.

          victim_poc_name: The Point of Contact (POC) for this EMI Report.

          victim_poc_phone: The phone number of the reporting POC, represented as digits only, no spaces or
              special characters.

          victim_poc_unit: The Unit or Organization of the reporting POC.

          victim_reaction: The victim reaction (e.g. LOITER ORBIT, RETASK ASSET, RETURN TO BASE,
              TROUBLESHOOT, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/emireport",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "isr": isr,
                    "report_id": report_id,
                    "report_time": report_time,
                    "report_type": report_type,
                    "request_assist": request_assist,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "actions_taken": actions_taken,
                    "aff_activity": aff_activity,
                    "alt": alt,
                    "aor": aor,
                    "band": band,
                    "beam_pattern": beam_pattern,
                    "channel": channel,
                    "chan_pirate": chan_pirate,
                    "description": description,
                    "dne_impact": dne_impact,
                    "emi_type": emi_type,
                    "end_time": end_time,
                    "frequency": frequency,
                    "geo_loc_err_ellp": geo_loc_err_ellp,
                    "gps_encrypted": gps_encrypted,
                    "gps_freq": gps_freq,
                    "high_affected_frequency": high_affected_frequency,
                    "intercept": intercept,
                    "intercept_lang": intercept_lang,
                    "intercept_type": intercept_type,
                    "int_src_amplitude": int_src_amplitude,
                    "int_src_bandwidth": int_src_bandwidth,
                    "int_src_cent_freq": int_src_cent_freq,
                    "int_src_encrypted": int_src_encrypted,
                    "int_src_modulation": int_src_modulation,
                    "isr_collection_impact": isr_collection_impact,
                    "kill_box": kill_box,
                    "lat": lat,
                    "link": link,
                    "lon": lon,
                    "mil_grid": mil_grid,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "persistence": persistence,
                    "platform": platform,
                    "rcvr_demod": rcvr_demod,
                    "rcvr_gain": rcvr_gain,
                    "rcvr_location": rcvr_location,
                    "rcvr_type": rcvr_type,
                    "resp_service": resp_service,
                    "satcom_priority": satcom_priority,
                    "sat_downlink_frequency": sat_downlink_frequency,
                    "sat_downlink_polarization": sat_downlink_polarization,
                    "sat_name": sat_name,
                    "sat_no": sat_no,
                    "sat_transponder_id": sat_transponder_id,
                    "sat_uplink_frequency": sat_uplink_frequency,
                    "sat_uplink_polarization": sat_uplink_polarization,
                    "status": status,
                    "supported_isr_role": supported_isr_role,
                    "system": system,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "victim_alt_country": victim_alt_country,
                    "victim_country_code": victim_country_code,
                    "victim_func_impacts": victim_func_impacts,
                    "victim_poc_mail": victim_poc_mail,
                    "victim_poc_name": victim_poc_name,
                    "victim_poc_phone": victim_poc_phone,
                    "victim_poc_unit": victim_poc_unit,
                    "victim_reaction": victim_reaction,
                },
                emireport_create_params.EmireportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        report_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmireportListResponse, AsyncOffsetPage[EmireportListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/emireport",
            page=AsyncOffsetPage[EmireportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_time": report_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emireport_list_params.EmireportListParams,
                ),
            ),
            model=EmireportListResponse,
        )

    async def count(
        self,
        *,
        report_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
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
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/emireport/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_time": report_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emireport_count_params.EmireportCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[emireport_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        EMIReport records as a POST body and ingest into the database. This operation is
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
            "/udl/emireport/createBulk",
            body=await async_maybe_transform(body, Iterable[emireport_create_bulk_params.Body]),
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
    ) -> EmireportGetResponse:
        """
        Service operation to get a single EMIReport record by its unique ID passed as a
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
            f"/udl/emireport/{id}",
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
                    emireport_get_params.EmireportGetParams,
                ),
            ),
            cast_to=EmireportGetResponse,
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
    ) -> EmireportQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/emireport/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmireportQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        report_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmireportTupleResponse:
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

          report_time: The reporting time of this EMI Report record, in ISO 8601 UTC format, with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/emireport/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "report_time": report_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emireport_tuple_params.EmireportTupleParams,
                ),
            ),
            cast_to=EmireportTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[emireport_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple EMIReport records as a POST body and ingest
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
            "/filedrop/udl-emireport",
            body=await async_maybe_transform(body, Iterable[emireport_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmireportResourceWithRawResponse:
    def __init__(self, emireport: EmireportResource) -> None:
        self._emireport = emireport

        self.create = to_raw_response_wrapper(
            emireport.create,
        )
        self.list = to_raw_response_wrapper(
            emireport.list,
        )
        self.count = to_raw_response_wrapper(
            emireport.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            emireport.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            emireport.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            emireport.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            emireport.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            emireport.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._emireport.history)


class AsyncEmireportResourceWithRawResponse:
    def __init__(self, emireport: AsyncEmireportResource) -> None:
        self._emireport = emireport

        self.create = async_to_raw_response_wrapper(
            emireport.create,
        )
        self.list = async_to_raw_response_wrapper(
            emireport.list,
        )
        self.count = async_to_raw_response_wrapper(
            emireport.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            emireport.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            emireport.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            emireport.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            emireport.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            emireport.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._emireport.history)


class EmireportResourceWithStreamingResponse:
    def __init__(self, emireport: EmireportResource) -> None:
        self._emireport = emireport

        self.create = to_streamed_response_wrapper(
            emireport.create,
        )
        self.list = to_streamed_response_wrapper(
            emireport.list,
        )
        self.count = to_streamed_response_wrapper(
            emireport.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            emireport.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            emireport.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            emireport.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            emireport.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            emireport.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._emireport.history)


class AsyncEmireportResourceWithStreamingResponse:
    def __init__(self, emireport: AsyncEmireportResource) -> None:
        self._emireport = emireport

        self.create = async_to_streamed_response_wrapper(
            emireport.create,
        )
        self.list = async_to_streamed_response_wrapper(
            emireport.list,
        )
        self.count = async_to_streamed_response_wrapper(
            emireport.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            emireport.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            emireport.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            emireport.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            emireport.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            emireport.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._emireport.history)
