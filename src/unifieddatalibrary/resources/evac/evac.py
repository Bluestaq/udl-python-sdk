# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .tuple import (
    TupleResource,
    AsyncTupleResource,
    TupleResourceWithRawResponse,
    AsyncTupleResourceWithRawResponse,
    TupleResourceWithStreamingResponse,
    AsyncTupleResourceWithStreamingResponse,
)
from ...types import (
    evac_list_params,
    evac_count_params,
    evac_create_params,
    evac_retrieve_params,
    evac_create_bulk_params,
    evac_unvalidated_publish_params,
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
from ...types.evac_abridged import EvacAbridged
from ...types.shared.evac_full import EvacFull

__all__ = ["EvacResource", "AsyncEvacResource"]


class EvacResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def tuple(self) -> TupleResource:
        return TupleResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvacResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EvacResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvacResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EvacResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        pickup_lat: float,
        pickup_lon: float,
        req_time: Union[str, datetime],
        source: str,
        type: Literal["REQUEST", "RESPONSE"],
        id: str | NotGiven = NOT_GIVEN,
        casualty_info: Iterable[evac_create_params.CasualtyInfo] | NotGiven = NOT_GIVEN,
        ce: float | NotGiven = NOT_GIVEN,
        cntct_freq: float | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        enemy_data: Iterable[evac_create_params.EnemyData] | NotGiven = NOT_GIVEN,
        id_weather_report: str | NotGiven = NOT_GIVEN,
        le: float | NotGiven = NOT_GIVEN,
        medevac_id: str | NotGiven = NOT_GIVEN,
        medic_req: bool | NotGiven = NOT_GIVEN,
        mission_type: str | NotGiven = NOT_GIVEN,
        num_ambulatory: int | NotGiven = NOT_GIVEN,
        num_casualties: int | NotGiven = NOT_GIVEN,
        num_kia: int | NotGiven = NOT_GIVEN,
        num_litter: int | NotGiven = NOT_GIVEN,
        num_wia: int | NotGiven = NOT_GIVEN,
        obstacles_remarks: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pickup_alt: float | NotGiven = NOT_GIVEN,
        pickup_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        req_call_sign: str | NotGiven = NOT_GIVEN,
        req_num: str | NotGiven = NOT_GIVEN,
        terrain: str | NotGiven = NOT_GIVEN,
        terrain_remarks: str | NotGiven = NOT_GIVEN,
        zone_contr_call_sign: str | NotGiven = NOT_GIVEN,
        zone_hot: bool | NotGiven = NOT_GIVEN,
        zone_marking: str | NotGiven = NOT_GIVEN,
        zone_marking_color: str | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        zone_security: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single evac as a POST body and ingest into the
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

          pickup_lat: WGS-84 latitude of the pickup location, in degrees. -90 to 90 degrees (negative
              values south of equator).

          pickup_lon: WGS-84 longitude of the pickup location, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          req_time: The request time, in ISO 8601 UTC format.

          source: Source of the data.

          type: The type of this medevac record (REQUEST, RESPONSE).

          id: Unique identifier of the record, auto-generated by the system.

          casualty_info: Identity and medical information on the patient to be evacuated.

          ce: Radius of circular area about lat/lon point, in meters (1-sigma, if representing
              error).

          cntct_freq: The contact frequency, in Hz, of the agency or zone controller.

          comments: Additional comments for the medevac mission.

          enemy_data: Data defining any enemy intelligence reported by the requestor.

          id_weather_report: Unique identifier of a weather report associated with this evacuation.

          le: Height above lat/lon point, in meters (1-sigma, if representing linear error).

          medevac_id: UUID identifying the medevac mission, which should remain the same on subsequent
              posts related to the same medevac mission.

          medic_req: Flag indicating whether the mission requires medical personnel.

          mission_type: The operation type of the evacuation. (NOT SPECIFIED, AIR, GROUND, SURFACE).

          num_ambulatory: Number of ambulatory personnel requiring evacuation.

          num_casualties: The count of people requiring medevac.

          num_kia: Number of people Killed In Action.

          num_litter: Number of littered personnel requiring evacuation.

          num_wia: Number of people Wounded In Action.

          obstacles_remarks: Amplifying data for the terrain describing important obstacles in or around the
              zone.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pickup_alt: Altitude relative to WGS-84 ellipsoid, in meters. Positive values indicate a
              point height above ellipsoid, and negative values indicate a point height below
              ellipsoid.

          pickup_time: The expected pickup time, in ISO 8601 UTC format.

          req_call_sign: The call sign of this medevac requestor.

          req_num: Externally provided Medevac request number (e.g. MED.1.223908).

          terrain: Short description of the terrain features of the pickup location (WOODS, TREES,
              PLOWED FIELDS, FLAT, STANDING WATER, MARSH, URBAN BUILT-UP AREA, MOUNTAIN, HILL,
              SAND TD, ROCKY, VALLEY, METAMORPHIC ICE, UNKNOWN TD, SEA, NO STATEMENT).

          terrain_remarks: Amplifying data for the terrain describing any notable additional terrain
              features.

          zone_contr_call_sign: The call sign of the zone controller.

          zone_hot: Flag indicating that the pickup site is hot and hostiles are in the area.

          zone_marking: The expected marker identifying the pickup site (SMOKE ZONE MARKING, FLARES,
              MIRROR, GLIDE ANGLE INDICATOR LIGHT, LIGHT ZONE MARKING, PANELS, FIRE, LASER
              DESIGNATOR, STROBE LIGHTS, VEHICLE LIGHTS, COLORED SMOKE, WHITE PHOSPHERUS,
              INFRARED, ILLUMINATION, FRATRICIDE FENCE).

          zone_marking_color: Color used for the pickup site marking (RED, WHITE, BLUE, YELLOW, GREEN, ORANGE,
              BLACK, PURPLE, BROWN, TAN, GRAY, SILVER, CAMOUFLAGE, OTHER COLOR).

          zone_name: The name of the zone.

          zone_security: The pickup site security (UNKNOWN ZONESECURITY, NO ENEMY, POSSIBLE ENEMY, ENEMY
              IN AREA USE CAUTION, ENEMY IN AREA ARMED ESCORT REQUIRED).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/evac",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "pickup_lat": pickup_lat,
                    "pickup_lon": pickup_lon,
                    "req_time": req_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "casualty_info": casualty_info,
                    "ce": ce,
                    "cntct_freq": cntct_freq,
                    "comments": comments,
                    "enemy_data": enemy_data,
                    "id_weather_report": id_weather_report,
                    "le": le,
                    "medevac_id": medevac_id,
                    "medic_req": medic_req,
                    "mission_type": mission_type,
                    "num_ambulatory": num_ambulatory,
                    "num_casualties": num_casualties,
                    "num_kia": num_kia,
                    "num_litter": num_litter,
                    "num_wia": num_wia,
                    "obstacles_remarks": obstacles_remarks,
                    "origin": origin,
                    "pickup_alt": pickup_alt,
                    "pickup_time": pickup_time,
                    "req_call_sign": req_call_sign,
                    "req_num": req_num,
                    "terrain": terrain,
                    "terrain_remarks": terrain_remarks,
                    "zone_contr_call_sign": zone_contr_call_sign,
                    "zone_hot": zone_hot,
                    "zone_marking": zone_marking,
                    "zone_marking_color": zone_marking_color,
                    "zone_name": zone_name,
                    "zone_security": zone_security,
                },
                evac_create_params.EvacCreateParams,
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
    ) -> EvacFull:
        """
        Service operation to get a single Evac by its unique ID passed as a path
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
            f"/udl/evac/{id}",
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
                    evac_retrieve_params.EvacRetrieveParams,
                ),
            ),
            cast_to=EvacFull,
        )

    def list(
        self,
        *,
        req_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EvacAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          req_time: The request time, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/evac",
            page=SyncOffsetPage[EvacAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "req_time": req_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    evac_list_params.EvacListParams,
                ),
            ),
            model=EvacAbridged,
        )

    def count(
        self,
        *,
        req_time: Union[str, datetime],
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
          req_time: The request time, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/evac/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "req_time": req_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    evac_count_params.EvacCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[evac_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of Evac
        records as a POST body and ingest into the database. This operation is not
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
            "/udl/evac/createBulk",
            body=maybe_transform(body, Iterable[evac_create_bulk_params.Body]),
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
            "/udl/evac/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[evac_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Evac events as a POST body and ingest into
        the database. Requires a specific role, please contact the UDL team to gain
        access. This operation is intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-evac",
            body=maybe_transform(body, Iterable[evac_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvacResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def tuple(self) -> AsyncTupleResource:
        return AsyncTupleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvacResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEvacResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvacResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEvacResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        pickup_lat: float,
        pickup_lon: float,
        req_time: Union[str, datetime],
        source: str,
        type: Literal["REQUEST", "RESPONSE"],
        id: str | NotGiven = NOT_GIVEN,
        casualty_info: Iterable[evac_create_params.CasualtyInfo] | NotGiven = NOT_GIVEN,
        ce: float | NotGiven = NOT_GIVEN,
        cntct_freq: float | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        enemy_data: Iterable[evac_create_params.EnemyData] | NotGiven = NOT_GIVEN,
        id_weather_report: str | NotGiven = NOT_GIVEN,
        le: float | NotGiven = NOT_GIVEN,
        medevac_id: str | NotGiven = NOT_GIVEN,
        medic_req: bool | NotGiven = NOT_GIVEN,
        mission_type: str | NotGiven = NOT_GIVEN,
        num_ambulatory: int | NotGiven = NOT_GIVEN,
        num_casualties: int | NotGiven = NOT_GIVEN,
        num_kia: int | NotGiven = NOT_GIVEN,
        num_litter: int | NotGiven = NOT_GIVEN,
        num_wia: int | NotGiven = NOT_GIVEN,
        obstacles_remarks: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pickup_alt: float | NotGiven = NOT_GIVEN,
        pickup_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        req_call_sign: str | NotGiven = NOT_GIVEN,
        req_num: str | NotGiven = NOT_GIVEN,
        terrain: str | NotGiven = NOT_GIVEN,
        terrain_remarks: str | NotGiven = NOT_GIVEN,
        zone_contr_call_sign: str | NotGiven = NOT_GIVEN,
        zone_hot: bool | NotGiven = NOT_GIVEN,
        zone_marking: str | NotGiven = NOT_GIVEN,
        zone_marking_color: str | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        zone_security: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single evac as a POST body and ingest into the
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

          pickup_lat: WGS-84 latitude of the pickup location, in degrees. -90 to 90 degrees (negative
              values south of equator).

          pickup_lon: WGS-84 longitude of the pickup location, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          req_time: The request time, in ISO 8601 UTC format.

          source: Source of the data.

          type: The type of this medevac record (REQUEST, RESPONSE).

          id: Unique identifier of the record, auto-generated by the system.

          casualty_info: Identity and medical information on the patient to be evacuated.

          ce: Radius of circular area about lat/lon point, in meters (1-sigma, if representing
              error).

          cntct_freq: The contact frequency, in Hz, of the agency or zone controller.

          comments: Additional comments for the medevac mission.

          enemy_data: Data defining any enemy intelligence reported by the requestor.

          id_weather_report: Unique identifier of a weather report associated with this evacuation.

          le: Height above lat/lon point, in meters (1-sigma, if representing linear error).

          medevac_id: UUID identifying the medevac mission, which should remain the same on subsequent
              posts related to the same medevac mission.

          medic_req: Flag indicating whether the mission requires medical personnel.

          mission_type: The operation type of the evacuation. (NOT SPECIFIED, AIR, GROUND, SURFACE).

          num_ambulatory: Number of ambulatory personnel requiring evacuation.

          num_casualties: The count of people requiring medevac.

          num_kia: Number of people Killed In Action.

          num_litter: Number of littered personnel requiring evacuation.

          num_wia: Number of people Wounded In Action.

          obstacles_remarks: Amplifying data for the terrain describing important obstacles in or around the
              zone.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pickup_alt: Altitude relative to WGS-84 ellipsoid, in meters. Positive values indicate a
              point height above ellipsoid, and negative values indicate a point height below
              ellipsoid.

          pickup_time: The expected pickup time, in ISO 8601 UTC format.

          req_call_sign: The call sign of this medevac requestor.

          req_num: Externally provided Medevac request number (e.g. MED.1.223908).

          terrain: Short description of the terrain features of the pickup location (WOODS, TREES,
              PLOWED FIELDS, FLAT, STANDING WATER, MARSH, URBAN BUILT-UP AREA, MOUNTAIN, HILL,
              SAND TD, ROCKY, VALLEY, METAMORPHIC ICE, UNKNOWN TD, SEA, NO STATEMENT).

          terrain_remarks: Amplifying data for the terrain describing any notable additional terrain
              features.

          zone_contr_call_sign: The call sign of the zone controller.

          zone_hot: Flag indicating that the pickup site is hot and hostiles are in the area.

          zone_marking: The expected marker identifying the pickup site (SMOKE ZONE MARKING, FLARES,
              MIRROR, GLIDE ANGLE INDICATOR LIGHT, LIGHT ZONE MARKING, PANELS, FIRE, LASER
              DESIGNATOR, STROBE LIGHTS, VEHICLE LIGHTS, COLORED SMOKE, WHITE PHOSPHERUS,
              INFRARED, ILLUMINATION, FRATRICIDE FENCE).

          zone_marking_color: Color used for the pickup site marking (RED, WHITE, BLUE, YELLOW, GREEN, ORANGE,
              BLACK, PURPLE, BROWN, TAN, GRAY, SILVER, CAMOUFLAGE, OTHER COLOR).

          zone_name: The name of the zone.

          zone_security: The pickup site security (UNKNOWN ZONESECURITY, NO ENEMY, POSSIBLE ENEMY, ENEMY
              IN AREA USE CAUTION, ENEMY IN AREA ARMED ESCORT REQUIRED).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/evac",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "pickup_lat": pickup_lat,
                    "pickup_lon": pickup_lon,
                    "req_time": req_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "casualty_info": casualty_info,
                    "ce": ce,
                    "cntct_freq": cntct_freq,
                    "comments": comments,
                    "enemy_data": enemy_data,
                    "id_weather_report": id_weather_report,
                    "le": le,
                    "medevac_id": medevac_id,
                    "medic_req": medic_req,
                    "mission_type": mission_type,
                    "num_ambulatory": num_ambulatory,
                    "num_casualties": num_casualties,
                    "num_kia": num_kia,
                    "num_litter": num_litter,
                    "num_wia": num_wia,
                    "obstacles_remarks": obstacles_remarks,
                    "origin": origin,
                    "pickup_alt": pickup_alt,
                    "pickup_time": pickup_time,
                    "req_call_sign": req_call_sign,
                    "req_num": req_num,
                    "terrain": terrain,
                    "terrain_remarks": terrain_remarks,
                    "zone_contr_call_sign": zone_contr_call_sign,
                    "zone_hot": zone_hot,
                    "zone_marking": zone_marking,
                    "zone_marking_color": zone_marking_color,
                    "zone_name": zone_name,
                    "zone_security": zone_security,
                },
                evac_create_params.EvacCreateParams,
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
    ) -> EvacFull:
        """
        Service operation to get a single Evac by its unique ID passed as a path
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
            f"/udl/evac/{id}",
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
                    evac_retrieve_params.EvacRetrieveParams,
                ),
            ),
            cast_to=EvacFull,
        )

    def list(
        self,
        *,
        req_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EvacAbridged, AsyncOffsetPage[EvacAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          req_time: The request time, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/evac",
            page=AsyncOffsetPage[EvacAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "req_time": req_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    evac_list_params.EvacListParams,
                ),
            ),
            model=EvacAbridged,
        )

    async def count(
        self,
        *,
        req_time: Union[str, datetime],
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
          req_time: The request time, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/evac/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "req_time": req_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    evac_count_params.EvacCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[evac_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of Evac
        records as a POST body and ingest into the database. This operation is not
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
            "/udl/evac/createBulk",
            body=await async_maybe_transform(body, Iterable[evac_create_bulk_params.Body]),
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
            "/udl/evac/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[evac_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Evac events as a POST body and ingest into
        the database. Requires a specific role, please contact the UDL team to gain
        access. This operation is intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-evac",
            body=await async_maybe_transform(body, Iterable[evac_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvacResourceWithRawResponse:
    def __init__(self, evac: EvacResource) -> None:
        self._evac = evac

        self.create = to_raw_response_wrapper(
            evac.create,
        )
        self.retrieve = to_raw_response_wrapper(
            evac.retrieve,
        )
        self.list = to_raw_response_wrapper(
            evac.list,
        )
        self.count = to_raw_response_wrapper(
            evac.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            evac.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            evac.query_help,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            evac.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._evac.history)

    @cached_property
    def tuple(self) -> TupleResourceWithRawResponse:
        return TupleResourceWithRawResponse(self._evac.tuple)


class AsyncEvacResourceWithRawResponse:
    def __init__(self, evac: AsyncEvacResource) -> None:
        self._evac = evac

        self.create = async_to_raw_response_wrapper(
            evac.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evac.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            evac.list,
        )
        self.count = async_to_raw_response_wrapper(
            evac.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            evac.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            evac.query_help,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            evac.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._evac.history)

    @cached_property
    def tuple(self) -> AsyncTupleResourceWithRawResponse:
        return AsyncTupleResourceWithRawResponse(self._evac.tuple)


class EvacResourceWithStreamingResponse:
    def __init__(self, evac: EvacResource) -> None:
        self._evac = evac

        self.create = to_streamed_response_wrapper(
            evac.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evac.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            evac.list,
        )
        self.count = to_streamed_response_wrapper(
            evac.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            evac.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            evac.query_help,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            evac.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._evac.history)

    @cached_property
    def tuple(self) -> TupleResourceWithStreamingResponse:
        return TupleResourceWithStreamingResponse(self._evac.tuple)


class AsyncEvacResourceWithStreamingResponse:
    def __init__(self, evac: AsyncEvacResource) -> None:
        self._evac = evac

        self.create = async_to_streamed_response_wrapper(
            evac.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evac.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            evac.list,
        )
        self.count = async_to_streamed_response_wrapper(
            evac.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            evac.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            evac.query_help,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            evac.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._evac.history)

    @cached_property
    def tuple(self) -> AsyncTupleResourceWithStreamingResponse:
        return AsyncTupleResourceWithStreamingResponse(self._evac.tuple)
