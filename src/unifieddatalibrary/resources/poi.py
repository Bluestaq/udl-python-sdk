# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    poi_get_params,
    poi_list_params,
    poi_count_params,
    poi_tuple_params,
    poi_create_params,
    poi_create_bulk_params,
    poi_unvalidated_publish_params,
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
from ..types.poi_get_response import PoiGetResponse
from ..types.poi_list_response import PoiListResponse
from ..types.poi_tuple_response import PoiTupleResponse
from ..types.poi_queryhelp_response import PoiQueryhelpResponse

__all__ = ["PoiResource", "AsyncPoiResource"]


class PoiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PoiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return PoiResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        poiid: str,
        source: str,
        ts: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        activity: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        asset: str | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        az: float | NotGiven = NOT_GIVEN,
        be_number: str | NotGiven = NOT_GIVEN,
        ce: float | NotGiven = NOT_GIVEN,
        cntct: str | NotGiven = NOT_GIVEN,
        conf: float | NotGiven = NOT_GIVEN,
        desc: str | NotGiven = NOT_GIVEN,
        el: float | NotGiven = NOT_GIVEN,
        elle: Iterable[float] | NotGiven = NOT_GIVEN,
        env: str | NotGiven = NOT_GIVEN,
        groups: List[str] | NotGiven = NOT_GIVEN,
        how: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_weather_report: List[str] | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        le: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        msnid: str | NotGiven = NOT_GIVEN,
        orientation: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        plat: str | NotGiven = NOT_GIVEN,
        pps: str | NotGiven = NOT_GIVEN,
        pri: int | NotGiven = NOT_GIVEN,
        spec: str | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        stale: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        trkid: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single POI as a POST body and ingest into the
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

          name: Name of the POI target object.

          poiid: Identifier of the actual Point of Interest or target object, which should remain
              the same on subsequent POI records of the same Point of Interest.

          source: Source of the data.

          ts: Activity/POI timestamp in ISO8601 UTC format.

          id: Unique identifier of the record, auto-generated by the system.

          activity: The activity in which the POI subject is engaged. Intended as, but not
              constrained to, MIL-STD-6016 environment dependent activity designations. The
              activity can be reported as either a combination of the code and environment
              (e.g. 30/LAND) or as the descriptive enumeration (e.g. TRAINING), which are
              equivalent.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alt: Point height above ellipsoid (WGS-84), in meters.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the Point of Interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          asset: ID/name of the platform or entity providing the POI data.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          az: Target object pointing azimuth angle, in degrees (for target with sensing or
              emitting capability).

          be_number: The Basic Encyclopedia Number associated with the POI, if applicable.

          ce: Radius of circular area about lat/lon point, in meters (1-sigma, if representing
              error).

          cntct: Contact information for assets reporting PPLI (Precise Participant Location and
              Identification). PPLI is a Link 16 message that is used by units to transmit
              complete location, identification, and limited status information.

          conf: POI confidence estimate (not standardized, but typically a value between 0 and
              1, with 0 indicating lowest confidence.

          desc: Description of the POI target object.

          el: Target object pointing elevation angle, in degrees (for target with sensing or
              emitting capability).

          elle: Elliptical area about the lat/lon point, specified as [semi-major axis (m),
              semi-minor axis (m), orientation (deg) off true North at POI].

          env: POI environment type (e.g., LAND, SURFACE, SUBSURFACE, UNKNOWN, etc.).

          groups: Optional array of groups used when a POI msg originates from a TAK server. Each
              group must be no longer than 256 characters. Groups identify a set of users
              targeted by the cot/poi msg.

          how: How the event point was generated, in CoT object heirarchy notation (optional,
              CoT).

          ident: Estimated identity of the point/object (e.g., FRIEND, HOSTILE, SUSPECT,
              ASSUMED_FRIEND, UNKNOWN, etc.).

          id_weather_report: Array of one or more unique identifiers of weather records associated with this
              POI. Each element in array must be 36 characters or less in length.

          lat: WGS-84 latitude of the POI, in degrees (+N, -S), -90 to 90.

          le: Height above lat/lon point, in meters (1-sigma, if representing linear error).

          lon: WGS-84 longitude of the POI, in degrees (+E, -W), -180 to 180.

          msnid: Optional mission ID related to the POI.

          orientation: The orientation of a vehicle, platform or other entity described by the POI. The
              orientation is defined as the pointing direction of the front/nose of the object
              in degrees clockwise from true North at the object point.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          plat: POI/object platform type (e.g., 14/GROUND, COMBAT_VEHICLE, etc.).

          pps: The purpose of this Point of Interest record (e.g., BDA, EQPT, EVENT, GEOL,
              HZRD, PPLI, SHOTBOX, SURVL, TGT, TSK, WTHR).

          pri: Priority of the POI target object.

          spec: Specific point/object type (e.g., 82/GROUND, LIGHT_TANK, etc.).

          src_ids: Array of UUIDs of the UDL data records that are related to the determination of
              this Point of Interest. See the associated 'srcTyps' array for the specific
              types of data, positionally corresponding to the UUIDs in this array. The
              'srcTyps' and 'srcIds' arrays must match in size. See the corresponding srcTyps
              array element for the data type of the UUID and use the appropriate API
              operation to retrieve that object (e.g. /udl/rfobservation/{uuid}).

          src_typs: Array of UDL record types (GROUNDIMAGE, RFOBS) that are related to the
              determination of this Point of Interest. See the associated 'srcIds' array for
              the record UUIDs, positionally corresponding to the record types in this array.
              The 'srcTyps' and 'srcIds' arrays must match in size.

          stale: Stale timestamp (optional), in ISO8601 UTC format.

          start: Start time of event validity (optional), in ISO8601 UTC format.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          trkid: Optional ID of an associated track related to the POI object, if applicable.
              This track ID should correlate the Point of Interest to a track from the Track
              service.

          type: Event type, in CoT object heirarchy notation (optional, CoT).

          urls: List of URLs to before/after images of this Point of Interest entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/poi",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "poiid": poiid,
                    "source": source,
                    "ts": ts,
                    "id": id,
                    "activity": activity,
                    "agjson": agjson,
                    "alt": alt,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "asset": asset,
                    "atext": atext,
                    "atype": atype,
                    "az": az,
                    "be_number": be_number,
                    "ce": ce,
                    "cntct": cntct,
                    "conf": conf,
                    "desc": desc,
                    "el": el,
                    "elle": elle,
                    "env": env,
                    "groups": groups,
                    "how": how,
                    "ident": ident,
                    "id_weather_report": id_weather_report,
                    "lat": lat,
                    "le": le,
                    "lon": lon,
                    "msnid": msnid,
                    "orientation": orientation,
                    "origin": origin,
                    "plat": plat,
                    "pps": pps,
                    "pri": pri,
                    "spec": spec,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "stale": stale,
                    "start": start,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "trkid": trkid,
                    "type": type,
                    "urls": urls,
                },
                poi_create_params.PoiCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[PoiListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: Activity/POI timestamp in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/poi",
            page=SyncOffsetPage[PoiListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    poi_list_params.PoiListParams,
                ),
            ),
            model=PoiListResponse,
        )

    def count(
        self,
        *,
        ts: Union[str, datetime],
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
          ts: Activity/POI timestamp in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/poi/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    poi_count_params.PoiCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[poi_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of POIs
        as a POST body and ingest into the database. This operation is not intended to
        be used for automated feeds into UDL. Data providers should contact the UDL team
        for specific role assignments and for instructions on setting up a permanent
        feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/poi/createBulk",
            body=maybe_transform(body, Iterable[poi_create_bulk_params.Body]),
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
    ) -> PoiGetResponse:
        """
        Service operation to get a single POI by its unique ID passed as a path
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
            f"/udl/poi/{id}",
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
                    poi_get_params.PoiGetParams,
                ),
            ),
            cast_to=PoiGetResponse,
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
    ) -> PoiQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/poi/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PoiQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoiTupleResponse:
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

          ts: Activity/POI timestamp in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/poi/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    poi_tuple_params.PoiTupleParams,
                ),
            ),
            cast_to=PoiTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[poi_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of POIs as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-poi",
            body=maybe_transform(body, Iterable[poi_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPoiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPoiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncPoiResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        poiid: str,
        source: str,
        ts: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        activity: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        asset: str | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        az: float | NotGiven = NOT_GIVEN,
        be_number: str | NotGiven = NOT_GIVEN,
        ce: float | NotGiven = NOT_GIVEN,
        cntct: str | NotGiven = NOT_GIVEN,
        conf: float | NotGiven = NOT_GIVEN,
        desc: str | NotGiven = NOT_GIVEN,
        el: float | NotGiven = NOT_GIVEN,
        elle: Iterable[float] | NotGiven = NOT_GIVEN,
        env: str | NotGiven = NOT_GIVEN,
        groups: List[str] | NotGiven = NOT_GIVEN,
        how: str | NotGiven = NOT_GIVEN,
        ident: str | NotGiven = NOT_GIVEN,
        id_weather_report: List[str] | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        le: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        msnid: str | NotGiven = NOT_GIVEN,
        orientation: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        plat: str | NotGiven = NOT_GIVEN,
        pps: str | NotGiven = NOT_GIVEN,
        pri: int | NotGiven = NOT_GIVEN,
        spec: str | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        stale: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        trkid: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single POI as a POST body and ingest into the
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

          name: Name of the POI target object.

          poiid: Identifier of the actual Point of Interest or target object, which should remain
              the same on subsequent POI records of the same Point of Interest.

          source: Source of the data.

          ts: Activity/POI timestamp in ISO8601 UTC format.

          id: Unique identifier of the record, auto-generated by the system.

          activity: The activity in which the POI subject is engaged. Intended as, but not
              constrained to, MIL-STD-6016 environment dependent activity designations. The
              activity can be reported as either a combination of the code and environment
              (e.g. 30/LAND) or as the descriptive enumeration (e.g. TRAINING), which are
              equivalent.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alt: Point height above ellipsoid (WGS-84), in meters.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the Point of Interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          asset: ID/name of the platform or entity providing the POI data.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          az: Target object pointing azimuth angle, in degrees (for target with sensing or
              emitting capability).

          be_number: The Basic Encyclopedia Number associated with the POI, if applicable.

          ce: Radius of circular area about lat/lon point, in meters (1-sigma, if representing
              error).

          cntct: Contact information for assets reporting PPLI (Precise Participant Location and
              Identification). PPLI is a Link 16 message that is used by units to transmit
              complete location, identification, and limited status information.

          conf: POI confidence estimate (not standardized, but typically a value between 0 and
              1, with 0 indicating lowest confidence.

          desc: Description of the POI target object.

          el: Target object pointing elevation angle, in degrees (for target with sensing or
              emitting capability).

          elle: Elliptical area about the lat/lon point, specified as [semi-major axis (m),
              semi-minor axis (m), orientation (deg) off true North at POI].

          env: POI environment type (e.g., LAND, SURFACE, SUBSURFACE, UNKNOWN, etc.).

          groups: Optional array of groups used when a POI msg originates from a TAK server. Each
              group must be no longer than 256 characters. Groups identify a set of users
              targeted by the cot/poi msg.

          how: How the event point was generated, in CoT object heirarchy notation (optional,
              CoT).

          ident: Estimated identity of the point/object (e.g., FRIEND, HOSTILE, SUSPECT,
              ASSUMED_FRIEND, UNKNOWN, etc.).

          id_weather_report: Array of one or more unique identifiers of weather records associated with this
              POI. Each element in array must be 36 characters or less in length.

          lat: WGS-84 latitude of the POI, in degrees (+N, -S), -90 to 90.

          le: Height above lat/lon point, in meters (1-sigma, if representing linear error).

          lon: WGS-84 longitude of the POI, in degrees (+E, -W), -180 to 180.

          msnid: Optional mission ID related to the POI.

          orientation: The orientation of a vehicle, platform or other entity described by the POI. The
              orientation is defined as the pointing direction of the front/nose of the object
              in degrees clockwise from true North at the object point.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          plat: POI/object platform type (e.g., 14/GROUND, COMBAT_VEHICLE, etc.).

          pps: The purpose of this Point of Interest record (e.g., BDA, EQPT, EVENT, GEOL,
              HZRD, PPLI, SHOTBOX, SURVL, TGT, TSK, WTHR).

          pri: Priority of the POI target object.

          spec: Specific point/object type (e.g., 82/GROUND, LIGHT_TANK, etc.).

          src_ids: Array of UUIDs of the UDL data records that are related to the determination of
              this Point of Interest. See the associated 'srcTyps' array for the specific
              types of data, positionally corresponding to the UUIDs in this array. The
              'srcTyps' and 'srcIds' arrays must match in size. See the corresponding srcTyps
              array element for the data type of the UUID and use the appropriate API
              operation to retrieve that object (e.g. /udl/rfobservation/{uuid}).

          src_typs: Array of UDL record types (GROUNDIMAGE, RFOBS) that are related to the
              determination of this Point of Interest. See the associated 'srcIds' array for
              the record UUIDs, positionally corresponding to the record types in this array.
              The 'srcTyps' and 'srcIds' arrays must match in size.

          stale: Stale timestamp (optional), in ISO8601 UTC format.

          start: Start time of event validity (optional), in ISO8601 UTC format.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          trkid: Optional ID of an associated track related to the POI object, if applicable.
              This track ID should correlate the Point of Interest to a track from the Track
              service.

          type: Event type, in CoT object heirarchy notation (optional, CoT).

          urls: List of URLs to before/after images of this Point of Interest entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/poi",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "poiid": poiid,
                    "source": source,
                    "ts": ts,
                    "id": id,
                    "activity": activity,
                    "agjson": agjson,
                    "alt": alt,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "asset": asset,
                    "atext": atext,
                    "atype": atype,
                    "az": az,
                    "be_number": be_number,
                    "ce": ce,
                    "cntct": cntct,
                    "conf": conf,
                    "desc": desc,
                    "el": el,
                    "elle": elle,
                    "env": env,
                    "groups": groups,
                    "how": how,
                    "ident": ident,
                    "id_weather_report": id_weather_report,
                    "lat": lat,
                    "le": le,
                    "lon": lon,
                    "msnid": msnid,
                    "orientation": orientation,
                    "origin": origin,
                    "plat": plat,
                    "pps": pps,
                    "pri": pri,
                    "spec": spec,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "stale": stale,
                    "start": start,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "trkid": trkid,
                    "type": type,
                    "urls": urls,
                },
                poi_create_params.PoiCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PoiListResponse, AsyncOffsetPage[PoiListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: Activity/POI timestamp in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/poi",
            page=AsyncOffsetPage[PoiListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    poi_list_params.PoiListParams,
                ),
            ),
            model=PoiListResponse,
        )

    async def count(
        self,
        *,
        ts: Union[str, datetime],
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
          ts: Activity/POI timestamp in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/poi/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    poi_count_params.PoiCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[poi_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of POIs
        as a POST body and ingest into the database. This operation is not intended to
        be used for automated feeds into UDL. Data providers should contact the UDL team
        for specific role assignments and for instructions on setting up a permanent
        feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/poi/createBulk",
            body=await async_maybe_transform(body, Iterable[poi_create_bulk_params.Body]),
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
    ) -> PoiGetResponse:
        """
        Service operation to get a single POI by its unique ID passed as a path
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
            f"/udl/poi/{id}",
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
                    poi_get_params.PoiGetParams,
                ),
            ),
            cast_to=PoiGetResponse,
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
    ) -> PoiQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/poi/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PoiQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoiTupleResponse:
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

          ts: Activity/POI timestamp in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/poi/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    poi_tuple_params.PoiTupleParams,
                ),
            ),
            cast_to=PoiTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[poi_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of POIs as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-poi",
            body=await async_maybe_transform(body, Iterable[poi_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PoiResourceWithRawResponse:
    def __init__(self, poi: PoiResource) -> None:
        self._poi = poi

        self.create = to_raw_response_wrapper(
            poi.create,
        )
        self.list = to_raw_response_wrapper(
            poi.list,
        )
        self.count = to_raw_response_wrapper(
            poi.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            poi.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            poi.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            poi.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            poi.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            poi.unvalidated_publish,
        )


class AsyncPoiResourceWithRawResponse:
    def __init__(self, poi: AsyncPoiResource) -> None:
        self._poi = poi

        self.create = async_to_raw_response_wrapper(
            poi.create,
        )
        self.list = async_to_raw_response_wrapper(
            poi.list,
        )
        self.count = async_to_raw_response_wrapper(
            poi.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            poi.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            poi.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            poi.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            poi.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            poi.unvalidated_publish,
        )


class PoiResourceWithStreamingResponse:
    def __init__(self, poi: PoiResource) -> None:
        self._poi = poi

        self.create = to_streamed_response_wrapper(
            poi.create,
        )
        self.list = to_streamed_response_wrapper(
            poi.list,
        )
        self.count = to_streamed_response_wrapper(
            poi.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            poi.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            poi.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            poi.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            poi.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            poi.unvalidated_publish,
        )


class AsyncPoiResourceWithStreamingResponse:
    def __init__(self, poi: AsyncPoiResource) -> None:
        self._poi = poi

        self.create = async_to_streamed_response_wrapper(
            poi.create,
        )
        self.list = async_to_streamed_response_wrapper(
            poi.list,
        )
        self.count = async_to_streamed_response_wrapper(
            poi.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            poi.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            poi.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            poi.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            poi.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            poi.unvalidated_publish,
        )
