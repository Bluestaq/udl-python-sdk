# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    rfgeolocation_list_params,
    rfgeolocation_count_params,
    rfgeolocation_tuple_params,
    rfgeolocation_create_params,
    rfgeolocation_create_bulk_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.rfgeolocation_get_response import RfgeolocationGetResponse
from ..types.rfgeolocation_list_response import RfgeolocationListResponse
from ..types.rfgeolocation_tuple_response import RfgeolocationTupleResponse

__all__ = ["RfgeolocationResource", "AsyncRfgeolocationResource"]


class RfgeolocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RfgeolocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return RfgeolocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RfgeolocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return RfgeolocationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        order_id: str,
        received_ts: Union[str, datetime],
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        alg_version: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        center_freq: float | NotGiven = NOT_GIVEN,
        conf_area: float | NotGiven = NOT_GIVEN,
        conf_orientation: float | NotGiven = NOT_GIVEN,
        conf_semi_major: float | NotGiven = NOT_GIVEN,
        conf_semi_minor: float | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        created_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        detect_alt: float | NotGiven = NOT_GIVEN,
        detect_lat: float | NotGiven = NOT_GIVEN,
        detect_lon: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        id_rf_emitter: str | NotGiven = NOT_GIVEN,
        max_freq: float | NotGiven = NOT_GIVEN,
        min_freq: float | NotGiven = NOT_GIVEN,
        num_bursts: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_rf_emitter_id: str | NotGiven = NOT_GIVEN,
        pass_group_id: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        signal_of_interest: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single RF geolocation as a POST body and ingest into
        the database. This operation is not intended to be used for automated feeds into
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

          order_id: The order identifier for this RF Geo Location data set.

          received_ts: The time representing the mean of the constituent single-burst observations in
              ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alg_version: The RFGeo algorithm type and version used in geolocation calculations.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the Point of Interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          center_freq: The detected signal frequency in megahertz.

          conf_area: The area of the confidence ellipse specified in meters squared to contain the
              emitter with a 95% probability.

          conf_orientation: Confidence ellipse orientation of semi-major axis about the detection location
              lat/lon point measured in degrees.

          conf_semi_major: Confidence ellipse semi-major axis about the detection location lat/lon point
              measured in meters.

          conf_semi_minor: Confidence ellipse semi-minor axis about the detection location lat/lon point
              measured in meters.

          constellation: The name of the satellite constellation.

          created_ts: Specifies the creation time associated with the order in ISO 8601 UTC with
              microsecond precision.

          detect_alt: The altitude relative to WGS-84 ellipsoid, in meters.

          detect_lat: WGS-84 latitude of the most likely emitter location coordinate point, in
              degrees. -90 to 90 degrees (negative values south of equator).

          detect_lon: WGS-84 longitude of the most likely emitter location coordinate point, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          end_time: The order end time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          id_rf_emitter: Optional identifier of the geolocated signal of interest RF Emitter for this
              observation. This ID can be used to obtain additional information on an RF
              Emitter object using the 'get by ID' operation (e.g. /udl/rfemitter/{id}). For
              example, the rfemitter object with idRFEmitter = abc would be queried as
              /udl/rfemitter/abc.

          max_freq: The maximum detected frequency in megahertz.

          min_freq: The minimum detected frequency in megahertz.

          num_bursts: The count of single-burst observations used for this geolocation observation.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier of the satellite used to identify and geolocate RF signals
              of interest of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_rf_emitter_id: Optional identifier of the emitter of interest for this observation. This may be
              an internal identifier and not necessarily a valid emitter Id.

          pass_group_id: Optional external identifier referencing the entity used in the calculation of
              the geolocation.

          sat_no: Satellite/catalog number of the target on-orbit object.

          signal_of_interest: The name of the signal of interest.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/rfgeolocation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "order_id": order_id,
                    "received_ts": received_ts,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "agjson": agjson,
                    "alg_version": alg_version,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "center_freq": center_freq,
                    "conf_area": conf_area,
                    "conf_orientation": conf_orientation,
                    "conf_semi_major": conf_semi_major,
                    "conf_semi_minor": conf_semi_minor,
                    "constellation": constellation,
                    "created_ts": created_ts,
                    "detect_alt": detect_alt,
                    "detect_lat": detect_lat,
                    "detect_lon": detect_lon,
                    "end_time": end_time,
                    "external_id": external_id,
                    "id_rf_emitter": id_rf_emitter,
                    "max_freq": max_freq,
                    "min_freq": min_freq,
                    "num_bursts": num_bursts,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_rf_emitter_id": orig_rf_emitter_id,
                    "pass_group_id": pass_group_id,
                    "sat_no": sat_no,
                    "signal_of_interest": signal_of_interest,
                    "tags": tags,
                },
                rfgeolocation_create_params.RfgeolocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RfgeolocationListResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/rfgeolocation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"start_time": start_time}, rfgeolocation_list_params.RfgeolocationListParams),
            ),
            cast_to=RfgeolocationListResponse,
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
        Service operation to delete a RF geolocation specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance. Note, delete operations do not remove data
        from historical or publish/subscribe stores.

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
            f"/udl/rfgeolocation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/rfgeolocation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"start_time": start_time}, rfgeolocation_count_params.RfgeolocationCountParams),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[rfgeolocation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of RF
        geolocations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/rfgeolocation/createBulk",
            body=maybe_transform(body, Iterable[rfgeolocation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RfgeolocationGetResponse:
        """
        Service operation to get a single RF geolocation by its unique ID passed as a
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
            f"/udl/rfgeolocation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RfgeolocationGetResponse,
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
            "/udl/rfgeolocation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RfgeolocationTupleResponse:
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

          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/rfgeolocation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                    },
                    rfgeolocation_tuple_params.RfgeolocationTupleParams,
                ),
            ),
            cast_to=RfgeolocationTupleResponse,
        )


class AsyncRfgeolocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRfgeolocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRfgeolocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRfgeolocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncRfgeolocationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        order_id: str,
        received_ts: Union[str, datetime],
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        alg_version: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        center_freq: float | NotGiven = NOT_GIVEN,
        conf_area: float | NotGiven = NOT_GIVEN,
        conf_orientation: float | NotGiven = NOT_GIVEN,
        conf_semi_major: float | NotGiven = NOT_GIVEN,
        conf_semi_minor: float | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        created_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        detect_alt: float | NotGiven = NOT_GIVEN,
        detect_lat: float | NotGiven = NOT_GIVEN,
        detect_lon: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        id_rf_emitter: str | NotGiven = NOT_GIVEN,
        max_freq: float | NotGiven = NOT_GIVEN,
        min_freq: float | NotGiven = NOT_GIVEN,
        num_bursts: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_rf_emitter_id: str | NotGiven = NOT_GIVEN,
        pass_group_id: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        signal_of_interest: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single RF geolocation as a POST body and ingest into
        the database. This operation is not intended to be used for automated feeds into
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

          order_id: The order identifier for this RF Geo Location data set.

          received_ts: The time representing the mean of the constituent single-burst observations in
              ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alg_version: The RFGeo algorithm type and version used in geolocation calculations.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the Point of Interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          center_freq: The detected signal frequency in megahertz.

          conf_area: The area of the confidence ellipse specified in meters squared to contain the
              emitter with a 95% probability.

          conf_orientation: Confidence ellipse orientation of semi-major axis about the detection location
              lat/lon point measured in degrees.

          conf_semi_major: Confidence ellipse semi-major axis about the detection location lat/lon point
              measured in meters.

          conf_semi_minor: Confidence ellipse semi-minor axis about the detection location lat/lon point
              measured in meters.

          constellation: The name of the satellite constellation.

          created_ts: Specifies the creation time associated with the order in ISO 8601 UTC with
              microsecond precision.

          detect_alt: The altitude relative to WGS-84 ellipsoid, in meters.

          detect_lat: WGS-84 latitude of the most likely emitter location coordinate point, in
              degrees. -90 to 90 degrees (negative values south of equator).

          detect_lon: WGS-84 longitude of the most likely emitter location coordinate point, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          end_time: The order end time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          id_rf_emitter: Optional identifier of the geolocated signal of interest RF Emitter for this
              observation. This ID can be used to obtain additional information on an RF
              Emitter object using the 'get by ID' operation (e.g. /udl/rfemitter/{id}). For
              example, the rfemitter object with idRFEmitter = abc would be queried as
              /udl/rfemitter/abc.

          max_freq: The maximum detected frequency in megahertz.

          min_freq: The minimum detected frequency in megahertz.

          num_bursts: The count of single-burst observations used for this geolocation observation.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier of the satellite used to identify and geolocate RF signals
              of interest of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_rf_emitter_id: Optional identifier of the emitter of interest for this observation. This may be
              an internal identifier and not necessarily a valid emitter Id.

          pass_group_id: Optional external identifier referencing the entity used in the calculation of
              the geolocation.

          sat_no: Satellite/catalog number of the target on-orbit object.

          signal_of_interest: The name of the signal of interest.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/rfgeolocation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "order_id": order_id,
                    "received_ts": received_ts,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "agjson": agjson,
                    "alg_version": alg_version,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "center_freq": center_freq,
                    "conf_area": conf_area,
                    "conf_orientation": conf_orientation,
                    "conf_semi_major": conf_semi_major,
                    "conf_semi_minor": conf_semi_minor,
                    "constellation": constellation,
                    "created_ts": created_ts,
                    "detect_alt": detect_alt,
                    "detect_lat": detect_lat,
                    "detect_lon": detect_lon,
                    "end_time": end_time,
                    "external_id": external_id,
                    "id_rf_emitter": id_rf_emitter,
                    "max_freq": max_freq,
                    "min_freq": min_freq,
                    "num_bursts": num_bursts,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_rf_emitter_id": orig_rf_emitter_id,
                    "pass_group_id": pass_group_id,
                    "sat_no": sat_no,
                    "signal_of_interest": signal_of_interest,
                    "tags": tags,
                },
                rfgeolocation_create_params.RfgeolocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        start_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RfgeolocationListResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/rfgeolocation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"start_time": start_time}, rfgeolocation_list_params.RfgeolocationListParams
                ),
            ),
            cast_to=RfgeolocationListResponse,
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
        Service operation to delete a RF geolocation specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance. Note, delete operations do not remove data
        from historical or publish/subscribe stores.

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
            f"/udl/rfgeolocation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/rfgeolocation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"start_time": start_time}, rfgeolocation_count_params.RfgeolocationCountParams
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[rfgeolocation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of RF
        geolocations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/rfgeolocation/createBulk",
            body=await async_maybe_transform(body, Iterable[rfgeolocation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RfgeolocationGetResponse:
        """
        Service operation to get a single RF geolocation by its unique ID passed as a
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
            f"/udl/rfgeolocation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RfgeolocationGetResponse,
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
            "/udl/rfgeolocation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RfgeolocationTupleResponse:
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

          start_time: The order start time for this RF Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/rfgeolocation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                    },
                    rfgeolocation_tuple_params.RfgeolocationTupleParams,
                ),
            ),
            cast_to=RfgeolocationTupleResponse,
        )


class RfgeolocationResourceWithRawResponse:
    def __init__(self, rfgeolocation: RfgeolocationResource) -> None:
        self._rfgeolocation = rfgeolocation

        self.create = to_raw_response_wrapper(
            rfgeolocation.create,
        )
        self.list = to_raw_response_wrapper(
            rfgeolocation.list,
        )
        self.delete = to_raw_response_wrapper(
            rfgeolocation.delete,
        )
        self.count = to_raw_response_wrapper(
            rfgeolocation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            rfgeolocation.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            rfgeolocation.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            rfgeolocation.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            rfgeolocation.tuple,
        )


class AsyncRfgeolocationResourceWithRawResponse:
    def __init__(self, rfgeolocation: AsyncRfgeolocationResource) -> None:
        self._rfgeolocation = rfgeolocation

        self.create = async_to_raw_response_wrapper(
            rfgeolocation.create,
        )
        self.list = async_to_raw_response_wrapper(
            rfgeolocation.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rfgeolocation.delete,
        )
        self.count = async_to_raw_response_wrapper(
            rfgeolocation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            rfgeolocation.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            rfgeolocation.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            rfgeolocation.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            rfgeolocation.tuple,
        )


class RfgeolocationResourceWithStreamingResponse:
    def __init__(self, rfgeolocation: RfgeolocationResource) -> None:
        self._rfgeolocation = rfgeolocation

        self.create = to_streamed_response_wrapper(
            rfgeolocation.create,
        )
        self.list = to_streamed_response_wrapper(
            rfgeolocation.list,
        )
        self.delete = to_streamed_response_wrapper(
            rfgeolocation.delete,
        )
        self.count = to_streamed_response_wrapper(
            rfgeolocation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            rfgeolocation.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            rfgeolocation.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            rfgeolocation.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            rfgeolocation.tuple,
        )


class AsyncRfgeolocationResourceWithStreamingResponse:
    def __init__(self, rfgeolocation: AsyncRfgeolocationResource) -> None:
        self._rfgeolocation = rfgeolocation

        self.create = async_to_streamed_response_wrapper(
            rfgeolocation.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rfgeolocation.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rfgeolocation.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            rfgeolocation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            rfgeolocation.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            rfgeolocation.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            rfgeolocation.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            rfgeolocation.tuple,
        )
