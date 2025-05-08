# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    emitter_geolocation_count_params,
    emitter_geolocation_query_params,
    emitter_geolocation_tuple_params,
    emitter_geolocation_create_params,
    emitter_geolocation_retrieve_params,
    emitter_geolocation_create_bulk_params,
    emitter_geolocation_unvalidated_publish_params,
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
from .._base_client import make_request_options
from ..types.emitter_geolocation_query_response import EmitterGeolocationQueryResponse
from ..types.emitter_geolocation_tuple_response import EmitterGeolocationTupleResponse
from ..types.emitter_geolocation_retrieve_response import EmitterGeolocationRetrieveResponse

__all__ = ["EmitterGeolocationResource", "AsyncEmitterGeolocationResource"]


class EmitterGeolocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmitterGeolocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EmitterGeolocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmitterGeolocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EmitterGeolocationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        signal_of_interest_type: str,
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
        cluster: str | NotGiven = NOT_GIVEN,
        conf_area: float | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        created_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        detect_alt: float | NotGiven = NOT_GIVEN,
        detect_lat: float | NotGiven = NOT_GIVEN,
        detect_lon: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        err_ellp: Iterable[float] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        id_rf_emitter: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        max_freq: float | NotGiven = NOT_GIVEN,
        min_freq: float | NotGiven = NOT_GIVEN,
        num_bursts: int | NotGiven = NOT_GIVEN,
        order_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_rf_emitter_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pass_group_id: str | NotGiven = NOT_GIVEN,
        received_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
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

          signal_of_interest_type: Type of the signal of interest of this Emitter Geo Location (e.g. RF).

          source: Source of the data.

          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alg_version: The EmitterGeo algorithm type and version used in Emitter geolocation
              calculations.

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

          cluster: The name(s) of the subset of constellation spacecraft that made this detection.

          conf_area: The area of the confidence ellipse specified in meters squared to contain the
              emitter with a 95% probability.

          constellation: The name of the satellite constellation.

          created_ts: Specifies the creation time associated with the order in ISO 8601 UTC with
              microsecond precision.

          detect_alt: The altitude relative to WGS-84 ellipsoid, in meters.

          detect_lat: WGS-84 latitude of the most likely emitter location coordinate point, in
              degrees. -90 to 90 degrees (negative values south of equator).

          detect_lon: WGS-84 longitude of the most likely emitter location coordinate point, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          end_time: The end time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          err_ellp: Confidence ellipsoid about the detection location [semi-major axis (m),
              semi-minor axis (m), orientation (deg)].

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          id_rf_emitter: Optional identifier of the geolocated signal of interest RF Emitter for this
              observation. This ID can be used to obtain additional information on an RF
              Emitter object using the 'get by ID' operation (e.g. /udl/rfemitter/{id}). For
              example, the rfemitter object with idRFEmitter = abc would be queried as
              /udl/rfemitter/abc.

          id_sensor: Unique identifier of the reporting sensor. This ID can be used to obtain
              additional information on a sensor using the 'get by ID' operation (e.g.
              /udl/sensor/{id}). For example, the sensor with idSensor = abc would be queried
              as /udl/sensor/abc. Used when Emitter geolocation is done by a single sensor.

          max_freq: The maximum detected frequency in megahertz.

          min_freq: The minimum detected frequency in megahertz.

          num_bursts: The count of single-burst observations used for this geolocation observation.

          order_id: The order identifier for this Emitter Geo Location data set.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier of the satellite used to identify and geolocate Emitter
              signals of interest of this observation. This may be an internal identifier and
              not necessarily a valid satellite number. Used when Emitter geolocation is done
              by a single satellite.

          orig_rf_emitter_id: Optional identifier of the emitter of interest for this observation. This may be
              an internal identifier and not necessarily a valid emitter Id.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this Emitter Geo Location. This may be an internal
              identifier and not necessarily a valid sensor ID. Used when Emitter geolocation
              is done by a single sensor.

          pass_group_id: Optional external identifier referencing the entity used in the calculation of
              the geolocation.

          received_ts: The time representing the mean of the constituent single-burst observations in
              ISO 8601 UTC with microsecond precision.

          sat_no: Satellite/catalog number of the on-orbit spacecraft used to identify and
              geolocate Emitter signals of interest of this detection. Used when Emitter
              geolocation is done by a single satellite.

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
            "/udl/emittergeolocation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "signal_of_interest_type": signal_of_interest_type,
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
                    "cluster": cluster,
                    "conf_area": conf_area,
                    "constellation": constellation,
                    "created_ts": created_ts,
                    "detect_alt": detect_alt,
                    "detect_lat": detect_lat,
                    "detect_lon": detect_lon,
                    "end_time": end_time,
                    "err_ellp": err_ellp,
                    "external_id": external_id,
                    "id_rf_emitter": id_rf_emitter,
                    "id_sensor": id_sensor,
                    "max_freq": max_freq,
                    "min_freq": min_freq,
                    "num_bursts": num_bursts,
                    "order_id": order_id,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_rf_emitter_id": orig_rf_emitter_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pass_group_id": pass_group_id,
                    "received_ts": received_ts,
                    "sat_no": sat_no,
                    "signal_of_interest": signal_of_interest,
                    "tags": tags,
                },
                emitter_geolocation_create_params.EmitterGeolocationCreateParams,
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
    ) -> EmitterGeolocationRetrieveResponse:
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
            f"/udl/emittergeolocation/{id}",
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
                    emitter_geolocation_retrieve_params.EmitterGeolocationRetrieveParams,
                ),
            ),
            cast_to=EmitterGeolocationRetrieveResponse,
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
            f"/udl/emittergeolocation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/emittergeolocation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emitter_geolocation_count_params.EmitterGeolocationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[emitter_geolocation_create_bulk_params.Body],
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
            "/udl/emittergeolocation/createBulk",
            body=maybe_transform(body, Iterable[emitter_geolocation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmitterGeolocationQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/emittergeolocation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emitter_geolocation_query_params.EmitterGeolocationQueryParams,
                ),
            ),
            cast_to=EmitterGeolocationQueryResponse,
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
            "/udl/emittergeolocation/queryhelp",
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
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmitterGeolocationTupleResponse:
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

          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/emittergeolocation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emitter_geolocation_tuple_params.EmitterGeolocationTupleParams,
                ),
            ),
            cast_to=EmitterGeolocationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[emitter_geolocation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple emittergeolocation records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-emittergeolocation",
            body=maybe_transform(body, Iterable[emitter_geolocation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmitterGeolocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmitterGeolocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEmitterGeolocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmitterGeolocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEmitterGeolocationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        signal_of_interest_type: str,
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
        cluster: str | NotGiven = NOT_GIVEN,
        conf_area: float | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        created_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        detect_alt: float | NotGiven = NOT_GIVEN,
        detect_lat: float | NotGiven = NOT_GIVEN,
        detect_lon: float | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        err_ellp: Iterable[float] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        id_rf_emitter: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        max_freq: float | NotGiven = NOT_GIVEN,
        min_freq: float | NotGiven = NOT_GIVEN,
        num_bursts: int | NotGiven = NOT_GIVEN,
        order_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_rf_emitter_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pass_group_id: str | NotGiven = NOT_GIVEN,
        received_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
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

          signal_of_interest_type: Type of the signal of interest of this Emitter Geo Location (e.g. RF).

          source: Source of the data.

          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alg_version: The EmitterGeo algorithm type and version used in Emitter geolocation
              calculations.

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

          cluster: The name(s) of the subset of constellation spacecraft that made this detection.

          conf_area: The area of the confidence ellipse specified in meters squared to contain the
              emitter with a 95% probability.

          constellation: The name of the satellite constellation.

          created_ts: Specifies the creation time associated with the order in ISO 8601 UTC with
              microsecond precision.

          detect_alt: The altitude relative to WGS-84 ellipsoid, in meters.

          detect_lat: WGS-84 latitude of the most likely emitter location coordinate point, in
              degrees. -90 to 90 degrees (negative values south of equator).

          detect_lon: WGS-84 longitude of the most likely emitter location coordinate point, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          end_time: The end time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision.

          err_ellp: Confidence ellipsoid about the detection location [semi-major axis (m),
              semi-minor axis (m), orientation (deg)].

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          id_rf_emitter: Optional identifier of the geolocated signal of interest RF Emitter for this
              observation. This ID can be used to obtain additional information on an RF
              Emitter object using the 'get by ID' operation (e.g. /udl/rfemitter/{id}). For
              example, the rfemitter object with idRFEmitter = abc would be queried as
              /udl/rfemitter/abc.

          id_sensor: Unique identifier of the reporting sensor. This ID can be used to obtain
              additional information on a sensor using the 'get by ID' operation (e.g.
              /udl/sensor/{id}). For example, the sensor with idSensor = abc would be queried
              as /udl/sensor/abc. Used when Emitter geolocation is done by a single sensor.

          max_freq: The maximum detected frequency in megahertz.

          min_freq: The minimum detected frequency in megahertz.

          num_bursts: The count of single-burst observations used for this geolocation observation.

          order_id: The order identifier for this Emitter Geo Location data set.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier of the satellite used to identify and geolocate Emitter
              signals of interest of this observation. This may be an internal identifier and
              not necessarily a valid satellite number. Used when Emitter geolocation is done
              by a single satellite.

          orig_rf_emitter_id: Optional identifier of the emitter of interest for this observation. This may be
              an internal identifier and not necessarily a valid emitter Id.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this Emitter Geo Location. This may be an internal
              identifier and not necessarily a valid sensor ID. Used when Emitter geolocation
              is done by a single sensor.

          pass_group_id: Optional external identifier referencing the entity used in the calculation of
              the geolocation.

          received_ts: The time representing the mean of the constituent single-burst observations in
              ISO 8601 UTC with microsecond precision.

          sat_no: Satellite/catalog number of the on-orbit spacecraft used to identify and
              geolocate Emitter signals of interest of this detection. Used when Emitter
              geolocation is done by a single satellite.

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
            "/udl/emittergeolocation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "signal_of_interest_type": signal_of_interest_type,
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
                    "cluster": cluster,
                    "conf_area": conf_area,
                    "constellation": constellation,
                    "created_ts": created_ts,
                    "detect_alt": detect_alt,
                    "detect_lat": detect_lat,
                    "detect_lon": detect_lon,
                    "end_time": end_time,
                    "err_ellp": err_ellp,
                    "external_id": external_id,
                    "id_rf_emitter": id_rf_emitter,
                    "id_sensor": id_sensor,
                    "max_freq": max_freq,
                    "min_freq": min_freq,
                    "num_bursts": num_bursts,
                    "order_id": order_id,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_rf_emitter_id": orig_rf_emitter_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pass_group_id": pass_group_id,
                    "received_ts": received_ts,
                    "sat_no": sat_no,
                    "signal_of_interest": signal_of_interest,
                    "tags": tags,
                },
                emitter_geolocation_create_params.EmitterGeolocationCreateParams,
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
    ) -> EmitterGeolocationRetrieveResponse:
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
            f"/udl/emittergeolocation/{id}",
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
                    emitter_geolocation_retrieve_params.EmitterGeolocationRetrieveParams,
                ),
            ),
            cast_to=EmitterGeolocationRetrieveResponse,
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
            f"/udl/emittergeolocation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/emittergeolocation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emitter_geolocation_count_params.EmitterGeolocationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[emitter_geolocation_create_bulk_params.Body],
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
            "/udl/emittergeolocation/createBulk",
            body=await async_maybe_transform(body, Iterable[emitter_geolocation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmitterGeolocationQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/emittergeolocation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emitter_geolocation_query_params.EmitterGeolocationQueryParams,
                ),
            ),
            cast_to=EmitterGeolocationQueryResponse,
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
            "/udl/emittergeolocation/queryhelp",
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
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmitterGeolocationTupleResponse:
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

          start_time: The start time for this Emitter Geo Location data set in ISO 8601 UTC with
              microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/emittergeolocation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    emitter_geolocation_tuple_params.EmitterGeolocationTupleParams,
                ),
            ),
            cast_to=EmitterGeolocationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[emitter_geolocation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple emittergeolocation records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-emittergeolocation",
            body=await async_maybe_transform(body, Iterable[emitter_geolocation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmitterGeolocationResourceWithRawResponse:
    def __init__(self, emitter_geolocation: EmitterGeolocationResource) -> None:
        self._emitter_geolocation = emitter_geolocation

        self.create = to_raw_response_wrapper(
            emitter_geolocation.create,
        )
        self.retrieve = to_raw_response_wrapper(
            emitter_geolocation.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            emitter_geolocation.delete,
        )
        self.count = to_raw_response_wrapper(
            emitter_geolocation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            emitter_geolocation.create_bulk,
        )
        self.query = to_raw_response_wrapper(
            emitter_geolocation.query,
        )
        self.query_help = to_raw_response_wrapper(
            emitter_geolocation.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            emitter_geolocation.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            emitter_geolocation.unvalidated_publish,
        )


class AsyncEmitterGeolocationResourceWithRawResponse:
    def __init__(self, emitter_geolocation: AsyncEmitterGeolocationResource) -> None:
        self._emitter_geolocation = emitter_geolocation

        self.create = async_to_raw_response_wrapper(
            emitter_geolocation.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            emitter_geolocation.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            emitter_geolocation.delete,
        )
        self.count = async_to_raw_response_wrapper(
            emitter_geolocation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            emitter_geolocation.create_bulk,
        )
        self.query = async_to_raw_response_wrapper(
            emitter_geolocation.query,
        )
        self.query_help = async_to_raw_response_wrapper(
            emitter_geolocation.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            emitter_geolocation.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            emitter_geolocation.unvalidated_publish,
        )


class EmitterGeolocationResourceWithStreamingResponse:
    def __init__(self, emitter_geolocation: EmitterGeolocationResource) -> None:
        self._emitter_geolocation = emitter_geolocation

        self.create = to_streamed_response_wrapper(
            emitter_geolocation.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            emitter_geolocation.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            emitter_geolocation.delete,
        )
        self.count = to_streamed_response_wrapper(
            emitter_geolocation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            emitter_geolocation.create_bulk,
        )
        self.query = to_streamed_response_wrapper(
            emitter_geolocation.query,
        )
        self.query_help = to_streamed_response_wrapper(
            emitter_geolocation.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            emitter_geolocation.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            emitter_geolocation.unvalidated_publish,
        )


class AsyncEmitterGeolocationResourceWithStreamingResponse:
    def __init__(self, emitter_geolocation: AsyncEmitterGeolocationResource) -> None:
        self._emitter_geolocation = emitter_geolocation

        self.create = async_to_streamed_response_wrapper(
            emitter_geolocation.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            emitter_geolocation.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            emitter_geolocation.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            emitter_geolocation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            emitter_geolocation.create_bulk,
        )
        self.query = async_to_streamed_response_wrapper(
            emitter_geolocation.query,
        )
        self.query_help = async_to_streamed_response_wrapper(
            emitter_geolocation.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            emitter_geolocation.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            emitter_geolocation.unvalidated_publish,
        )
