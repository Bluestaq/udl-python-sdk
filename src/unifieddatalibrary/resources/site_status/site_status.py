# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    site_status_get_params,
    site_status_list_params,
    site_status_count_params,
    site_status_tuple_params,
    site_status_create_params,
    site_status_update_params,
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
from ...types.site_status_get_response import SiteStatusGetResponse
from ...types.site_status_list_response import SiteStatusListResponse
from ...types.site_status_tuple_response import SiteStatusTupleResponse

__all__ = ["SiteStatusResource", "AsyncSiteStatusResource"]


class SiteStatusResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SiteStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SiteStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiteStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SiteStatusResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_site: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        cat: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        cold_inventory: int | NotGiven = NOT_GIVEN,
        comm_impairment: str | NotGiven = NOT_GIVEN,
        cpcon: Literal["1", "2", "3", "4", "5"] | NotGiven = NOT_GIVEN,
        eoc: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        fpcon: Literal["NORMAL", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        hot_inventory: int | NotGiven = NOT_GIVEN,
        hpcon: Literal["0", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        inst_status: Literal["FMC", "PMC", "NMC", "UNK"] | NotGiven = NOT_GIVEN,
        link: List[str] | NotGiven = NOT_GIVEN,
        link_status: List[str] | NotGiven = NOT_GIVEN,
        missile: List[str] | NotGiven = NOT_GIVEN,
        missile_inventory: Iterable[int] | NotGiven = NOT_GIVEN,
        mobile_alt_id: str | NotGiven = NOT_GIVEN,
        ops_capability: str | NotGiven = NOT_GIVEN,
        ops_impairment: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pes: bool | NotGiven = NOT_GIVEN,
        poiid: str | NotGiven = NOT_GIVEN,
        radar_status: List[str] | NotGiven = NOT_GIVEN,
        radar_system: List[str] | NotGiven = NOT_GIVEN,
        radiate_mode: str | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sam_mode: str | NotGiven = NOT_GIVEN,
        site_type: str | NotGiven = NOT_GIVEN,
        time_function: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_ref_l16: str | NotGiven = NOT_GIVEN,
        weather_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SiteStatus object as a POST body and ingest
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

          id_site: The ID of the site, if this status is associated with a fixed site or platform.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          cat: Crisis Action Team (CAT).

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          cold_inventory: Estimated number of cold missiles of all types remaining in weapons system
              inventory.

          comm_impairment: The communications component causing the platform or system to be less than
              fully operational.

          cpcon: Cyberspace Protection Condition (CPCON).

              1 - VERY HIGH - Critical functions.

              2 - HIGH - Critical and essential functions.

              3 - MEDIUM - Critical, essential, and support functions.

              4 - LOW - All functions.

              5 - VERY LOW - All functions.

          eoc: Emergency Operations Center (EOC) status.

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          fpcon: Force Protection Condition (FPCON).

              NORMAL - Applies when a general global threat of possible terrorist activity
              exists and warrants a routine security posture.

              ALPHA - Applies when an increased general threat of possible terrorist activity
              against personnel or facilities. Nature and extent of threat are unpredictable.

              BRAVO - Applies when an increased or predictable threat of terrorist activity
              exists.

              CHARLIE - Applies when an incident occurs or intelligence is received indicating
              some form of terrorist action against personnel and facilities is imminent.

              DELTA - Applies in the immediate area where an attack has occurred or when
              intelligence is received indicating terrorist action against a location is
              imminent.

          hot_inventory: Estimated number of hot missiles of all types remaining in weapons system
              inventory.

          hpcon: Health Protection Condition (HPCON).

              0 - Routine, no community transmission.

              ALPHA - Limited, community transmission beginning.

              BRAVO - Moderate, increased community transmission.

              CHARLIE - Substantial, sustained community transmission.

              DELTA - Severe, widespread community transmission.

          inst_status: The status of the installation.

              FMC - Fully Mission Capable

              PMC - Partially Mission Capable

              NMC - Non Mission Capable

              UNK - Unknown.

          link: Array of Link item(s) for which status is available and reported (ATDL, IJMS,
              LINK-1, LINK-11, LINK-11B, LINK-16). This array must be the same length as the
              linkStatus array.

          link_status: Array of the status (AVAILABLE, DEGRADED, NOT AVAILABLE, etc.) for each links in
              the link array. This array must be the same length as the link array, and the
              status must correspond to the appropriate position index in the link array.

          missile: Array of specific missile types for which an estimated inventory count is
              available (e.g. GMD TYPE A, HARPOON, TOMAHAWK, etc.). This array must be the
              same length as the missileInventory array.

          missile_inventory: Array of the quantity of each of the missile items. This array must be the same
              length as the missile array, and the values must correspond to appropriate
              position index in the missile array.

          mobile_alt_id: Alternate Identifier for a mobile or transportable platform provided by source.

          ops_capability: The operational status of the platform (e.g. Fully Operational, Partially
              Operational, Not Operational, etc.).

          ops_impairment: The primary component degrading the operational capability of the platform or
              system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pes: Position Engagement Status flag, Indicating whether this platform is initiating
              multiple simultaneous engagements. A value of 1/True indicates the platform is
              initiating multiple simultaneous engagements.

          poiid: The POI (point of interest) ID related to this platform, if available.

          radar_status: Array of the status (NON-OPERATIONAL, OPERATIONAL, OFF) for each radar system in
              the radarSystem array. This array must be the same length as the radarSystem
              array, and the status must correspond to the appropriate position index in the
              radarSystem array.

          radar_system: Array of radar system(s) for which status is available and reported
              (ACQUISITION, IFFSIF, ILLUMINATING, MODE-4, PRIMARY SURVEILLANCE, SECONDARY
              SURVEILLANCE, TERTIARY SURVEILLANCE). This array must be the same length as the
              radarStatus array.

          radiate_mode: SAM sensor radar surveillance mode (Active, Passive, Off).

          report_time: Time of report, in ISO8601 UTC format.

          sam_mode: The state of a SAM unit (e.g. Initialization, Standby, Reorientation, etc.).

          site_type: Optional site type or further detail of type. Intended for, but not limited to,
              Link-16 site type specifications (e.g. ADOC, GACC, SOC, TACC, etc.).

          time_function: Description of the time function associated with the reportTime (e.g.
              Activation, Deactivation, Arrival, Departure, etc.), if applicable.

          track_id: The track ID related to this platform (if mobile or transportable), if
              available.

          track_ref_l16: Link-16 specific reference track number.

          weather_message: Description of the current weather conditions over a site.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/sitestatus",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_site": id_site,
                    "source": source,
                    "id": id,
                    "cat": cat,
                    "cold_inventory": cold_inventory,
                    "comm_impairment": comm_impairment,
                    "cpcon": cpcon,
                    "eoc": eoc,
                    "fpcon": fpcon,
                    "hot_inventory": hot_inventory,
                    "hpcon": hpcon,
                    "inst_status": inst_status,
                    "link": link,
                    "link_status": link_status,
                    "missile": missile,
                    "missile_inventory": missile_inventory,
                    "mobile_alt_id": mobile_alt_id,
                    "ops_capability": ops_capability,
                    "ops_impairment": ops_impairment,
                    "origin": origin,
                    "pes": pes,
                    "poiid": poiid,
                    "radar_status": radar_status,
                    "radar_system": radar_system,
                    "radiate_mode": radiate_mode,
                    "report_time": report_time,
                    "sam_mode": sam_mode,
                    "site_type": site_type,
                    "time_function": time_function,
                    "track_id": track_id,
                    "track_ref_l16": track_ref_l16,
                    "weather_message": weather_message,
                },
                site_status_create_params.SiteStatusCreateParams,
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
        id_site: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        cat: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        cold_inventory: int | NotGiven = NOT_GIVEN,
        comm_impairment: str | NotGiven = NOT_GIVEN,
        cpcon: Literal["1", "2", "3", "4", "5"] | NotGiven = NOT_GIVEN,
        eoc: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        fpcon: Literal["NORMAL", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        hot_inventory: int | NotGiven = NOT_GIVEN,
        hpcon: Literal["0", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        inst_status: Literal["FMC", "PMC", "NMC", "UNK"] | NotGiven = NOT_GIVEN,
        link: List[str] | NotGiven = NOT_GIVEN,
        link_status: List[str] | NotGiven = NOT_GIVEN,
        missile: List[str] | NotGiven = NOT_GIVEN,
        missile_inventory: Iterable[int] | NotGiven = NOT_GIVEN,
        mobile_alt_id: str | NotGiven = NOT_GIVEN,
        ops_capability: str | NotGiven = NOT_GIVEN,
        ops_impairment: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pes: bool | NotGiven = NOT_GIVEN,
        poiid: str | NotGiven = NOT_GIVEN,
        radar_status: List[str] | NotGiven = NOT_GIVEN,
        radar_system: List[str] | NotGiven = NOT_GIVEN,
        radiate_mode: str | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sam_mode: str | NotGiven = NOT_GIVEN,
        site_type: str | NotGiven = NOT_GIVEN,
        time_function: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_ref_l16: str | NotGiven = NOT_GIVEN,
        weather_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single SiteStatus object.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

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

          id_site: The ID of the site, if this status is associated with a fixed site or platform.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          cat: Crisis Action Team (CAT).

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          cold_inventory: Estimated number of cold missiles of all types remaining in weapons system
              inventory.

          comm_impairment: The communications component causing the platform or system to be less than
              fully operational.

          cpcon: Cyberspace Protection Condition (CPCON).

              1 - VERY HIGH - Critical functions.

              2 - HIGH - Critical and essential functions.

              3 - MEDIUM - Critical, essential, and support functions.

              4 - LOW - All functions.

              5 - VERY LOW - All functions.

          eoc: Emergency Operations Center (EOC) status.

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          fpcon: Force Protection Condition (FPCON).

              NORMAL - Applies when a general global threat of possible terrorist activity
              exists and warrants a routine security posture.

              ALPHA - Applies when an increased general threat of possible terrorist activity
              against personnel or facilities. Nature and extent of threat are unpredictable.

              BRAVO - Applies when an increased or predictable threat of terrorist activity
              exists.

              CHARLIE - Applies when an incident occurs or intelligence is received indicating
              some form of terrorist action against personnel and facilities is imminent.

              DELTA - Applies in the immediate area where an attack has occurred or when
              intelligence is received indicating terrorist action against a location is
              imminent.

          hot_inventory: Estimated number of hot missiles of all types remaining in weapons system
              inventory.

          hpcon: Health Protection Condition (HPCON).

              0 - Routine, no community transmission.

              ALPHA - Limited, community transmission beginning.

              BRAVO - Moderate, increased community transmission.

              CHARLIE - Substantial, sustained community transmission.

              DELTA - Severe, widespread community transmission.

          inst_status: The status of the installation.

              FMC - Fully Mission Capable

              PMC - Partially Mission Capable

              NMC - Non Mission Capable

              UNK - Unknown.

          link: Array of Link item(s) for which status is available and reported (ATDL, IJMS,
              LINK-1, LINK-11, LINK-11B, LINK-16). This array must be the same length as the
              linkStatus array.

          link_status: Array of the status (AVAILABLE, DEGRADED, NOT AVAILABLE, etc.) for each links in
              the link array. This array must be the same length as the link array, and the
              status must correspond to the appropriate position index in the link array.

          missile: Array of specific missile types for which an estimated inventory count is
              available (e.g. GMD TYPE A, HARPOON, TOMAHAWK, etc.). This array must be the
              same length as the missileInventory array.

          missile_inventory: Array of the quantity of each of the missile items. This array must be the same
              length as the missile array, and the values must correspond to appropriate
              position index in the missile array.

          mobile_alt_id: Alternate Identifier for a mobile or transportable platform provided by source.

          ops_capability: The operational status of the platform (e.g. Fully Operational, Partially
              Operational, Not Operational, etc.).

          ops_impairment: The primary component degrading the operational capability of the platform or
              system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pes: Position Engagement Status flag, Indicating whether this platform is initiating
              multiple simultaneous engagements. A value of 1/True indicates the platform is
              initiating multiple simultaneous engagements.

          poiid: The POI (point of interest) ID related to this platform, if available.

          radar_status: Array of the status (NON-OPERATIONAL, OPERATIONAL, OFF) for each radar system in
              the radarSystem array. This array must be the same length as the radarSystem
              array, and the status must correspond to the appropriate position index in the
              radarSystem array.

          radar_system: Array of radar system(s) for which status is available and reported
              (ACQUISITION, IFFSIF, ILLUMINATING, MODE-4, PRIMARY SURVEILLANCE, SECONDARY
              SURVEILLANCE, TERTIARY SURVEILLANCE). This array must be the same length as the
              radarStatus array.

          radiate_mode: SAM sensor radar surveillance mode (Active, Passive, Off).

          report_time: Time of report, in ISO8601 UTC format.

          sam_mode: The state of a SAM unit (e.g. Initialization, Standby, Reorientation, etc.).

          site_type: Optional site type or further detail of type. Intended for, but not limited to,
              Link-16 site type specifications (e.g. ADOC, GACC, SOC, TACC, etc.).

          time_function: Description of the time function associated with the reportTime (e.g.
              Activation, Deactivation, Arrival, Departure, etc.), if applicable.

          track_id: The track ID related to this platform (if mobile or transportable), if
              available.

          track_ref_l16: Link-16 specific reference track number.

          weather_message: Description of the current weather conditions over a site.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/sitestatus/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_site": id_site,
                    "source": source,
                    "body_id": body_id,
                    "cat": cat,
                    "cold_inventory": cold_inventory,
                    "comm_impairment": comm_impairment,
                    "cpcon": cpcon,
                    "eoc": eoc,
                    "fpcon": fpcon,
                    "hot_inventory": hot_inventory,
                    "hpcon": hpcon,
                    "inst_status": inst_status,
                    "link": link,
                    "link_status": link_status,
                    "missile": missile,
                    "missile_inventory": missile_inventory,
                    "mobile_alt_id": mobile_alt_id,
                    "ops_capability": ops_capability,
                    "ops_impairment": ops_impairment,
                    "origin": origin,
                    "pes": pes,
                    "poiid": poiid,
                    "radar_status": radar_status,
                    "radar_system": radar_system,
                    "radiate_mode": radiate_mode,
                    "report_time": report_time,
                    "sam_mode": sam_mode,
                    "site_type": site_type,
                    "time_function": time_function,
                    "track_id": track_id,
                    "track_ref_l16": track_ref_l16,
                    "weather_message": weather_message,
                },
                site_status_update_params.SiteStatusUpdateParams,
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
    ) -> SyncOffsetPage[SiteStatusListResponse]:
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
            "/udl/sitestatus",
            page=SyncOffsetPage[SiteStatusListResponse],
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
                    site_status_list_params.SiteStatusListParams,
                ),
            ),
            model=SiteStatusListResponse,
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
        Service operation to delete an SiteStatus object specified by the passed ID path
        parameter. Note, delete operations do not remove data from historical or
        publish/subscribe stores. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/sitestatus/{id}",
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
            "/udl/sitestatus/count",
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
                    site_status_count_params.SiteStatusCountParams,
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
    ) -> SiteStatusGetResponse:
        """
        Service operation to get a single SiteStatus record by its unique ID passed as a
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
            f"/udl/sitestatus/{id}",
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
                    site_status_get_params.SiteStatusGetParams,
                ),
            ),
            cast_to=SiteStatusGetResponse,
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
            "/udl/sitestatus/queryhelp",
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
    ) -> SiteStatusTupleResponse:
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
            "/udl/sitestatus/tuple",
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
                    site_status_tuple_params.SiteStatusTupleParams,
                ),
            ),
            cast_to=SiteStatusTupleResponse,
        )


class AsyncSiteStatusResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSiteStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSiteStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiteStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSiteStatusResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_site: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        cat: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        cold_inventory: int | NotGiven = NOT_GIVEN,
        comm_impairment: str | NotGiven = NOT_GIVEN,
        cpcon: Literal["1", "2", "3", "4", "5"] | NotGiven = NOT_GIVEN,
        eoc: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        fpcon: Literal["NORMAL", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        hot_inventory: int | NotGiven = NOT_GIVEN,
        hpcon: Literal["0", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        inst_status: Literal["FMC", "PMC", "NMC", "UNK"] | NotGiven = NOT_GIVEN,
        link: List[str] | NotGiven = NOT_GIVEN,
        link_status: List[str] | NotGiven = NOT_GIVEN,
        missile: List[str] | NotGiven = NOT_GIVEN,
        missile_inventory: Iterable[int] | NotGiven = NOT_GIVEN,
        mobile_alt_id: str | NotGiven = NOT_GIVEN,
        ops_capability: str | NotGiven = NOT_GIVEN,
        ops_impairment: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pes: bool | NotGiven = NOT_GIVEN,
        poiid: str | NotGiven = NOT_GIVEN,
        radar_status: List[str] | NotGiven = NOT_GIVEN,
        radar_system: List[str] | NotGiven = NOT_GIVEN,
        radiate_mode: str | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sam_mode: str | NotGiven = NOT_GIVEN,
        site_type: str | NotGiven = NOT_GIVEN,
        time_function: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_ref_l16: str | NotGiven = NOT_GIVEN,
        weather_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SiteStatus object as a POST body and ingest
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

          id_site: The ID of the site, if this status is associated with a fixed site or platform.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          cat: Crisis Action Team (CAT).

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          cold_inventory: Estimated number of cold missiles of all types remaining in weapons system
              inventory.

          comm_impairment: The communications component causing the platform or system to be less than
              fully operational.

          cpcon: Cyberspace Protection Condition (CPCON).

              1 - VERY HIGH - Critical functions.

              2 - HIGH - Critical and essential functions.

              3 - MEDIUM - Critical, essential, and support functions.

              4 - LOW - All functions.

              5 - VERY LOW - All functions.

          eoc: Emergency Operations Center (EOC) status.

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          fpcon: Force Protection Condition (FPCON).

              NORMAL - Applies when a general global threat of possible terrorist activity
              exists and warrants a routine security posture.

              ALPHA - Applies when an increased general threat of possible terrorist activity
              against personnel or facilities. Nature and extent of threat are unpredictable.

              BRAVO - Applies when an increased or predictable threat of terrorist activity
              exists.

              CHARLIE - Applies when an incident occurs or intelligence is received indicating
              some form of terrorist action against personnel and facilities is imminent.

              DELTA - Applies in the immediate area where an attack has occurred or when
              intelligence is received indicating terrorist action against a location is
              imminent.

          hot_inventory: Estimated number of hot missiles of all types remaining in weapons system
              inventory.

          hpcon: Health Protection Condition (HPCON).

              0 - Routine, no community transmission.

              ALPHA - Limited, community transmission beginning.

              BRAVO - Moderate, increased community transmission.

              CHARLIE - Substantial, sustained community transmission.

              DELTA - Severe, widespread community transmission.

          inst_status: The status of the installation.

              FMC - Fully Mission Capable

              PMC - Partially Mission Capable

              NMC - Non Mission Capable

              UNK - Unknown.

          link: Array of Link item(s) for which status is available and reported (ATDL, IJMS,
              LINK-1, LINK-11, LINK-11B, LINK-16). This array must be the same length as the
              linkStatus array.

          link_status: Array of the status (AVAILABLE, DEGRADED, NOT AVAILABLE, etc.) for each links in
              the link array. This array must be the same length as the link array, and the
              status must correspond to the appropriate position index in the link array.

          missile: Array of specific missile types for which an estimated inventory count is
              available (e.g. GMD TYPE A, HARPOON, TOMAHAWK, etc.). This array must be the
              same length as the missileInventory array.

          missile_inventory: Array of the quantity of each of the missile items. This array must be the same
              length as the missile array, and the values must correspond to appropriate
              position index in the missile array.

          mobile_alt_id: Alternate Identifier for a mobile or transportable platform provided by source.

          ops_capability: The operational status of the platform (e.g. Fully Operational, Partially
              Operational, Not Operational, etc.).

          ops_impairment: The primary component degrading the operational capability of the platform or
              system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pes: Position Engagement Status flag, Indicating whether this platform is initiating
              multiple simultaneous engagements. A value of 1/True indicates the platform is
              initiating multiple simultaneous engagements.

          poiid: The POI (point of interest) ID related to this platform, if available.

          radar_status: Array of the status (NON-OPERATIONAL, OPERATIONAL, OFF) for each radar system in
              the radarSystem array. This array must be the same length as the radarSystem
              array, and the status must correspond to the appropriate position index in the
              radarSystem array.

          radar_system: Array of radar system(s) for which status is available and reported
              (ACQUISITION, IFFSIF, ILLUMINATING, MODE-4, PRIMARY SURVEILLANCE, SECONDARY
              SURVEILLANCE, TERTIARY SURVEILLANCE). This array must be the same length as the
              radarStatus array.

          radiate_mode: SAM sensor radar surveillance mode (Active, Passive, Off).

          report_time: Time of report, in ISO8601 UTC format.

          sam_mode: The state of a SAM unit (e.g. Initialization, Standby, Reorientation, etc.).

          site_type: Optional site type or further detail of type. Intended for, but not limited to,
              Link-16 site type specifications (e.g. ADOC, GACC, SOC, TACC, etc.).

          time_function: Description of the time function associated with the reportTime (e.g.
              Activation, Deactivation, Arrival, Departure, etc.), if applicable.

          track_id: The track ID related to this platform (if mobile or transportable), if
              available.

          track_ref_l16: Link-16 specific reference track number.

          weather_message: Description of the current weather conditions over a site.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/sitestatus",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_site": id_site,
                    "source": source,
                    "id": id,
                    "cat": cat,
                    "cold_inventory": cold_inventory,
                    "comm_impairment": comm_impairment,
                    "cpcon": cpcon,
                    "eoc": eoc,
                    "fpcon": fpcon,
                    "hot_inventory": hot_inventory,
                    "hpcon": hpcon,
                    "inst_status": inst_status,
                    "link": link,
                    "link_status": link_status,
                    "missile": missile,
                    "missile_inventory": missile_inventory,
                    "mobile_alt_id": mobile_alt_id,
                    "ops_capability": ops_capability,
                    "ops_impairment": ops_impairment,
                    "origin": origin,
                    "pes": pes,
                    "poiid": poiid,
                    "radar_status": radar_status,
                    "radar_system": radar_system,
                    "radiate_mode": radiate_mode,
                    "report_time": report_time,
                    "sam_mode": sam_mode,
                    "site_type": site_type,
                    "time_function": time_function,
                    "track_id": track_id,
                    "track_ref_l16": track_ref_l16,
                    "weather_message": weather_message,
                },
                site_status_create_params.SiteStatusCreateParams,
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
        id_site: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        cat: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        cold_inventory: int | NotGiven = NOT_GIVEN,
        comm_impairment: str | NotGiven = NOT_GIVEN,
        cpcon: Literal["1", "2", "3", "4", "5"] | NotGiven = NOT_GIVEN,
        eoc: Literal["COLD", "WARM", "HOT"] | NotGiven = NOT_GIVEN,
        fpcon: Literal["NORMAL", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        hot_inventory: int | NotGiven = NOT_GIVEN,
        hpcon: Literal["0", "ALPHA", "BRAVO", "CHARLIE", "DELTA"] | NotGiven = NOT_GIVEN,
        inst_status: Literal["FMC", "PMC", "NMC", "UNK"] | NotGiven = NOT_GIVEN,
        link: List[str] | NotGiven = NOT_GIVEN,
        link_status: List[str] | NotGiven = NOT_GIVEN,
        missile: List[str] | NotGiven = NOT_GIVEN,
        missile_inventory: Iterable[int] | NotGiven = NOT_GIVEN,
        mobile_alt_id: str | NotGiven = NOT_GIVEN,
        ops_capability: str | NotGiven = NOT_GIVEN,
        ops_impairment: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pes: bool | NotGiven = NOT_GIVEN,
        poiid: str | NotGiven = NOT_GIVEN,
        radar_status: List[str] | NotGiven = NOT_GIVEN,
        radar_system: List[str] | NotGiven = NOT_GIVEN,
        radiate_mode: str | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sam_mode: str | NotGiven = NOT_GIVEN,
        site_type: str | NotGiven = NOT_GIVEN,
        time_function: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_ref_l16: str | NotGiven = NOT_GIVEN,
        weather_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single SiteStatus object.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

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

          id_site: The ID of the site, if this status is associated with a fixed site or platform.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          cat: Crisis Action Team (CAT).

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          cold_inventory: Estimated number of cold missiles of all types remaining in weapons system
              inventory.

          comm_impairment: The communications component causing the platform or system to be less than
              fully operational.

          cpcon: Cyberspace Protection Condition (CPCON).

              1 - VERY HIGH - Critical functions.

              2 - HIGH - Critical and essential functions.

              3 - MEDIUM - Critical, essential, and support functions.

              4 - LOW - All functions.

              5 - VERY LOW - All functions.

          eoc: Emergency Operations Center (EOC) status.

              COLD - Not in use.

              WARM - Facility prepped/possible skeleton crew.

              HOT - Fully active.

          fpcon: Force Protection Condition (FPCON).

              NORMAL - Applies when a general global threat of possible terrorist activity
              exists and warrants a routine security posture.

              ALPHA - Applies when an increased general threat of possible terrorist activity
              against personnel or facilities. Nature and extent of threat are unpredictable.

              BRAVO - Applies when an increased or predictable threat of terrorist activity
              exists.

              CHARLIE - Applies when an incident occurs or intelligence is received indicating
              some form of terrorist action against personnel and facilities is imminent.

              DELTA - Applies in the immediate area where an attack has occurred or when
              intelligence is received indicating terrorist action against a location is
              imminent.

          hot_inventory: Estimated number of hot missiles of all types remaining in weapons system
              inventory.

          hpcon: Health Protection Condition (HPCON).

              0 - Routine, no community transmission.

              ALPHA - Limited, community transmission beginning.

              BRAVO - Moderate, increased community transmission.

              CHARLIE - Substantial, sustained community transmission.

              DELTA - Severe, widespread community transmission.

          inst_status: The status of the installation.

              FMC - Fully Mission Capable

              PMC - Partially Mission Capable

              NMC - Non Mission Capable

              UNK - Unknown.

          link: Array of Link item(s) for which status is available and reported (ATDL, IJMS,
              LINK-1, LINK-11, LINK-11B, LINK-16). This array must be the same length as the
              linkStatus array.

          link_status: Array of the status (AVAILABLE, DEGRADED, NOT AVAILABLE, etc.) for each links in
              the link array. This array must be the same length as the link array, and the
              status must correspond to the appropriate position index in the link array.

          missile: Array of specific missile types for which an estimated inventory count is
              available (e.g. GMD TYPE A, HARPOON, TOMAHAWK, etc.). This array must be the
              same length as the missileInventory array.

          missile_inventory: Array of the quantity of each of the missile items. This array must be the same
              length as the missile array, and the values must correspond to appropriate
              position index in the missile array.

          mobile_alt_id: Alternate Identifier for a mobile or transportable platform provided by source.

          ops_capability: The operational status of the platform (e.g. Fully Operational, Partially
              Operational, Not Operational, etc.).

          ops_impairment: The primary component degrading the operational capability of the platform or
              system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pes: Position Engagement Status flag, Indicating whether this platform is initiating
              multiple simultaneous engagements. A value of 1/True indicates the platform is
              initiating multiple simultaneous engagements.

          poiid: The POI (point of interest) ID related to this platform, if available.

          radar_status: Array of the status (NON-OPERATIONAL, OPERATIONAL, OFF) for each radar system in
              the radarSystem array. This array must be the same length as the radarSystem
              array, and the status must correspond to the appropriate position index in the
              radarSystem array.

          radar_system: Array of radar system(s) for which status is available and reported
              (ACQUISITION, IFFSIF, ILLUMINATING, MODE-4, PRIMARY SURVEILLANCE, SECONDARY
              SURVEILLANCE, TERTIARY SURVEILLANCE). This array must be the same length as the
              radarStatus array.

          radiate_mode: SAM sensor radar surveillance mode (Active, Passive, Off).

          report_time: Time of report, in ISO8601 UTC format.

          sam_mode: The state of a SAM unit (e.g. Initialization, Standby, Reorientation, etc.).

          site_type: Optional site type or further detail of type. Intended for, but not limited to,
              Link-16 site type specifications (e.g. ADOC, GACC, SOC, TACC, etc.).

          time_function: Description of the time function associated with the reportTime (e.g.
              Activation, Deactivation, Arrival, Departure, etc.), if applicable.

          track_id: The track ID related to this platform (if mobile or transportable), if
              available.

          track_ref_l16: Link-16 specific reference track number.

          weather_message: Description of the current weather conditions over a site.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/sitestatus/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_site": id_site,
                    "source": source,
                    "body_id": body_id,
                    "cat": cat,
                    "cold_inventory": cold_inventory,
                    "comm_impairment": comm_impairment,
                    "cpcon": cpcon,
                    "eoc": eoc,
                    "fpcon": fpcon,
                    "hot_inventory": hot_inventory,
                    "hpcon": hpcon,
                    "inst_status": inst_status,
                    "link": link,
                    "link_status": link_status,
                    "missile": missile,
                    "missile_inventory": missile_inventory,
                    "mobile_alt_id": mobile_alt_id,
                    "ops_capability": ops_capability,
                    "ops_impairment": ops_impairment,
                    "origin": origin,
                    "pes": pes,
                    "poiid": poiid,
                    "radar_status": radar_status,
                    "radar_system": radar_system,
                    "radiate_mode": radiate_mode,
                    "report_time": report_time,
                    "sam_mode": sam_mode,
                    "site_type": site_type,
                    "time_function": time_function,
                    "track_id": track_id,
                    "track_ref_l16": track_ref_l16,
                    "weather_message": weather_message,
                },
                site_status_update_params.SiteStatusUpdateParams,
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
    ) -> AsyncPaginator[SiteStatusListResponse, AsyncOffsetPage[SiteStatusListResponse]]:
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
            "/udl/sitestatus",
            page=AsyncOffsetPage[SiteStatusListResponse],
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
                    site_status_list_params.SiteStatusListParams,
                ),
            ),
            model=SiteStatusListResponse,
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
        Service operation to delete an SiteStatus object specified by the passed ID path
        parameter. Note, delete operations do not remove data from historical or
        publish/subscribe stores. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/sitestatus/{id}",
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
            "/udl/sitestatus/count",
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
                    site_status_count_params.SiteStatusCountParams,
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
    ) -> SiteStatusGetResponse:
        """
        Service operation to get a single SiteStatus record by its unique ID passed as a
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
            f"/udl/sitestatus/{id}",
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
                    site_status_get_params.SiteStatusGetParams,
                ),
            ),
            cast_to=SiteStatusGetResponse,
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
            "/udl/sitestatus/queryhelp",
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
    ) -> SiteStatusTupleResponse:
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
            "/udl/sitestatus/tuple",
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
                    site_status_tuple_params.SiteStatusTupleParams,
                ),
            ),
            cast_to=SiteStatusTupleResponse,
        )


class SiteStatusResourceWithRawResponse:
    def __init__(self, site_status: SiteStatusResource) -> None:
        self._site_status = site_status

        self.create = to_raw_response_wrapper(
            site_status.create,
        )
        self.update = to_raw_response_wrapper(
            site_status.update,
        )
        self.list = to_raw_response_wrapper(
            site_status.list,
        )
        self.delete = to_raw_response_wrapper(
            site_status.delete,
        )
        self.count = to_raw_response_wrapper(
            site_status.count,
        )
        self.get = to_raw_response_wrapper(
            site_status.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            site_status.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            site_status.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._site_status.history)


class AsyncSiteStatusResourceWithRawResponse:
    def __init__(self, site_status: AsyncSiteStatusResource) -> None:
        self._site_status = site_status

        self.create = async_to_raw_response_wrapper(
            site_status.create,
        )
        self.update = async_to_raw_response_wrapper(
            site_status.update,
        )
        self.list = async_to_raw_response_wrapper(
            site_status.list,
        )
        self.delete = async_to_raw_response_wrapper(
            site_status.delete,
        )
        self.count = async_to_raw_response_wrapper(
            site_status.count,
        )
        self.get = async_to_raw_response_wrapper(
            site_status.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            site_status.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            site_status.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._site_status.history)


class SiteStatusResourceWithStreamingResponse:
    def __init__(self, site_status: SiteStatusResource) -> None:
        self._site_status = site_status

        self.create = to_streamed_response_wrapper(
            site_status.create,
        )
        self.update = to_streamed_response_wrapper(
            site_status.update,
        )
        self.list = to_streamed_response_wrapper(
            site_status.list,
        )
        self.delete = to_streamed_response_wrapper(
            site_status.delete,
        )
        self.count = to_streamed_response_wrapper(
            site_status.count,
        )
        self.get = to_streamed_response_wrapper(
            site_status.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            site_status.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            site_status.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._site_status.history)


class AsyncSiteStatusResourceWithStreamingResponse:
    def __init__(self, site_status: AsyncSiteStatusResource) -> None:
        self._site_status = site_status

        self.create = async_to_streamed_response_wrapper(
            site_status.create,
        )
        self.update = async_to_streamed_response_wrapper(
            site_status.update,
        )
        self.list = async_to_streamed_response_wrapper(
            site_status.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            site_status.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            site_status.count,
        )
        self.get = async_to_streamed_response_wrapper(
            site_status.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            site_status.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            site_status.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._site_status.history)
