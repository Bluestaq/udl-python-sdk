# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    event_evolution_list_params,
    event_evolution_count_params,
    event_evolution_tuple_params,
    event_evolution_create_params,
    event_evolution_retrieve_params,
    event_evolution_create_bulk_params,
    event_evolution_unvalidated_publish_params,
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
from ...types.shared.event_evolution_full import EventEvolutionFull
from ...types.event_evolution_list_response import EventEvolutionListResponse
from ...types.event_evolution_tuple_response import EventEvolutionTupleResponse
from ...types.event_evolution_queryhelp_response import EventEvolutionQueryhelpResponse

__all__ = ["EventEvolutionResource", "AsyncEventEvolutionResource"]


class EventEvolutionResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventEvolutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EventEvolutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventEvolutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EventEvolutionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_id: str,
        source: str,
        start_time: Union[str, datetime],
        summary: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        data_description: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        geo_admin_level1: str | NotGiven = NOT_GIVEN,
        geo_admin_level2: str | NotGiven = NOT_GIVEN,
        geo_admin_level3: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        redact: bool | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        url: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EventEvolution object as a POST body and
        ingest into the database. A specific role is required to perform this service
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

          event_id: User-provided unique identifier of this activity or event. This ID should remain
              the same on subsequent updates in order to associate all records pertaining to
              the activity or event.

          source: Source of the data.

          start_time: The actual or estimated start time of the activity or event, in ISO 8601 UTC
              format.

          summary: Summary or description of the activity or event.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          category: The activity or event type associated with this record (e.g. BREAKUP, DIRECT
              FIRE, IED, LAUNCH, PROTEST, etc.). For Significant Activities, recommended but
              not constrained to, CAMEO.Manual.1.1b3 Chapter 6. Note that the evolution of an
              event may incorporate records of various types, for example, a LAUNCH event may
              evolve into a BREAKUP event.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL’s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          data_description: Optional description of the relationship between the records provided in the
              srcTyps/srcIds and the activity or event.

          end_time: The actual or estimated start time of the activity or event, in ISO 8601 UTC
              format.

          geo_admin_level1: Administrative boundaries of the first sub-national level. Level 1 is simply the
              largest demarcation under whatever demarcation criteria has been determined by
              the governing body. For example this may be the state/province in which a
              terrestrial event takes place, or with which the event is attributed for
              non-localized or non-terrestrial activity.

          geo_admin_level2: Administrative boundaries of the second sub-national level. Level 2 is simply
              the second largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example this may be the city/district in
              which a terrestrial event takes place, or with which the event is attributed for
              non-localized or non-terrestrial activity.

          geo_admin_level3: Administrative boundaries of the third sub-national level. Level 3 is simply the
              third largest demarcation under whatever demarcation criteria has been
              determined by the governing body.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          redact: Flag indicating that this record is for the purpose of redacting one or more
              previously specified records from association with this activity or event. If
              this flag is set then all records indicated in srcTyps/srcIds should be removed
              from event association.

          src_ids: Array of UUIDs of the UDL data records that are related to the determination of
              this activity or event. See the associated 'srcTyps' array for the specific
              types of data, positionally corresponding to the UUIDs in this array. The
              'srcTyps' and 'srcIds' arrays must match in size. See the corresponding srcTyps
              array element for the data type of the UUID and use the appropriate API
              operation to retrieve that object.

          src_typs: Array of UDL record types (AIS, CONJUNCTION, DOA, ELSET, EO, ESID, GROUNDIMAGE,
              POI, MANEUVER, MTI, NOTIFICATION, RADAR, RF, SIGACT, SKYIMAGE, SV, TRACK) that
              are related to this activity or event. See the associated 'srcIds' array for the
              record UUIDs, positionally corresponding to the record types in this array. The
              'srcTyps' and 'srcIds' arrays must match in size.

          status: The status of this activity or event. (ACTIVE, CONCLUDED, UNKNOWN).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          url: List of URLs to before/after images of this point of interest entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/eventevolution",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_id": event_id,
                    "source": source,
                    "start_time": start_time,
                    "summary": summary,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "category": category,
                    "country_code": country_code,
                    "data_description": data_description,
                    "end_time": end_time,
                    "geo_admin_level1": geo_admin_level1,
                    "geo_admin_level2": geo_admin_level2,
                    "geo_admin_level3": geo_admin_level3,
                    "origin": origin,
                    "redact": redact,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "status": status,
                    "tags": tags,
                    "url": url,
                },
                event_evolution_create_params.EventEvolutionCreateParams,
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
    ) -> EventEvolutionFull:
        """
        Service operation to get a single EventEvolution by its unique ID passed as a
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
            f"/udl/eventevolution/{id}",
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
                    event_evolution_retrieve_params.EventEvolutionRetrieveParams,
                ),
            ),
            cast_to=EventEvolutionFull,
        )

    def list(
        self,
        *,
        event_id: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EventEvolutionListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_id: (One or more of fields 'eventId, startTime' are required.) User-provided unique
              identifier of this activity or event. This ID should remain the same on
              subsequent updates in order to associate all records pertaining to the activity
              or event.

          start_time: (One or more of fields 'eventId, startTime' are required.) The actual or
              estimated start time of the activity or event, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eventevolution",
            page=SyncOffsetPage[EventEvolutionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_id": event_id,
                        "first_result": first_result,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    event_evolution_list_params.EventEvolutionListParams,
                ),
            ),
            model=EventEvolutionListResponse,
        )

    def count(
        self,
        *,
        event_id: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          event_id: (One or more of fields 'eventId, startTime' are required.) User-provided unique
              identifier of this activity or event. This ID should remain the same on
              subsequent updates in order to associate all records pertaining to the activity
              or event.

          start_time: (One or more of fields 'eventId, startTime' are required.) The actual or
              estimated start time of the activity or event, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/eventevolution/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_id": event_id,
                        "first_result": first_result,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    event_evolution_count_params.EventEvolutionCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[event_evolution_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        EventEvolution records as a POST body and ingest into the database. Requires
        specific roles, please contact the UDL team to gain access. This operation is
        not intended to be used for automated feeds into UDL...data providers should
        contact the UDL team for instructions on setting up a permanent feed through an
        alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/eventevolution/createBulk",
            body=maybe_transform(body, Iterable[event_evolution_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> EventEvolutionQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/eventevolution/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventEvolutionQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        event_id: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventEvolutionTupleResponse:
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

          event_id: (One or more of fields 'eventId, startTime' are required.) User-provided unique
              identifier of this activity or event. This ID should remain the same on
              subsequent updates in order to associate all records pertaining to the activity
              or event.

          start_time: (One or more of fields 'eventId, startTime' are required.) The actual or
              estimated start time of the activity or event, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/eventevolution/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "event_id": event_id,
                        "first_result": first_result,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    event_evolution_tuple_params.EventEvolutionTupleParams,
                ),
            ),
            cast_to=EventEvolutionTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[event_evolution_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of EventEvolution records as a POST body and
        ingest into the database. Requires a specific role, please contact the UDL team
        to gain access. This operation is intended to be used for automated feeds into
        UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-eventevolution",
            body=maybe_transform(body, Iterable[event_evolution_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEventEvolutionResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventEvolutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEventEvolutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventEvolutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEventEvolutionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_id: str,
        source: str,
        start_time: Union[str, datetime],
        summary: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        data_description: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        geo_admin_level1: str | NotGiven = NOT_GIVEN,
        geo_admin_level2: str | NotGiven = NOT_GIVEN,
        geo_admin_level3: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        redact: bool | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        url: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EventEvolution object as a POST body and
        ingest into the database. A specific role is required to perform this service
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

          event_id: User-provided unique identifier of this activity or event. This ID should remain
              the same on subsequent updates in order to associate all records pertaining to
              the activity or event.

          source: Source of the data.

          start_time: The actual or estimated start time of the activity or event, in ISO 8601 UTC
              format.

          summary: Summary or description of the activity or event.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          category: The activity or event type associated with this record (e.g. BREAKUP, DIRECT
              FIRE, IED, LAUNCH, PROTEST, etc.). For Significant Activities, recommended but
              not constrained to, CAMEO.Manual.1.1b3 Chapter 6. Note that the evolution of an
              event may incorporate records of various types, for example, a LAUNCH event may
              evolve into a BREAKUP event.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL’s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          data_description: Optional description of the relationship between the records provided in the
              srcTyps/srcIds and the activity or event.

          end_time: The actual or estimated start time of the activity or event, in ISO 8601 UTC
              format.

          geo_admin_level1: Administrative boundaries of the first sub-national level. Level 1 is simply the
              largest demarcation under whatever demarcation criteria has been determined by
              the governing body. For example this may be the state/province in which a
              terrestrial event takes place, or with which the event is attributed for
              non-localized or non-terrestrial activity.

          geo_admin_level2: Administrative boundaries of the second sub-national level. Level 2 is simply
              the second largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example this may be the city/district in
              which a terrestrial event takes place, or with which the event is attributed for
              non-localized or non-terrestrial activity.

          geo_admin_level3: Administrative boundaries of the third sub-national level. Level 3 is simply the
              third largest demarcation under whatever demarcation criteria has been
              determined by the governing body.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          redact: Flag indicating that this record is for the purpose of redacting one or more
              previously specified records from association with this activity or event. If
              this flag is set then all records indicated in srcTyps/srcIds should be removed
              from event association.

          src_ids: Array of UUIDs of the UDL data records that are related to the determination of
              this activity or event. See the associated 'srcTyps' array for the specific
              types of data, positionally corresponding to the UUIDs in this array. The
              'srcTyps' and 'srcIds' arrays must match in size. See the corresponding srcTyps
              array element for the data type of the UUID and use the appropriate API
              operation to retrieve that object.

          src_typs: Array of UDL record types (AIS, CONJUNCTION, DOA, ELSET, EO, ESID, GROUNDIMAGE,
              POI, MANEUVER, MTI, NOTIFICATION, RADAR, RF, SIGACT, SKYIMAGE, SV, TRACK) that
              are related to this activity or event. See the associated 'srcIds' array for the
              record UUIDs, positionally corresponding to the record types in this array. The
              'srcTyps' and 'srcIds' arrays must match in size.

          status: The status of this activity or event. (ACTIVE, CONCLUDED, UNKNOWN).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          url: List of URLs to before/after images of this point of interest entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/eventevolution",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_id": event_id,
                    "source": source,
                    "start_time": start_time,
                    "summary": summary,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "category": category,
                    "country_code": country_code,
                    "data_description": data_description,
                    "end_time": end_time,
                    "geo_admin_level1": geo_admin_level1,
                    "geo_admin_level2": geo_admin_level2,
                    "geo_admin_level3": geo_admin_level3,
                    "origin": origin,
                    "redact": redact,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "status": status,
                    "tags": tags,
                    "url": url,
                },
                event_evolution_create_params.EventEvolutionCreateParams,
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
    ) -> EventEvolutionFull:
        """
        Service operation to get a single EventEvolution by its unique ID passed as a
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
            f"/udl/eventevolution/{id}",
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
                    event_evolution_retrieve_params.EventEvolutionRetrieveParams,
                ),
            ),
            cast_to=EventEvolutionFull,
        )

    def list(
        self,
        *,
        event_id: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventEvolutionListResponse, AsyncOffsetPage[EventEvolutionListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_id: (One or more of fields 'eventId, startTime' are required.) User-provided unique
              identifier of this activity or event. This ID should remain the same on
              subsequent updates in order to associate all records pertaining to the activity
              or event.

          start_time: (One or more of fields 'eventId, startTime' are required.) The actual or
              estimated start time of the activity or event, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eventevolution",
            page=AsyncOffsetPage[EventEvolutionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_id": event_id,
                        "first_result": first_result,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    event_evolution_list_params.EventEvolutionListParams,
                ),
            ),
            model=EventEvolutionListResponse,
        )

    async def count(
        self,
        *,
        event_id: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          event_id: (One or more of fields 'eventId, startTime' are required.) User-provided unique
              identifier of this activity or event. This ID should remain the same on
              subsequent updates in order to associate all records pertaining to the activity
              or event.

          start_time: (One or more of fields 'eventId, startTime' are required.) The actual or
              estimated start time of the activity or event, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/eventevolution/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_id": event_id,
                        "first_result": first_result,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    event_evolution_count_params.EventEvolutionCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[event_evolution_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        EventEvolution records as a POST body and ingest into the database. Requires
        specific roles, please contact the UDL team to gain access. This operation is
        not intended to be used for automated feeds into UDL...data providers should
        contact the UDL team for instructions on setting up a permanent feed through an
        alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/eventevolution/createBulk",
            body=await async_maybe_transform(body, Iterable[event_evolution_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> EventEvolutionQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/eventevolution/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventEvolutionQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        event_id: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventEvolutionTupleResponse:
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

          event_id: (One or more of fields 'eventId, startTime' are required.) User-provided unique
              identifier of this activity or event. This ID should remain the same on
              subsequent updates in order to associate all records pertaining to the activity
              or event.

          start_time: (One or more of fields 'eventId, startTime' are required.) The actual or
              estimated start time of the activity or event, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/eventevolution/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "event_id": event_id,
                        "first_result": first_result,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    event_evolution_tuple_params.EventEvolutionTupleParams,
                ),
            ),
            cast_to=EventEvolutionTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[event_evolution_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of EventEvolution records as a POST body and
        ingest into the database. Requires a specific role, please contact the UDL team
        to gain access. This operation is intended to be used for automated feeds into
        UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-eventevolution",
            body=await async_maybe_transform(body, Iterable[event_evolution_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EventEvolutionResourceWithRawResponse:
    def __init__(self, event_evolution: EventEvolutionResource) -> None:
        self._event_evolution = event_evolution

        self.create = to_raw_response_wrapper(
            event_evolution.create,
        )
        self.retrieve = to_raw_response_wrapper(
            event_evolution.retrieve,
        )
        self.list = to_raw_response_wrapper(
            event_evolution.list,
        )
        self.count = to_raw_response_wrapper(
            event_evolution.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            event_evolution.create_bulk,
        )
        self.queryhelp = to_raw_response_wrapper(
            event_evolution.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            event_evolution.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            event_evolution.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._event_evolution.history)


class AsyncEventEvolutionResourceWithRawResponse:
    def __init__(self, event_evolution: AsyncEventEvolutionResource) -> None:
        self._event_evolution = event_evolution

        self.create = async_to_raw_response_wrapper(
            event_evolution.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            event_evolution.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            event_evolution.list,
        )
        self.count = async_to_raw_response_wrapper(
            event_evolution.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            event_evolution.create_bulk,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            event_evolution.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            event_evolution.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            event_evolution.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._event_evolution.history)


class EventEvolutionResourceWithStreamingResponse:
    def __init__(self, event_evolution: EventEvolutionResource) -> None:
        self._event_evolution = event_evolution

        self.create = to_streamed_response_wrapper(
            event_evolution.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            event_evolution.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            event_evolution.list,
        )
        self.count = to_streamed_response_wrapper(
            event_evolution.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            event_evolution.create_bulk,
        )
        self.queryhelp = to_streamed_response_wrapper(
            event_evolution.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            event_evolution.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            event_evolution.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._event_evolution.history)


class AsyncEventEvolutionResourceWithStreamingResponse:
    def __init__(self, event_evolution: AsyncEventEvolutionResource) -> None:
        self._event_evolution = event_evolution

        self.create = async_to_streamed_response_wrapper(
            event_evolution.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            event_evolution.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            event_evolution.list,
        )
        self.count = async_to_streamed_response_wrapper(
            event_evolution.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            event_evolution.create_bulk,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            event_evolution.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            event_evolution.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            event_evolution.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._event_evolution.history)
